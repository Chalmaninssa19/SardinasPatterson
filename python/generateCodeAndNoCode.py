import random
import pandas as pd
from itertools import combinations
import algoSardinasPatterson as algo
import math

#Genere un mot binaire de longueur comprise entre min_len et max_len
def generate_binary_word(min_len, max_len) :
    length = random.randint(min_len, max_len)
    return ''.join(random.choice('01') for _ in range(length))

#Genere un langage avecdes mots de longueurs donnees
def generate_language(min_size, max_size, min_word_len, max_word_len) :
    size = random.randint(min_size, max_size)
    return [generate_binary_word(min_word_len, max_word_len) for _ in range(size)]

#Calculer la variance d'un language
def calcul_variance(language, average) :
    variance = 0
    for word in language :
        diff = (len(word) - average)**2
        variance = variance + diff
    return variance

#Calculer l'ecart-type
def calcul_ecart_type(variance) :
    return math.sqrt(variance)

#Compter le nombre dans la liste
def count_number(list, number) :
    count = 0
    for item in list :
        for string in item :
            if string == str(number) :
                count = count + 1
    return count

#Representation binaire du langage
def binary_representation(list) :
    binary = ''
    for item in list :
        binary = binary + '' + item
    return binary

#Genere n langages codes distincts
def generate_code_languages(df, n, min_size, max_size, min_word_len, max_word_len) :
    codes = []
    while len(codes) < n :
        language = generate_language(min_size, max_size, min_word_len, max_word_len)
        if algo.algoSardinasPatterson(language) == True and language not in codes :
            size_min_word = min(len(s) for s in language)
            size_max_word = max(len(s) for s in language)
            average_length_word = sum(len(s) for s in language) / len(language)
            language_length = len(language)
            number_0 = count_number(language, 0)
            number_1 = count_number(language, 1)
            variance = calcul_variance(language, average_length_word)
            ecart_type = calcul_ecart_type(variance)
            is_code = 1
            new_row = {
                'language': language,
                'length': language_length,
                'size_min_word': size_min_word,
                'size_max_word': size_max_word,
                'size_average_word': round(average_length_word, 2),
                'number_0': number_0,
                'number_1': number_1,
                'variance': round(variance, 2),
                'ecart_type': ecart_type,
                'is_code': is_code
            }
            codes.append(new_row)

            
    # Convertir la liste de dictionnaires en DataFrame et concaténer
    df = pd.concat([df, pd.DataFrame(codes)], ignore_index=True)
    
    return df
    
#Genere n langages non codes distincts
def generate_no_code_languages(df, n, min_size, max_size, min_word_len, max_word_len) :
    no_codes = []
    while len(no_codes) < n :
        language = generate_language(min_size, max_size, min_word_len, max_word_len)
        if algo.algoSardinasPatterson(language) == False and language not in no_codes :         
            size_min_word = min(len(s) for s in language)
            size_max_word = max(len(s) for s in language)
            average_length_word = sum(len(s) for s in language) / len(language)
            language_length = len(language)
            number_0 = count_number(language, 0)
            number_1 = count_number(language, 1)
            variance = calcul_variance(language, average_length_word)
            ecart_type = calcul_ecart_type(variance)
            is_code = 0
            new_row = {
                'language': language,
                'length': language_length,
                'size_min_word': size_min_word,
                'size_max_word': size_max_word,
                'size_average_word': round(average_length_word, 2),
                'number_0': number_0,
                'number_1': number_1,
                'variance': round(variance, 2),
                'ecart_type': ecart_type,
                'is_code': is_code
            }
            no_codes.append(new_row)
    
    # Convertir la liste de dictionnaires en DataFrame et concaténer
    df = pd.concat([df, pd.DataFrame(no_codes)], ignore_index=True)

    return df