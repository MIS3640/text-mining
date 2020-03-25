import math 
import string 
import sys 
  
def read_file(filename):  
    '''
    Read file.
    '''
    try: 
        with open(filename, encoding="utf8") as f: 
            data = f.read() 
        return data 
      
    except IOError: 
        print("Error opening or reading input file: ", filename) 
        sys.exit() 
  
# splitting the text lines into words 
# translation table is a global variable 
# mapping upper case to lower case and 
# punctuation to spaces 
translation_table = str.maketrans(string.punctuation+string.ascii_uppercase, 
                                     " "*len(string.punctuation)+string.ascii_lowercase) 
       

def get_words_from_line_list(text):  
    '''
    Return a list of the words in the file.
    '''
    text = text.translate(translation_table) 
    word_list = text.split() 
      
    return word_list 
  
  
def count_frequency(word_list):  
    '''
    Count frequency of each word and return a dictionary which maps the words to their frequency.
    '''
      
    D = {} 
      
    for new_word in word_list: 
          
        if new_word in D: 
            D[new_word] = D[new_word] + 1
              
        else: 
            D[new_word] = 1
              
    return D 
  

def word_frequencies_for_file(filename): 
    '''
    Return dictionary of (word,frequency) and pair from the previous dictionary.
    ''' 
      
    line_list = read_file(filename) 
    word_list = get_words_from_line_list(line_list) 
    freq_mapping = count_frequency(word_list) 
  
    print("File", filename, ":", ) 
    print(len(line_list), "lines, ", ) 
    print(len(word_list), "words, ", ) 
    print(len(freq_mapping), "distinct words") 
  
    return freq_mapping 
  
  
def dotProduct(D1, D2): 
    '''
    Returns the dot product of two books.
    ''' 
    Sum = 0.0
      
    for key in D1: 
          
        if key in D2: 
            Sum += (D1[key] * D2[key]) 
              
    return Sum
  
  
def vector_angle(D1, D2):  
    '''
    Returns the angle in radians between document vectors. 
    '''
    numerator = dotProduct(D1, D2) 
    denominator = math.sqrt(dotProduct(D1, D1)*dotProduct(D2, D2)) 
      
    return math.acos(numerator / denominator) 
  
  
def documentSimilarity(filename_1, filename_2): 
      
   # filename_1 = sys.argv[1] 
   # filename_2 = sys.argv[2] 
    sorted_word_list_1 = word_frequencies_for_file(filename_1) 
    sorted_word_list_2 = word_frequencies_for_file(filename_2) 
    distance = vector_angle(sorted_word_list_1, sorted_word_list_2) 
      
    print("The distance between the documents is: % 0.6f (radians)"% distance) 
      
# Driver code 
documentSimilarity('Assignment 2/Walden.txt','Assignment 2/Beyond_good_evil.txt') 
documentSimilarity('Assignment 2/Walden.txt','Assignment 2/Alice.txt')
documentSimilarity('Assignment 2/Beyond_good_evil.txt','Assignment 2/Alice.txt')
