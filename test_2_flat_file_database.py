import json
import os
import pytest
from src.flat_file.data_handler import Data_handler
from src.flat_file.user import User

test_file_name = "db_flat_file_test.json"

def delete_json_files():
    if os.path.exists(test_file_name):
        os.remove(test_file_name)

@pytest.fixture(scope="function", autouse=True)
def cleanup_files():
    delete_json_files()
    yield
    delete_json_files()

# --- TESTS ---

def test_create_and_find_user():
    """
    RISIKO: Hvis denne test fejler, kan systemet ikke gemme data. 
    Dette fører til totalt datatab for brugerne.
    """
    # GIVEN: En tom database-fil
    data_handler = Data_handler(test_file_name)
    assert data_handler.get_number_of_users() == 0

    # WHEN: En ny bruger oprettes med alle påkrævede felter
    data_handler.create_user("John", "Doe", "Main Street", 10, "secret")

    # THEN: Skal databasen indeholde 1 bruger og kunne hente den korrekte data
    assert data_handler.get_number_of_users() == 1
    user:User = data_handler.get_user_by_id(0)
    assert user.first_name == "John"
    assert user.password == "secret"

def test_disable_enable_user():
    """
    RISIKO: Hvis deaktivering fejler, kan administratorer ikke spærre 
    kompromitterede konti, hvilket er en alvorlig sikkerhedsbrist.
    """
    # GIVEN: En database med en aktiv bruger
    data_handler = Data_handler(test_file_name)
    data_handler.create_user("John", "Doe", "Main Street", 11, "secret")
    user:User = data_handler.get_user_by_id(0)
    assert user.enabled == True

    # WHEN: Brugeren deaktiveres
    data_handler.disable_user(0)
    
    # THEN: Skal brugerens enabled-status være False
    assert user.enabled == False