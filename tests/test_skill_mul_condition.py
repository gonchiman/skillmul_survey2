from enum import Enum

from constants.skill_type import SkillType
from services.skill_mul_service.skill_mul_condition import SkillMulCondition


class FakeOperatorNames(Enum):
    FAKEOPERATOR = "fake_operator"


def test_skill_mul_condition():
    operator_name = FakeOperatorNames.FAKEOPERATOR
    skill_type = SkillType.BATTLE
    skill_id = 1
    stack = 0

    cond = SkillMulCondition(
        operator_name,
        skill_type,
        skill_id,
        stack
    )

    assert cond.operator_name == FakeOperatorNames.FAKEOPERATOR
    assert cond.skill_type == SkillType.BATTLE
    assert cond.skill_id == 1
    assert cond.stack == 0