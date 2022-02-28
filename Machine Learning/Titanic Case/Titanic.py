#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


# In[2]:


entrenamiento = pd. read_csv('titanic.csv')


# In[4]:


entrenamiento.head ()


# In[ ]:





# In[7]:


sns.countplot(x='Survived', data=entrenamiento)


# In[8]:


sns.countplot (x='Survived',data=entrenamiento, hue='Pclass')


# In[9]:


sns.countplot (x='Survived',data=entrenamiento, hue='Sex')


# In[10]:


sns.distplot(entrenamiento ['Age'].dropna(), kde=False, bins=40)


# In[12]:


sns.countplot(x='SibSp', data=entrenamiento)


# In[13]:


entrenamiento['Fare'].hist(bins=20)


# In[14]:


sns.heatmap(entrenamiento.isnull())


# In[17]:


sns.boxplot(x='Pclass', y='Age', data=entrenamiento)


# In[21]:


def edad_media(columnas):
    edad = columnas [0]
    clase = columnas [1]
    if pd.isnull(edad):
        if clase == 1:
             return 38
        elif clase == 2:
             return 29
        else:
             return 25
    else:
         return edad


# In[22]:


sns.heatmap(entrenamiento.isnull())


# In[23]:


def edad_media(columnas):
    edad = columnas [0]
    clase = columnas [1]
    if pd.isnull(edad):
        if clase == 1:
             return 38
        elif clase == 2:
             return 29
        else:
             return 25
    else:
         return edad


# In[25]:


entrenamiento['Age'] = entrenamiento[['Age', 'Pclass']].apply(edad_media, axis=1)


# In[26]:


sns.heatmap(entrenamiento.isnull())


# In[29]:


entrenamiento.drop('Cabin',axis=1,inplace=True)


# In[30]:


sns.heatmap(entrenamiento.isnull())


# In[31]:


pd.get_dummies(entrenamiento ['Sex'])


# In[35]:


sexo = pd.get_dummies (entrenamiento['Sex'],drop_first=True)


# In[36]:


sexo = pd.get_dummies (entrenamiento['Sex'],drop_first=True)


# In[37]:


pd.get_dummies(entrenamiento['Embarked'])


# In[38]:


pd.get_dummies(entrenamiento['Embarked'])


# In[40]:


puerto = pd.get_dummies (entrenamiento['Embarked'], drop_first=True)


# In[41]:


entrenamiento  = pd.concat ( [entrenamiento, sexo, puerto], axis=1) 


# In[43]:


entrenamiento.drop( ['PassengerId', 'Name', 'Sex','Ticket', 'Embarked'], axis=1, inplace=True)


# In[44]:


entrenamiento.head ()


# In[45]:


X = entrenamiento.drop('Survived', axis=1)


# In[46]:


y = entrenamiento ['Survived'] 


# In[48]:


from sklearn.model_selection import train_test_split


# In[49]:


X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=45)


# In[50]:


from sklearn. linear_model import LogisticRegression


# In[51]:


modelo = LogisticRegression() 


# In[52]:


modelo.fit(Xtřain, y_train)


# In[53]:


modelo.fit(X_train, y_train)


# In[54]:


predicciones = modelo.predict(X_test) 


# In[55]:


from sklearn.metrics import classification_report


# In[56]:


print(classification_report(y_test,predicciones))


# In[57]:


from sklearn.metrics import confusion_matrix


# In[58]:


confusion_matrix(y_test,predicciones)


# In[ ]:




