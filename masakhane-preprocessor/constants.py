import sys
import unicodedata


#from https://github.com/jfilter/clean-text/blob/master/cleantext/constants.py
PUNCT_TRANSLATE_UNICODE = dict.fromkeys(
    (i for i in range(sys.maxunicode) if unicodedata.category(chr(i)).startswith("P")),
    "",
)


SYMBOLS_TRANSLATE_UNICODE = dict.fromkeys(
    (i for i in range(sys.maxunicode) if unicodedata.category(chr(i)).startswith("S")),
    "",
)
