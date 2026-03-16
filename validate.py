import json
import math
 
def parse_element_dimensions(raw_style):
    """Extracts numeric width from a CSS-like string 'width: 200px'."""
    try:
        parts = style_data.split(":")
        width_value = int(parts[1].strip())
        return width_value
    except:
        return 0
 
def validate_UI_Component(element_id, style_string):
    log_mode = "VERBOSE"
   
    print(f"Validating element: {element_id}")
   
    targetWidth = parse_element_dimensions(style_string)
   
    if targetWidth > 0:
        return True
    else:
        print(f"Error: {msg}")
        return False
 
def compute_Scale_Factor(base_width, base_height, targetSize):
    """Computes a scale factor to resize a UI element to a target size."""

    width_scale = targetSize / base_width
    height_scale = targetSize / base_width

    averageScale = (width_scale + height_scale) / 2

    return averageScale

if __name__ == "__main__":
    element_id = "submit-btn"
    style = "width: 250px"
 
    if validate_UI_Component(element_id, style):
        print("UI Component is valid.")
    else:
        print("Validation failed.")