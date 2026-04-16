from src.entities.operator_base import OperatorBase


class Rossi(OperatorBase):
    BATTLE_SKILLS = [192, 288]
    COMBO_SKILLS = [150, 300]
    ULTIMATES = [600, 250, 750]
    COMBO_SKILL_STACK_MUL = 180