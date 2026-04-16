from src.entities.skill_mul_condition import SkillMulCondition
from src.services.skill_mul_service import SkillMulService
from src.services.skill_mul_statistics_service import SkillMulStatisticsService


class SkillMulStatisticsServiceForPersonal:
    @staticmethod
    def get_deviation_from_mean(cond: SkillMulCondition) -> float:
        skill_mul = SkillMulService.get_skill_mul(cond)
        skill_mul_mean = SkillMulStatisticsService.get_mean(cond.skill_type)
        return skill_mul - skill_mul_mean
    
    @staticmethod
    def get_deviation_from_median(cond: SkillMulCondition) -> float:
        skill_mul = SkillMulService.get_skill_mul(cond)
        skill_mul_median = SkillMulStatisticsService.get_median(cond.skill_type)
        return skill_mul - skill_mul_median
    
    @staticmethod
    def get_standard_score(cond: SkillMulCondition) -> float:
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