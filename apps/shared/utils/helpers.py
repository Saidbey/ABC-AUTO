def is_int(num: str):
    try:
        int(num)
        return True
    except ValueError:
        return False
