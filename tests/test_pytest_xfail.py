import pytest


@pytest.mark.xfail(reason='найден баг в приложении, из-за которого тест падает с ошибкой')
def test_with_bug():
    assert 1 == 2


@pytest.mark.xfail(reason='баг уже исправлен, но на тесте все еще висит маркировка xfail')
def test_without_bug():
    ...
