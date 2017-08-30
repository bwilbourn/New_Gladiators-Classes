from random import randint
from termcolor import colored


class NewGladiator:
    """ Creates a new gladiator. """

    def __init__(self, health, rage, damage_low, damage_high, name):
        """ 
        (int, int, int, int, str)
        Each new gladiator has health, rage, damage_low,
        and damage_high. """

        self.health = health
        self.rage = rage
        self.damage_low = damage_low
        self.damage_high = damage_high
        self.name = name

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

        other.health = max(other.health, 0)
        return self, other

    def punch(self, other):
        super_punch = self.damage_high
        other.health -= super_punch * 2
        other.health = max(other.health, 0)
        self.rage = 0
        self.health = self.health // 2

    def get_health_bar(self):
        if self.health <= 45:
            attrs = ['blink']
        else:
            attrs = []

        total_blocks = 50
        red_blocks = self.health // 2
        white_blocks = total_blocks - red_blocks
        red_health = colored(red_blocks * '@', 'red', attrs=attrs)
        missing_health = colored(white_blocks * '@', 'white', attrs=attrs)
        return red_health + missing_health

    def __str__(self):
        return 'Gladiator: {} || health: {}, rage: {}, damage_low: {}, damage_high: {}'.format(
            self.name, self.health, self.rage, self.damage_low,
            self.damage_high)

    def __repr__(self):
        return 'Gladiator({0}: {1}, {2}, {3}, {4})'.format(
            self.name, self.health, self.rage, self.damage_low,
            self.damage_high)
