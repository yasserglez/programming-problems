# https://www.hackerrank.com/challenges/stack-exchange-question-classifier

import sys
import json

import numpy as np
from sklearn.pipeline import Pipeline
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import SGDClassifier
from sklearn.cross_validation import cross_val_score


def load_corpus(f):
    n = int(f.readline())
    corpus = ([], [])
    for i in range(n):
        doc = json.loads(f.readline())
        corpus[0].append('{} {}'.format(doc['question'], doc['excerpt']))
        if 'topic' in doc:
            corpus[1].append(doc['topic'])
    return corpus


def build_model(corpus):
    model = Pipeline([
        ('tfidf', TfidfVectorizer(stop_words='english')),
        ('classifier', SGDClassifier(loss='log', penalty='none', n_iter=100)),
    ])
    # scores = cross_val_score(model, corpus[0], corpus[1], cv=10, n_jobs=-1)
    # print('CV score:', np.mean(scores))
    model.fit(corpus[0], corpus[1])
    return model


if __name__ == '__main__':
    np.random.seed(sum(map(ord, 'stack-exchange-question-classifier')))
    with open('training.json') as f:
        training_data = load_corpus(f)
    model = build_model(training_data)
    test_data = load_corpus(sys.stdin)
    topics = model.predict(test_data[0])
    print('\n'.join(str(topic) for topic in topics))
