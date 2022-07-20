#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


# In[43]:


class automatedEDA():
    def __init__(self , data):
        self.data = pd.read_csv(data)
    def loadData(self):        
        return self.data
    #def imputeMissingValuesByMode(self)
    def missingValues(self):
        print("Check if theres Missing Values : ")
        print(self.data.isnull().sum())
        print("Percentage of missing Values: ")
        print(self.data.isna().sum()/self.data.shape[0])
    def totalView(self):
        print("This Head of File:\n" , self.data.head())
        print("This Tail of File:\n" , self.data.tail())
        print("This Description of File:\n" , self.data.describe())
        print("This info of File:\n" , self.data.info())
        print("This shape of File:\n" , self.data.shape)
        print("This columns of File:\n" , self.data.columns)
        print("This Unique values of File:\n" ,self.data.nunique())
        print("This Missing values of File:\n" ,self.data.isnull().sum())
    def everyCloumnGraph(self):
        sns.set()

        numeric_columns = [x for x in self.data.columns if self.data.dtypes[x] in ['float', 'int']]

        for var in numeric_columns:
            fig, ax = plt.subplots()
            ax.hist(self.data[var], bins=25)
            ax.set_title(f'Distribution of {var}')
    def cloumnsInfo(self):

        numeric_columns = [x for x in self.data.columns if self.data.dtypes[x] in ['float', 'int']]

        for var in numeric_columns:
            print ("Column" , self.data[var] , " Description is :\n" , self.data.describe() ,)
        

        
    def detectOutliers(self):
        
        numeric_columns = [x for x in self.data.columns if self.data.dtypes[x] in ['float', 'int']]

        for var in numeric_columns:
            p0=self.data[var].min()
            p100=self.data[var].max()
            q1=self.data[var].quantile(0.25)
            q2=self.data[var].quantile(0.5)
            q3=self.data[var].quantile(0.75)
            iqr=q3-q1
            lc = q1 - 1.5*iqr
            uc = q3 + 1.5*iqr
           
            print( "Column: " , var ,"\n", "p0 = " , p0 ,", p100 = " , p100 ,", lc = " , lc ,", uc = " , uc , '\n' )
    def univarteAnalysisForAllColumns(self):
        
        numeric_columns = [x for x in self.data.columns if self.data.dtypes[x] in ['float', 'int']]
        for var in numeric_columns:
            self.data[var].hist()
            print("Column: ", var)
            plt.show()
            
    def boxPlotForAllColumns(self):
        numeric_columns = [x for x in self.data.columns if self.data.dtypes[x] in ['float', 'int']]
        for var in numeric_columns:
            self.data[var].plot(kind = 'box')
            print("Column: ", var)
            plt.show()

    def bivariateAnalysis(X , Y):
        plt.scatter(x= X , y= Y)
        plt.show()
        
    def correlationMatrix(self):
        self.data.select_dtypes(['float64' , 'int64']).corr()
    def heatMap(self):
        sns.heatmap(10*self.data.select_dtypes(['float64' , 'int64']).corr(),annot=True)
        plt.show()
        
        
    
        
        
        
        
        
   
        
        


# In[44]:


file = automatedEDA("Features data set.csv")


# In[46]:


file.heatMap()


# In[25]:


file.loadData()


# In[26]:


file.univarteAnalysisForAllColumns()


# In[15]:


file.missingValues()


# In[9]:


file.totalView()


# In[14]:


file.totalView()


# In[11]:


file.everyCloumnGraph()


# In[18]:


file.cloumnsInfo()


# In[4]:


file.detectOutliers()


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




