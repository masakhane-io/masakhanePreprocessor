import re
import os
import sys
import json
import unicodedata
from cleantext import clean
from pathlib import Path
from langs import get_correct_language_code


#Each language has its own preprocessing rules
#-allowed_symbols, disallowed_symbols which affects punct
#strip punctuation
#strip symbols


def read_json(file):
    with open(file,'r',encoding='utf8') as f:
        return json.load(f)
def read_file(file):
    with open(file,'r',encoding='utf8') as f:
        return list(f.readlines())
        
def save_list_to_file(list_text,save_filename,output_path):
    with open(os.path.join(output_path,save_filename),'w+',encoding='utf8') as output:
        for text in list_text:
            output.write(text.strip()+'\n')
            
    return True 

def get_ord(n: list):
    '''
    does ord(a) for each a in n, but also checks for when a is not a single character
    '''
    allowed_ints = []
    allowed_char = []
    
    for a in n:
        try:
            allowed_ints.append(ord(a))
        except Exception:
            #a is not a single character. use its char instead of ord()
            allowed_char.append(a)
    return allowed_ints,allowed_char
   
class Preprocessor():
    def __init__(self,lang='',
                    use_diacritics=False,
                    lower=False,
                    strip_punctuation=True,
                    strip_symbols=True,             # BELOW ARE FURTHER PARAMETERS FROM CLEAN-TEXT. If you set lang, I recommend not to touch below as it's been done for You already
                    fix_unicode=False,
                    no_line_breaks=False,           # fully strip line breaks as opposed to only normalizing them
                    no_urls=False,                  # replace all URLs with a special token
                    no_emails=False,                # replace all email addresses with a special token
                    no_phone_numbers=False,         # replace all phone numbers with a special token
                    no_numbers=False,               # replace all numbers with a special token
                    no_digits=False,                # replace all digits with a special token
                    no_currency_symbols=False,      # replace all currency symbols with a special token
                    no_punct=False,                 # remove punctuations
                    replace_with_punct="",          # instead of removing punctuations you may replace them
                    replace_with_url="<URL>",
                    replace_with_email="<EMAIL>",
                    replace_with_phone_number="<PHONE>",
                    replace_with_number="<NUMBER>",
                    replace_with_digit="0",
                    replace_with_currency_symbol="<CUR>"):
        
        if lang!='':
            lang = get_correct_language_code(lang)
            if not lang:
                print(f'Could not get the correct code for your language. If you cannot find your language in the available languages please raise an issue.')
  
        self.USE_DIACRITICS=False
        
        #Default language rules
        self.lang_rules={"allowed_symbols": [], "diacritics": False}
       
       
        #-----------------------
        try:
            self.lang_rules = read_json(f'rules/{lang}.json')
        except Exception as e:
            #Language rules probably does not exist. For now pass
            #TO DO: Make better
            print(f'Cannot find the rules for your language. Switching to the default. Call .available_langs() to get the current available languages')
            pass
        
        #-------------------------
        
        #-----------------------------
        languages = read_json('languages.json')
        self.language_map={}
        for l_ in languages:
            self.language_map.update({l_['language_short']:l_})
        #-----------------------------
       
         
        if use_diacritics or self.lang_rules['diacritics']:
            self.USE_DIACRITICS=True
            
        self.strip_punctuation=strip_punctuation
        self.strip_symbols=strip_symbols
           
        self.allowed_symbols,self.allowed_chars= get_ord(self.lang_rules['allowed_symbols'])
                
        #from https://github.com/jfilter/clean-text/blob/master/cleantext/constants.py
        #Unicode characters: https://www.fileformat.info/info/unicode/category/index.htm
        self.PUNCT_TRANSLATE_UNICODE = dict.fromkeys(
            (i for i in range(sys.maxunicode) if unicodedata.category(chr(i)).startswith("P") and i not in self.allowed_symbols and chr(i) not in self.allowed_chars),
            "",
        )
        
        self.SYMBOLS_TRANSLATE_UNICODE = dict.fromkeys(
            (i for i in range(sys.maxunicode) if unicodedata.category(chr(i)).startswith("S") and i not in self.allowed_symbols and chr(i) not in self.allowed_chars),
            "",
        )

            
        self.clean_text_kwargs = {
        'text':'',
        'fix_unicode':fix_unicode,
        'to_ascii':False if self.USE_DIACRITICS else True,
        'lower':False if not lower else True,
        'no_line_breaks':no_line_breaks,
        'no_urls':no_urls,
        'no_emails':no_emails,
        'no_phone_numbers':no_phone_numbers,
        'no_numbers':no_numbers,
        'no_digits':no_digits,
        'no_currency_symbols':no_currency_symbols,
        'replace_with_punct':replace_with_punct,          # instead of removing punctuations you may replace them. #from CLEAN-TEXT
        'replace_with_url':replace_with_url,
        'replace_with_email':replace_with_email,
        'replace_with_phone_number':replace_with_phone_number,
        'replace_with_number':replace_with_number,
        'replace_with_digit':replace_with_digit,
        'replace_with_currency_symbol':replace_with_currency_symbol
        }
        
    def available_langs(self):
        available_langs = [str(f.name).split('.json')[0] for f in os.scandir('rules') if str(f.name).endswith('json')]
        return list([f"{a} -> {self.language_map[a]['language']}" for a in available_langs])
        
    
    def preprocess_str(self,text):
        self.clean_text_kwargs['text']=text
        text = clean(**self.clean_text_kwargs)
        
        #Now for punctuation and symbols removal
        if self.strip_punctuation:
            text=text.translate(self.PUNCT_TRANSLATE_UNICODE)
        if self.strip_symbols:
            text = text.translate(self.SYMBOLS_TRANSLATE_UNICODE)
        
        return text
    
    def preprocess_file(self,filename,output_path=None):
        
        path = Path(filename)
        
        if not output_path:
            output_path = path.parent.absolute()

        
        try:
            files = read_file(filename)
        except Exception as e:
            raise Exception(f'Error occured while reading file {filename}. See error below: \n {e}')
        
        clean_texts = [self.preprocess_str(txt) for txt in files]
        new_filename = str(path.name).split(path.suffix)[0]+'_CLEAN'+path.suffix
        if save_list_to_file(clean_texts,new_filename,output_path):
            print(f'Clean file(s) saved successfully to {os.path.join(output_path,new_filename)}')

if __name__ == "__main__":
    #Testing for Fon
    my_prep = Preprocessor(lang='fon')
    print(my_prep.available_langs())
    print(my_prep.preprocess_str('è:ụẹ́ēạ́ị̄ìīí ði ɔ na-aga enyiɛ̆"he went":, ɛ̃ winnya ɖu nɔ mya nukún nú mǐî, ï hú nǔ bǐ ɔ mǐ sixuὲ` nugbǒmaɖɔ dó mɔ nǔ ɖò dandan é ɖé'))
