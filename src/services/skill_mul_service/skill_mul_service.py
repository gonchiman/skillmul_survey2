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
    def get_skill_ids(operator_name, skill_type) -> list:
        operator_cls = OperatorRepository.get_by_id(operator_name)

        if skill_type == SkillType.BATTLE:
            return list(operator_cls.BATTLE_SKILLS.keys())
        
        if skill_type == SkillType.COMBO:
            return list(operator_cls.COMBO_SKILLS.keys())
        
        if skill_type == SkillType.ULTIMATE:
            return list(operator_cls.ULTIMATES.keys())
        
        raise ValueError("invalid skill type")

    @staticmethod
    def get_stacks(operator_name, skill_type) -> list:
        operator_cls = OperatorRepository.get_by_id(operator_name)
        initial_stacks = [0]
        multiple_stacks = [s for s in range(0, 5)]

        if skill_type == SkillType.BATTLE:
            if operator_cls.BATTLE_SKILL_STACK_MUL is None:
                return initial_stacks
            return multiple_stacks
        
        if skill_type == SkillType.COMBO:
            if operator_cls.COMBO_SKILL_STACK_MUL is None:
                return initial_stacks
            return multiple_stacks
        
        if skill_type == SkillType.ULTIMATE:
            if operator_cls.ULTIMATE_STACK_MUL is None:
                return initial_stacks
            return multiple_stacks
        
        raise ValueError("invalid skill type")