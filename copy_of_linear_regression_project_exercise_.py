# -*- coding: utf-8 -*-
"""Copy of Linear Regression - Project Exercise .ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1fkts3F13a1kHetp5g5CYC3vMl70tz8pP

# Linear Regression - Project Exercise

Congratulations! You just got some contract work with an Ecommerce company based in New York City that sells clothing online but they also have in-store style and clothing advice sessions. Customers come in to the store, have sessions/meetings with a personal stylist, then they can go home and order either on a mobile app or website for the clothes they want.

The company is trying to decide whether to focus their efforts on their mobile app experience or their website. They've hired you on contract to help them figure it out! Let's get started!

Just follow the steps below to analyze the customer data (it's fake, don't worry I didn't give you real credit card numbers or emails).

## Imports
** Import pandas, numpy, matplotlib,and seaborn. Then set %matplotlib inline
(You'll import sklearn as you need it.)**
"""

import numpy as np
import pandas as pd
import seaborn as sns

"""## Get the Data

We'll work with the Ecommerce Customers csv file from the company. It has Customer info, suchas Email, Address, and their color Avatar. Then it also has numerical value columns:

* Avg. Session Length: Average session of in-store style advice sessions.
* Time on App: Average time spent on App in minutes
* Time on Website: Average time spent on Website in minutes
* Length of Membership: How many years the customer has been a member.

** Read in the Ecommerce Customers csv file as a DataFrame called customers.**
"""

from google.colab import files
data = files.upload()

"""**Check the head of customers, and check out its info() and describe() methods.**"""

df_ecomm = pd.read_csv('ecomm.csv')

df_ecomm.head()

df_ecomm.info()

df_ecomm.describe()
#(include='all')

df_ecomm.corr()

df_ecomm.drop('Address',axis=1,inplace=True)

df_ecomm.drop('Email',axis=1,inplace=True)

df_ecomm.head(10)

df_ecomm.drop('Avatar',axis=1,inplace=True)
#Doubtfull as it contains only 138 distinct values.

"""## Exploratory Data Analysis

**Let's explore the data!**

For the rest of the exercise we'll only be using the numerical data of the csv file.
___
**Use seaborn to create a jointplot to compare the Time on Website and Yearly Amount Spent columns. Does the correlation make sense?**
"""

from sklearn.model_selection import train_test_split
x_train,x_test,y_train,y_test = train_test_split(df_ecomm.drop('Time on Website',axis=1),df_ecomm['Yearly Amount Spent'],train_size=.8)

x_test.shape

x_train.shape

y_train.shape

y_test.shape

from sklearn.linear_model import LinearRegression

import matplotlib.pyplot as plt
plt.scatter(y_test,y_test)

sns.heatmap(df_ecomm.corr())

sns.jointplot(data=df_ecomm,y='Yearly Amount Spent',x='Time on Website',kind='reg')

"""** Do the same but with the Time on App column instead. **"""

sns.jointplot(data=df_ecomm, y='Yearly Amount Spent', x='Time on App', kind='reg')

"""** Use jointplot to create a 2D hex bin plot comparing Time on App and Length of Membership.**"""

sns.jointplot(x="Time on App", y="Length of Membership", kind="hex", data=df_ecomm, color="skyblue")

"""**Let's explore these types of relationships across the entire data set. Use [pairplot](https://stanford.edu/~mwaskom/software/seaborn/tutorial/axis_grids.html#plotting-pairwise-relationships-with-pairgrid-and-pairplot) to recreate the plot below.(Don't worry about the the colors)**"""

sns.pairplot(df_ecomm)

"""**Based off this plot what looks to be the most correlated feature with Yearly Amount Spent?**"""

sns.scatterplot(x='Time on App', y='Yearly Amount Spent', data=df_ecomm)
#sns.pairplot(df_ecomm.corr())

"""**Create a linear model plot (using seaborn's lmplot) of  Yearly Amount Spent vs. Length of Membership. **"""

sns.lmplot(x='Length of Membership',y='Yearly Amount Spent',data=df_ecomm)

"""## Training and Testing Data

Now that we've explored the data a bit, let's go ahead and split the data into training and testing sets.
** Set a variable X equal to the numerical features of the customers and a variable y equal to the "Yearly Amount Spent" column. **
"""

from sklearn.model_selection import train_test_split
x=df_ecomm.select_dtypes(include='number').drop('Yearly Amount Spent',axis=1)
y=df_ecomm['Yearly Amount Spent']

"""** Use model_selection.train_test_split from sklearn to split the data into training and testing sets. Set test_size=0.3 and random_state=101**"""

x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.3,random_state=101)

"""## Training the Model

Now its time to train our model on our training data!

** Import LinearRegression from sklearn.linear_model **
"""

from sklearn.linear_model import LinearRegression

"""**Create an instance of a LinearRegression() model named lm.**"""

LinReg=LinearRegression()

"""** Train/fit lm on the training data.**"""

LinReg.fit(x_train,y_train)

"""**Print out the coefficients of the model**"""

coefficients=LinReg.coef_

"""## Predicting Test Data
Now that we have fit our model, let's evaluate its performance by predicting off the test values!

** Use lm.predict() to predict off the X_test set of the data.**
"""

y_pred=LinReg.predict(x_test)

"""** Create a scatterplot of the real test values versus the predicted values. **"""

sns.scatterplot(x=y_test,y=y_pred)

"""## Evaluating the Model

Let's evaluate our model performance by calculating the residual sum of squares and the explained variance score (R^2).

** Calculate the Mean Absolute Error, Mean Squared Error, and the Root Mean Squared Error. Refer to the lecture or to Wikipedia for the formulas**
"""

from sklearn import metrics
metrics.mean_absolute_error(y_test,y_pred)

metrics.mean_squared_error(y_test,y_pred)

import numpy as np
np.sqrt(metrics.mean_squared_error(y_test,y_pred))

above_line = 0
on_line= 0
below_line = 0

for i,j in zip(y_pred,y_test):
  if i>j:
    above_line+=1
  elif j>i :
    below_line +=1
  elif i==j :
    on_line+=1

print('above_line: ',above_line,'\non_line: ',on_line,'\nbelow_line: ',below_line)

"""Residuals

---



You should have gotten a very good model with a good fit. Let's quickly explore the residuals to make sure everything was okay with our data.

**Plot a histogram of the residuals and make sure it looks normally distributed. Use either seaborn distplot, or just plt.hist().**
"""

import matplotlib.pyplot as plt
plt.hist(df_ecomm)



"""## Conclusion
We still want to figure out the answer to the original question, do we focus our efforst on mobile app or website development? Or maybe that doesn't even really matter, and Membership Time is what is really important.  Let's see if we can interpret the coefficients at all to get an idea.

** Recreate the dataframe below. **
"""

df_ecomm

"""** How can you interpret these coefficients? **"""

coefficients=LinReg.coef_
for feature, coefficient in zip(x_train.columns, coefficients):
    print(f'{feature}: {coefficient}')

"""**Do you think the company should focus more on their mobile app or on their website?**

As we can see by the coefficiet above,Time spent on App is much more than that of Time spent on the website,so hence Company should focus there efforts on there 'APP'.

## Great Job!

Congrats on your contract work! The company loved the insights! Let's move on.
"""