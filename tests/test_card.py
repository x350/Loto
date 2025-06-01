

def test_type_user_card(new_card):
    assert isinstance(new_card.user, str)


def test_str_card(new_card):
    assert str(new_card) == new_card.user


def test_check_number_in_card(new_card, new_pouch):
    total_number = 0
    for item in new_pouch:
        result = new_card.check_number_in_card(item)
        if result:
            total_number += 1
    assert total_number == 15


