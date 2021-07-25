# Cyberbullying_Detection

Clone GitHub repository
-------------
```
$ git clone https://github.com/anuragwatane/Cyberbullying_Detection.git
```

Create Virtual Environment
-------------
```
$ pip install virtualenv

$ cd <path to project directory>

$ virtualenv venv

$ venv\Scripts\activate
```
Install required packages
-------------
Make sure virtual environment is activated

$ pip install -r [requirements.txt](https://github.com/anuragwatane/Cyberbullying_Detection/blob/main/requirements.txt)


Data
-------------
The [Dataset](https://github.com/anuragwatane/Cyberbullying_Detection/tree/main/Datasets) folder contains Twitter data.

The Twitter data is downloaded from websites below
1. https://hasocfire.github.io/hasoc/2020/dataset.html
2. https://www.kaggle.com/c/si650winter11/overview

The combined dataset is prepared by executing [data_merging.py](https://github.com/anuragwatane/Cyberbullying_Detection/blob/main/Data_Preprocessing/data_merging.py)

Config
-------------
Make sure that all the file paths are present in [config.py](https://github.com/anuragwatane/Cyberbullying_Detection/blob/main/config.py)

Training
-------------
* To train the BERT model for binary classes, execute [bert_model_on_english_dataset_binary_classes.ipynb](https://github.com/anuragwatane/Cyberbullying_Detection/blob/main/BERT_Training/bert_model_on_english_dataset_binary_classes.ipynb) on Google [Colab](https://drive.google.com/file/d/1258b28if_YD8K789PdxF5gpV0HRCuPVW/view?usp=sharing).

  * The time taken to train the BERT model on GPU is much less.

* To train the ML and Ensemble model for binary classes, execute [Ensemble_prediction_Twitter_Data.ipynb](https://github.com/anuragwatane/Cyberbullying_Detection/blob/main/ML_and_Ensemble_Training/Ensemble_prediction_Twitter_Data.ipynb) on Google [Colab](https://colab.research.google.com/drive/1DRlVYmZfNYKLdPyQ4Q-9bns2kcjI8JTU?usp=sharing).

  * Change the code to train ML and Ensemble model using GPU.
  
Saved Model
-------------
The saved model for BERT model is in [folder](https://github.com/anuragwatane/Cyberbullying_Detection/tree/main/BERT_model_saved_using_weights_name_config_name)

The saved ML and Ensemble model is in folder [ML_and_Ensemble_models](https://github.com/anuragwatane/Cyberbullying_Detection/tree/main/ML_and_Ensemble_models)

Flask Web App
------------
The end points of the Flask Web App is in [app.py](https://github.com/anuragwatane/Cyberbullying_Detection/blob/main/app.py).
It is the starting point of the Flask Web App.

How to run Flask App on local machine?
------------
Make sure virtual environment is activated

Set the file with starting point
```
$ set FLASK_APP=app.py
```

Start the Flask App to access from IPv4 address
```
$ flask run --host 0.0.0.0
```

Docker command to build the Flask app
------------
```
$ cd <path to project directory>

$ docker build -t cyberbullying-detection:<tag-name> .
```

Tag and push to Docker Hub
------------
```
$ docker login

$ docker tag cyberbullying-detection:<tag-name> anuragwatane/cyberbullying-detection-repo:BERT-tag

$ docker push anuragwatane/cyberbullying-detection-repo:BERT-tag
```

Docker command to RUN the app
-----------
```
$ docker pull anuragwatane/cyberbullying-detection-repo:BERT-tag

$ docker run -p 4000:80 anuragwatane/cyberbullying-detection-repo:BERT-tag
```

Docker Hub repository URL
------------
https://hub.docker.com/repository/docker/anuragwatane/cyberbullying-detection-repo

Web App URL
------------
The deployed Web App is present at https://cyberbullying-detection-docker.azurewebsites.net/
