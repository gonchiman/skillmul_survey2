from src.constants.operator_names import OperatorNames
from src.constants.skill_type import SkillType
from src.entities.skill_mul_condition import SkillMulCondition


def test_skill_mul_condition_stores_values():
    cond = SkillMulCondition(
        operator_name=OperatorNames.LIFENG,
        skill_type=SkillType.BATTLE,
    )

    assert cond.operator_name == OperatorNames.LIFENG
    assert cond.skill_type == SkillType.BATTLE