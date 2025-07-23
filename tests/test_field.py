import pytest
from field import Field


@pytest.mark.parametrize("width, height", [
    (10, 10), (100, 100), (1, 1)
])
def test_field_creation(width, height):
    field = Field(width, height)
    assert field.width == width
    assert field.height == height
    assert field.field.shape == (height, width)
    assert field.field.sum() == 0

@pytest.mark.parametrize("width, height", [
    (0, 0), (-1, 10), (4, -1)
])
def test_invalid_field_creation(width, height):
    with pytest.raises(AssertionError):
        Field(width, height)
