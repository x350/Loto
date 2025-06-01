
def test_len_pouch(new_pouch):
    result = [item for item in new_pouch]
    assert len(result) == 90


def test_type_element_in_pouch(new_pouch):
    result = [item for item in new_pouch]
    assert isinstance(result[0], str)