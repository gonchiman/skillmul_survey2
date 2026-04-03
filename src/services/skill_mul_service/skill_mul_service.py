from src.constants.skill_type import SkillType
from src.repositories.operator_repository import OperatorRepository
from src.services.skill_mul_service.skill_mul_condition import SkillMulCondition


class SkillMulService:
    @staticmethod
    def get_skill_mul(cond: SkillMulCondition) -> int:
        operator_cls = OperatorRepository.get_by_id(cond.operator_name)

        if cond.skill_type == SkillType.BATTLE:
            return operator_cls.get_battle_skill_mul(cond.skill_id, cond.stack)
        
        if cond.skill_type == SkillType.COMBO:
            return operator_cls.get_combo_skill_mul(cond.skill_id, cond.stack)
        
        if cond.skill_type == SkillType.ULTIMATE:
            return operator_cls.get_ultimate_mul(cond.skill_id, cond.stack)
        
        raise ValueError("invalid skill type")