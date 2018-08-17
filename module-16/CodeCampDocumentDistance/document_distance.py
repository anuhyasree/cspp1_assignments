'''
   Document Distance - A detailed description is given in the PDF
'''



import re
import math

def clean_up(input_str):
    """ removing the numbers special characters and some seperating symbols"""
    input_str = input_str.lower()
    regex = re.compile('[^a-z ]')
    input_str = regex.sub('', input_str)
    list_of_words = input_str.split()
    for _, j in enumerate(list_of_words):
        j = j.strip()
        #list_of_words[each_word_index] = list_of_words[each_word_index].strip()
    return list_of_words

    #return [regex.sub('',each_word.strip())for each_word in input_string.lower().split('')]

def remove_stop_words(list_of_words):
    """removing the stopword a , an, and , the, etc some connectiong words
    and words in the stopwords text file"""
    stop_words = load_stopwords('stopwords.txt')
    for each_word in stop_words:
        while each_word in list_of_words:
            list_of_words.remove(each_word)
    return list_of_words

def dict_frequency(list_of_words, index, dict_ionary):
    """ calculating the frequency of the words occurance in the dictionary """
    for each_word in list_of_words:
        if each_word != "":
            if each_word not in dict_ionary:
                dict_ionary[each_word] = [0, 0]
            dict_ionary[each_word][index] += 1
    return dict_ionary

def  computation_values(dict_ionary):
    """ Calculating the cosine value and retuning the value """
    nume_rator = sum(value[0] * value[1] for value in dict_ionary.values())
    denominator_1 = math.sqrt(sum(value[0]**2 for value in dict_ionary.values()))
    denominator_2 = math.sqrt(sum(value[1]**2 for value in dict_ionary.values()))
    return nume_rator/(denominator_1 * denominator_2)


def similarity(dict_1, dict_2):
    '''
        Compute the document distance as given in the PDF
    '''
    input_1 = clean_up(dict_1)
    input_2 = clean_up(dict_2)
    input_1 = remove_stop_words(input_1)
    input_2 = remove_stop_words(input_2)
    d_ict = {}
    d_ict = dict_frequency(input_1, 0, d_ict)
    d_ict = dict_frequency(input_2, 1, d_ict)
    return computation_values(d_ict)

def load_stopwords(file_name):
    '''
        loads stop words from a file and returns a dict_ionary
    '''
    stopwords = {}
    with open(file_name, 'r') as text_file:
        for line in text_file:
            stopwords[line.strip()] = 0
    return stopwords

def main():
    '''
        take two inputs and call the similarity function
    '''
    input_1 = input()
    input_2 = input()
    print(similarity(input_1, input_2))

if __name__ == '__main__':
    main()
