import new_core as core
from termcolor import cprint


def welcome_window():
    print('\n')
    cprint(
        '                (O)\n'
        '                <M\n'
        '     o          <M  PREPARE FOR TOTAL DOMINATION!!!\n'
        '    /| ......  /:M\----------------------------------------------,,,,,,\n'
        '  (O)[]XXXXXX[]I:K+}=====<\{H\}>=====',
        'yellow',
        end="")
    cprint('MADE BY BRITNEY', 'cyan', attrs=['blink'], end="")
    cprint(
        '====================>\n'
        "    \| ^^^^^^  \:W/----------------------------------------------''''''\n"
        '     o          <W  A Gladiator Battle Game\n'
        '                <W\n'
        '                (O)\n',
        'yellow',
        end="")
    print('\n')


def prep_player_one():
    cprint('          /)                                                 \n'
           '         //                                                  \n'
           '.-------| |--------------------------------------------.__   \n'
           '|WMWMWMW| |>>>>>>>>--THOR-->>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>:> \n'
           "`-------| |--------------------------------------------'^^   \n"
           '         \\\\                                                  \n'
           '          \)                                                 \n',
           'blue')


def prep_player_two():
    cprint('                                           &&                  \n'
           '                                           &&                  \n'
           ' ______________________________,___________&&&&              & \n'
           '/____________LOKI__________________________&@@@@@@@@@@@@@@@@&&}\n'
           '\\______________________________ ___________&@@@@@@@@@@@@@@@@&&}\n'
           '                               `           &&&&              & \n'
           '                                           &&                  \n'
           '                                           &&                  \n',
           'green')


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
    welcome_window()
    gladiator_1 = core.NewGladiator(100, 0, 10, 20, 'Thor')
    gladiator_2 = core.NewGladiator(100, 0, 10, 20, 'Loki')
    while True:
        print(gladiator_1)
        cprint(gladiator_1.get_health_bar(), 'red', end="\n\n")

        print(gladiator_2)
        cprint(gladiator_2.get_health_bar(), 'red', end="\n\n")

        prep_player_one()
        battle(gladiator_1, gladiator_2)
        if gladiator_2.is_dead():
            print('{} is dead, {} wins!'.format(gladiator_2.name,
                                                gladiator_1.name))
            break

        prep_player_two()
        battle(gladiator_2, gladiator_1)
        if gladiator_1.is_dead():
            print('{} is dead, {} wins!'.format(gladiator_1.name,
                                                gladiator_2.name))
            break
    print(gladiator_1)
    cprint(gladiator_1.get_health_bar(), 'red', end="\n\n")

    print(gladiator_2)
    cprint(gladiator_2.get_health_bar(), 'red', end="\n\n")


if __name__ == '__main__':
    main()