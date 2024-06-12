from sklearn.svm import LinearSVC
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import confusion_matrix, accuracy_score
from joblib import dump
from joblib import load
import pandas as pd
import generateCodeAndNoCode as gcn

#Stocker dans un fichier csv les donnees d'un dataframe
def to_csv(df, csv_file_path) :
    df.to_csv(csv_file_path, sep=';', index=False)

#Charger le dataframe venant du csv
def load_df(csv_file_path) :
    df = pd.read_csv(csv_file_path, sep=";")

    return df


#Entrainer le modele
def train_model(data) :
    #Recuperer les features et la classe
    X = data.iloc[:, 1:-1]
    y = data.iloc[:, -1]
    y = y.astype('int')
    #20% donnee de test et les restes sont pour l'entrainement
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.20,random_state = 0)
    
    # Entrainement d'un modèle SVM linéaire
    model = RandomForestClassifier(random_state=0)
    model = model.fit(X_train, y_train)
    
    #Avoir les predictions par les donnees de test
    y_pred = model.predict(X_test)
    
    #Resultat des predictions
    cm = confusion_matrix(y_test, y_pred)
    #print("Resultat des predictions :")
    #print(cm)
    
    #Evaluation du precision
    #print("Evaluation du precision : " + str(accuracy_score(y_test, y_pred)))
    ev = str(accuracy_score(y_test, y_pred))
    
    return model, ev

#Enregistrer le model d'entrainement
def save_model(model, path) :    
    dump(model, path)

#Charger le model d'entrainement
def load_model(model_train_path) :   
    return load(model_train_path)

#Entrainer et sauvergarder le modele
def train_and_save_model(data, path) :
    model, ev = train_model(data)
    ev = round(float(ev) * 100, 2)
    print(str(ev)+'%')
    save_model(model, path)

    return ev

#Preparation du donnee d'entree
def get_language_matrix(language) :
    size_min_word = min(len(s) for s in language)
    size_max_word = max(len(s) for s in language)
    average_length_word = sum(len(s) for s in language) / len(language)
    language_length = len(language)
    number_0 = gcn.count_number(language, 0)
    number_1 = gcn.count_number(language, 1)
    variance = gcn.calcul_variance(language, average_length_word)
    ecart_type = gcn.calcul_ecart_type(variance)
    new_row = {
        'language': language,
        'length': language_length,
        'size_min_word': size_min_word,
        'size_max_word': size_max_word,
        'size_average_word': round(average_length_word, 2),
        'number_0': number_0,
        'number_1': number_1,
        'variance': round(variance, 2),
        'ecart_type': ecart_type
    }
    lang_matrix = [new_row]
    
    columns = ['language', 'length', 'size_min_word', 'size_max_word', 'size_average_word', 'number_0', 'number_1', 'variance', 'ecart_type']
    df = pd.DataFrame(lang_matrix, columns=columns)

    return df
    
#Avoir la prediction
def get_predict(language, model_train) :  
    language_matrix = get_language_matrix(language)
    # Charger le modèle et effectuer la prédiction
    modelLoad = load_model(model_train)
    prediction = modelLoad.predict(language_matrix.iloc[:, 1:])
    return prediction