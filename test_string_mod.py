
# test_string_mod.py

# the attributes in the <html> tag stop Firefox from printing out the address of the page - Firefox specific

test_string_acc = '''<html moznomarginboxes mozdisallowselectionprint>
<head>
<style>
th {text-align: left;}
</style>
</head>
<body>
<h2 style="text-align:center">Account for Anaesthetic</h2><br>
<h3>Dr John Tillett</h3>
7 Henry Lawson Drive<br>
Villawood NSW 2163<br>
<br>
Provider Number: 0307195H<br>
<br>
Account Enquiries: ph 0408 116 320 fax 02 8382 6602<br>
<br>
Patient Details:<br>
<br><br>
%s<br>
<br><br>
%s<br>
<br><br><br><br>
Date of Procedure: %s<br>
<br>
Place of Procedure: Diagnostic Endoscopy Centre, Darlinghurst, NSW 2010<br>
<br>
Procedure performed by Dr. %s<br>
<br><br><br>
<table>
<tr>
<th style="width:250px">Item Number</th>
<th></th> 
<th>Fee</th>
</tr>
<tr><td>17610</td><td>$</td><td style="text-align:right">%.2f</td></tr>'''
