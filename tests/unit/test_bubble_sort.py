import pytest
from src.bubble_sort import bubble_sort1
from src.bubble_sort import bubble_sort2


@pytest.mark.parametrize(
    "input_lst, output_lst",
    [
        ([4, 11, 0, 6, 3, 17, 10, 14, 15, 12], [0, 3, 4, 6, 10, 11, 12, 14, 15, 17]),
        ([], []),
        ([1], [1]),
        ([4, 0], [0, 4])
    ]
)
class TestBubbleSort:
    def test_bubble1(self, input_lst, output_lst):
        assert bubble_sort1(input_lst) == output_lst

    def test_bubble2(self, input_lst, output_lst):
        assert bubble_sort2(input_lst) == output_lst
