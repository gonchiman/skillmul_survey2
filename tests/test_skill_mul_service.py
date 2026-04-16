from enum import Enum

import pytest

from src.services.skill_mul_service import SkillMulService
from src.constants.operator_names import OperatorNames
from src.constants.skill_type import SkillType
from src.entities.skill_mul_condition import SkillMulCondition


class FakeSKillType(Enum):
    FAKE = "fake"

def test_get_skill_mul_normal():
    cond = SkillMulCondition(
        operator_name=OperatorNames.LIFENG,
        skill_type=SkillType.BATTLE,
    )

    assert SkillMulService.get_skill_mul(cond) == sum([86, 86, 268])

def test_get_skill_mul_value_error_when_skill_type_is_invalid():
    cond = SkillMulCondition(
        operator_name=OperatorNames.LIFENG,
        skill_type=FakeSKillType.FAKE,
    )

    with pytest.raises(ValueError):
        SkillMulService.get_skill_mul(cond)

def test_get_skill_mul_confirm_rossi_is_correct():
    cond_battle = SkillMulCondition(
        operator_name=OperatorNames.ROSSI,
        skill_type=SkillType.BATTLE,
    )
    cond_combo = SkillMulCondition(
        operator_name=OperatorNames.ROSSI,
        skill_type=SkillType.COMBO,
    )
    cond_ultimate = SkillMulCondition(
        operator_name=OperatorNames.ROSSI,
        skill_type=SkillType.ULTIMATE,
    )

    skill_mul_battle = SkillMulService.get_skill_mul(cond_battle)
    skill_mul_combo = SkillMulService.get_skill_mul(cond_combo)
    skill_mul_ultimate = SkillMulService.get_skill_mul(cond_ultimate)

    assert skill_mul_battle == sum([192, 288])
    assert skill_mul_combo == sum([150, 300, 180*4])
    assert skill_mul_ultimate == sum([600, 250, 750])