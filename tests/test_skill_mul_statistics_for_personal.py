import pandas as pd

from src.constants.operator_names import OperatorNames
from src.constants.skill_type import SkillType
from src.entities.skill_mul_condition import SkillMulCondition
from src.services.skill_mul_service import SkillMulService
from src.services.skill_mul_statistics_service import SkillMulStatisticsService
from src.services.skill_mul_statistics_service_for_personal import SkillMulStatisticsServiceForPersonal


def test_get_statistics_returns_correct_values(monkeypatch):
    mock_table = pd.DataFrame({
        "battle_skill": [10, 20, 30],
        "combo_skill": [40, 50, 60],
        "ultimate": [70, 80, 90],
    })

    monkeypatch.setattr(
        SkillMulStatisticsService,
        "_get_skill_mul_df",
        staticmethod(lambda: mock_table),
    )

    monkeypatch.setattr(
        SkillMulService,
        "get_skill_mul",
        staticmethod(lambda cond: 20),
    )

    cond = SkillMulCondition(
        OperatorNames.LIFENG,
        SkillType.BATTLE,
    )

    deviation =  SkillMulStatisticsServiceForPersonal.get_deviation_from_mean(cond)
    deviation_from_median = SkillMulStatisticsServiceForPersonal.get_deviation_from_median(cond)
    standard_score = SkillMulStatisticsServiceForPersonal.get_standard_score(cond)

    assert deviation == 0.0
    assert deviation_from_median == 0.0
    assert standard_score == 50.0

def test_get_statistics_when_skills_deal_no_damages(monkeypatch):
    mock_table = pd.DataFrame({
        "battle_skill": [10, 20, 30],
        "combo_skill": [40, 50, 60],
        "ultimate": [70, 80, 90],
    })

    monkeypatch.setattr(
        SkillMulStatisticsService,
        "_get_skill_mul_df",
        staticmethod(lambda: mock_table),
    )

    monkeypatch.setattr(
        SkillMulStatisticsServiceForPersonal,
        "_has_damage_skill",
        staticmethod(lambda cond: False),
    )

    cond = SkillMulCondition(
        OperatorNames.LIFENG,
        SkillType.BATTLE,
    )

    deviation =  SkillMulStatisticsServiceForPersonal.get_deviation_from_mean(cond)
    deviation_from_median = SkillMulStatisticsServiceForPersonal.get_deviation_from_median(cond)
    standard_score = SkillMulStatisticsServiceForPersonal.get_standard_score(cond)

    assert deviation == None
    assert deviation_from_median == None
    assert standard_score == None