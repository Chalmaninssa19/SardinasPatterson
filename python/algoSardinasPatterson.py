#Enlever le prefixe d'un mot
def remove_prefixe(word, prefix) :
    if(word == prefix) :
        return 'e'
    if(word.startswith(prefix)) :
        return word[len(prefix):]
    return None
    
#Trouver le residuel d'un langage
def residuel(langage, prefixe) :
    residuel = []
    for i in range(len(langage)) :
        motSansPrefixe = remove_prefixe(langage[i], prefixe)
        if motSansPrefixe != None :
            residuel.append(motSansPrefixe)

    return residuel

#Convertir une liste a deux dimension a une dimension
def convert_in_one_dimension(list) :
    list1Dimension = []
    for i in range(len(list)) :
        for j in range(len(list[i])) :
            list1Dimension.append(list[i][j])
    return list1Dimension
    
#Trouver le quotient d'un langage
def quotient(langage, M) :
    quotient = []
    for i in range(len(M)) :
        residuelValue = residuel(langage, M[i])
        quotient.append(residuelValue)

    quotientConverted = convert_in_one_dimension(quotient) 
    quotientWithoutDoublon = list(set(quotientConverted))
    return quotientWithoutDoublon

#Est ce que la liste contient un epsilon
def isHavingEpsilon(list, epsilon) :
    for i in range(len(list)) :
        if(list[i] == epsilon) :
            return True
    return False

#Est ce que la liste est deja dans la liste a deux dimensions
def isListInListTwoDimension(list2D, list1D) :
    if list1D in list2D :
        return True
    return False

#Est ce que le langage est un code ou non
def algoSardinasPatterson(langage) :
    
    if langage == None or len(langage) == 0 or '' in langage :
        return False
        
    M = []
    M.append(langage)
    count = 1
        
    while True :
        quotientValue = quotient(langage, M[-1])
        if(count == 1) :
            quotientValue.remove('e')
        havingEpsilon = isHavingEpsilon(quotientValue, 'e')
        if(havingEpsilon and count > 1 == True) :
            M.append(quotientValue)
            return False
        isListInListQuotient = isListInListTwoDimension(M, quotientValue)
        if(isListInListQuotient == True) :
            M.append(quotientValue)
            return True
        count = count + 1
        M.append(quotientValue)
#original_tab = [1, 2, 2, 3, 4, 4, 5]
#sans_doublon = list(set(original_tab))
#print(sans_doublon)

#L = ['0', '01', '110', '1101', '1111']
#isCode = algoSardinasPatterson(L)
#print(isCode)