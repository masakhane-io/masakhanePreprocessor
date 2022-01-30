# Stopwords for African languages

This is a project to include stopwords for African languages in NLP. The importance of stopwords in NLP analysis cannot be over-emphasized.

## Contributing
1. Fork the repository. We are interested in the `african-stopwords` folder. 
2. Go to the  `.txt` file of your language tag in the `languages` folder. Consult [LANGUAGE-TABLE.md](LANGUAGE-TABLE.md) for the tag of your language. If the file isn't there, please create one. 
3. Edit the file: add more stopwords for your language or delete the wrong ones.
4. Make a pull request for merging.

Alternatively,

5. If navigating Github is complex, just write down the stopwords for your language in a `txt` file and send on [Masakhane Slack](https://www.google.com/url?q=https%3A%2F%2Fjoin.slack.com%2Ft%2Fmasakhane-nlp%2Fshared_invite%2FenQtODM3ODA3ODE0ODIwLTAyYzg3M2E3Nzg4Y2I3NzgxNDg4MmNlZDE4OTBjMzBjMjg4NTcxMWZlYTg3ZDljMTU4M2FjOTk3MDVjOWM2NGM&sa=D&sntz=1&usg=AFQjCNGNjFNyyutwL-wQso1gYPGCSXGevg)).
6. If there are websites/resources with african stopwords, please indicate (via an issue or [Masakhane Slack](https://www.google.com/url?q=https%3A%2F%2Fjoin.slack.com%2Ft%2Fmasakhane-nlp%2Fshared_invite%2FenQtODM3ODA3ODE0ODIwLTAyYzg3M2E3Nzg4Y2I3NzgxNDg4MmNlZDE4OTBjMzBjMjg4NTcxMWZlYTg3ZDljMTU4M2FjOTk3MDVjOWM2NGM&sa=D&sntz=1&usg=AFQjCNGNjFNyyutwL-wQso1gYPGCSXGevg)).


__Please fill the [Contribution Highlight Table](https://github.com/masakhane-io/masakhane-preprocessing/tree/main/african-stopwords/languages#contribution-highlight) while adding stopwords for your language.__  


### Discussion

Seeing that the choice of what constitutes a stopword in an African language may be open to debate, [here](https://github.com/masakhane-io/masakhane-preprocessing/discussions/categories/african-stopwords) is a forum for scholars, researchers, linguists, etc to discuss on some controversial stop words or non-stopwords in your African languages.

If you're not sure if a word is/is not a stopword, the discussion will help.
If you feel a new word should be added as a stopword in your language, please create a discussion around it.

- Click [here to browse through the current discussions](https://github.com/masakhane-io/masakhane-preprocessing/discussions/categories/african-stopwords). Join the discussion. Some African languages do not have a fixed definition of what constitutes a stopword. It is up to US to define them TOGETHER.
- Click [here to start a new discussion on african-stopwords](https://github.com/masakhane-io/masakhane-preprocessing/discussions/new?category=african-stopwords).

## Plan
Open to suggestions. For now I think we can:

1. Compile a good list of african stopwords and make a feature request to have it added on [nltk](https://github.com/nltk/nltk/blob/develop/CONTRIBUTING.md).

## Extracting from monolingual corpus
The file `extract.py` will extract the unqiue words (and their frequency) from a monolingual corpus file. 

Please use the extracted words and their frequency to generate and review stopwords for a language.

We are working on the intuition that stpwords for a given language will have a high frequency compared to non-stopwords

```python
"""
Usage
---------------------  
--file (-i) : input file
--output (-o) : output file 
--freq (-f) : frequency threshold. If this is specified, output will be only the words with frequency greater than or equal to the threshold
"""
```  
___

- Initial stopwords list for Afrikaans, Hausa, Lugbarati, Lugbarati (Official), Somali, Sesotho, Kiswahili, Yoruba, and isiZulu got from [here](https://www.kaggle.com/rtatman/stopword-lists-for-african-languages). 