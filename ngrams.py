from nltk import bigrams,ngrams
from nltk.corpus import stopwords
from nltk.tokenize import RegexpTokenizer

def get_text(file):
    f = open(file)
    return f.read().lower()
    
def remove_stopwords(text):
    stop  = stopwords.words('english')
    text = [i for i in text.split() if i not in stop]
    return " ".join(text)
    
def remove_punc(text):
    token = RegexpTokenizer(r'\w+')
    text = token.tokenize(text)
    return " ".join(text)
    
def get_bigrams(text):
    """Returns a set of string tuples"""
    grams = bigrams(text.split())
    return_val = []
    for i,gram in enumerate(grams):
        return_val.append(gram)
    return set(return_val)
    
def get_unigrams(text):
    return set(text.split())
    
def get_jiccard(set1,set2):
    """Input: Two sets of string tuples
    Output: The Jiccard index of the sets which is contained in [0,1]"""
    return len(set1 & set2) / float(len(set1 | set2))
    
def score_text(text,base_post):
    text = remove_stopwords(text)
    text = remove_punc(text)
    grams = get_bigrams(text) | get_unigrams(text)
    return get_jiccard(grams,base_post)

def build_ideal_post():
    """Builds the job posting that is used as the "ideal" job 
    posting.  All candidate postings are compared to this one."""
    text = get_text("ideal_post")
    text = remove_stopwords(text)
    text = remove_punc(text)
    grams = get_bigrams(text) | get_unigrams(text)
    return grams    

