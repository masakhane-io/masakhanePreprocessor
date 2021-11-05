import re
import os
import sys
import json
import unicodedata
from cleantext import clean
from pathlib import Path
from langs import get_correct_language_code

#Designed by Chris Emezue

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


class Preprocessor():
    def __init__(self,lang='',
                      use_diacritics=False,
                      lower=False,
                      strip_punctuation=True,
                      strip_symbols=True):
        
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
           
        self.allowed_symbols= [ord(a) for a in self.lang_rules['allowed_symbols']]
                
        #from https://github.com/jfilter/clean-text/blob/master/cleantext/constants.py
        self.PUNCT_TRANSLATE_UNICODE = dict.fromkeys(
            (i for i in range(sys.maxunicode) if unicodedata.category(chr(i)).startswith("P") and i not in self.allowed_symbols),
            "",
        )
        
        self.SYMBOLS_TRANSLATE_UNICODE = dict.fromkeys(
            (i for i in range(sys.maxunicode) if unicodedata.category(chr(i)).startswith("S") and i not in self.allowed_symbols),
            "",
        )

            
        self.clean_text_kwargs = {
        'text':'',
        'fix_unicode':False,
        'to_ascii':False if self.USE_DIACRITICS else True,
        'lower':False if not lower else True,
        'no_line_breaks':False,
        'no_urls':True,
        'no_emails':True,
        'no_phone_numbers':True,
        'no_numbers':False,
        'no_digits':False,
        'no_currency_symbols':True
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
    my_prep = Preprocessor(lang='yor',lower=True)
    print(my_prep.available_langs())
    print(my_prep.preprocess_str('Dịka● ndọrọndọrọọchịchị maka ntuliaka ọkwa Gọvanọ Anambra steeti si na-aga nke afọ 2021, ndị nọ.'))
