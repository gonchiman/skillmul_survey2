from src.constants.skill_type import SkillType
from src.entities.skill_mul_condition import SkillMulCondition
from src.repositories.operator_repository import OperatorRepository
from src.services.skill_mul_service import SkillMulService
from src.services.skill_mul_statistics_service import SkillMulStatisticsService


class SkillMulStatisticsServiceForPersonal:
    @staticmethod
    def get_deviation_from_mean(cond: SkillMulCondition) -> float | None:
        if not SkillMulStatisticsServiceForPersonal._has_damage_skill(cond):
            return None
        
        skill_mul = SkillMulService.get_skill_mul(cond)
        skill_mul_mean = SkillMulStatisticsService.get_mean(cond.skill_type)

        return skill_mul - skill_mul_mean
    
    @staticmethod
    def get_deviation_from_median(cond: SkillMulCondition) -> float:
        if not SkillMulStatisticsServiceForPersonal._has_damage_skill(cond):
            return None

        skill_mul = SkillMulService.get_skill_mul(cond)
        skill_mul_median = SkillMulStatisticsService.get_median(cond.skill_type)

        return skill_mul - skill_mul_median
    
    @staticmethod
    def get_standard_score(cond: SkillMulCondition) -> float:
        if not SkillMulStatisticsServiceForPersonal._has_damage_skill(cond):
            return None
        
        skill_mul = SkillMulService.get_skill_mul(cond)
        skill_mul_mean = SkillMulStatisticsService.get_mean(cond.skill_type)
        skill_mul_std = SkillMulStatisticsService.get_std(cond.skill_type)

        return SkillMulStatisticsServiceForPersonal._cal_standard_score(
            skill_mul,
            skill_mul_mean,
            skill_mul_std,
        )
    
    @staticmethod
    def _cal_standard_score(score, mean, std) -> float:
        return 50 + 10 * (score - mean) / std
    
    @staticmethod
    def _has_damage_skill(cond: SkillMulCondition) -> bool:
        operator_cls = OperatorRepository.get_by_id(cond.operator_name)

        if cond.skill_type == SkillType.BATTLE:
            return bool(operator_cls.BATTLE_SKILLS)
        elif cond.skill_type == SkillType.COMBO:
            return bool(operator_cls.COMBO_SKILLS)
        elif cond.skill_type == SkillType.ULTIMATE:
            return bool(operator_cls.ULTIMATES)
        
        raise ValueError("invalid skill type")