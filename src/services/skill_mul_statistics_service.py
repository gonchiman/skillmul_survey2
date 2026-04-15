import pandas as pd

from src.constants.skill_type import SkillType
from src.repositories.skill_type_repository import SkillTypeRepository
from src.services.skill_mul_table_builder import SkillMulTableBuilder


class SkillMulStatisticsService:
    @classmethod
    def get_mean(cls, skill_type: SkillType) -> float:
        return cls._get_series(skill_type).mean()

    @classmethod
    def get_median(cls, skill_type: SkillType) -> float:
        return cls._get_series(skill_type).median()

    @classmethod
    def get_std(cls, skill_type: SkillType) -> float:
        return cls._get_series(skill_type).std(ddof=0)

    @staticmethod
    def _get_skill_mul_df() -> pd.DataFrame:
        return SkillMulTableBuilder.get_skill_mul_table()
    
    @classmethod
    def _get_series(cls, skill_type: SkillType) -> pd.Series:
        df = cls._get_skill_mul_df()
        col = SkillTypeRepository.get_col_by_enum(skill_type)
        return df[col]