from constants.operator_names import OperatorNames
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
    
    @staticmethod
    def get_skill_ids(operator_name: OperatorNames, skill_type: SkillType) -> list:
        operator_cls = OperatorRepository.get_by_id(operator_name)

        if skill_type == SkillType.BATTLE:
            return list(operator_cls.BATTLE_SKILLS.keys())
        
        if skill_type == SkillType.COMBO:
            return list(operator_cls.COMBO_SKILLS.keys())
        
        if skill_type == SkillType.ULTIMATE:
            return list(operator_cls.ULTIMATES.keys())
        
        raise ValueError("invalid skill type")

    @staticmethod
    def get_stacks(operator_name: OperatorNames, skill_type: SkillType) -> list:
        operator_cls = OperatorRepository.get_by_id(operator_name)

        if skill_type == SkillType.BATTLE:
            stack_mul = operator_cls.BATTLE_SKILL_STACK_MUL
        elif skill_type == SkillType.COMBO:
            stack_mul = operator_cls.COMBO_SKILL_STACK_MUL
        elif skill_type == SkillType.ULTIMATE:
            stack_mul = operator_cls.ULTIMATE_STACK_MUL
        else:
            raise ValueError("invalid skill type")
        
        return [0] if stack_mul is None else list(range(5))