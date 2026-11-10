import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
from sklearn.feature_extraction.text import TfidfVectorizer #!==> Convert text into numbers:--
import numpy as  np

df=pd.read_csv(r"C:\Users\Yash\OneDrive\Desktop\python practise for codes\.vscode\AI Ml\spam_detection_Dataset.csv")
# print(df.head())
# print(df.tail())
# print(df.info()) #==>  5572 entries
# print(df.describe())
"""
        Category                 Message

count      5572                    5572
unique        2                    5157 (5572-5157=> 415 repeated same message)
top         ham  Sorry, I'll call later (mostly repeated message)
freq       4825                      30



on the bais of this clean something:

1.delete repeated message
2.mostly repeated message kitne bar repeat hua
3.repeated kitne hai
4.spam kitne hai or ham kitne hai...
"""
print(df.columns) #==> ['Category', 'Message']
unique_cate=df["Category"].unique() #==> ['ham', 'spam']
# print(unique_cate)
unique_msge=df["Message"].unique() #==> Length: 5157
unique_msge=df["Message"].value_counts() #& by this we get to know konse message kitni  baar aaye hai
# print(unique_msge)
"""
Sorry, I'll call later                                                                                                                                            
30
I cant pick the phone right now. Pls send a message                                                                                                                
12
Ok...                                                                                                                                                                                  
10
Please call our customer service representative on FREEPHONE 0808 145 4742 between 9am-11pm as you have WON a guaranteed £1000 cash or £5000 prize!                                     
4
Wen ur lovable bcums angry wid u, dnt take it seriously.. Coz being angry is d most childish n true way of showing deep affection, care n luv!.. kettoda manda... Have nice day da.     
4
                                                                                                                                                                                       ..
This is the 2nd time we have tried 2 contact u. U have won the £750 Pound prize. 2 claim is easy, call 087187272008 NOW1! Only 10p per minute. BT-national-rate.                        
1
Will ü b going to esplanade fr home?                                                                                                                                                    
1
Pity, * was in mood for that. So...any other suggestions?                                                                                                                               
1
The guy did some bitching but I acted like i'd be interested in buying something else next week and he gave it to us for free                                                           
1
Rofl. Its true to its name                                                                                                                                                              
1
"""
#^ dataframe me esa konsa message hai jo 30 baar aa rha hai :??

# sorry_msge= df[df["Message"]==df["Message"].value_counts()]
# print(sorry_msge)
print("===========================")

# print(df["Message"].value_counts()==30)



# print(df["Message"]=="30")





#! ???????????????????
#^ how many are duplicates from the data.
# total_Length: 5157
print("Chu Chu ki Chooo==============================")
# print(duplicate)

#^ deleting repeated message....
# drop=df["Message"].drop_duplicates(subset="Message")
# print(drop)


df = df.drop_duplicates(subset="Message")
print(df)
duplicate=df["Message"].duplicated().sum()  #==> 415
print(duplicate)
#* Now their are 0 duplicates in the data.
# print(df.count())

# * remove the spaces from the data....
# df.columns=df.columns.str.strip() #& Strip func columns me lagta hai dataframe par nahi.
# print(df.head())

#^ Applying machine learning :=============

#* Decoding spam or not spam into 0 and 1  using map function:-

df["Category"]=df["Category"].map({"ham":1,"spam":0})
# print(df["Category"].unique()) ==> ['ham', 'spam']
# print(df["Category"])

#! df["message"]=> is text column - have to convert it in 0 & 1 first : Using Vectorizer(TdidfVectorizer):
#* First have to import it from feature_extraction.text :

#^ Have to create the  object of vectorizer 
vectorizer=TfidfVectorizer()
#* Have to fit and transform the vectorizer 
txt_to_num=vectorizer.fit_transform(df["Message"])    

"""
<Compressed Sparse Row sparse matrix of dtype 'float64'
        with 67934 stored elements and shape (5157, 8709)>
  Coords        Values
  (0, 3567)     0.1472838323968625
  (0, 8080)     0.2284805832636267
  (0, 4370)     0.32548246375773743
"""


#* Saperating input x and output/target y:
X=txt_to_num
Y=df["Category"]

# print(X)
# print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
#^ Testing the model :
x_train,x_test,y_train,y_test=train_test_split(X,Y,test_size=0.3,random_state=42)


#^ model selection: Model is logistic reg (used for yes or no output)
#^ have to impport logistic regression from .linear_model
model=LogisticRegression(random_state=42)


#^ now we have to fir the model on the training part:---- 
model.fit(x_train,y_train)


#^ Now we have to predict the model: 
y_pred= model.predict(x_test)
print("Value that Machine predicted: ",y_pred) # ==>  [1 0 1 ... 1 1 1]

#^ Now we want the accuracy of the model:
accuracy=   accuracy_score(y_pred,y_test)
print("accuracy score(How exact your model is): ",accuracy) #==> 0.95

#! Now : hum machine se exact kese bulvay ke spam hai na non spam : In text formats:-----
print(model.predict(np.array(["I cant pick the phone right now. Pls send a message"])))