from src.constants.skill_type import SkillType
from src.constants.skill_mul_columns import BATTLE_SKILL_COL, COMBO_SKILL_COL, ULTIMATE_COL


class SkillTypeRepository:
    @staticmethod
    def get_col_by_enum(skill_type: SkillType) -> str:
        match skill_type:
            case SkillType.BATTLE:
                return BATTLE_SKILL_COL
            case SkillType.COMBO:
                return COMBO_SKILL_COL
            case SkillType.ULTIMATE:
                return ULTIMATE_COL