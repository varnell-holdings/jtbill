loop_flag = False


def consult_check(consult, doctor, upper, lower):
    doc_test = doctor in {'Dr A Wettstein', 'Dr S Ghaly',
                          'Dr S Vivekanandarajah'}
    path = upper in {'pb', 'pp'} or lower in {'cb', 'cp', 'sb', 'sp'}
    cv_test = (doctor == 'Dr C Vickers') and path
    return doc_test or cv_test


def get_consult(doctor, upper, lower, loop_flag):
    while True:
        consult = input('Consult: ')
        if consult == '0':
            consult = 'none'
        if consult == 'q':
            loop_flag = True
            break
        if consult in {'110', '116', 'none'}:
            break
        print('TRY AGAIN!')

    if consult_check(consult, doctor, upper, lower) and loop_flag is False:
        print('Confirm with {} that he/she'
              ' does not want a consult'.format(doctor))
        while True:
            consult = input('Consult either 0,110,116: ')
            if consult == '0':
                consult = 'none'
            if consult in {'110', '116', 'none'}:
                break

    return consult, loop_flag


if __name__ == '__main__':
    print(get_consult('Dr A Wettstein', '0', 'co', loop_flag))
