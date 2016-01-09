{\rtf1\ansi\ansicpg1252\cocoartf1265\cocoasubrtf210
{\fonttbl\f0\fswiss\fcharset0 Helvetica;}
{\colortbl;\red255\green255\blue255;}
\paperw11900\paperh16840\margl1440\margr1440\vieww10800\viewh8400\viewkind0
\pard\tx566\tx1133\tx1700\tx2267\tx2834\tx3401\tx3968\tx4535\tx5102\tx5669\tx6236\tx6803\pardirnatural

\f0\fs24 \cf0 John Billing program Jan 2015\
\
Basic workflow\
\
At work.\
\
Enter data for each patient using google form JT patient 2\
This send info to google docs spreadsheet JT patient 2 responses\
\
At home - this only works on jot\'92s mac air for the moment\
Download JT patient 2 responses as a csv file into downloads folder \
Drag the downloaded file onto pat1.app (yellow dot). this changes its name to pat1.csv (also yellow dot) and opens terminal program.\
In terminal navigate to /Users/jtair/Dropbox/DEC/\'91billing program\'92\
run ./runbiller.sh\
This will start the main python program called jt_billing_1.py\
The program will ask for the date to print off (only on day at a time) in format \'97/\'97/\'97\'97\
The program will output the number of patient accounts printed\
The program prints each account as a web (html) file into the folder  /Users/jtair/Dropbox/DEC/Patient Invoices\
\
The presence of these files triggers an Automator program(print invoices.workflow(Folder Action)) that opens the accounts in Firefox. It then asks for confirmation that they were opened.  Press Yes. This deletes the accounts from the folder in Dropbox.\
Now to print the accounts which are in Firefox tabs\
Ensure you have Automator open.\
 In the task bar  have Finder,Launchpad,Firefox,Automator arranged from the left\
In Automator open print-tabs.workflow\
In the \'91LOOP\'94 pane ask to Loop Automatically the appropriate number of times\
Then hit \'91RUN\'94\
This start a simple Macro that does the job for you.\
Note that bulk bill and Garrison Accounts will be printed. Just discard.}