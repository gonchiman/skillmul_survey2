from enum import Enum

import pytest

from src.services.skill_mul_service.skill_mul_service import SkillMulService
from src.constants.operator_names import OperatorNames
from src.constants.skill_type import SkillType
from src.services.skill_mul_service.skill_mul_condition import SkillMulCondition


class FakeSKillType(Enum):
    FAKE = "fake"

def test_get_skill_mul_normal():
    cond = SkillMulCondition(
        operator_name=OperatorNames.LIFENG,
        skill_type=SkillType.BATTLE,
        skill_id=1,
    )

    assert SkillMulService.get_skill_mul(cond) == sum([86, 86, 268])

def test_get_skill_mul_value_error_when_skill_type_is_invalid():
    cond = SkillMulCondition(
        operator_name=OperatorNames.LIFENG,
        skill_type=FakeSKillType.FAKE,
        skill_id=1,
    )

    with pytest.raises(ValueError):
        SkillMulService.get_skill_mul(cond)