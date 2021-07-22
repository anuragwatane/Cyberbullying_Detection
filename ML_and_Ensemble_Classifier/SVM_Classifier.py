import pickle
from config import ProductionConfig as cfg
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.svm import SVC
from sklearn.pipeline import Pipeline

class svm_classifier_cls:

    def __init__(self):
        self.svm_model = cfg.svm_model

    def classify_sentence_svm(self, sentence):

        with open(self.svm_model, 'rb') as trained_model:
            countvec_svm_model = pickle.load(trained_model)

        y_pred = countvec_svm_model.predict([sentence])
        print(f"predicted label by SVM is {y_pred}")
        return y_pred[0]

if __name__ == "__main__":
    text = """
    I really dont want to start my weekend off this way - yet here I am. This vile post should be labeled a lie
    """

    obj = svm_classifier_cls()

    print(obj.classify_sentence_svm(text))