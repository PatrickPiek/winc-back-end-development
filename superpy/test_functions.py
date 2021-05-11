from functions import generate_ean13


def test1_generate_ean13():
    assert generate_ean13(
        [9, 7, 8, 0, 1, 4, 1, 0, 2, 6, 6, 2]) == '9780141026626'


def test2_generate_ean13():
    assert generate_ean13('978014102662') == '9780141026626'


def test3_generate_ean13():
    assert generate_ean13(978014102662) == '9780141026626'


def test4_generate_ean13():
    ean = generate_ean13('abc')
    assert [isinstance(int(i), int) for i in str(ean)]


test1_generate_ean13()
test2_generate_ean13()
test3_generate_ean13()
test4_generate_ean13()
