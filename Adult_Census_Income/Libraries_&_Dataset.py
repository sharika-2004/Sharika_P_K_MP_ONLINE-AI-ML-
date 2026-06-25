import pandas as pd
import numpy as np

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder, StandardScaler

from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.svm import SVC

from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, roc_auc_score

##DATASET
url = "https://archive.ics.uci.edu/ml/machine-learning-databases/adult/adult.data"

columns = [
    'age', 'workclass', 'fnlwgt', 'education',
    'education-num', 'marital-status', 'occupation',
    'relationship', 'race', 'sex', 'capital-gain',
    'capital-loss', 'hours-per-week', 'native-country',
    'income'
]

df = pd.read_csv(url, header=None, names=columns, skipinitialspace=True)

df.head()

##Output of dataset cell
age	workclass	          fnlwgt	education	education-num	marital-status	occupation	  relationship	    race	sex	 capital-gain	capital-loss	hours-per-week	native-country	income
39	State-gov	          77516	    Bachelors	13              Never-married	Adm-clerical	Not-in-family	White	Male	2174	           0	          40	     United-States	<=50K
50	Self-emp-not-inc	  83311	    Bachelors	13	        Married-civ-spouse	Exec-managerial	Husband	         White	Male	0	               0	          13  	     United-States	<=50K
38	Private	              215646	HS-grad	    9	               Divorced	   Handlers-cleaners Not-in-family	 White	Male	0	               0	           40	     United-States	<=50K
53	Private             	234721	11th	     7	         Married-civ-spouse	Handlers-cleaners	Husband    	Black	Male	0	               0	            40       	United-States	<=50K
28	Private	                338409	Bachelors	13	           Married-civ-spouse	Prof-specialty	Wife	      Black	Female	0	               0	            40	          Cuba	         <=50K

