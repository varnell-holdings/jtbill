import sys
sys.path.append('/Users/jtair/Dropbox/decprograms/billingprogram/new_billing-development')

import  login_and_run

def test_login_and_run(monkeypatch):
    monkeypatch.setattr( login_and_run, 'get_anaesthetist', lambda: 'Dr J Tester')
    monkeypatch.setattr(login_and_run, 'input', lambda: '')
    login_and_run.login_and_run('r2')
