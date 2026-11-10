from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfVectorizer

bow = CountVectorizer()
tfidf = TfidfVectorizer()


Message = [
        "Congratulations! You have won a free iPhone. Click here to claim.",
        "Hi, are we still meeting at 5 PM today?",
        "URGENT! You have won $5000. Send your bank details to receive the prize.",
        "Please send me the project report when you get time."
]

st = set()
# st.update(["hello","ram","hello"])

# s ="congratulations! you have won a free iphone. click here to claim"
# print(s.split())
for i in Message:
    st.update(i.lower().split())
print(len(st))



# bg = bow.fit_transform(Message)

# tf = tfidf.fit_transform(Message)

# print(tf.toarray())
# feature_names = tfidf.get_feature_names_out()

# print(feature_names)
"""
[0 0 0 0 1 1 1 0 1 0 1 1 0 1 0 0 0 0 0 0 0 0 0 0 0 0 1 0 0 0 0 1 1 0]
 [0 1 1 0 0 0 0 0 0 0 0 0 1 0 0 1 0 1 0 0 0 0 0 1 0 0 0 1 0 1 0 0 0 0]
 [1 0 0 1 0 0 0 1 0 0 1 0 0 0 0 0 0 0 1 0 1 0 1 0 1 0 1 0 1 0 0 1 1 1]
 [0 0 0 0 0 0 0 0 0 1 0 0 0 0 1 0 1 0 0 1 0 1 1 0 1 1 0 0 0 0 1 0 1 0]]
"""