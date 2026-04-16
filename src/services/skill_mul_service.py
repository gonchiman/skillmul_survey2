from src.constants.figures import MAX_STACKS
from src.constants.skill_type import SkillType
from src.repositories.operator_repository import OperatorRepository
from src.entities.skill_mul_condition import SkillMulCondition


class SkillMulService:
    @staticmethod
    def get_skill_mul(cond: SkillMulCondition) -> int:
        operator_cls = OperatorRepository.get_by_id(cond.operator_name)

        if cond.skill_type == SkillType.BATTLE:
            if operator_cls.is_battle_skill_stack_mul():
                return operator_cls.get_battle_skill_mul(1, MAX_STACKS)
            return operator_cls.get_battle_skill_mul(1, 0)
        
        if cond.skill_type == SkillType.COMBO:
            if operator_cls.is_combo_skill_stack_mul():
                return operator_cls.get_combo_skill_mul(1, MAX_STACKS)
            return operator_cls.get_combo_skill_mul(1, 0)
        
        if cond.skill_type == SkillType.ULTIMATE:
            if operator_cls.is_ultimate_skill_stack_mul():
                return operator_cls.get_ultimate_mul(1, MAX_STACKS)
            return operator_cls.get_ultimate_mul(1, 0)
        
        raise ValueError("invalid skill type")