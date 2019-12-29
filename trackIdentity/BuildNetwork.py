#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import json
import pickle
import os
import itertools
from ast import literal_eval


# In[2]:


filename = "/home/osboxes/proj/twitter/tweets.data"
f = "%a %b %d %H:%M:%S +0000 %Y"


# In[3]:


if len(os.listdir("/home/osboxes/proj/twitter/trackIdentity"))>2:
    OldErrors = pickle.load(open('/home/osboxes/proj/twitter/trackIdentity/errors.pkl', 'rb'))
    OldNtweets = pickle.load(open('/home/osboxes/proj/twitter/trackIdentity/ntweets.pkl', 'rb'))
    OldLinksDf = pickle.load(open('/home/osboxes/proj/twitter/trackIdentity/linksdf.pkl', 'rb'))
    OldGraphDf = pickle.load(open('/home/osboxes/proj/twitter/trackIdentity/graphdf.pkl', 'rb'))
else:
    OldNtweets = -1
    OldErrors = 0
    OldLinksDf = pd.DataFrame()
    OldGraphDf = pd.DataFrame()


# In[4]:


print(OldErrors)
print(OldNtweets)
print(len(OldLinksDf))
print(len(OldGraphDf))


# In[15]:


def BuildGraphLinksUser(UserRTList):
    UserRTID = [item[0] for item in UserRTList]
    UserRTLinks = [pair for pair in itertools.combinations(UserRTID,2)]
    return UserRTLinks

def BuildGraphLinksDf(df):
    RTlist = df.RT.tolist()
    GraphLinksDf = []
    for UserRTList in RTlist:
        GraphLinksDf = GraphLinksDf + BuildGraphLinksUser(UserRTList)
    return GraphLinksDf

def RetrieveComputer(GraphLinksDf):
    compteur = {}
    for link in GraphLinksDf:
        compteur[link] = compteur.get(link, 0) + 1
    return compteur

def DefineGraphDf(computer):
    GraphComputerDf = pd.DataFrame(data=computer,index=[0]).    T.    reset_index().    rename(columns={"level_0": "A", "level_1": "B", 0 : "f"})
    return GraphComputerDf


# In[16]:


def RetrieveTweetsFromLastPoint(filename,LineMemorisied):

    # Initialisation
    maliste = []
    errors = 0
    ntweets = 0
    
    # Read New Tweets
    with open(filename) as fp:
        for line in fp:
            ntweets = ntweets + 1 
            if ntweets > LineMemorisied:
                try:
                    maliste.append(literal_eval(line))
                except:
                    errors = errors + 1

    return maliste,errors,ntweets,LineMemorisied


# In[17]:


maliste,NewErrors,NewNtweets,NewLineMemorisied = RetrieveTweetsFromLastPoint(filename,OldNtweets)


# In[18]:


tweetsdf = pd.DataFrame(maliste)
NewLinksDf = tweetsdf[["USERID","AUTHORID","TWEETTIMESTAMP"]][tweetsdf.AUTHORID != ""]
NewLinksDf.TWEETTIMESTAMP = pd.to_datetime(NewLinksDf.TWEETTIMESTAMP,format = f, errors='ignore')
NewLinksDf.TWEETTIMESTAMP = NewLinksDf.TWEETTIMESTAMP.map(lambda a : a.value // 10**9)
NewLinksDf = NewLinksDf.groupby('USERID')[['AUTHORID','TWEETTIMESTAMP']].apply(lambda x: [tuple(i) for i in x.values]).reset_index(name='RT')


# In[19]:


GraphLinksDf = BuildGraphLinksDf(NewLinksDf)
computer = RetrieveComputer(GraphLinksDf)
NewGraphDf = DefineGraphDf(computer)


# In[20]:


NewLinksDf = OldLinksDf.append(NewLinksDf)
NewLinksDf = NewLinksDf.groupby('USERID').RT.apply(sum).reset_index(name='RT')


# In[21]:


NewGraphDf = OldGraphDf.append(NewGraphDf)
NewGraphDf = NewGraphDf.groupby(["A","B"]).f.sum().reset_index()


# In[22]:


pickle.dump(NewErrors + OldErrors, open('/home/osboxes/proj/twitter/trackIdentity/errors.pkl', 'wb'))
pickle.dump(NewNtweets, open('/home/osboxes/proj/twitter/trackIdentity/ntweets.pkl', 'wb'))
pickle.dump(NewLinksDf, open('/home/osboxes/proj/twitter/trackIdentity/linksdf.pkl', 'wb'))
pickle.dump(NewGraphDf, open('/home/osboxes/proj/twitter/trackIdentity/graphdf.pkl', 'wb'))


# In[ ]:




