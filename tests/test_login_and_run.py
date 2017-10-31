# test_login_and_run.py
from pprint import pprint

ANAESTHETISTS = {'tt': 'Dr T Thompson', 'sv': 'Dr S Vuong',
                 'cb': 'Dr C Brown', 'jr': 'Dr J Riley',
                 'js': 'Dr J Stevens', 'db': 'Dr D Bowring',
                 'gos': "Dr G O'Sullivan", 'jt': 'Dr J Tester',
                 'rw': 'Dr Rebecca Wood', 'mm': 'Dr M Moyle',
                 'locum': 'locum', '1545': 'Dr J Tillett'}


def login_and_run():
    data_string = 'anaesthetist,nurse,asa,upper,lower,banding,consult,message,\
    time_in_theatre,ref,full_fund,insur_code,fund_number,clips,varix_flag,\
    varix_lot, in_formatted,out_formatted,doctor,mrn,print_name,address,dob,\
    mcn,time_code,acct_proc_date,upper_done,upper_done,asa_three,invoice,\
    today_for_db'

    data_list = data_string.split(',')
    data_list = [_.lstrip() for _ in data_list]
    data_length = len(data_list)
    ep_data = {d: e for d, e in zip(data_list, [''] * data_length)}

    while True:
        initials = input('Anaesthetist:  ').lower()
        if initials in ANAESTHETISTS:
            ep_data['anaesthetist'] = ANAESTHETISTS[initials]
            break
    print ('Welcome Dr {}! Press Enter to continue.'.format(
        ep_data['anaesthetist'].split()[-1]))
    # while True:
    #     bill(ep_data)
    return ep_data


if __name__ == '__main__':
    pprint(login_and_run())
