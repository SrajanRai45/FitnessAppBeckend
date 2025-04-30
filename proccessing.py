def is_convertible_to_string(value):
    try:
        str(value)
        return True
    except Exception:
        return False
