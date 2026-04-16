class OperatorBase:
    BATTLE_SKILLS = ()
    COMBO_SKILLS = ()
    ULTIMATES = ()
    BATTLE_SKILL_STACK_MUL = None
    COMBO_SKILL_STACK_MUL = None
    ULTIMATE_STACK_MUL = None

    @classmethod
    def _calc_mul(cls, 
                  skill_mul: tuple[int], 
                  stack: int, 
                  stack_mul: int | None
    ) -> int:
        if stack < 0:
            raise ValueError("stack must be 0 or greater.")
        
        extra = 0
        if stack > 0:
            if stack_mul is None:
                raise ValueError("This operator doesn't support stack.")
            extra = stack_mul * stack

        return sum(skill_mul) + extra
    
    @classmethod
    def get_battle_skill_mul(cls, stack: int) -> int:
        return cls._calc_mul(cls.BATTLE_SKILLS, stack, cls.BATTLE_SKILL_STACK_MUL)

    @classmethod
    def get_combo_skill_mul(cls, stack: int) -> int:
        return cls._calc_mul(cls.COMBO_SKILLS, stack, cls.COMBO_SKILL_STACK_MUL)

    @classmethod
    def get_ultimate_mul(cls, stack: int) -> int:
        return cls._calc_mul(cls.ULTIMATES, stack, cls.ULTIMATE_STACK_MUL)
    
    @classmethod
    def is_battle_skill_stack_mul(cls) -> bool:
        if cls.BATTLE_SKILL_STACK_MUL is None:
            return False
        return True
    
    @classmethod
    def is_combo_skill_stack_mul(cls) -> bool:
        if cls.COMBO_SKILL_STACK_MUL is None:
            return False
        return True
    
    @classmethod
    def is_ultimate_skill_stack_mul(cls) -> bool:
        if cls.ULTIMATE_STACK_MUL is None:
            return False
        return True