"""
    language.tokens is a module for splitting text into word-like tokens.

    TODO: context, handle char like '-' differently inside a word

"""

def __space(s, filter_fn):
    def __replace(c):
        # Supports Unicode, string.punctuation is ASCII only.
        if filter_fn(c):
            return c
        return ' ' + c + ' '
    return ''.join([__replace(c) for c in s])

def space_punct(s):
    """
        >>> space_punct('This is not a test.')
        'This is not a test . '

        >>> space_punct("Don't know, it's carbon-neutral...")
        "Don ' t know ,  it ' s carbon - neutral .  .  . "

        >>> space_punct("Где-то в Нью-Йорке говорилось «7 разбойниц!»")
        'Где - то в Нью - Йорке говорилось  « 7 разбойниц !  » '

    """
    return __space(s, lambda c: c.isalnum() or c.isspace())

def on_whitespace(s):
    """
        Returns tokens taking whitespace as word boundaries

        >>> on_whitespace('This is not a test.')
        ['This', 'is', 'not', 'a', 'test.']

        Args:
            s: a string

        Returns:
            list: a list of strings
    """
    return s.split()
