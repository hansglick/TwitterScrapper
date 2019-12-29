#!/usr/bin/env python
# coding: utf-8

# In[353]:


import pandas as pd
import json
import pickle
import os
from ast import literal_eval


# In[391]:


filename = "/home/osboxes/proj/twitter/tweets.data"
f = "%a %b %d %H:%M:%S +0000 %Y"


# In[404]:


if len(os.listdir("/home/osboxes/proj/twitter/track"))>1:
    OldErrors = pickle.load(open('/home/osboxes/proj/twitter/track/errors.pkl', 'rb'))
    OldNtweets = pickle.load(open('/home/osboxes/proj/twitter/track/ntweets.pkl', 'rb'))
    OldLinksDf = pickle.load(open('/home/osboxes/proj/twitter/track/linksdf.pkl', 'rb'))
else:
    OldNtweets = -1
    OldErrors = 0
    OldLinksDf = pd.DataFrame()


# In[393]:


print(OldErrors)
print(OldNtweets)
print(len(OldLinksDf))


# In[394]:


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


# In[395]:


maliste,NewErrors,NewNtweets,NewLineMemorisied = RetrieveTweetsFromLastPoint(filename,OldNtweets)


# In[396]:


tweetsdf = pd.DataFrame(maliste)
NewLinksDf = tweetsdf[["USERID","AUTHORID","TWEETTIMESTAMP"]][tweetsdf.AUTHORID != ""]
NewLinksDf.TWEETTIMESTAMP = pd.to_datetime(NewLinksDf.TWEETTIMESTAMP,format = f, errors='ignore')
NewLinksDf.TWEETTIMESTAMP = NewLinksDf.TWEETTIMESTAMP.map(lambda a : a.value // 10**9)
NewLinksDf = NewLinksDf.groupby('USERID')[['AUTHORID','TWEETTIMESTAMP']].apply(lambda x: [tuple(i) for i in x.values]).reset_index(name='RT')


# In[397]:


NewLinksDf = OldLinksDf.append(NewLinksDf)
NewLinksDf = NewLinksDf.groupby('USERID').RT.apply(sum).reset_index(name='RT')


# In[398]:


pickle.dump(NewErrors + OldErrors, open('/home/osboxes/proj/twitter/track/errors.pkl', 'wb'))
pickle.dump(NewNtweets, open('/home/osboxes/proj/twitter/track/ntweets.pkl', 'wb'))
pickle.dump(NewLinksDf, open('/home/osboxes/proj/twitter/track/linksdf.pkl', 'wb'))


# In[ ]:


print(len(NewLinksDf))


# In[ ]:




