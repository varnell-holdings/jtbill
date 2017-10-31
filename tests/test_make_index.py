# test_make_episode_string.py

import datetime
import glob
import os.path
import shutil
import sys


sys.path.append('/Users/jtair/Dropbox/decprograms/billingprogram/new_billing-development')

from functions import *


if __name__ == '__main__':
    print(make_index(make_episode_string(
        '9:42', 'Dr S Ghaly', 'Ms Penny Rees', None,
        None, '32090-00', 'Testing', 'Dr J Tillett', 'R1')))
