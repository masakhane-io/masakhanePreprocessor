import os
import re


#by Chris Emezue
#Comiling lots of preprocessing here for African languages.
#Trying to build a kind of preprocessor from this so that people don't need to be doing this manually for their African language (AL).
#Like a mini NLTK that takes care of the language complexities of ALs -- things like keeping diacritics,etc.



def cleanhtml(raw_html):
    # https://stackoverflow.com/a/12982689/11814682
    #cleanr = re.compile('<.*?>')
    cleanr = re.compile('<.*?>|&([a-z0-9]+|#[0-9]{1,6}|#x[0-9a-f]{1,6});')
    cleantext = re.sub(cleanr, '', raw_html)
    return cleantext


def preprocess_sentence(w):
   w= w.strip()
   w = cleanhtml(w)
   w=re.sub(r'[a-zA-Z ]+:[ “"«]','',w)
   #w=re.sub(r'[^A-Za-z0-9\s\’\-\.,]+','',w)
   w=re.sub(r'[\n\r\t]+',' ',w)
   w = re.sub(r"[;@#?!&$]+\ *", " ", w)   
   w= re.sub(r'[\․®●□•◆▪©!"#€■$%&\(\)\*\+/:;<=>?@\[\]^_`‘→{|}~«»”“]+','',w)
   w = re.sub(r'^[0-9,\-\. ]+','',w)
   w = re.sub(r' [ ]+',' ',w)
   w = re.sub(r' [0-9]+ [-,] [0-9]+',' ',w)
   w = re.sub(r' [0-9]+ [0-9 ]+ [0-9]+',' ',w)
   w = re.sub(r' [ ]+',' ',w)
   w = re.sub(r"' '",'',w)
   w=re.sub(r'\.—','.',w)
   w=re.sub(r'\.[​ ]+—','.',w)
   #w=re.sub(r'\.[ \.]+','.',w)

   w=re.sub(r"^[‘']+",'',w)
   w=re.sub(r"[’']+$",'',w)
   w=re.sub(r',[, ]+',',',w)
   w=re.sub(r'\.[ \.]+','.',w)
   return w
   
def preprocess_sentence_fon(w):
   w= w.strip()
   w = cleanhtml(w)
   w=re.sub(r'[a-zA-Z ]+:[ “"«]','',w)
   #w=re.sub(r'[^A-Za-z0-9\s\’\-\.,]+','',w)
   w=re.sub(r'[\n\r\t]+',' ',w)
   w = re.sub(r"[;@#?!&$]+\ *", " ", w)   
   w= re.sub(r'[\․●□•◆▪■©!"#€$%&\(\)\*\+/:;<=>?@\[\]^_`‘→{|}~«»”“]+','',w)
   w = re.sub(r'^[0-9,\-\. ]+','',w)
   w = re.sub(r' [ ]+',' ',w)
   w = re.sub(r' [0-9]+ [-,] [0-9]+',' ',w)
   w = re.sub(r' [0-9]+ [0-9 ]+ [0-9]+',' ',w)
   w = re.sub(r' [ ]+',' ',w)
   w = re.sub(r"' '",'',w)
   w=re.sub(r'\.[ \.]+','.',w)
   w=re.sub(r'\.—','.',w)
   w=re.sub(r'\.[​ ]+—','.',w)

   w=re.sub(r"^[‘']+",'',w)
   w=re.sub(r"[’']+$",'',w)
   w=re.sub(r',[, ]+',',',w)
   w=re.sub(r'\.[ \.]+','.',w)
   return w
   
def preprocess_sentence_ig(w):
   w= w.strip()
   w = cleanhtml(w)
   #w=re.sub(r'[a-zA-Z ]+:[ “"«]','',w)
   #w=re.sub(r'[^A-Za-z0-9\s\’\-\.,]+','',w)
   w=re.sub(r'[\n\r\t]+',' ',w)
   w = re.sub(r"[;@#?!&$]+\ *", " ", w)   
   w= re.sub(r'[\․●□•◆▪©!"■#€$%&\(\)\*\+/:;<=>?@\[\]^_`‘→{|}~«»”“]+','',w)
   w = re.sub(r'^[0-9,\-\. ]+','',w)
   w = re.sub(r' [ ]+',' ',w)
   w = re.sub(r' [0-9]+ [-,] [0-9]+',' ',w)
   w = re.sub(r' [0-9]+ [0-9 ]+ [0-9]+',' ',w)
   w = re.sub(r' [ ]+',' ',w)
   w = re.sub(r"' '",'',w)
   w=re.sub(r'⁠⁠⁠⁠.’','.',w)
   w=re.sub(r'\.[ \.]+','.',w)
   w=re.sub(r'\.—','.',w)
   w=re.sub(r'\.[​ ]+—','.',w)

   w=re.sub(r"^[‘']+",'',w)
   w=re.sub(r"[’']+$",'',w)
   w=re.sub(r',[, ]+',',',w)
   w=re.sub(r'\.[ \.]+','.',w)
   
   return w
def preprocess_sentence_xh(w):
   w= w.strip()
   w = cleanhtml(w)
   #w=re.sub(r'[a-zA-Z ]+:[ “"«]','',w)
   w=re.sub(r'[^A-Za-z0-9\s\’\-\.,]+','',w)
   w=re.sub(r'[\n\r\t]+',' ',w)
   w = re.sub(r"[;@#?!&$]+\ *", " ", w)   
   w= re.sub(r'[\․®●□•◆▪©!"#€$%■&\(\)\*\+/:;<=>?@\[\]^_`‘→{|}~«»”“]+','',w)
   w = re.sub(r'^[0-9,\-\. ]+','',w)
   w = re.sub(r' [ ]+',' ',w)
   w = re.sub(r' [0-9]+ [-,] [0-9]+',' ',w)
   w = re.sub(r' [0-9]+ [0-9 ]+ [0-9]+',' ',w)
   w = re.sub(r' [ ]+',' ',w)
   w = re.sub(r"' '",'',w)
   w=re.sub(r'\.[ \.]+','.',w)
   w=re.sub(r'\.—','.',w)
   w=re.sub(r'\.[​ ]+—','.',w)

   w=re.sub(r"^[‘']+",'',w)
   w=re.sub(r"[’']+$",'',w)
   w=re.sub(r',[, ]+',',',w)
   w=re.sub(r'\.[ \.]+','.',w)
   return w
   
def preprocess_sentence_rw(w):
   w= w.strip()
   w = cleanhtml(w)
   w=re.sub(r'[a-zA-Z ]+:[ “"«]','',w)
   #w=re.sub(r'[^A-Za-z0-9\s\’\-\.,]+','',w)
   w=re.sub(r'[\n\r\t]+',' ',w)
   w = re.sub(r"[;@#?!&$]+\ *", " ", w)   
   w= re.sub(r'[\․●□•◆▪©!"#€$■%&\(\)\*\+/:;<=>?@\[\]^_`→{|}~«»”“]+','',w)
   w = re.sub(r'^[0-9,\-\. ]+','',w)
   w = re.sub(r' [ ]+',' ',w)
   w = re.sub(r' [0-9]+ [-,] [0-9]+',' ',w)
   w = re.sub(r' [0-9]+ [0-9 ]+ [0-9]+',' ',w)

   w=re.sub(r"^[‘']+",'',w)
   w=re.sub(r"[’']+$",'',w)

   w = re.sub(r' [ ]+',' ',w)
   w = re.sub(r"' '",'',w)
   w=re.sub(r'\.—','.',w)
   w=re.sub(r'\.[​ ]+—','.',w)
   w=re.sub(r',[, ]+',',',w)
   w=re.sub(r'\.[ \.]+','.',w)
   #w=re.sub(r'\.[ \.]+','.',w)
   return w
   

def preprocess_sentence_sw(w):
   w= w.strip()
   w = cleanhtml(w)
   w=re.sub(r'[a-zA-Z ]+:[ “"«]','',w)
   w=re.sub(r'[^A-Za-z0-9\s\’\-\.,]+','',w)
   w=re.sub(r'[\n\r\t]+',' ',w)
   w = re.sub(r"[;@#?!&$]+\ *", " ", w)   
   w= re.sub(r'[\․●□•◆▪©!"■#$€%&\(\)\*\+/:;<=>?@\[\]^_`→{|}~«»”“]+','',w)
   w= re.sub(r"[']+",'',w)
   w = re.sub(r'^[0-9,\-\. ]+','',w)
   w = re.sub(r' [ ]+',' ',w)
   w = re.sub(r' [0-9]+ [-,] [0-9]+',' ',w)
   w = re.sub(r' [0-9]+ [0-9 ]+ [0-9]+',' ',w)
   w = re.sub(r' [ ]+',' ',w)
   w = re.sub(r"' '",'',w)

   w=re.sub(r"^[‘']+",'',w)
   w=re.sub(r"[’']+$",'',w)

   w = re.sub(r"^[,'\.]+",'',w)
   w=re.sub(r'\.[ \.]+','.',w)
   w=re.sub(r'\.—','.',w)
   w=re.sub(r'\.[​ ]+—','.',w)
   w=re.sub(r',[, ]+',',',w)
   w=re.sub(r'\.[ \.]+','.',w)

   
   return w

def preprocess_sentence_yo(w):
   w= w.strip()
   w = cleanhtml(w)
   w=re.sub(r'[a-zA-Z ]+:[ “"«]','',w)
   #w=re.sub(r'[^A-Za-z0-9\s\’\-\.,]+','',w)
   w=re.sub(r'[\n\r\t]+',' ',w)
   w = re.sub(r"[;@#?!&$]+\ *", " ", w)   
   w= re.sub(r'[●®□•◆▪©!"#$■€%&\(\)\*\+/:;<=>?@\[\]^_→{|}~«»”“]+','',w)
   #w= re.sub(r"[']+",'',w)
   w = re.sub(r'^[0-9,\-\. ]+','',w)
   w = re.sub(r' [ ]+',' ',w)
   w = re.sub(r' [0-9]+ [-,] [0-9]+',' ',w)
   w = re.sub(r' [0-9]+ [0-9 ]+ [0-9]+',' ',w)
   w = re.sub(r' [ ]+',' ',w)
   w=re.sub(r"^[‘']+",'',w)
   w=re.sub(r"[’']+$",'',w)

   w = re.sub(r"' '",'',w)


   w = re.sub(r"^[,'\.]+",'',w)
   w=re.sub(r'\.[ \.]+','.',w)
   w=re.sub(r'\.—','.',w)
   w=re.sub(r'\.[​ ]+—','.',w)
   w=re.sub(r',[, ]+',',',w)

   w=re.sub(r'\.[ \.]+','.',w)
   
   return w



preprocess_map = {
    'yo':preprocess_sentence_yo,
    'fon':preprocess_sentence_fon,
    'rw':preprocess_sentence_rw,
    'sw':preprocess_sentence_sw,
    'xh':preprocess_sentence_xh,
    'ig':preprocess_sentence_ig,
    'en':preprocess_sentence,
    'fr':preprocess_sentence
}