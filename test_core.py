import new_core


class TestNewGladiator:
    def test_init(self):
        gladiator = new_core.NewGladiator(100, 0, 10, 20, 'Thor')
        assert gladiator.health == 100
        assert gladiator.rage == 0
        assert gladiator.damage_low == 10
        assert gladiator.damage_high == 20
        assert gladiator.name == 'Thor'

    def test_is_dead(self):
        gladiator_1 = new_core.NewGladiator(0, 20, -1, 10, 'Thor')
        assert gladiator_1.is_dead() == True
        gladiator_1 = new_core.NewGladiator(1, 20, -1, 10, 'Thor')
        assert gladiator_1.is_dead() == False
