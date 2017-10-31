# get_banding(consultant, lower)
import re

import names_and_codes as nc


def get_banding(consultant, lower, message, loop_flag):
    if consultant not in nc.BANDERS or lower == '0':
        banding = '0'
        return banding, message, loop_flag
    while True:
        banding = input('Anal:   ')
        b_match = re.match(r'^[abq0]$', banding)
        if b_match:
            if banding == 'b':
                message += ' - Banding haemorrhoids'
            elif banding == 'a':
                message += '-Anal dilatation'
            elif banding == 'q':
                loop_flag = True
            if banding in {'a', 'b'} and consultant == 'Dr A Wettstein':
                message += ' - Bill bilateral pudendal blocks'
            break
        print('\033[31;1m' + 'TRY AGAIN!')
    return banding, message, loop_flag


if __name__ == '__main__':
    print(get_banding('Dr A Wettstein', 'co', 'test', False))
