import csv, os, webbrowser

# fund_fees is a dictionary with the key
# being the health fund ID and the data being a list with the consult fee
# and the unit fee for each fund.
# also import medicare codes
from module.fundfees import fund_fees, pe_code, col_code, age_code, sick_code

# these html codes for the account
from module.templates import base_html, table_html, terminal_html

while True:
    try:
        csvfile = open('/Users/jtair/Downloads/JT Patients 2016 (Responses) - Form responses 1.csv', 'r')
    except IOError:
        url = 'https://docs.google.com/spreadsheets/d/13p-ZYuUlmxo9fqnxru1Pg06xLES0gt_TwPJAw5nZrYU/edit?usp=sharing'
        webbrowser.open(url)
        break

    patlist = csv.reader(csvfile)
    number_to_print = 0         # output the number of accounts printed as a check
    input_day = input("input day in format --   ")
    input_month = input("input month in format --   ")
    for row in patlist:
        if input_day == row[0][0:2] and input_month == row[0][3:5]\
                and row[2] not in ['BB', 'GARRISON', 'OS', 'VA']:
            # extract data from csv file into variables - these are strings
            ep_date = row[0][0:2] + '-' + row[0][3:5] + '-' + row[0][6:10]
            patient = row[1]
            fund = row[2]
            endo = row[3]
            colon = row[4]
            age = row[5]
            sick = row[6]
            time = row[7]
            doctor = row[8]

            number_to_print += 1

            # get fees from module depending on fund
            fee_package = fund_fees[fund]
            consult = fee_package[0]
            consult_as_float = float(fee_package[0])
            unit = float(fee_package[1])

            # get time info and calculate time fee
            # the fourth digit in the time code gives the number of units
            time_length = int(time[3])
            time_fee = time_length * unit

            # calculate total_fee, initialise total_fee and add on consult
            total_fee = consult_as_float

            if endo == 'Yes':
                total_fee += (unit * 5)
            if endo == 'No' and colon == 'Yes':
                total_fee += (unit * 4)
            if age == 'Yes':
                total_fee += unit
            if sick == 'Yes':
                total_fee += unit

            # add on time fees
            total_fee = total_fee + (time_length * unit)

            # put data (including consult fee) into base_html code
            output_html = base_html % (patient, fund, ep_date, doctor, consult)
            # now append lines to the Fees Table at the bottom of the account
            if endo == 'Yes':
                output_html = output_html + table_html % (pe_code, 5 * unit)
                if colon == 'Yes':
                    output_html = output_html + table_html % (col_code, 0.00)
            if endo == 'No' and colon == 'Yes':
                output_html = output_html + table_html % (col_code, 4 * unit)
            if age == 'Yes':
                output_html = output_html + table_html % (age_code, unit)
            if sick == 'Yes':
                output_html = output_html + table_html % (sick_code, unit)

            # add on time fee
            output_html = output_html + table_html % (time, time_fee)
            # add on total fee
            output_html = output_html + table_html % ('Total Fee', total_fee)
            # add on terminal html code
            output_html = output_html + terminal_html

            # print output_html to file
            with open('/Users/jtair/Documents/Invoices/'
                      + row[1] + '.html', 'w') as ep_file:
                ep_file.write(output_html)
    csvfile.close()
    # final print out of number of accounts - done as a check

    if number_to_print == 0:
        print('***There seems to be no patients that day.***')
        print('     ***********')
    else:
        print('Number of accounts printed is {}'.format(number_to_print))
        print('      **********')
        # pyautogui.hotkey('fn', 'f2')
    more = input('Print more accounts? y or n :')
    if more == 'n':
        os.remove('/Users/jtair/Downloads/JT Patients 2016 (Responses) - Form responses 1.csv')
        break
