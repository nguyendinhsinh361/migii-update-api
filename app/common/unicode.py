import re
import unicodedata


def contains_latin_or_special(text):
    latin_or_special_pattern = re.compile(
        r'^[a-zA-Z0-9!@#$%^&*()_+{}\[\]:;"\'<>,.?/\\|\-~`\s\n]+$')
    return bool(latin_or_special_pattern.match(text))


def is_special_character(text):
    special_character = re.compile(
        r'^[!@#$%^&*()_+{}\[\]:;"\'<>,.?/\\|\-~`]+$')
    return bool(special_character.match(text))


def is_latin(text):
    latin_character = re.compile(r'^[a-zA-Z0-9]+$')
    return bool(latin_character.match(text))


def flatten_recursive(lst):
    result = []
    for item in lst:
        if isinstance(item, list):
            result.extend(flatten_recursive(item))
        else:
            result.append(item)
    return result


def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        return False


def is_hiragana(text):
    for char in text:
        if unicodedata.name(char).startswith("HIRAGANA"):
            continue
        else:
            return False
    return True


def is_katakana(text):
    for char in text:
        if unicodedata.name(char).startswith("KATAKANA"):
            continue
        else:
            return False
    return True


def is_kanji(text):
    for char in text:
        if "CJK UNIFIED IDEOGRAPH" in unicodedata.name(char):
            return True
    return False


def is_break_sentence(word):
    return re.search(r'[.,!]$', word)


def contains_vietnamese(text):
    vietnamese_pattern = re.compile("[À-ỹỳỷỹằẳắấầẩẫậậắằẳầẩậẫâăđĐ]+")
    match = vietnamese_pattern.search(text)
    return match is not None


def contains_tag(text):
    pattern_angle_brackets = re.compile(r'<[^/][^>]*>')
    pattern_closing_angle_brackets = re.compile(r'</[^>]*>')
    if re.search(pattern_angle_brackets, text) or re.search(pattern_closing_angle_brackets, text):
        return True
    return False


def separate_text(text):
    parts = re.findall(r'(\d+|\D+)', text)
    return [part if part.isdigit() else part for part in parts]
