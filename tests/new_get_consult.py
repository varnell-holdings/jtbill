# new_get_consult.py

import names_and_codes as nc

import colorama

colorama.init(autoreset=True)


def get_consult(consultant, upper, lower, time_in_theatre, loop_flag):
    consult = 'none'

    if consultant == 'Dr A Stoita' or consultant not in nc.PARTNERS:
        return (consult, loop_flag)

    if consultant in nc.CONSULTERS:
        while True:
            consult = input('Consult 110 or 116: ')
            if consult == 'q':
                loop_flag = True
                break
            if consult in {'110', '116'}:
                break
            print('\033[31;1m' + 'TRY AGAIN!')
        return (consult, loop_flag)

    if consultant == 'Dr R Feller':
        print("Dr Feller does 110's on new patients only")
        while True:
            consult = input('110 or 0: ')
            if consult == 'q':
                loop_flag = True
                break
            if consult in {'110', '0'}:
                break
            print('\033[31;1m' + 'TRY AGAIN!')
        return (consult, loop_flag)

    if consultant == 'Dr C Bariol':
        while True:
            consult = input('110, 116, 0: ')
            if consult == 'q':
                loop_flag = True
                break
            if consult in {'110', '116', '0'}:
                break
            print('\033[31;1m' + 'TRY AGAIN!')
        return (consult, loop_flag)

    if consultant == 'Dr D Williams':
        if int(time_in_theatre) > 30 and lower != '0':
            print('\033[31;1m' + 'Dr Williams will bill a 110.')
            while True:
                response = input('Confirm y/n ')
                if response.lower() in {'y', 'n'}:
                    break
            if response == 'y':
                consult = '110'
        return (consult, loop_flag)

    if consultant == 'Dr C Vickers':
        pu = upper in {'pb', 'pp', 'od'}
        pl = lower in {'cb', 'cp', 'sb', 'sp', 'csp'}
        if pu or pl:
            consult = '116'
        return (consult, loop_flag)
