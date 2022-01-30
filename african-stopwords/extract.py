import re,os
import sys, getopt
import collections


def match(input_string):
    #remove numbers
    input_string = re.sub(r'[0-9]+','',input_string)
    words = re.findall(r'\w+', input_string)
    return words

def extract(file,freq):
    #Extract the stopwords from
    # --file: input corpus file
    # --freq: frequency threshold
    with open(file,'r',encoding='utf8') as f:
        file_lines = f.readlines()
        file_ = ' '.join(file_lines)
    if not file_:
        raise Exception('Error loading the input file')
    words = match(file_)
    
    freq_dict = collections.Counter(words).most_common()
    return freq_dict


def main(args):
    ABOUT = """
    python3 extract.py will extract the unqiue words (And their frequency) from a monolingual corpus file. 
    The idea is to use the extracted words and their frequency to generate and review stopwords for a language.
    We are working on the idea that stpwords for a given language will have a high frequency compared to non-stopwords
   
   
    Usage
    ---------------------  
    --file (-i) : input file
    --output (-o) : output file 
    --freq (-f) : frequency threshold. If this is specified, output will be only the words with frequency greater than or equal to the threshold
    
    """   
    FREQ=None
    INPUT_FILE = None
    OUTPUT_FILE=None
    try:
        opts, args = getopt.getopt(args,'i:o:f',["file=","output=","freq="])
    except getopt.GetoptError as e:
        print (ABOUT)
        sys.exit(2)

    for opt, arg in opts:
        opt=opt.strip()
        if opt in ['--file','-i']:
            INPUT_FILE = arg
            if not os.path.isfile(INPUT_FILE):
                raise Exception(f'Input file is empty or does not exist')
        if opt in ['--freq','-f']:
            FREQ=arg
        if opt in ['--output','-o']:
            OUTPUT_FILE=arg 
    if OUTPUT_FILE==None:
        raise Exception(f'Output file needs to be specified')

    freq_dict = extract('pidgin_corpus.txt',100) 
  
    # If `freq`` is not given then output `word freq` per line
    # Else, pick only the words >= freq and display them as `word` per line
    if FREQ==None:
        with open(OUTPUT_FILE,'w+',encoding='utf8')as f:
            for word, freq in freq_dict:
                f.write(f'{word}\t{freq}\n')    
        print(f'Words with their frequency saved to {OUTPUT_FILE}')
    else:
        FREQ=int(FREQ)
        threshold = [(w,f) for w,f in freq_dict if f>=FREQ]
        if threshold==[]:
            raise Exception(f'No words could be extracted for your threshold frequency -> {FREQ}. Please try a lower frequency.')
        with open(OUTPUT_FILE,'w+',encoding='utf8')as f:
            for word, freq in threshold:
                f.write(f'{word}\n')    
        print(f'Words above {FREQ} have been saved to {OUTPUT_FILE}')



if __name__ == "__main__":
    main(sys.argv[1:])
    
