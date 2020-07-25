# User-Knowledge-Modeling

## Project Overview

 * A webapp that classifies the User Knowledge Level
 
 * Classified and compared results using Logistic Regression, Stochastic Gradient Descent, K Nearest Neighbor, Decision Tree, Support Vector Classification
 
 * Optimized KNeighborsClassifier, Support Vector Classifier using GridSearchCV and DecisionTreeClassifier using RandomizedSearchCV
 
 * Built an API using flask
 
 
 ## Glimpse of the webapp
 
 ![Glimpse](https://github.com/Harshal131/User-Knowledge-Modeling/blob/master/Model%20Findings/Glimpse.gif)
 
 
 ## Code and Resources Used
 
 **Python Version** : 3.8.2

**Packages** : pandas, numpy, sklearn, matplotlib, seaborn, flask, pickle

**Pandas cheat sheet** : https://pandas.pydata.org/Pandas_Cheat_Sheet.pdf

**Flask Productionization** : https://towardsdatascience.com/productionize-a-machine-learning-model-with-flask-and-heroku-8201260503d2


## Correlation Matrix

![Correlation Matrix](https://github.com/Harshal131/User-Knowledge-Modeling/blob/master/Model%20Findings/correlation_matrix.png)


## Pairplot

![Pairplot](https://github.com/Harshal131/User-Knowledge-Modeling/blob/master/Model%20Findings/pairplot.png)


## Model Comparision

| Model | Accuracy |
| :---:  |          :---: |
| Logistic Regression, | 70%   |
| Stochastic Gradient Descent     | 74%     |
| K Nearest Neighbor  |  86%     |
|Decision Tree| 86% |
|Support Vector Classification| 95%|


## Productionization 

* Built a flask API endpoint that was hosted on a local webserver. The API endpoint takes in a request with a list of values such as STG, SCG, STR, LPR, PEG and returns the classification of the User Level Knowledge.
