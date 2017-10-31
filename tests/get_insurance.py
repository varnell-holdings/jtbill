import pprint

import colorama
import names_and_codes as nc

colorama.init(autoreset=True)


def get_insurance(asa, anaesthetist, message):
    if asa is None or anaesthetist not in nc.BILLING_ANAESTHETISTS:
        ref = full_fund = insur_code = fund_number = 'na'
        return insur_code, fund_number, ref, full_fund, message
    # get full_fund and insur_code
    while True:
        fund_input = input('Fund:   ')
        if fund_input in nc.FUND_ABREVIATION:
            insur_code = nc.FUND_ABREVIATION[fund_input]
            break
        print('Your choices are.')
        pprint.pprint(nc.FUND_ABREVIATION)

    if insur_code == 'ahsa':
        while True:
            ahsa_fund = input('Fund first two letters or o or h: ')
            if ahsa_fund == 'h':
                pprint.pprint(nc.AHSA_DIC)
            elif ahsa_fund not in nc.AHSA_DIC:
                print('\033[31;1m' + 'TRY AGAIN!')
                continue
            elif ahsa_fund == 'o':
                full_fund = input('Enter Fund Name:  ')
                break
            else:
                full_fund = nc.AHSA_DIC[ahsa_fund]
                break
    elif insur_code == 'os':
        while True:
            os_fund = input('OS patient Fund: ')
            if os_fund in {'h', 'b', 'm', 'n', 'o'}:  # o means not in fund
                break
            print('\033[31;1m' + "Choices: h, b, m, n, o")
        os_insur_code = nc.FUND_ABREVIATION[os_fund]
        full_fund = nc.FUND_DIC[os_insur_code]
    else:
        full_fund = nc.FUND_DIC[insur_code]
    print()
    # get ref and fund_number
    if full_fund == 'Overseas':  # overseas patient not in fund
        ref = fund_number = 'na'
    elif insur_code == 'os':  # overseas patient in fund
        ref = 'na'
        fund_number = input('F Num:  ')
        message = ' JT will bill {}.'.format(full_fund)
    elif insur_code == 'ga':
        ref = input('Episode ID: ')
        print()
        fund_number = input('Approval Number: ')
    elif insur_code == 'va':
        ref = 'na'
        fund_number = input('VA Num: ')
    elif insur_code == 'bb':
        while True:
            ref = input('Ref:    ')
            if ref.isdigit() and len(ref) == 1 and ref != '0':
                break
        fund_number = 'na'
        message += ' JT will bulk bill'
    else:
        while True:
            ref = input('Ref:    ')
            if ref.isdigit() and len(ref) == 1 and ref != '0':
                break
            print('\033[31;1m' + 'TRY AGAIN! Single digit only.')
        print()
        while True:
            fund_number = input('F Num:  ')
            if fund_number[:-1].isdigit():  # med private has a final letter
                break
            print('\033[31;1m' + 'TRY AGAIN!')

    return insur_code, fund_number, ref, full_fund, message


if __name__ == '__main__':
    print(get_insurance('92059-39', 'Dr J Tillett', ''))
