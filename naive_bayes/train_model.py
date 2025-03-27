import pandas as pd
from model.preprocess import preprocess
from model.naive_bayes import NaiveBayesClassifier

df = pd.read_csv("fake reviews dataset.csv")

texts = [preprocess(t) for t in df["text_"].astype(str)]
labels = df["label"].values

nb = NaiveBayesClassifier()
nb.train(texts, labels)
nb.save("./model/trained_model.pkl")