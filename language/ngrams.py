import language.tokens as tokens

def __ngrams(s, n=3):
    """ Raw n-grams from a sequence

        If the sequence is a string, it will return char-level n-grams.
        If the sequence is a list of words, it will return word-level n-grams.

        Note: it treats space (' ') and punctuation like any other character.

            >>> ngrams('This is not a test!')
            [('T', 'h', 'i'), ('h', 'i', 's'), ('i', 's', ' '), ('s', ' ', 'i'),
            (' ', 'i', 's'), ('i', 's', ' '), ('s', ' ', 'n'), (' ', 'n', 'o'),
            ('n', 'o', 't'), ('o', 't', ' '), ('t', ' ', 'a'), (' ', 'a', ' '),
            ('a', ' ', 't'), (' ', 't', 'e'), ('t', 'e', 's'), ('e', 's', 't'),
            ('s', 't', '!')]
            >>> ngrams(["This", "is", "not", "a", "test!"])
            [('This', 'is', 'not'), ('is', 'not', 'a'), ('not', 'a', 'test!')]

        Args:
            s: a string or a list of strings
            n: an int for the n in n-gram

        Returns:
            list: tuples of char-level or word-level n-grams
    """
    return list(zip(*[s[i:] for i in range(n)]))

def word_ngrams(s, n=3, token_fn=tokens.on_whitespace):
    """
        Word-level n-grams in a string

        By default, whitespace is assumed to be a word boundary.

        >>> ng.word_ngrams('This is not a test!')
        [('This', 'is', 'not'), ('is', 'not', 'a'), ('not', 'a', 'test!')]

        If the sequence's length is less than or equal to n, the n-grams are
        simply the sequence itself.

        >>> ng.word_ngrams('Test!')
        [('Test!')]

        Args:
            s: a string

        Returns:
            list: tuples of word-level n-grams
    """
    tokens = token_fn(s)
    return __ngrams(tokens, n=min(len(tokens), n))

def char_ngrams(s, n=3, token_fn=tokens.on_whitespace):
    """
        Character-level n-grams from within the words in a string.

        By default, the word boundary is assumed to be whitespace.  n-grams are
        not taken across word boundaries, only within words.

        If a word's length is less than or equal to n, the n-grams are simply a
        list with the word itself.

        >>> ng.char_ngrams('This is not a test!')
        ['Thi', 'his', 'is', 'not', 'a', 'tes', 'est', 'st!']

        Therefore some n-grams may have a length less than n, like 'is' and 'a'
        in this example.

        Args:
            s: a string
            n: an int for the n in n-gram
            token_fn: a function that splits a string into a list of strings

        Returns:
            list: strings of char-level n-grams
    """
    tokens = token_fn(s)
    ngram_tuples = [__ngrams(t, n=min(len(t), n)) for t in tokens]
    def unpack(l):
        return sum(l, [])
    def untuple(l):
        return [''.join(t) for t in l]
    return untuple(unpack(ngram_tuples))


def __matches(s1, s2, ngrams_fn, n=3):
    """
        Returns the n-grams that match between two sequences

        See also: SequenceMatcher.get_matching_blocks

        Args:
            s1: a string
            s2: another string
            n: an int for the n in n-gram

        Returns:
            set:
    """
    ngrams1, ngrams2 = set(ngrams_fn(s1, n=n)), set(ngrams_fn(s2, n=n))
    return ngrams1.intersection(ngrams2)

def char_matches(s1, s2, n=3):
    """
        Character-level n-grams that match between two strings

        Args:
            s1: a string
            s2: another string
            n: an int for the n in n-gram

        Returns:
            set: the n-grams found in both strings
    """
    return __matches(s1, s2, char_ngrams, n=n)

def word_matches(s1, s2, n=3):
    """
        Word-level n-grams that match between two strings

        Args:
            s1: a string
            s2: another string
            n: an int for the n in n-gram

        Returns:
            set: the n-grams found in both strings
    """
    return __matches(s1, s2, word_ngrams, n=n)

def __similarity(s1, s2, ngrams_fn, n=3):
    """
        The fraction of n-grams matching between two sequences

        Args:
            s1: a string
            s2: another string
            n: an int for the n in n-gram

        Returns:
            float: the fraction of n-grams matching
    """
    ngrams1, ngrams2 = set(ngrams_fn(s1, n=n)), set(ngrams_fn(s2, n=n))
    matches = ngrams1.intersection(ngrams2)
    return 2 * len(matches) / (len(ngrams1) + len(ngrams2))

def char_similarity(s1, s2, n=3):
    return __similarity(s1, s2, char_ngrams, n=n)

def word_similarity(s1, s2, n=3):
    return __similarity(s1, s2, word_ngrams, n=n)

# TODO: def __counts(s, n=3):
