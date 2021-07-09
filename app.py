from flask import Flask, render_template, request
from flask_cors import CORS
import pandas as pd
import sys

from BERT import classify_sentence_bert
from config import ProductionConfig as cfg

obj_classify_sentence_bert = classify_sentence_bert.classify_sentence_bert_cls()  # create object of the class

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

        pred_class = obj_classify_sentence_bert.classify_sentence_2(text)

        label = cfg.binary_classes_bert.get(pred_class)

        result = {'Model': 'Bert', 'Class': label}

        df = pd.DataFrame(columns=['Model', 'Class'])
        df = df.append(result, ignore_index=True)

        return render_template('index.html', table = df.to_html(classes='data', header="true", index=False) )
    except:
        print("Unexpected error:", sys.exc_info()[1])
        #raise  # uncomment to view complete error
        return ("Unexpected error: " + str(sys.exc_info()[1]))

if __name__=='__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)