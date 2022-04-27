from langcodes import *
import json


# This will help with 
# 1. mapping an African language name to its lang code
# 2. mapping any language code to its BCP47 variant.


def read_json(file):
    with open(file,'r',encoding='utf8') as f:
        return json.load(f)

#African languages list from https://github.com/dsfsi/masakhane-web/blob/master/src/server/core/languages.json
languages = read_json('masakhanePreprocessor/languages.json')
language_mapping =   {}
for l in languages:
    language_mapping.update({l['language_en'].lower():l['language_short']})
    language_mapping.update({l['language_native'].lower():l['language_short']})
    


def get_correct_language_code(lang_code: str):
    
    lang_code=lang_code.lower()
    try:
        c_lang = standardize_tag(lang_code)
        return c_lang
    except Exception:
        #lang_code is most likely a language and not a language code. Let's try to get its correct language code
        african_languages_list = list(set(language_mapping.keys()))
        if lang_code in african_languages_list:
            return language_mapping[lang_code]
        else:
            #The user most likely made a mistake in writing the language. 
            return None
        
        
        