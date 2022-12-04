import numpy as np
import pandas as pd
import random
import spacy
import translators as ts

nlp = spacy.load('en_core_web_sm')
#input type: string

#random swap
def random_swap(sentence, swap_num = 2, nlp = spacy.load('en_core_web_sm')):
    tokens = nlp(sentence)
    str_list = [str(tok) for tok in tokens]
    for i in range (1,swap_num):
        a,b = random.randint(0,len(str_list)-1),random.randint(0,len(str_list)-1)
        temp = str_list[a]
        str_list[a] = str_list[b]
        str_list[b] = temp
    aug_sentence = ' '.join(str_list)    
    
    return aug_sentence

#random delete
def random_delete(sentence, delete_num = 1, nlp = spacy.load('en_core_web_sm')):
    tokens = nlp(sentence)
    str_list = [str(tok) for tok in tokens]
    if len(str_list) <= 5:
        return ' '.join(str_list)
    if delete_num < 0:
        delete_num = 0
    for i in range(delete_num):
        a = random.randint(0,len(str_list)-1)
        str_list.remove(str_list[a])
    aug_sentence = ' '.join(str_list)
    return aug_sentence

#translate and translate
def double_translate(sentence,lang = 'zh-TW'):
    #https://www.loc.gov/standards/iso639-2/php/code_list.php
    first_trans = ts.google(sentence, from_language='en', to_language= lang)
    return ts.google(first_trans, from_language=lang ,to_language='en')