import pickle
from config import ProductionConfig as cfg
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import Pipeline

class multiNB_classifier_cls:

    def __init__(self):
        self.multiNB_model = cfg.multiNB_model

    def classify_sentence_multiNB(self, sentence):

        with open(self.multiNB_model, 'rb') as trained_model:
            countvec_multiNB_model = pickle.load(trained_model)

        y_pred = countvec_multiNB_model.predict([sentence])
        print(f"predicted label by MultinomialNB is {y_pred}")
        return y_pred[0]

if __name__ == "__main__":
    text = """
    I really dont want to start my weekend off this way - yet here I am. This vile post should be labeled a lie
    """

    obj = multiNB_classifier_cls()

    print(obj.classify_sentence_multiNB(text))