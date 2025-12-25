import pytest
from crm import User, where, table
from tinydb import TinyDB
from tinydb.storages import MemoryStorage

@pytest.fixture
def setup_db():
    User.DB = TinyDB(storage=MemoryStorage)

@pytest.fixture
def user(setup_db):
    u =  User(first_name="Boris",
              last_name="Danmitonde",
              phone_number="(+221) 782507858",
              address="Rue 10, Geneve")
    u.save()
    return u


def test_last_name(user):
    assert user.last_name == "Danmitonde"


def test_first_name(user):
    assert user.first_name == "Boris"


def test_phone_number(user):
    assert user.phone_number == "(+221) 782507858"


def test_address(user):
    assert user.address == "Rue 10, Geneve"


def test_full_name(user):
    assert user.full_name == "Boris Danmitonde"


def test_db_instance(user):
    assert isinstance(user.db_instance, table.Document)
    assert user.db_instance["first_name"] == "Boris"
    assert user.db_instance["last_name"] == "Danmitonde"
    assert user.db_instance["phone_number"] == "(+221) 782507858"
    assert user.db_instance["address"] == "Rue 10, Geneve"


def test_not_db_instance(setup_db):
    u = User(first_name="Boris",
             last_name="Danmitonde",
             phone_number="(+221) 782507858",
             address="Rue 10, Geneve")
    assert u.db_instance is None


def test__check_phone_number(setup_db):
    u = User(first_name="Boris",
             last_name="Danmitonde",
             phone_number="(+221) 782507858",
             address="Rue 10, Geneve")
    u.save(validate_data=True)
    assert u.exists() is True


def test__check_phone_number_wrong_length(setup_db):
    u = User(first_name="Boris",
             last_name="Danmitonde",
             phone_number="(+221) 78250",
             address="Rue 10, Geneve")
    with pytest.raises(ValueError) as err:
        u._check_phone_number()

    assert "invalide" in str(err.value)


def test__check_phone_number_not_digits(user):
    u = User(first_name="Boris",
             last_name="Danmitonde",
             phone_number="(+221) abcd",
             address="Rue 10, Geneve")
    with pytest.raises(ValueError) as err:
        u._check_phone_number()
    assert "invalide" in str(err.value)


def test__check_names_no_first_name(setup_db):
    u = User(first_name="",
             last_name="Danmitonde",
             phone_number="(+221) 78250",
             address="Rue 10, Geneve")
    with pytest.raises(ValueError) as err:
        u._check_names()
    assert "Le prénom et le nom de famille ne peuvent pas être vides." in str(err.value)


def test__check_names_no_last_name(setup_db):
    u = User(first_name="Boris",
             last_name="",
             phone_number="(+221) 78250",
             address="Rue 10, Geneve")
    with pytest.raises(ValueError) as err:
        u._check_names()
    assert "Le prénom et le nom de famille ne peuvent pas être vides." in str(err.value)


def test__check_names_empty(setup_db):
    u = User(first_name="",
             last_name="",
             phone_number="(+221) 78250",
             address="Rue 10, Geneve")
    with pytest.raises(ValueError) as err:
        u._check_names()
    assert "Le prénom et le nom de famille ne peuvent pas être vides." in str(err.value)


def test__check_names_invalid_characters(setup_db):
    u = User(first_name="Boris%$¨$$$",
             last_name="Danmitonde",
             phone_number="(+221) 78250",
             address="Rue 10, Geneve")
    with pytest.raises(ValueError) as err:
        u._check_names()
    assert "invalide" in str(err.value)


def test__check_names(setup_db):
    u = User(first_name="Boris",
             last_name="Danmitonde",
             phone_number="(+221) 78250",
             address="Rue 10, Geneve")
    assert u._check_names() is None


def test_exists(user):
    assert user.exists() is True


def test_not_exists(setup_db):
    u = User(first_name="Boris",
             last_name="Danmitonde",
             phone_number="(+221) 782507858",
             address="Rue 10, Geneve")

    assert u.exists() is False


def test_delete_existing_user(user):
    assert len(user.delete()) > 0


def test_delete_not_existing_user(setup_db):
    u = User(first_name="Boris",
             last_name="Danmitonde",
             phone_number="(+221) 782507858",
             address="Rue 10, Geneve")
    assert len(u.delete()) == 0


def test_save_existing_user(user):
    saved = user.save()
    assert isinstance(saved, int)
    assert saved == -1


def test_save_not_existing_user(setup_db):
    u = User(first_name="Boris",
             last_name="Danmitonde",
             phone_number="(+221) 782507858",
             address="Rue 10, Geneve")
    saved = u.save()
    assert isinstance(saved, int)
    assert saved > 0
