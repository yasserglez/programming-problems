# https://www.hackerrank.com/challenges/document-classification

import sys
import pprint

import numpy as np
from sklearn.pipeline import Pipeline
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import SGDClassifier
from sklearn.grid_search import GridSearchCV


def load_corpus(f, has_classes=True):
    num_docs = int(f.readline())
    corpus = ([] if has_classes else None, [])
    for i in range(num_docs):
        line = f.readline()
        if has_classes:
            i = line.find(' ')
            class_ = int(line[:i])
            doc = line[i+1:]
            corpus[0].append(class_)
        else:
            doc = line
        corpus[1].append(doc)
    return corpus


def train_classifier(training_data):
    model = Pipeline([
        ('tfidf', TfidfVectorizer(stop_words='english')),
        ('classifier', SGDClassifier(penalty='l2')),
    ])

    # param_grid = {
    #     'classifier__loss': ('hinge', 'log'),
    #     'classifier__alpha': np.logspace(-6, 0, 7),
    #     'classifier__n_iter': (5, 10, 30, 50),
    # }
    # grid_search = GridSearchCV(model, param_grid, cv=10, n_jobs=-1, verbose=1)
    # grid_search.fit(training_data[1], training_data[0])
    # print('Best score: %0.3f' % grid_search.best_score_)
    # print('Best parameters:')
    # pprint.pprint(grid_search.best_params_)
    # Best score: 0.969

    best_params = {
        'classifier__alpha': 1e-05,
        'classifier__loss': 'hinge',
        'classifier__n_iter': 10,
    }
    model.set_params(**best_params)
    model.fit(training_data[1], training_data[0])
    return model


if __name__ == '__main__':
    np.random.seed(sum(map(ord, 'document-classification')))
    with open('trainingdata.txt') as f:
        training_data = load_corpus(f, has_classes=True)
    classifier = train_classifier(training_data)
    test_data = load_corpus(sys.stdin, has_classes=False)
    classes = classifier.predict(test_data[1])
    print('\n'.join(str(class_) for class_ in classes))
