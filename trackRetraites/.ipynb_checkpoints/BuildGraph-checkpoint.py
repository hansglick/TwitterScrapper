#!/usr/bin/env python
# coding: utf-8

# In[221]:


import pandas as pd
import pickle
import itertools
from ast import literal_eval


# In[222]:


gdf = pickle.load(open('/home/osboxes/proj/twitter/track/graphdf.pkl', 'rb'))
filename = '/home/osboxes/proj/twitter/tweets.data'


# In[223]:


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


# In[224]:


maliste,NewErrors,NewNtweets,NewLineMemorisied = RetrieveTweetsFromLastPoint(filename,0)


# In[225]:


tdf = pd.DataFrame(maliste)
a = tdf[["USERNAME","USERID"]].rename(columns = {"USERNAME" : "NAME", "USERID" : "ID"})
b = tdf[["AUTHORNAME","AUTHORID"]].rename(columns = {"AUTHORNAME" : "NAME", "AUTHORID" : "ID"})
tdf = pd.concat([a,b],axis=0, sort=False)
tdf = tdf.drop_duplicates()


# In[226]:


final = gdf.merge(tdf,how="left",left_on="A",right_on="ID",).rename(columns = {"NAME" : "ANAME"}).drop(columns='ID')

final = final.merge(tdf,how="left",left_on="B",right_on="ID").rename(columns = {"NAME" : "BNAME"}).drop(columns=['ID'])

final.sort_values(by="f",ascending=False,inplace=True)
final = final[final.A != final.B]
final.reset_index(drop=True,inplace=True)


# In[227]:


pickle.dump(final, open('/home/osboxes/proj/twitter/track/GraphIdentity.pkl', 'wb'))


# In[228]:


print("Nombre de links :",len(final))


# In[230]:


print("")
print(final[["A","B","f"]].head)


# In[ ]:




