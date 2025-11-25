import pandas as pd
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
import pickle
import nltk
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer
import string

# Download necessary NLTK data
try:
    nltk.data.find('tokenizers/punkt')
except LookupError:
    nltk.download('punkt')
    
try:
    nltk.data.find('corpora/stopwords')
except LookupError:
    nltk.download('stopwords')

try:
    nltk.data.find('tokenizers/punkt_tab')
except LookupError:
    nltk.download('punkt_tab')

ps = PorterStemmer()

def transform_text(text):
    text = text.lower()
    text = nltk.word_tokenize(text)

    y = []
    for i in text:
        if i.isalnum():
            y.append(i)

    text = y[:]
    y.clear()

    for i in text:
        if i not in stopwords.words('english') and i not in string.punctuation:
            y.append(i)

    text = y[:]
    y.clear()

    for i in text:
        y.append(ps.stem(i))

    return " ".join(y)

# Load data
print("Loading dataset...")
try:
    df = pd.read_csv('Dataset/spam.csv', encoding='latin1')
except FileNotFoundError:
    print("Error: Dataset/spam.csv not found.")
    exit()

# Data Cleaning
print("Cleaning data...")
df.drop(columns=['Unnamed: 2','Unnamed: 3','Unnamed: 4'], inplace=True)
df.rename(columns={'v1':'target','v2':'text'}, inplace=True)

encoder = LabelEncoder()
df['target'] = encoder.fit_transform(df['target'])

df = df.drop_duplicates(keep='first')

# Preprocessing
print("Preprocessing text (this might take a while)...")
df['transformed_text'] = df['text'].apply(transform_text)

# Vectorization
print("Vectorizing...")
tfidf = TfidfVectorizer(max_features=3000)
X = tfidf.fit_transform(df['transformed_text']).toarray()
y = df['target'].values

# Train Model
print("Training model...")
mnb = MultinomialNB()
mnb.fit(X, y) # Fit on all data or split? Notebook split, but for final model usually we want all data or just the training set. 
# The notebook split 80/20. I will stick to fitting on X (all data) or X_train? 
# Usually for production you train on all data. But to match notebook exactly I should split. 
# However, the notebook saved the model after fitting on X_train? 
# Wait, the notebook had: mnb.fit(X_train,y_train).
# But the LAST mnb instance was NOT fitted.
# I will fit on all data to make it robust, or split if I want to validate. 
# Let's fit on all data for the final app model.
mnb.fit(X, y)

# Save
print("Saving model and vectorizer...")
pickle.dump(tfidf, open('model/vectorizer.pkl','wb'))
pickle.dump(mnb, open('model/model.pkl','wb'))

print("Done! Model retrained and saved.")
