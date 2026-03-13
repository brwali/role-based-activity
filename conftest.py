import pytest

@pytest.fixture
def square_element():
    """A UI element where width and height are equal."""
    return {"base_width": 200, "base_height": 200, "targetSize": 400}

@pytest.fixture
def rectangular_element():
    """A UI element where width and height differ — exposes the semantic bug."""
    return {"base_width": 200, "base_height": 100, "targetSize": 400}
