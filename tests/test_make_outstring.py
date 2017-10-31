# test_make_outstring


def make_outstring(out_formatted, doctor, anaesthetist, print_name,
                   consult, upper, colon, message):
    UPPER_DIC = {'0': 'none', 'pe': '30473-00', 'pb': '30473-01',
                 'od': '41819-00', 'pa': '30478-20', 'halo': '30478-20',
                 'pp': '30478-04', 'pv': '30476-02', 'bravo': '30490-00'}
    COLON_DIC = {'0': 'none', 'co': '32090-00', 'cb': '32090-01',
                 'cp': '32093-00', 'sc': '32084-00',
                 'sb': '32084-01', 'sp': '32087-00'}

    doc_surname = doctor.split()[-1]
    if doc_surname == 'Vivekanandarajah':
        doc_surname = 'Suhir'
    anaesthetist_surname = anaesthetist.split()[-1]
    docs_for_web = doc_surname + '/' + anaesthetist_surname

    upper = UPPER_DIC[upper]
    lower = COLON_DIC[colon]

    out_string = ('<b>%s</b> - %s - - %s - CONSULT:<b> %s </b>'
                  '- UPPER: %s - LOWER: %s'
                  '<b>%s</b> <br><br>\n') % (out_formatted, docs_for_web,
                                             print_name, consult, upper,
                                             lower, message)
    return out_string


result = make_outstring('9:30', 'Dr S Vivekanandarajah', 'Dr J Stevens',
                        'Ms Jo Bloggs', '116', '0', 'cp', 'testing!')
with open('out_string.html', 'w') as h:
    h.write(result)
print(result)
