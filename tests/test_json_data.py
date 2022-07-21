from main import validate
import pytest


def test_validate_ok_email():
    """
    Тест валидации корректных данных
    """
    assert validate(email='denismalyshev@ginoice.com', password='4815@Test')


@pytest.mark.parametrize('email,', ['denismalyshevginoice.com',
                                    'denismalyshev@ginoice',
                                    '@ginoice.com',
                                    'denismalyshev'])
def test_validate_wrong_email(email):
    """
    Тест валидации некорретного эмейла
    """
    with pytest.raises(ValueError):
        validate(email, '4815@Test')


@pytest.mark.parametrize('password', ['4815@Te',
                                      '@Test',
                                      '4815@test'])
def test_validate_wrong_password(password):
    """
    Тест валидации некорретного пароля
    """
    with pytest.raises(ValueError):
        validate('denismalyshev@ginoice.com', password)
