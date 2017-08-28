import new_core


def main():
    print('Prepare for total domination!! ')
    gladiator_1 = new_core.NewGladiator(100, 0, 10, 20)
    gladiator_2 = new_core.NewGladiator(100, 0, 10, 20)
    while True:
        choice = input("""Gladiator1, what's your move?\n
        \t-heal
        \t-attack
        \t-power punch
        \t-pass
        \t-quit\n""")
        if choice == 'attack':
            gladiator_1.attack(gladiator_2)
            if gladiator_2.is_dead():
                print('Gladiator2 is dead, Gladiator1 wins. ')
                break
        elif choice == 'power punch':
            gladiator_1.punch(gladiator_2)
            if gladiator_2.is_dead():
                print('Gladiator2 is dead, Gladiator1 wins.')
                break
        elif choice == 'heal':
            gladiator_1.heal()
        elif choice == 'pass':
            print('pass')
        elif choice == 'quit':
            exit()
        print('gladiator_1:', gladiator_1)
        print('gladiator_2:', gladiator_2)

        choice = input("""Gladiator2, what's your move?\n
        \t-heal
        \t-attack
        \t-power punch
        \t-pass
        \t-quit\n""")
        if choice == 'attack':
            gladiator_2.attack(gladiator_1)
            if gladiator_1.is_dead():
                print('Gladiator1 is dead, Gladiator2 wins.')
                break
        elif choice == 'power punch':
            gladiator_2.punch(gladiator_1)
            if gladiator_1.is_dead():
                print('Gladiator1 is dead, Gladiator2 wins.')
                break
        elif choice == 'heal':
            gladiator_2.heal()
        elif choice == 'pass':
            print('pass')
        elif choice == 'quit':
            exit()
        print('gladiator_2:', gladiator_2)
        print('gladiator_1:', gladiator_1)


if __name__ == '__main__':
    main()