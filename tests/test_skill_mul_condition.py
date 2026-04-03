from constants.operator_names import OperatorNames
from constants.skill_type import SkillType
from services.skill_mul_service.skill_mul_condition import SkillMulCondition


def test_skill_mul_condition_stores_values():
    cond = SkillMulCondition(
        operator_name=OperatorNames.LIFENG,
        skill_type=SkillType.BATTLE,
        skill_id=1,
        stack=0,
    )

    assert cond.operator_name == OperatorNames.LIFENG
    assert cond.skill_type == SkillType.BATTLE
    assert cond.skill_id == 1
    assert cond.stack == 0