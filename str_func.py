def foo(some_str):
    """Все буквы становятся вверхнем регистре"""
    return some_str.upper()
def capitalize_words(string):
    """делает заглавными первые буквы каждого слова в строчке"""
    words = string.split()
    capitalized_words = [word.capitalize() for word in words]
    return ' '.join(capitalized_words)
