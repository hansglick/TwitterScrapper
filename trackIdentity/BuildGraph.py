#!/usr/bin/env python
# coding: utf-8

# In[64]:


import pandas as pd
import pickle
import itertools
from ast import literal_eval


# In[65]:


gdf = pickle.load(open('/home/osboxes/proj/twitter/trackIdentity/graphdf.pkl', 'rb'))
filename = '/home/osboxes/proj/twitter/tweets.data'


# In[66]:


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


# In[67]:


maliste,NewErrors,NewNtweets,NewLineMemorisied = RetrieveTweetsFromLastPoint(filename,0)
tdf = pd.DataFrame(maliste)


# In[70]:


a = tdf[["USERNAME",
         "USERID",
         "USERFOLLOWERS",
         "USERFNAME",
         "USERDESCRIPTION"]].\
rename(columns = {"USERNAME" : "NAME",
                  "USERID" : "ID",
                  "USERFOLLOWERS" : "NFOL",
                  "USERFNAME" : "FNAME",
                  "USERDESCRIPTION":"DESCRIPTION"})

b = tdf[["AUTHORNAME",
         "AUTHORID",
         "AUTHORFOLLOWERS",
         "AUTHORFNAME",
         "AUTHORDESCRIPTION"]].\
rename(columns = {"AUTHORNAME" : "NAME",
                  "AUTHORID" : "ID",
                  "AUTHORFOLLOWERS" :"NFOL",
                  "AUTHORFNAME":"FNAME",
                  "AUTHORDESCRIPTION":"DESCRIPTION"})


# In[71]:


tdf = pd.concat([a,b],axis=0, sort=False)
tdf.sort_values(by="FNAME",ascending=False,inplace=True)
tdf = tdf.drop_duplicates(subset = ["ID"])


# In[72]:


final = gdf.merge(tdf,how="left",left_on="A",right_on="ID",).rename(columns = {"NAME" : "ANAME",
                  "NFOL":"ANFOL",
                  "DESCRIPTION" : "ADESCRIPTION","FNAME":"AFNAME"}).drop(columns='ID')

final = final.merge(tdf,how="left",left_on="B",right_on="ID").rename(columns = {"NAME" : "BNAME",
                  "NFOL":"BNFOL",
                  "DESCRIPTION" : "BDESCRIPTION","FNAME":"BFNAME"}).drop(columns=['ID'])

final.sort_values(by="f",ascending=False,inplace=True)
final = final[final.A != final.B]
final.reset_index(drop=True,inplace=True)


# In[73]:


pickle.dump(final, open('/home/osboxes/proj/twitter/trackIdentity/GraphIdentity.pkl', 'wb'))


# In[74]:


print("Nombre de links :",len(final))


# In[75]:


print("")
print(final[["A","B","f"]].head())


# In[76]:


final.to_csv("graph.csv",index=False)

