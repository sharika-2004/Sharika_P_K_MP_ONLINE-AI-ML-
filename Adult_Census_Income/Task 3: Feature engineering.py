label_encoders = {}

for col in df.columns:
    if df[col].dtype == 'object':
        le = LabelEncoder()
        df[col] = le.fit_transform(df[col])
        label_encoders[col] = le

df.head()

##OUTPUT
age	workclass	fnlwgt	education	education-num	marital-status	occupation	relationship	race	sex	capital-gain	capital-loss	hours-per-week	native-country	income
39	   5	    77516	     9	       13	             4	             0	          1	       4	   1	    2174	          0	           40	             38	           0
50	   4    	83311	     9	       13              	2	             3	          0	       4	   1	      0	            0	            13	           38	           0
38	   2	    215646	    11	     9	             0	             5	          1	       4	   1	      0	            0	            40	           38	           0 
53	   2	    234721	     1	      7	             2	             5	          0	       2	   1	      0	            0	            40	           38	           0
28	   2	     338409	      9	     13	             2	             9	          5	       2    	0	      0	            0	            40             	4	           0


##CODE
X = df.drop('income', axis=1)
y = df['income']

X_train, X_test, y_train, y_test = train_test_split(
    X, y,
    test_size=0.2,
    random_state=42
)

print(X_train.shape)
print(X_test.shape)
scaler = StandardScaler()

X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)
