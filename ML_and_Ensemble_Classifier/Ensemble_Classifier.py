import pickle
from config import ProductionConfig as cfg
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.ensemble import VotingClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.svm import SVC
from sklearn.linear_model import SGDClassifier
from sklearn.naive_bayes import MultinomialNB

class ensemble_classifier_cls:

    def __init__(self):
        self.ensemble_model = cfg.ensemble_model

    def classify_sentence_ensemble(self, sentence):

        with open(self.ensemble_model, 'rb') as trained_model:
            countvec_voteCLF_model = pickle.load(trained_model)

        y_pred = countvec_voteCLF_model.predict([sentence])
        print(f"predicted label by Ensemble Model is {y_pred}")
        return y_pred[0]

if __name__ == "__main__":
    text = """
    I really dont want to start my weekend off this way - yet here I am. This vile post should be labeled a lie
    """

    obj = ensemble_classifier_cls()

    print(obj.classify_sentence_ensemble(text))
