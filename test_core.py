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

    def test_heal(self):
        gladiator_1 = new_core.NewGladiator(15, 20, 100, 10, 'Thor')
        assert gladiator_1.heal() == gladiator_1

    def test_attack(self):
        gladiator_1 = new_core.NewGladiator(75, 0, 10, 10, 'Thor')
        gladiator_2 = new_core.NewGladiator(75, 0, 11, 13, 'Loki')
        gladiator_1.attack(gladiator_2)
        assert gladiator_1.rage == 15
        assert gladiator_2.health == 65
        gladiator_2 = new_core.NewGladiator(75, 100, 10, 10, 'Loki')
        gladiator_1 = new_core.NewGladiator(65, 100, 11, 13, 'Thor')
        gladiator_2.attack(gladiator_1)
        assert gladiator_2.rage == 0
        assert gladiator_1.health == 45

    def test_punch(self):
        gladiator_1 = new_core.NewGladiator(50, 100, 10, 10, 'Thor')
        gladiator_2 = new_core.NewGladiator(75, 100, 10, 10, 'Loki')
        gladiator_1.punch(gladiator_2)
        assert gladiator_2.health == 55
        assert gladiator_1.rage == 0
        assert gladiator_1.health == 25
        gladiator_2 = new_core.NewGladiator(75, 0, 10, 10, 'Thor')
        gladiator_1 = new_core.NewGladiator(75, 0, 10, 10, 'Loki')
        gladiator_2.punch(gladiator_1)
        assert gladiator_1.rage == 0
        assert gladiator_2.health == 37

    def test_str(self):
        gladiator_1 = new_core.NewGladiator(50, 100, 10, 10, 'Thor')
        assert str(
            gladiator_1
        ) == "Gladiator: Thor || health: 50, rage: 100, damage_low: 10, damage_high: 10"

    def test_repr(self):
        gladiator_1 = new_core.NewGladiator(50, 100, 10, 10, 'Thor')
        assert repr(gladiator_1) == 'Gladiator(Thor: 50, 100, 10, 10)'
