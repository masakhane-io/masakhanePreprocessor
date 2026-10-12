import pytest

from masakhanePreprocessor import Preprocessor


def test_resources_load_outside_checkout(tmp_path, monkeypatch):
    monkeypatch.chdir(tmp_path)
    prep = Preprocessor(lang='ig')
    assert '-' in prep.lang_rules['allowed_symbols']
    assert prep.preprocess_str('Dịka● na-aga') == 'Dịka na-aga'
    prep.available_langs()


@pytest.mark.parametrize('name,expected', [('corpus', 'corpus_CLEAN'),
                                          ('part.txt.backup.txt', 'part.txt.backup_CLEAN.txt'),
                                          ('corpus.txt', 'corpus_CLEAN.txt')])
def test_output_filename_preserves_stem(tmp_path, name, expected):
    source = tmp_path / name
    source.write_text('Dịka● na-aga\n', encoding='utf-8')
    prep = Preprocessor(lang='ig')
    prep.preprocess_file(source)
    assert (tmp_path / expected).read_text(encoding='utf-8') == 'Dịka na-aga\n'
    assert source.read_text(encoding='utf-8') == 'Dịka● na-aga\n'


def test_explicit_no_punct_honored():
    prep = Preprocessor(lang='ig', strip_punctuation=False, strip_symbols=False, no_punct=True)
    assert prep.preprocess_str('word!') == 'word'


def test_default_keeps_language_punctuation():
    prep = Preprocessor(lang='ig')
    assert prep.preprocess_str("na-aga 'okwu',") == "na-aga 'okwu'"


def test_diacritics_and_combining_marks_remain():
    prep = Preprocessor(lang='fon')
    assert prep.preprocess_str('ɛ̃ ɔ̀ ɛ̆!') == 'ɛ̃ ɔ̀ ɛ̆'
