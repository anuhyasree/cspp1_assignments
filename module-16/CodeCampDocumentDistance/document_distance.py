'''
    Document Distance - A detailed description is given in the PDF
'''
def wordlist(input_1):
    line_1 = input_1
    line_1 = line_1.lower()
    print (line_1)
    line_1 = line_1.replace('.','').replace('?','').replace(',','')\
        .replace('4','').replace('5','').replace('6','').replace('7','')\
        .replace('!','').replace('1','').replace('2','').replace('3','')\
        .replace('8','').replace('9','').replace('0','')
    line_1 = line_1.split(' ')
    #print(line_1)
    """dict reading for word count"""
    word_freq_dict = {}
    for word_s in line_1:
        if word_s not in word_freq_dict:
            word_freq_dict[word_s] = 1
        else:
            word_freq_dict[word_s] += 1
    print(word_freq_dict)
    return word_freq_dict

def similarity(dict1, dict2):
    '''
        Compute the document distance as given in the PDF
    '''
    new_dict1 = wordlist(dict1)
    new_dict2 = wordlist(dict2)
    stop_words = load_stopwords('stopwords.txt')
    for word_s in stop_words:
        if word_s in new_dict1:
           del new_dict1[word_s]
    for word_s in stop_words:
        if word_s in new_dict2:
            del new_dict2[word_s]
    return new_dict1, new_dict2

def load_stopwords(filename):
    '''
        loads stop words from a file and returns a dictionary
    '''
    stopwords = {}
    with open(filename, 'r') as filename:
        for line in filename:
            stopwords[line.strip()] = 0
        #print(stopwords)
    return stopwords

def main():
    '''
        take two inputs and call the similarity function
    '''
    input1 = input()
    input2 = input()

    print(similarity(input1, input2))

if __name__ == '__main__':
    main()
