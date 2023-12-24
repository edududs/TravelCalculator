import re


def convert_string_to_float(value):
    cleaned_value = re.sub(r"[^\d.,]", "", value)
    cleaned_value = cleaned_value.replace(",", ".")
    try:
        return float(cleaned_value)
    except ValueError:
        return False


def convert_string_to_int(string):
    cleaned_value = re.sub(r"[^\d]", "", string)
    try:
        return int(cleaned_value)
    except ValueError:
        return None
