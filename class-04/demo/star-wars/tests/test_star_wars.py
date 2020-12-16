from star_wars import __version__
from star_wars.star_wars import JediMaster, SithLord, ForceUser
import pytest


def test_version():
    assert __version__ == '0.1.0'


# @pytest.mark.skip('Pending Code')
def test_jedi_master():
    assert JediMaster()


# @pytest.mark.skip('Pending Code')
def test_jedi_master_name_blank():
    player = JediMaster()
    actual = player.name
    expected = 'Random Jedi'
    assert actual == expected


# @pytest.mark.skip('Pending Code')
def test_jedi_master_name_luke():
    player = JediMaster('Luke')
    actual = player.name
    expected = 'Luke'
    assert actual == expected


# @pytest.mark.skip('Pending Code')
def test_jedi_master_name_luke_new(luke):
    actual = luke.name
    expected = 'Luke'
    assert actual == expected


# @pytest.mark.skip('Pending Code')
def test_jedi_master_attacking(luke):
    actual = luke.attacking()
    expected = 'Luke is Force attacking!'
    assert actual == expected


# @pytest.mark.skip('Pending Code')
def test_jedi_master_getting_attacked(luke):
    actual = luke.getting_hit()
    expected = 'Luke is being attacked!'
    assert actual == expected


# @pytest.mark.skip('Pending Code')
def test_sith_lord_name_darth_vader(vader):
    actual = vader.name
    expected = 'Darth Vader'
    assert actual == expected


# @pytest.mark.skip('Pending Code')
def test_sith_lord_attacking(vader):
    actual = vader.attacking()
    expected = 'Darth Vader is attacking!'
    assert actual == expected


# @pytest.mark.skip('Pending Code')
def test_non_sith_lord_getting_attacked(vader):
    actual = vader.getting_hit()
    expected = 'Darth Vader is being attacked!'
    assert actual == expected


# @pytest.mark.skip('Pending Code')
def test_jedi_class_method():
    actual = JediMaster.get_code()
    expected = 'There is no emotion!'
    assert actual == expected


# @pytest.mark.skip('Pending Code')
def test_sith_class_method():
    actual = JediMaster.get_code()
    expected = 'Peace is a lie!'
    actual = expected


# @pytest.mark.skip('Pending Code')
def test_force_user_count():
    actual = JediMaster.get_count()
    expected = 0
    assert actual == expected

    JediMaster('Luke')
    SithLord('Darth Vader')

    actual = ForceUser.get_count()
    expected = 2
    assert actual == expected


@pytest.fixture(autouse=True)
def counter_reset():
    JediMaster.count = 0
    SithLord.count = 0


@pytest.fixture
def luke():
    return JediMaster('Luke')


@pytest.fixture
def vader():
    return SithLord('Darth Vader')

