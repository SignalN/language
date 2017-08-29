# language

*language* is a set of very basic building blocks for working with natural language text in Python.

*language* is designed to be lightweight, modular, usable in production and inherently language-agnostic - it should support applications that use text in hundreds of languages.

*language* is available [on PyPI](https://pypi.python.org/pypi/language).  To install:

    pip install language

### language.chars

*language.chars* is for working with individual characters beyond the built-in *isupper()*, *isalnum()*, *string.punctuation* and so on.

### language.tokens

*language.tokens* splits text into word-like tokens.

To add space around punctuation:
```
>>>import language.tokens as tokens
>>> tokens.space_punct("This isn't a test, you know!")
"This isn ' t a test ,  you know ! "
>>> tokens.space_punct("Don't know, it's carbon-neutral...")
"Don ' t know ,  it ' s carbon - neutral .  .  . "
>>> tokens.space_punct("Где-то в Нью-Йорке говорилось «7 разбойниц!»")
'Где - то в Нью - Йорке говорилось  « 7 разбойниц !  » '
```

Then simply split on whitespace:
```
>>> s = tokens.space_punct("This isn't a test, you know!")
>>> tokens.on_whitespace(s)
['This', 'isn', "'", 't', 'a', 'test', ',', 'you', 'know', '!']
```

### language.ngrams

*language.ngrams* supports both word-level and character-level [n-grams](https://en.wikipedia.org/wiki/N-gram).

```
>>> import language.ngrams as ng
>>> ng.word_ngrams('This is not a test.')
[('This', 'is', 'not'), ('is', 'not', 'a'), ('not', 'a', 'test.')]
>>> ng.char_ngrams('This is not a test.')
['Thi', 'his', 'is', 'not', 'a', 'tes', 'est', 'st.']
```

To diff two strings:

```
>>> ng.char_matches("Microsoft is a company.", "Microsoft - компания.")
{'ros', 'oft', 'cro', 'Mic', 'icr', 'oso', 'sof'}
>>> ng.char_matches("She is going to Rome.", "Lei va a Roma.")
{'Rom'}
```

To compare two strings:

```
>>> ng.char_similarity("Microsoft is a company.", "Microsoft - компания.")
0.4666666666666667
>>> ng.char_similarity("She is going to Rome.", "Lei va a Roma.")
0.13333333333333333
>>> ng.char_similarity("Microsoft is a company.", "Microsoft-ը ընկերություն է:")
0.4
>>> ng.char_similarity("Microsoft is a company.", "Majkrosoft je kompanija.")
0.4375
>>> ng.char_similarity("Happy birthday.", "Happy birthday")
0.9473684210526315
>>> ng.char_similarity("Happy birthday.", "Happy birthday.")
1.0
>>> ng.char_similarity("Happy birthday.", "С днем рождения!")
0.0
```
