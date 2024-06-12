import modele as md
import sys

language_in = sys.argv[1] 
language = language_in.split(', ')
model_train_path = '/var/www/html/sardinasPatterson/python/model_saved.joblib'
prediction = md.get_predict(language, model_train_path)
result = ''
if prediction[0] == 0 :
    result = '<p class="para" style="color: red; font-size: 100px">FALSE<p>'
else :
    result = '<p class="para" style="color: green; font-size: 100px">TRUE<p>'

print(result)