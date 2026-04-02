class Rossi:
    BATTLE_SKILL_1 = [192]
    BATTLE_SKILL_2 = [192, 288]
    COMBO_SKILL_1 = [150]
    COMBO_SKILL_2 = [150, 300]
    COMBO_SKILL_STACK = 180
    ULTIMATE_1 = [600, 250, 750]

    def get_battle_skill_mul(self, id, stack=0):
        match id:
            case 1:
                return sum(self.BATTLE_SKILL_1)
            case 2:
                return sum(self.BATTLE_SKILL_2)
            
    def get_combo_skill_mul(self, id, stack=0):
        stack_mul = self.COMBO_SKILL_STACK * stack
        match id:
            case 1:
                return sum(self.COMBO_SKILL_1)
            case 2:
                return sum(self.COMBO_SKILL_2) + stack_mul
            
    def get_ultimate_mul(self, id, stack=0):
        match id:
            case 1:
                return sum(self.ULTIMATE_1)