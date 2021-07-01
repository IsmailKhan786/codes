#download data.json first which has data of json
import json #to load json data
import difflib # to get  close matching wordes ie if user type waterrr 
from difflib import get_close_matches as gcm 
#get close matcxhes method takes close matches ie if the word  id waterr the most similar word from dictnory will be taken\
    

data = json.load(open("data.json"))#to load json data
def translate(word):
        word = word.lower()   # if user enter word in like WaTeR it should conv to lowr case
        if word in data:
           return data[word]
        elif(word.title() in data): # if word in dict is Delhi and user put delhi 
            return data[word.title()]
        elif(word.upper() in data): # if word in dictnoey is USA and user put usa
            return data[word.upper()]
        elif len(gcm(word,data.keys())) > 0:  #data.kleys as we need keys from json 
            #get_close_matches('waterrr', ["water",'rain'],number of close matches,cutoff from 1)
            #cut pff means  close match whivh has similaroty more then 0.8 etc in scale of 1
            d= gcm(word,data.keys())[0]
            ab = input(f"Did you mean {d}.? Press Y for Yes and N for No")
            if ab == 'y': # if user put waterr it ask did u mean water
               return data[gcm(word,data.keys())[0]] # gives first most similar word
            elif ab == 'n':
               return 'Mismatched'
            else:
               return "Wrong input"
        else:
            return "Sorry the word does not exixsts"

word1 = input("Enter the word")
output = translate(word1)
if type(output)==list:
    for i in output:
      print(i)
else:
    print(output)
  