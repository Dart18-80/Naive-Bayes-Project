import math
import pickle
from collections import defaultdict

def int_dict():
    return defaultdict(int)

def outer_dict():
    return defaultdict(int_dict)

class NaiveBayesClassifier:
    def __init__(self):
        self.classes = set()
        self.class_word_counts = outer_dict()
        self.class_counts = defaultdict(int)
        self.vocab = set()

    def train(self, documents, labels):
        for doc, label in zip(documents, labels):
            self.classes.add(label)
            self.class_counts[label] += 1
            for word in doc:
                self.vocab.add(word)
                self.class_word_counts[label][word] += 1

    def predict(self, doc):
        scores = {}
        for c in self.classes:
            log_prob = math.log(self.class_counts[c] / sum(self.class_counts.values()))
            total_words = sum(self.class_word_counts[c].values())
            for word in doc:
                word_freq = self.class_word_counts[c].get(word, 0)
                log_prob += math.log((word_freq + 1) / (total_words + len(self.vocab)))
            scores[c] = log_prob
        return max(scores, key=scores.get)

    def save(self, path):
        with open(path, 'wb') as f:
            pickle.dump(self, f)

    @staticmethod
    def load(path):
        with open(path, 'rb') as f:
            return pickle.load(f)
