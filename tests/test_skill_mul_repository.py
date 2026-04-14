from enum import Enum

from src.constants.skill_type import SkillType
from src.repositories.skill_type_repository import SkillTypeRepository


def test_get_col_by_enum():
    battle_skill = SkillType.BATTLE
    combo_skill = SkillType.COMBO
    ultimate = SkillType.ULTIMATE

    assert SkillTypeRepository.get_col_by_enum(battle_skill) == "battle_skill"
    assert SkillTypeRepository.get_col_by_enum(combo_skill) == "combo_skill"
    assert SkillTypeRepository.get_col_by_enum(ultimate) == "ultimate"