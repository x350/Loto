import pytest
from pouch import Pouch
from card import Card
from table import Table
@pytest.fixture
def new_pouch():
    return Pouch()


@pytest.fixture
def new_card():
    return Card(user='Bob', npc=False)


@pytest.fixture
def new_table(users):
    return Table(users)


