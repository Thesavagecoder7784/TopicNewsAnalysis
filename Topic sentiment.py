#!/usr/bin/env python
# coding: utf-8

# In[1]:


from time import sleep
from random import randint
import newsapi
import requests
from newspaper import Article
import pprint
import matplotlib.pyplot as plt
import pandas as pd
import re
import nltk
nltk.download('punkt')


# In[2]:


plt.rcParams['figure.figsize'] = [30, 15]


# In[3]:


#api key
secret = 'b198ef97107247fd87d110e9af018212'
# Define the endpoint
url = 'https://newsapi.org/v2/everything?'
query = str(input("Enter a topic you are interested about "))
# Specify the query and
# number of returns
parameters = {
    'q': query, # query phrase
    'sortBy':'relevancy',
    "pagesize": 100, # maximum is 100
    "apikey": secret # your own API key
}
# Make the request
response = requests.get(url, params = parameters)
#Convert the response to JSON format and pretty print it
response_json = response.json()
pprint.pprint(response_json)


# In[ ]:


print(response_json['totalResults'])


# In[ ]:


from newspaper import Config

user_agent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'
config = Config()

config.browser_user_agent = user_agent
config.request_timeout = 20


# In[ ]:


for i in range(100):
    url = response_json['articles'][i]['url']
    article = Article(url)
    try:
        article.download()
        article.parse()
        article.nlp()
        print("Number" , i + 1)
        print("Title" ,article.title)
        print("Description", response_json['articles'][i]['description'])
        print("Time", response_json['articles'][i]['publishedAt'])
        print("Source", response_json['articles'][i]['source']['name'])
        print("Keywords" , article.keywords)
        print("Summary", article.summary)
        print("\n")
    except:
        continue    


# In[ ]:


title = []
date = []
description = []
time = []
source = []
text = []
keywords = []
summary = []
links = []
for i in range(100):
    url = response_json['articles'][i]['url']
    links.append(url)
    article = Article(url, config=config)
    try:
        article.download()
        article.parse()
        
    except:
        continue
        
    article.nlp()
    print("Number" , i + 1)
    title.append(article.title)
    text.append(article.text)
    description.append(response_json['articles'][i]['description'])
    date.append(article.publish_date)
    time.append(response_json['articles'][i]['publishedAt'])
    source.append(response_json['articles'][i]['source']['name'])
    keywords.append(article.keywords)
    summary.append(article.summary)
    print("\n")


# In[ ]:


dict = {'date': date, 'time' : time, 'source' : source, 'title': title, 'text' : text, 'description': description,
        'summary' : summary, 'keywords': keywords}


# In[ ]:


dict['description']


# In[ ]:


from sentic import SenticPhrase
text = dict['description'][1]
sp = SenticPhrase(text)
print(sp.info(text))
print(text)


# In[ ]:


from sentic import SenticPhrase


# sp.get_sentics()
# sp.get_moodtags()
# sp.get_sentiment()
# sp.get_polarity()
# sp.get_semantics()

# In[ ]:


lsentiment = []
sentence = []
semantics = []
moodtags = []
sentics = []
for i in range(len(dict['summary'])):    
    text = dict['summary'][i]
    sp = SenticPhrase(text)
    sentiment = sp.info(text)
    sentence.append(text)
    sentics.append(sp.get_sentics())
    moodtags.append(sp.get_moodtags())
    semantics.append(sp.get_semantics())
    lsentiment.append(sp.info(text))
    print(dict['title'][i], '\n')
    print(sp.info(text))
    print('\n')


# In[ ]:


#Polarity
polarity = 0
for i in range(len(lsentiment)):
    polarity += lsentiment[i]['polarity']
print("Mean polarity = ",polarity/(len(lsentiment)))


# In[ ]:


#Words

from collections import Counter
#Words associated
finalsemantics = []
for l in semantics:
    for word in l:
        finalsemantics.append(word)

frequencyword = {}
# iterating over the list
for item in finalsemantics:
    # checking the element in dictionary
    if item in frequencyword:
    # incrementing the counr
        frequencyword[item] += 1
    else:
    # initializing the count
        frequencyword[item] = 1

# printing the frequency
print(frequencyword)

# Finding 3 highest values
highword = Counter(frequencyword).most_common(10)
print("Dictionary with 3 highest values:")
print("Keys: Values")
for i in highword:
    print(i[0]," :",i[1]," ")


# In[ ]:


for i in highword:
    plt.bar(i[0], i[1])
plt.grid(color='#95a5a6', linestyle='--', linewidth=2, axis='y', alpha=0.7)
plt.xticks(fontsize = 25,rotation = 45)
plt.yticks(fontsize = 25)
plt.xlabel("Word",fontsize = 30)
plt.ylabel("Number of tags",fontsize = 30)
plt.title("Number of tags associated with each word",fontsize = 50)
plt.show()


# In[ ]:


#Moodtags
from collections import Counter
# Moodtags
moodtagswords = []
for l in moodtags:
    for word in l:
        moodtagswords.append(word)

frequencytag = {}
# iterating over the list
for item in moodtagswords:
    # checking the element in dictionary
    if item in frequencytag:
    # incrementing the counr
        frequencytag[item] += 1
    else:
    # initializing the count
        frequencytag[item] = 1

# printing the frequency
print(frequencytag)

# Finding 3 highest values
hightag = Counter(frequencytag).most_common(20)
print("Dictionary with 3 highest values:")
print("Keys: Values")
for i in hightag:
    print(i[0]," :",i[1]," ")


# In[ ]:


for i in hightag:
    plt.bar(i[0], i[1])
plt.grid(color='#95a5a6', linestyle='--', linewidth=2, axis='y', alpha=0.7)
plt.xticks(fontsize = 25,rotation = 45)
plt.yticks(fontsize = 25)
plt.xlabel("Moodtag",fontsize = 30)
plt.ylabel("Number of tags",fontsize = 30)
plt.title("Number of tags associated with each moodtag",fontsize = 50)
plt.show()


# In[ ]:


sp.get_sentics(text)


# In[ ]:


pleasantness = 0
attention = 0
sensitivity = 0
aptitude = 0

for i in range(len(dict['summary'])):
    text = dict['description'][i]
    pleasantness = pleasantness + sp.get_sentics(text)['pleasantness']
    attention = attention + sp.get_sentics(text)['attention']
    sensitivity = sensitivity + sp.get_sentics(text)['sensitivity']
    aptitude = aptitude + sp.get_sentics(text)['aptitude']
mean_pleasantness = pleasantness/len(dict['summary'])    
mean_attention = attention/len(dict['summary'])    
mean_sensitivity = sensitivity/len(dict['summary'])    
mean_aptitude = aptitude/len(dict['summary'])    

print("Mean pleasantness",mean_pleasantness)
print("Mean attention",mean_attention)
print("Mean sensitivity",mean_sensitivity)
print("Mean aptitude",mean_aptitude)


# In[ ]:


#Sentics
from collections import Counter
senticattr = []
for l in sentics:
    for word in l:
        senticattr.append(word)

frequencysentic = {}
# iterating over the list
for item in senticattr:
    # checking the element in dictionary
    if item in frequencysentic:
    # incrementing the counr
        frequencysentic[item] += 1
    else:
    # initializing the count
        frequencysentic[item] = 1

# printing the frequency
print(frequencysentic)

# Finding 3 highest values
highsentic = Counter(frequencysentic).most_common(10)
print("Dictionary with 3 highest values:")
print("Keys: Values")
for i in highsentic:
    print(i[0]," :",i[1]," ")


# In[ ]:


for i in highsentic:
    plt.bar(i[0], i[1])
plt.grid(color='#95a5a6', linestyle='--', linewidth=2, axis='y', alpha=0.7)
plt.xticks(fontsize = 25,rotation = 45)
plt.yticks(fontsize = 25)
plt.xlabel("Sentic ",fontsize = 30)
plt.ylabel("Number of tags",fontsize = 30)
plt.title("Number of tags associated with each sentic",fontsize = 50)
plt.show()


# In[ ]:


#Sentiment
sentimentslist = []
for i in range(len(lsentiment)):    
    print(title[i])
    sentimentslist.append(lsentiment[i]['sentiment'])
    print(lsentiment[i]['sentiment'])
    print('\n')


# In[ ]:


frequency = {}
# iterating over the list
for item in sentimentslist:
    # checking the element in dictionary
    if item in frequency:
    # incrementing the counr
        frequency[item] += 1
    else:
    # initializing the count
        frequency[item] = 1

# printing the frequency
print(frequency)


# In[ ]:


plt.bar(range(len(frequency)), list(frequency.values()), align='center')
plt.xticks(range(len(frequency)), list(frequency.keys()),fontsize = 25)
plt.grid(color='#95a5a6', linestyle='--', linewidth=2, axis='y', alpha=0.7)
plt.yticks(fontsize = 25)
plt.xlabel("Sentiment",fontsize = 30)
plt.ylabel("Number of articles",fontsize = 30)
plt.title("Number of articles per sentiment",fontsize = 50)
plt.show()


# In[ ]:





# In[ ]:




