import pandas as pd

from src.constants.operator_names import OperatorNames
from src.constants.skill_mul_columns import SKILL_MUL_COLUMNS, SkillMulColumns
from src.constants.skill_type import SkillType
from src.entities.skill_mul_condition import SkillMulCondition
from src.repositories.operator_repository import OperatorRepository
from src.services.skill_mul_service import SkillMulService


class SkillMulTableBuilder:
    @staticmethod
    def get_skill_mul_table() -> pd.DataFrame:
        data = SkillMulTableBuilder._get_data()
        return pd.DataFrame.from_dict(
            data,
            orient="index",
            columns=SKILL_MUL_COLUMNS,
        )
    
    @staticmethod
    def sort_skill_mul_table(
        skill_mul_table: pd.DataFrame,
        skill_type: SkillType,
        ascending: bool,
    ) -> pd.DataFrame:
        column = SkillMulTableBuilder._get_skill_mul_column(skill_type)
        return skill_mul_table.sort_values(
            by=column,
            ascending=ascending,
        )

    @staticmethod
    def _get_data() -> dict:
        keys = list()
        values = list()

        for operator_name in OperatorNames:
            keys.append(operator_name)
            skill_muls = list()

            for skill_type in SkillType:
                cond = SkillMulCondition(
                    operator_name=operator_name,
                    skill_type=skill_type,
                )

                if not SkillMulTableBuilder._has_damage_skill(cond):
                    skill_muls.append(float("nan"))
                    continue

                skill_mul = SkillMulService.get_skill_mul(cond)
                skill_muls.append(skill_mul)

            values.append(skill_muls)

        return dict(zip(keys, values))
    
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
    
    @staticmethod
    def _get_skill_mul_column(skill_type: SkillType) -> str:
        match skill_type:
            case SkillType.BATTLE:
                return SkillMulColumns.BATTLE
            case SkillType.COMBO:
                return SkillMulColumns.COMBO
            case SkillType.ULTIMATE:
                return SkillMulColumns.ULTIMATE
            case _:
                raise ValueError(f"Invalid skill_type: {skill_type}")