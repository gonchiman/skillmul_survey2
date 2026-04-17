import statistics

import pandas as pd
import pytest

from src.constants.skill_type import SkillType
from src.services.skill_mul_statistics_service import SkillMulStatisticsService


def test_get_statistics_with_fixed_dataframe(monkeypatch):
    df = pd.DataFrame({
        "battle_skill": [10, 20, 30],
        "combo_skill": [40, 50, 60],
        "ultimate": [70, 80, 90],
    })

    monkeypatch.setattr(
        SkillMulStatisticsService,
        "_get_skill_mul_df",
        staticmethod(lambda: df),
    )

    assert SkillMulStatisticsService.get_mean(SkillType.BATTLE) == 20.0
    assert SkillMulStatisticsService.get_median(SkillType.BATTLE) == 20.0
    assert SkillMulStatisticsService.get_std(SkillType.BATTLE) == pytest.approx(statistics.pstdev([10, 20, 30]))

def test_get_statistics_returns_float():
    for skill_type in SkillType:
        mean = SkillMulStatisticsService.get_mean(skill_type)
        median = SkillMulStatisticsService.get_median(skill_type)
        std = SkillMulStatisticsService.get_std(skill_type)

        assert isinstance(mean, float)
        assert isinstance(median, float)
        assert isinstance(std, float)

def test_get_statistics_is_non_negative():
    for skill_type in SkillType:
        mean = SkillMulStatisticsService.get_mean(skill_type)
        median = SkillMulStatisticsService.get_median(skill_type)
        std = SkillMulStatisticsService.get_std(skill_type)

        assert mean >= 0
        assert median >= 0
        assert std >= 0

def test_get_statistics_when_columns_have_nan_value(monkeypatch):
    df = pd.DataFrame({
        "battle_skill": [10, float("nan"), 30],
        "combo_skill": [40, float("nan"), 60],
        "ultimate": [70, float("nan"), 90],
    })

    monkeypatch.setattr(
        SkillMulStatisticsService,
        "_get_skill_mul_df",
        staticmethod(lambda: df),
    )

    assert SkillMulStatisticsService.get_mean(SkillType.BATTLE) == statistics.mean([10, 30])
    assert SkillMulStatisticsService.get_median(SkillType.BATTLE) == statistics.median([10, 30])
    assert SkillMulStatisticsService.get_std(SkillType.BATTLE) == pytest.approx(statistics.pstdev([10, 30]))