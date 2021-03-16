"""Test for my functions.

Note: because these are 'empty' functions (return None), here we just test
  that the functions execute, and return None, as expected.
"""

def test_your_birth_date():
    assert callable(your_birth_date)
    assert your_birth_date('September', 12) != True
    assert your_birth_date('July', 12) != None

def test_your_zodiac_sign():
    assert callable(your_zodiac_sign)
    assert isinstance(your_zodiac_sign('September', 12), str)
    assert your_zodiac_sign('September', 12) == 'Virgo'

def test_zodiac_compatability():
    assert callable(zodiac_compatability)
    assert isinstance(zodiac_compatability('Virgo'),str)
    assert zodiac_compatability('Scorpio') == 'Pisces', 'Aries'

def run_tests():
    test_your_birth_date
    test_your_zodiac_sign
    test_zodiac_compatability