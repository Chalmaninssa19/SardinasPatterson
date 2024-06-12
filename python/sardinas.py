import algoSardinasPatterson as algo
import sys

language_in = sys.argv[1] 
language = language_in.split(', ')
result = ''
isCode = algo.algoSardinasPatterson(language)

if isCode == False :
    result = '<p class="para" style="color: red; font-size: 100px">FALSE<p>'
else :
    result = '<p class="para" style="color: green; font-size: 100px">TRUE<p>'

print(result)