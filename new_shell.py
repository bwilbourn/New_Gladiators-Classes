import new_core as core


def battle(attacker, defender):
    choice = ''
    while True:
        choice = input("""{}, what's your move?\n
            \t-heal
            \t-attack
            \t-power punch
            \t-pass
            \t-quit\n""".format(attacker.name))
        if choice in ['heal', 'attack', 'power punch', 'pass', 'quit']:
            break
    if choice == 'attack':
        attacker.attack(defender)
    elif choice == 'power punch':
        attacker.punch(defender)
    elif choice == 'heal':
        attacker.heal()
    elif choice == 'quit':
        exit()
    else:
        print('pass')


def main():
    print('Prepare for total domination!! ')
    gladiator_1 = core.NewGladiator(100, 0, 10, 20, 'Thor')
    gladiator_2 = core.NewGladiator(100, 0, 10, 20, 'Loki')
    while True:
        print(gladiator_1)
        print(gladiator_2)

        battle(gladiator_1, gladiator_2)
        if gladiator_2.is_dead():
            print('{} is dead, {} wins!'.format(gladiator_2.name,
                                                gladiator_1.name))
            exit()

        battle(gladiator_2, gladiator_1)
        if gladiator_1.is_dead():
            print('{} is dead, {} wins!'.format(gladiator_1.name,
                                                gladiator_2.name))
            exit()


if __name__ == '__main__':
    main()