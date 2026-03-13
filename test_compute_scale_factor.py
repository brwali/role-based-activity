from validate import compute_Scale_Factor

def test_scale_factor_square_element(square_element):
    """
    With base_width=200, base_height=200, targetSize=400:
    """
    result = compute_Scale_Factor(**square_element)
    assert result == 2.0

def test_scale_factor_rectangular_element(rectangular_element):
    """
    With base_width=200, base_height=100, targetSize=400:
    """
    result = compute_Scale_Factor(**rectangular_element)
    assert result == 3.0
