# masakhane-preprocessing
An effective preprocessing tool for African languages [Beta version].

This builds on the [clean-text](https://github.com/jfilter/clean-text/tree/master/cleantext) preprocessor.

## How to Use
Install:
```pip install masakhane-preprocessor```
## Preprocessor
You only need to specify your language and it loads the important preprocessing style for You!

You initialize the `Preprocessor` in Python as follows:
```python
from masakhane-preprocessor import Preprocessor

my_prep = Preprocessor(lang='ig')
```
Other parameters you can configure are:
```python
my_prep = Preprocessor(lang='ig',
              use_diacritics=False,
              lower=False,
              strip_punctuation=True,
              strip_symbols=True)
```
### preproces_str
To preprocess a string use the `preproces_str` function:
```python
clean_text = my_prep.preprocess_str('''Dịka● ndọrọndọrọọchịchị maka ntuliaka ọkwa Gọvanọ
                                       Anambra steeti si na-aga nke afọ 2021, ndị nọ.''')
```
You get the following as output:
```Dịka ndọrọndọrọọchịchị maka ntuliaka ọkwa Gọvanọ Anambra steeti si na-aga nke afọ 2021 ndị nọ```

> Notice how the `●` character has been removed, but the `-`, which is an important part of Igbo, remains untouched.


### preprocess_file
To preprocess a file use the `preprocess_file` function:
```python
my_prep.preprocess_file('./ig.txt',
                        output_path=None #Specify the output path. If unspecified, uses the parent directory of file)
```
On successful completion you get this message:
`Clean file(s) saved successfully to xxxxxxx/ig_CLEAN.txt`

### Properties of the preprocessing tool
1. Language first
2. Simple to use

## Contribution
We are open and grateful for ideas to make this better. You can propose ideas as issues or pull requests.

