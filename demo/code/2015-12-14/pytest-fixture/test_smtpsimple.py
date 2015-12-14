import pytest

@pytest.fixture
def smtp():
    import smtplib
    return smtplib.SMTP("smtp.163.com")

def test_ehlo(smtp):
    print(type(smtp))
    response, msg = smtp.ehlo()
    assert response == 250
    assert 0
