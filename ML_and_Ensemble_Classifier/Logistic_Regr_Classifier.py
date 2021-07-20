import pickle
from config import ProductionConfig as cfg
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import Pipeline

class logis_reg_classifier_cls:

    def __init__(self):
        self.logis_reg_model = cfg.logis_reg_model

    def classify_sentence_log_reg(self, sentence):

        with open(self.logis_reg_model, 'rb') as trained_model:
            countvec_loglr_model = pickle.load(trained_model)

        y_pred = countvec_loglr_model.predict([sentence])
        print(f"predicted label by Logistic Regression is {y_pred}")
        return y_pred[0]

if __name__ == "__main__":
    text = """
    I really dont want to start my weekend off this way - yet here I am. This vile post should be labeled a lie
    """

    obj = logis_reg_classifier_cls()

    print(obj.classify_sentence_log_reg(text))