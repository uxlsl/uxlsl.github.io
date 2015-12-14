# content of conftest.py
import pytest
import smtplib

@pytest.fixture(scope="module",
                params=["smtp.163.com","smtp.126.com"]
        )
def smtp(request):
    smtp = smtplib.SMTP(request.params)
    def fin():
        print("teardown smtp")
        smtp.close()
    request.addfinalizer(fin)
    return smtp
