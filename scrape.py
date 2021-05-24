from urllib.request import Request, urlopen
import pandas as pd
from io import BytesIO
import csv, re
import requests
from bs4 import BeautifulSoup
import nltk
from nltk.sentiment import SentimentIntensityAnalyzer
from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator


import matplotlib.pyplot as plt
    
req = Request('https://www.glassdoor.co.in/Reviews/Neustar-Reviews-E13026.htm', headers={'User-Agent': 'Mozilla/5.0'})
webpage = urlopen(req).read()
print(type(webpage))
# print(webpage)
f = open("sample.html", "wb")
f.write(webpage)
with open("sample.html",encoding="utf8") as fp:
    soup = BeautifulSoup(fp, "html.parser")

t = soup.get_text().split()

g = open("sample_output2.txt", "w",encoding="utf8")
g.write(str(t))
stopwords = nltk.corpus.stopwords.words("english")
word = [i for i in str(t).split(',') if i.lower() not in stopwords]
for w in word:
    text = ''.join(str(i) for i in w if i.isalpha())
    sia = SentimentIntensityAnalyzer()
    s = text,',',sia.polarity_scores(text)
    theTokens = re.findall(r'\b\w[\w-]*\b', text.lower())
    # print(theTokens[:5])
numPosWords = 0
positive_words = open("positive-words.txt", "r",encoding="utf8")
negative_words = open("negative-words.txt", "r",encoding="utf8")
pw  = positive_words.read()
# print(pw)
word = [i for i in str(t).split(',') if i.lower() not in stopwords]
for w in word:
    text = ''.join(str(i) for i in w if i.isalpha())
    # print(text)
for wd in text:
    if wd in pw:
        numPosWords += 1
print(wd,pw,numPosWords)
    # print(s)
    # s = list(print(s, sep=' ', end='', flush=True))
    # print(type(s))
    # h = open("result1.txt", "w",encoding="utf8")
    # h.write(s)
    # txt = [t for t in s]
#     h = open("result1.txt", "w",encoding="utf8")
#     h.write(str(t))
# j=open("result1.txt", "r",encoding="utf8")
# wd = [k for k in j if k.isalpha()]
# print(wd)

f.close()
