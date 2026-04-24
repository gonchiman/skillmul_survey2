import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parents[1]))

from src.constants.skill_type import SkillType
from src.services.skill_mul_graph_service import SkillMulGraphService


def get_histgram():
    skill_type = SkillType.BATTLE
    skill_mul = 400

    SkillMulGraphService.get_histogram(skill_type, skill_mul)


get_histgram()