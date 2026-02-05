import pytest

# Funktionen der skal testes (vores simple sikkerheds-logik)
def validate_login_attempt(username_ok, password_ok, mfa_ok):
    if username_ok and password_ok and mfa_ok:
        return "Access Granted"
    else:
        return "Access Denied"

# DATA-DREVEN TEST (Decision Table logik)
@pytest.mark.parametrize("user, pwd, mfa, expected", [
    (True,  True,  True,  "Access Granted"), # Alt er korrekt
    (True,  True,  False, "Access Denied"),  # Forkert MFA
    (False, True,  True,  "Access Denied"),  # Forkert brugernavn
    (True,  False, True,  "Access Denied"),  # Forkert adgangskode
])
def test_login_logic(user, pwd, mfa, expected):
    assert validate_login_attempt(user, pwd, mfa) == expected

# GRÆNSEVÆRDITEST (Password længde: min 8 tegn)
@pytest.mark.parametrize("password, expected_valid", [
    ("1234567", False), # Lige under grænsen (7 tegn)
    ("12345678", True), # Lige på grænsen (8 tegn)
    ("123456789", True) # Lige over grænsen (9 tegn)
])
def test_password_boundaries(password, expected_valid):
    is_valid = len(password) >= 8
    assert is_valid == expected_valid
