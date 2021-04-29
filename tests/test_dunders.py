import pytest
from data_classes.linked_list import LinkedList
from hash_table.hash_table import HashTable

@pytest.fixture  
def ht():
    ht_ = HashTable()
    ht_.add('doge', 300)
    ht_.add('bit-krypt', 100)
    return ht_


@pytest.fixture 
def ll():
    l_l = LinkedList()
    return l_l

    

def test_ll_len_with_val_as_iterable(ll):
    ll.insert(('a', 4))
    actual = len(ll)
    expected = 1
    assert actual == expected


def test_ll_len_with_empty_ll(ll):
    actual = len(ll)
    expected = 0
    assert actual == expected

def test_ht_contains_true(ht):
    actual = ht.contains('doge')
    expected = True
    assert actual == expected

def test_ht_contains_false(ht):
    actual = ht.contains('monkey')
    expected = False
    assert actual == expected

def test_ht_add(ht):
    ht.add('monkey', 10)
    actual = ht.contains('monkey')
    expected = True
    assert actual == expected


# @pytest.mark.skip('pending code')
def test_ht_str(ht):
    actual = ht.__str__()
    expected = 'hashtable instance, size: 256'
    assert actual == expected

# @pytest.mark.skip('pending code')
def test_ht_repr(ht):
    actual = ht.__repr__()
    expected = '3 entries found in HashTable'
    assert actual == expected


def test_ht_records(ht):
    actual = ht.__records__()
    expected = 3
    assert actual == expected


