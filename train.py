import pickle
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from data import training_data

# training_data is a LIST of (text, category) tuples
X_texts = [text for text, label in training_data]
y_labels = [label for text, label in training_data]

# Vectorize input text
vectorizer = TfidfVectorizer()
X = vectorizer.fit_transform(X_texts)

# Train Naive Bayes model
model = MultinomialNB()
model.fit(X, y_labels)

# Save vectorizer + model
with open("model.pkl", "wb") as f:
    pickle.dump((vectorizer, model), f)

print("Training complete! Model saved as model.pkl")