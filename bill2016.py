#! /usr/bin/python

'''Python 2.7.2 '''
import csv

# this a dictionary called fund_fees with the key
# being the health fund ID and the data being a list with the consult fee
# and the unit fee for each fund.
from module.fundfees import fund_fees

# this is the base html code for the account
from module.templates import base_html

# html snippet that is appended to base_html to build the fee part of account
from module.templates import table_html

# medicare codes
from module.fundfees import pe_code
from module.fundfees import col_code
from module.fundfees import age_code
from module.fundfees import sick_code

number_to_print = 0

input_day = raw_input("input day in format --   ")
input_month = raw_input("input month in format --   ")

with open('/Users/jtair/Downloads/JT Patients 2016.csv', 'rb') as csvfile:
    patlist = csv.reader(csvfile)
    for row in patlist:
        ep_time_stamp = row[0]
        ep_day = ep_time_stamp[8:10]
        ep_month = ep_time_stamp[5:7]
        ep_date = ep_day + '-' + ep_month + '-' + ep_time_stamp[0:4]

        if ep_day == input_day and ep_month == input_month\
                and row[2] not in ['BB', 'GARRISON', 'OS', 'VA']:
            # extract data from csv file into variables - these are strings
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
            consult_as_float = float(consult)
            unit = float(fee_package[1])
            # get time info and calculate time fee
            # the fourth digit in the time code gives the number of units
            time_length = int(time[3])
            time_fee = time_length * unit

            # calculate total_fee
            total_fee = consult_as_float
            if endo == 'Yes':
                total_fee = total_fee + (5 * unit)
                if age == 'Yes':
                    total_fee = total_fee + unit
                    if sick == 'Yes':
                        total_fee = total_fee + unit
                else:
                    if sick == 'Yes':
                        total_fee = total_fee + unit
            else:
                total_fee = total_fee + (4 * unit)
                if age == 'Yes':
                    total_fee = total_fee + unit
                    if sick == 'Yes':
                        total_fee = total_fee + unit
                else:
                    if sick == 'Yes':
                        total_fee = total_fee + unit
            total_fee = total_fee + (time_length * unit)  # add on time fees

            # output to string to make html
            html_output = base_html % (patient, fund, ep_date, doctor, consult)
            # now append lines to the Fees Table at the bottom of the account
            if endo == 'Yes':
                html_output = html_output + table_html % (pe_code, 5 * unit)
                if colon == 'Yes':
                    html_output = html_output + table_html % (col_code, 0.00)
                    if age == 'Yes':
                        html_output = html_output + table_html % (age_code, unit)
                        if sick == 'Yes':
                            html_output = html_output + table_html % (sick_code, unit)
                    else:
                        if sick == 'Yes':
                            html_output = html_output + table_html % (sick_code, unit)
                elif age == 'Yes':
                        html_output = html_output + table_html % (age_code, unit)
                        if sick == 'Yes':
                            html_output = html_output + table_html % (sick_code, unit)
                elif sick == 'Yes':
                            html_output = html_output + table_html % (sick_code, unit)

            else:
                html_output = html_output + table_html % (col_code, 4 * unit)
                if age == 'Yes':
                    html_output = html_output + table_html % (age_code, unit)
                    if sick == 'Yes':
                        html_output = html_output + table_html % (sick_code, unit)
                else:
                    if sick == 'Yes':
                        html_output = html_output + table_html % (sick_code, unit)

            html_output = html_output + table_html % (time, time_fee)
            html_output = html_output + table_html % ('Total Fee', total_fee)
            html_terminal = '</table>\n</body>\n</html>'
            html_output = html_output + html_terminal

            # print html_output to file
            with open('/Users/jtair/Dropbox/DEC/PATIENT INVOICES/' + row[1] + '.html', 'w') as ep_file:
                ep_file.write(html_output)

# final print out of number of accounts done
print 'Number of accounts printed is {}'.format(number_to_print)
