import pytest
from src.linked_list import LinkedList
from src.linked_list import Node
from src.bubble_sort import bubble_sort1
from src.bubble_sort import bubble_sort2


@pytest.fixture(scope="session")
def default_node():
    return Node(5)


@pytest.fixture(scope="session")
def default_linked_list():
    return LinkedList(10)
