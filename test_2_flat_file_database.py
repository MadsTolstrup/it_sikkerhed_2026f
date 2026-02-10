import os
import pytest
from src.flat_file.data_handler import Data_handler
from src.flat_file.user import User

test_file_name = "db_flat_file_test.json"

# Helper til at rydde op
def delete_json_files():
    if os.path.exists(test_file_name):
        os.remove(test_file_name)

# Setup og cleanup for hver test
@pytest.fixture(scope="function", autouse=True)
def cleanup_files():
    delete_json_files()
    yield
    delete_json_files()

# --- TESTS ---

def test_create_and_find_user():
    """
    RISIKO: Hvis denne test fejler, kan systemet ikke gemme data korrekt. 
    Det betyder, at alle nye brugeroplysninger går tabt permanent.
    """
    # GIVEN: En Data_handler instans og en tom database-fil
    data_handler = Data_handler(test_file_name)
    assert data_handler.get_number_of_users() == 0

    # WHEN: En ny bruger oprettes med et password i klartekst ("secret")
    data_handler.create_user("John", "Doe", "Main Street", 10, "secret")

    # THEN: Skal databasen indeholde 1 bruger
    assert data_handler.get_number_of_users() == 1
    user:User = data_handler.get_user_by_id(0)
    
    # THEN: Brugerens data skal matche, MEN passwordet skal være hashes (GDPR/Sikkerhed)
    assert user.first_name == "John"
    assert user.password != "secret"  # Verificerer at hashing er implementeret
    assert len(user.password) == 64   # SHA-256 hashes er altid 64 tegn lange

def test_disable_enable_user():
    """
    RISIKO: Hvis status-ændring fejler, kan man ikke spærre kompromitterede konti.
    Dette er en kritisk sikkerhedsrisiko for systemets integritet.
    """
    # GIVEN: En database med en bruger der er 'enabled'
    data_handler = Data_handler(test_file_name)
    data_handler.create_user("Jane", "Doe", "Side Street", 5, "password123")
    user:User = data_handler.get_user_by_id(0)
    assert user.enabled is True

    # WHEN: Funktionen disable_user kaldes
    data_handler.disable_user(0)
    
    # THEN: Skal brugerens status være ændret til False i systemet
    assert user.enabled is False
    # THEN: Passwordet skal stadig fremstå som en sikker hash
    assert len(user.password) == 64