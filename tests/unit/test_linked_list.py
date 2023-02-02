import pytest
from src.linked_list import Node
from src.linked_list import LinkedList


@pytest.mark.parametrize(
    "input_value, output_value, input_next",
    [
        (100, 100, None),
        (0, 0, None),
        (-1, -1, None),
        ("a", "a", None),
        ([1, 2, 3], [1, 2, 3], None)
    ]
)
def test_default_node(input_value, output_value, input_next):
    node = Node(input_value)
    assert node.value == output_value
    assert node.next == input_next
