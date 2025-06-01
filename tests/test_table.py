import pytest


@pytest.mark.parametrize('users', [2])
def test_create_users(new_table):
    assert new_table._users == 2


@pytest.mark.parametrize('users', [2])
def test_str_tabel(new_table):
    assert len(str(new_table).split(',')) == 2