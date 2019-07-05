import re
import pandas as pd
import numpy as np
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
from keras.models import load_model
from sklearn.feature_extraction.text import CountVectorizer
import tweepy


#API keys from developer.twitter.com
apikey='7NCzIYyE6v4rXHFgBfMjy6GqD'
apisecretkey='mkD5V5WdViePkoiNdt5R4W0o8PJ8tojHXUxGgMzHhctp0rbRI6'
acctoken='1144102706333618176-wIUa115mxUw7n1IHmpFEW5RTSs81li'
acctokensecret='ccwvQxyexrKQTpdzRJyxgF6nJratx2qvKzTbWrrMwgPYn'


p=PorterStemmer()
stwrds=stopwords.words("english")
def filtr(st):
    arr=[re.sub("[http,@,#].*","",x) for x in st.split() if x not in stwrds]
    arr=[p.stem(x) for x in arr]
    return ' '.join(arr)
    

auth =tweepy.OAuthHandler(apikey,apisecretkey)
auth.set_access_token(acctoken,acctokensecret)
api=tweepy.API(auth)
user=input("Enter Twitter Username: ")
tweets=tweepy.Cursor(api.search,q='@'+user).items(50)
text=[]
for t in tweets:
    text.append(filtr(t.text))
    text.append("|||")
    
text=' '.join(text)

tcv=CountVectorizer(decode_error="replace",vocabulary=pickle.load(open("vocab.pkl","rb")))
m=load_model('mymodel.h5')
res=np.argmax(m.predict(tcv.transform([text])))
typ=['INFJ', 'ENTP', 'INTP', 'INTJ', 'ENTJ', 'ENFJ', 'INFP', 'ENFP',
       'ISFP', 'ISTP', 'ISFJ', 'ISTJ', 'ESTP', 'ESFP', 'ESTJ', 'ESFJ']
print("Personality: "+typ[res])
print('Introversion (I) – Extroversion (E)\nIntuition (N) – Sensing (S)\nThinking (T) – Feeling (F)\nJudging (J) – Perceiving (P)')