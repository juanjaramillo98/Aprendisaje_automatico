import pickle

def save_vectorizer(vectorizer, file_path='./vectorizer.pkl'):
    with open(file_path, 'wb') as file:
        pickle.dump(vectorizer, file)

def load_vectorizer(file_path='./vectorizer.pkl'):
    vectorizer = None
    with open(file_path, 'rb') as file:
        vectorizer = pickle.load(file) 
    return vectorizer
