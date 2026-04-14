import pandas as pd

from src.constants.operator_names import OperatorNames
from src.constants.skill_mul_columns import SKILL_MUL_COLUMNS
from src.constants.skill_type import SkillType
from src.entities.skill_mul_condition import SkillMulCondition
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
                skill_mul = SkillMulService.get_skill_mul(cond)
                skill_muls.append(skill_mul)

            values.append(skill_muls)

        return dict(zip(keys, values))