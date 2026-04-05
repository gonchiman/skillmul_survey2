from ..operator_base import OperatorBase


class Rossi(OperatorBase):
    BATTLE_SKILLS = {
        1: [192, 288]
    }
    COMBO_SKILLS = {
        1: [150, 300]
    }
    ULTIMATES = {
        1: [600, 250, 750],
    }
    COMBO_SKILL_STACK_MUL = 180