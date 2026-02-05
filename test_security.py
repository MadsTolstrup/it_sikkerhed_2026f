import pytest

# En simpel funktion der simulerer login-logik
def validate_login(username_ok, password_ok, mfa_ok):
    if username_ok and password_ok and mfa_ok:
        return "Access Granted"
    else:
        return "Access Denied"

# DATA-DREVEN TEST (Decision Table + Boundary Test)
@pytest.mark.parametrize("user, pwd, mfa, expected", [
    (True,  True,  True,  "Access Granted"), # R2 i diasshow
    (True,  True,  False, "Access Denied"),  # R3 i diasshow
    (False, True,  True,  "Access Denied"),  # Forkert bruger
    (True,  False, True,  "Access Denied"),  # Forkert password
])
def test_login_decision_table(user, pwd, mfa, expected):
    assert validate_login(user, pwd, mfa) == expected

# En hurtig Boundary Test for password længde (min 8 tegn)
@pytest.mark.parametrize("password, expected", [
    ("1234567", False), # Lige under (7)
    ("12345678", True), # Lige på (8)
    ("123456789", True) # Lige over (9)
])
def test_password_boundary(password, expected):
    is_valid = len(password) >= 8
    assert is_valid == expected