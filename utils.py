import pickle

with open("model.pkl", "rb") as f:
    vectorizer, model = pickle.load(f)

def predict_with_confidence(user_input):
    user_input = user_input.lower().strip()
    X = vectorizer.transform([user_input])
    probas = model.predict_proba(X)[0]
    confidence = max(probas)
    category = model.classes_[probas.argmax()]
    return category, confidence