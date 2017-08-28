from random import randint


class NewGladiator:
    """ Creates a new gladiator. """

    def __init__(self, health, rage, damage_low, damage_high):
        """ Each new gladiator has health, rage, damage_low,
        and damage_high. """

        self.health = health
        self.rage = rage
        self.damage_low = damage_low
        self.damage_high = damage_high

    def is_dead(self):
        if self.health <= 0:
            return True
        else:
            return False

    def heal(self):
        if self.rage >= 10:
            self.rage = max(self.rage - 10, 0)
            self.health = min(self.health + 5, 100)
            return self

    def attack(self, other):
        damage_dealt = randint(self.damage_low, self.damage_high)
        if randint(1, 100) <= self.rage:
            other.health -= damage_dealt * 2
            self.rage = 0
        else:
            other.health -= damage_dealt
            self.rage += 15
        return self, other

    def punch(self, other):
        super_punch = self.damage_high
        other.health -= super_punch * 2
        self.rage = 0
        self.health = self.health * .5

    def __str__(self):
        return 'health: {0}, rage: {1}, damage_low: {2}, damage_high: {3}'.format(
            self.health, self.rage, self.damage_low, self.damage_high)

    def __repr__(self):
        return 'Gladiator({0}, {1}, {2}, {3})'.format(
            self.health, self.rage, self.damage_low, self.damage_high)
