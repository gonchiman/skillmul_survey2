from src.services.skill_mul_service.skill_mul_service import SkillMulService
from src.constants.operator_names import OperatorNames
from src.constants.skill_type import SkillType
from src.services.skill_mul_service.skill_mul_condition import SkillMulCondition


def test_get_skill_mul_normal():
    cond = SkillMulCondition(
        operator_name=OperatorNames.LIFENG,
        skill_type=SkillType.BATTLE,
        skill_id=1,
    )

    assert SkillMulService.get_skill_mul(cond) == sum([86, 86, 268])