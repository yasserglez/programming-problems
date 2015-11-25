# https://www.hackerrank.com/challenges/document-classification

import sys

import numpy as np
from sklearn.pipeline import Pipeline
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import SGDClassifier
from sklearn.cross_validation import cross_val_score


def load_corpus(f, has_classes=True):
    num_docs = int(f.readline())
    corpus = ([], [])
    for i in range(num_docs):
        line = f.readline()
        if has_classes:
            i = line.find(' ')
            class_ = int(line[:i])
            doc = line[i+1:]
            corpus[1].append(class_)
        else:
            doc = line
        corpus[0].append(doc)
    return corpus


def train_classifier(corpus):
    model = Pipeline([
        ('tfidf', TfidfVectorizer(stop_words='english')),
        ('classifier', SGDClassifier(loss='log', penalty='none', n_iter=100)),
    ])
    # scores = cross_val_score(model, corpus[0], corpus[1], cv=10, n_jobs=-1)
    # print('CV score:', np.mean(scores))
    model.fit(corpus[0], corpus[1])
    return model


if __name__ == '__main__':
    np.random.seed(sum(map(ord, 'document-classification')))
    with open('trainingdata.txt') as f:
        training_data = load_corpus(f, has_classes=True)
    classifier = train_classifier(training_data)
    test_data = load_corpus(sys.stdin, has_classes=False)
    classes = classifier.predict(test_data[0])
    print('\n'.join(str(class_) for class_ in classes))
