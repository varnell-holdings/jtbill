#! /usr/bin/python

'''Python 2.7.2 '''
import csv
import fundfees #this a dictionary called fund_fees with the key being the health fund ID and the data being a tuple of the consult fee and the unit fee for each fund.
import test_string_mod # this file contains a string variable called 'test_string_acc' which is the base html code for the account

pe_code = 20740
col_code = 20810
age_code = 25015
sick_code = 25000
tabl_html ='<tr><td>%s</td><td>$</td><td style="text-align:right"> %.2f</td></tr>\n' # this is the repetetive html that goes into the Fees Table
count = 0
date = raw_input("input date in format --/--/----  ==>  ")

with open('/Users/jtair/Downloads/JT Patients 2 (Responses) - Form responses 1.csv','rb') as csvfile:
    patlist = csv.reader(csvfile)
    for row in patlist:
        ep_time_stamp = row[0]
        ep_date = ep_time_stamp[:10]
        
        if ep_date == date and row[2] not in ['BB','GARRISON','OS','VA']:
            # extract data from csv file into variables - these are strings
            patient = row[1]
            fund = row[2]
            endo = row[3]
            colon = row[4]
            age = row[5]
            sick = row[6]
            time = row[7]
            doctor = row[8]
            count = count + 1

            #get fees from module depending on fund
            fee_package = fundfees.fund_fees[fund]
            consult = fee_package[0]
            consult_as_float = float(consult)
            unit = float(fee_package[1])
            #get time info and calculate time fee - the fourth digit in the time code gives the number of units
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
            total_fee = total_fee + (time_length * unit) # add on the time fees
            
                
                    
            #output to string to make html
            html_output = test_string_mod.test_string_acc %(patient,fund,ep_date,doctor,consult)
            #now we progressively append lines to the Fees Table at the bottom of the account
            if endo == 'Yes':
                html_output = html_output + tabl_html % (pe_code,5 * unit)
                if colon == 'Yes':
                    html_output = html_output + tabl_html % (col_code,0.00)
                    if age == 'Yes':
                        html_output = html_output + tabl_html % (age_code,unit)
                        if sick == 'Yes':
                            html_output = html_output + tabl_html % (sick_code,unit)
                    else:
                        if sick == 'Yes':
                            html_output = html_output + tabl_html % (sick_code, unit)
                elif age == 'Yes':
                        html_output = html_output + tabl_html % (age_code,unit)
                        if sick == 'Yes':
                            html_output = html_output + tabl_html % (sick_code,unit)
                elif sick == 'Yes':
                            html_output = html_output + tabl_html % (sick_code,unit)

            else:
                html_output = html_output + tabl_html % (col_code,4 * unit)
                if age == 'Yes':
                    html_output = html_output + tabl_html % (age_code,unit)
                    if sick == 'Yes':
                        html_output = html_output + tabl_html % (sick_code,unit)
                else:
                    if sick == 'Yes':
                        html_output = html_output + tabl_html % (sick_code,unit)
                
                


            
            
            html_output = html_output + tabl_html % (time, time_fee)
            html_output = html_output + tabl_html % ('Total Fee',total_fee)
            html_terminal = '</table>\n</body>\n</html>'
            html_output = html_output + html_terminal
            
            #print html_output to file
            ep_file = open('/Users/jtair/Dropbox/DEC/PATIENT INVOICES/' + row[1] + '.html','w')
            ep_file.write(html_output)
            ep_file.close()
print 'Number of accounts printed for %s is %s' % (date, count) # final print out of number of accounts done
