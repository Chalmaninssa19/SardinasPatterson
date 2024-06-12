import pandas as pd
import generateCodeAndNoCode as gcn
import modele as md

# Define the columns and create an empty DataFrame
columns = ['language', 'length', 'size_min_word', 'size_max_word', 'size_average_word', 'number_0', 'number_1', 'variance', 'ecart_type', 'is_code']
df = pd.DataFrame(columns=columns)
n = 2500
min_size = 1
max_size = 10
min_word_len = 1
max_word_len = 7
csv_file_path = '/var/www/html/sardinasPatterson/python/datas.csv'
df = gcn.generate_code_languages(df, n, min_size, max_size, min_word_len, max_word_len)
df = gcn.generate_no_code_languages(df, n, min_size, max_size, min_word_len, max_word_len)
#md.to_csv(df, csv_file_path)
#datas = md.load_df(csv_file_path)
model_train_path = '/var/www/html/sardinasPatterson/python/model_saved.joblib'
evaluation_prediction_string = md.train_and_save_model(df, model_train_path)
#evaluation_prediction = round(float(evaluation_prediction_string)*100, 2)
#print(str(evaluation_prediction)+'%')