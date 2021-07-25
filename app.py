from flask import Flask, render_template, request
from flask_cors import CORS
import pandas as pd
import traceback
from config import ProductionConfig as cfg

from BERT import classify_sentence_bert
obj_classify_sentence_bert = classify_sentence_bert.classify_sentence_bert_cls()  # create object of the class

from ML_and_Ensemble_Classifier import Logistic_Regr_Classifier, Ensemble_Classifier, SVM_Classifier, MultiNB_Classifier
obj_classify_sentence_logr = Logistic_Regr_Classifier.logis_reg_classifier_cls()
obj_classify_sentence_svm = SVM_Classifier.svm_classifier_cls()
obj_classify_sentence_multiNB = MultiNB_Classifier.multiNB_classifier_cls()
obj_classify_sentence_ensemble = Ensemble_Classifier.ensemble_classifier_cls()

app = Flask(__name__)
cors = CORS(app)  # need flask_cors to do a cross-origin request


# Start - load config file #
if app.config["ENV"] == "production":
    app.config.from_object("config.ProductionConfig")
else:
    app.config.from_object("config.DevelopmentConfig")
# End - load config file #


@app.route('/', methods=['GET','POST'])
def index():
    return render_template('index.html')


@app.route('/submit_text', methods=['GET','POST'])
def submit_text():
    try:
        text = request.form['text_name']
        df = pd.DataFrame(columns=['Model', 'Class'])

        pred_class = obj_classify_sentence_bert.classify_sentence_2(text)

        label = cfg.binary_classes_bert.get(pred_class)

        result = {'Model': 'Bert', 'Class': label}

        df = df.append(result, ignore_index=True)

        pred_class_lr = obj_classify_sentence_logr.classify_sentence_log_reg(text)
        label_lr = cfg.binary_classes_bert.get(pred_class_lr)
        result_lr = {'Model': 'Logistic Regression', 'Class': label_lr}
        df = df.append(result_lr, ignore_index=True)

        pred_class_svm = obj_classify_sentence_svm.classify_sentence_svm(text)
        label_svm = cfg.binary_classes_bert.get(pred_class_svm)
        result_svm = {'Model': 'Support Vector Machine', 'Class': label_svm}
        df = df.append(result_svm, ignore_index=True)

        pred_class_multiNB = obj_classify_sentence_multiNB.classify_sentence_multiNB(text)
        label_multiNB = cfg.binary_classes_bert.get(pred_class_multiNB)
        result_multiNB = {'Model': 'MultinomialNB', 'Class': label_multiNB}
        df = df.append(result_multiNB, ignore_index=True)

        pred_class_ensemble = obj_classify_sentence_ensemble.classify_sentence_ensemble(text)
        label_ensemble = cfg.binary_classes_bert.get(pred_class_ensemble)
        result_ensemble = {'Model': 'Ensemble Model', 'Class': label_ensemble}
        df = df.append(result_ensemble, ignore_index=True)

        return render_template('index.html', table = df.to_html(classes='data', header="true", index=False) )
    except:
        print(str(traceback.format_exc()))
        #raise  # uncomment to view complete error
        return (str(traceback.format_exc()))

if __name__=='__main__':
    #app.run(debug=True, host='0.0.0.0', port=5000)
    #app.run(debug=True, host='0.0.0.0')  # for Flask on azure
    app.run(host='0.0.0.0', port=80)  # for docker image