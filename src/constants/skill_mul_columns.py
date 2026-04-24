from enum import Enum


BATTLE_SKILL_COL = "battle_skill"
COMBO_SKILL_COL = "combo_skill"
ULTIMATE_COL = "ultimate"

SKILL_MUL_COLUMNS = [
    BATTLE_SKILL_COL,
    COMBO_SKILL_COL,
    ULTIMATE_COL,
]

class SkillMulColumns(Enum):
    BATTLE = "battle_skill"
    COMBO = "combo_skill"
    ULTIMATE = "ultimate"