import pytest

from src.entities.skill_muls.operator_base import OperatorBase


class FakeOperator1(OperatorBase):
    BATTLE_SKILLS = {
        1: [100, 150, 200]
    }
    COMBO_SKILLS = {
        1: [100, 150, 200]
    }
    ULTIMATES = {
        1: [100, 150, 200]
    }
    BATTLE_SKILL_STACK_MUL = 100
    COMBO_SKILL_STACK_MUL = 100
    ULTIMATE_STACK_MUL = 100

class FakeOperator2(OperatorBase):
    BATTLE_SKILLS = {
        1: [100, 150, 200]
    }
    COMBO_SKILLS = {
        1: [100, 150, 200]
    }
    ULTIMATES = {
        1: [100, 150, 200]
    }


def test_get_skill_mul_without_stack():
    battle_skill_mul = FakeOperator1.get_battle_skill_mul(1)
    combo_skill_mul = FakeOperator1.get_combo_skill_mul(1)
    ultimate_mul = FakeOperator1.get_ultimate_mul(1)

    assert battle_skill_mul == sum([100, 150, 200])
    assert combo_skill_mul == sum([100, 150, 200])
    assert ultimate_mul == sum([100, 150, 200])

def test_get_skill_mul_with_stack():
    for i in range(0, 5):
        battle_skill_mul = FakeOperator1.get_battle_skill_mul(1, i)
        combo_skill_mul = FakeOperator1.get_combo_skill_mul(1, i)
        ultimate_mul = FakeOperator1.get_ultimate_mul(1, i)

        assert battle_skill_mul == sum([100, 150, 200]) + 100 * i
        assert combo_skill_mul == sum([100, 150, 200]) + 100 * i
        assert ultimate_mul == sum([100, 150, 200]) + 100 * i

def test_get_skill_mul_invalid_skill_id():
    skill_id = 2

    with pytest.raises(ValueError):
        FakeOperator1.get_battle_skill_mul(skill_id)

    with pytest.raises(ValueError):
        FakeOperator1.get_combo_skill_mul(skill_id)

    with pytest.raises(ValueError):
        FakeOperator1.get_ultimate_mul(skill_id)

def test_get_skill_mul_invalid_stack_1():
    skill_id = 1
    stack = -1

    with pytest.raises(ValueError):
        FakeOperator1.get_battle_skill_mul(skill_id, stack)

    with pytest.raises(ValueError):
        FakeOperator1.get_combo_skill_mul(skill_id, stack)

    with pytest.raises(ValueError):
        FakeOperator1.get_ultimate_mul(skill_id, stack)

def test_get_skill_mul_invalid_stack_2():
    skill_id = 1
    stack = 1

    with pytest.raises(ValueError):
        FakeOperator2.get_battle_skill_mul(skill_id, stack)

    with pytest.raises(ValueError):
        FakeOperator2.get_combo_skill_mul(skill_id, stack)

    with pytest.raises(ValueError):
        FakeOperator2.get_ultimate_mul(skill_id, stack)