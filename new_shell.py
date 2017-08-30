import new_core as core
from termcolor import cprint


def welcome_window():
    print('\n')
    cprint(
        '                (O)                                                       \n'
        '                <M                                                        \n'
        '     o          <M  PREPARE FOR TOTAL DOMINATION!!!                       \n'
        '    /| ......  /:M\----------------------------------------------,,,,,,   \n'
        '  (O)[]XXXXXX[]I:K+}=====<\{H\}>=====',
        'blue',
        attrs=['reverse', 'bold'],
        end="")
    cprint('MADE BY BRITNEY', 'yellow', attrs=['blink'], end="")
    cprint(
        '====================> \n'
        "    \| ^^^^^^  \:W/----------------------------------------------''''''   \n"
        '     o          <W  A Gladiator Battle Game                               \n'
        '                <W                                                        \n'
        '                (O)                                                       \n',
        'blue',
        attrs=['reverse', 'bold'],
        end="")
    print('\n')


def dead_skull():
    cprint(
        '                           uuuuuuu                        \n'
        '                       uu$$$$$$$$$$$uu                    \n'
        '                    uu$$$$$$$$$$$$$$$$$uu                 \n'
        '                   u$$$$$$$$$$$$$$$$$$$$$u                \n'
        '                  u$$$$$$$$$$$$$$$$$$$$$$$u               \n'
        '                 u$$$$$$$$$$$$$$$$$$$$$$$$$u              \n'
        '                 u$$$$$$$$$$$$$$$$$$$$$$$$$u              \n'
        '                 u$$$$$$"   "$$$"   "$$$$$$u              \n'
        '                 "$$$$"      u$u       $$$$"              \n'
        '                  $$$u       u$u       u$$$               \n'
        '                  $$$u      u$$$u      u$$$               \n'
        '                   "$$$$uu$$$   $$$uu$$$$"                \n'
        '                    "$$$$$$$"   "$$$$$$$"                 \n'
        '                      u$$$$$$$u$$$$$$$u                   \n'
        '                       u$"$"$"$"$"$"$u                    \n'
        '           uuu         $$u$ $ $ $ $u$$        uuu         \n'
        '           u$$$$        $$$$$u$u$u$$$       u$$$$         \n'
        '            $$$$$uu      "$$$$$$$$$"     uu$$$$$$         \n'
        '            u$$$$$$$$$$$uu    """""    uuuu$$$$$$$$$$     \n'
        '           $$$$"""$$$$$$$$$$uuu   uu$$$$$$$$$"""$$$"      \n'
        '            """      ""$$$$$$$$$$$uu ""$"""               \n'
        '                   uuuu ""$$$$$$$$$$uuu                   \n'
        '            u$$$uuu$$$$$$$$$uu ""$$$$$$$$$$$uuu$$$        \n'
        '            $$$$$$$$$""""           ""$$$$$$$$$$$"        \n'
        '             "$$$$$"                      ""$$$$""        \n'
        '               $$$"                         $$$$"         \n',
        'red',
        attrs=['blink'],
        end="")


def game_over():
    cprint(
        ' ██████╗  █████╗ ███╗   ███╗███████╗     ██████╗ ██╗   ██╗███████╗██████╗ ██╗          \n'
        '██╔════╝ ██╔══██╗████╗ ████║██╔════╝    ██╔═══██╗██║   ██║██╔════╝██╔══██╗██║          \n'
        '██║  ███╗███████║██╔████╔██║█████╗      ██║   ██║██║   ██║█████╗  ██████╔╝██║          \n'
        '██║   ██║██╔══██║██║╚██╔╝██║██╔══╝      ██║   ██║╚██╗ ██╔╝██╔══╝  ██╔══██╗╚═╝          \n'
        '╚██████╔╝██║  ██║██║ ╚═╝ ██║███████╗    ╚██████╔╝ ╚████╔╝ ███████╗██║  ██║██╗          \n'
        ' ╚═════╝ ╚═╝  ╚═╝╚═╝     ╚═╝╚══════╝     ╚═════╝   ╚═══╝  ╚══════╝╚═╝  ╚═╝╚═╝          \n',
        'cyan',
        attrs=['blink'],
        end="")


def prep_player_one():
    cprint(
        '          /)                                                 \n'
        '         //                                                  \n'
        '.-------| |--------------------------------------------.__   \n'
        '|WMWMWMW| |>>>>>>>>--THOR-->>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>:> \n'
        "`-------| |--------------------------------------------'^^   \n"
        '         \\\\                                                  \n'
        '          \)                                                 \n',
        'blue',
        attrs=['bold'])


def prep_player_two():
    cprint(
        '                                           &&                  \n'
        '                                           &&                  \n'
        ' ______________________________,___________&&&&              & \n'
        '/____________LOKI__________________________&@@@@@@@@@@@@@@@@&&}\n'
        '\\______________________________ ___________&@@@@@@@@@@@@@@@@&&}\n'
        '                               `           &&&&              & \n'
        '                                           &&                  \n'
        '                                           &&                  \n',
        'green',
        attrs=['bold'])


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
        red_text, white_text = gladiator_1.get_health_bar()
        print(red_text, end="")
        print(white_text, end="\n\n")

        print(gladiator_2)
        red_text, white_text = gladiator_2.get_health_bar()
        print(red_text, end="")
        print(white_text, end="\n\n")

        prep_player_one()
        battle(gladiator_1, gladiator_2)
        if gladiator_2.is_dead():
            dead_skull()
            game_over()
            print('{} is dead, {} wins!'.format(gladiator_2.name,
                                                gladiator_1.name))
            break

        prep_player_two()
        battle(gladiator_2, gladiator_1)
        if gladiator_1.is_dead():
            dead_skull()
            game_over()
            print('{} is dead, {} wins!'.format(gladiator_1.name,
                                                gladiator_2.name))
            break
    print(gladiator_1)
    red_text, white_text = gladiator_1.get_health_bar()
    print(red_text, end="")
    print(white_text, end="\n\n")

    print(gladiator_2)
    red_text, white_text = gladiator_2.get_health_bar()
    print(red_text, end="")
    print(white_text, end="\n\n")


if __name__ == '__main__':
    main()