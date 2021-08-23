import os

class Config(object):
    DEBUG = False
    TESTING = False

    #bert_model_and_tokenizer_path = os.path.join( os.path.dirname( os.path.abspath(__file__) ), "BERT_model_saved_using_weights_name_config_name" )

    #bert_state_dict_config = os.path.join( os.path.dirname( os.path.abspath(__file__) ), "task1_model_with_state_dict", "config_file.bin" )
    #bert_state_dict_model = os.path.join( os.path.dirname( os.path.abspath(__file__) ), "task1_model_with_state_dict", "model_file.bin" )
    #bert_state_dict_vocab = os.path.join(os.path.dirname(os.path.abspath(__file__)), "task1_model_with_state_dict", "vocab_file.bin")

    bert_state_dict_config = os.path.join( os.path.dirname( os.path.abspath(__file__) ), "BERT_model_saved_using_weights_name_config_name", "config.json" )
    bert_state_dict_model = os.path.join( os.path.dirname( os.path.abspath(__file__) ), "BERT_model_saved_using_weights_name_config_name", "pytorch_model.bin" )
    bert_state_dict_vocab = os.path.join(os.path.dirname(os.path.abspath(__file__)), "BERT_model_saved_using_weights_name_config_name", "vocab.txt")

    #bert_model_and_tokenizer_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'task1_model_save_by_epoch', 'model_english_epoch_4')
    #bert_state_dict_vocab = os.path.join(os.path.dirname(os.path.abspath(__file__)), "task1_model_save_by_epoch", "vocab.txt")

    logis_reg_model = os.path.join(os.path.dirname(os.path.abspath(__file__)), "ML_and_Ensemble_models", "countvec_loglr.pkl")
    svm_model = os.path.join(os.path.dirname(os.path.abspath(__file__)), "ML_and_Ensemble_models", "countvec_SVM.pkl")
    multiNB_model = os.path.join(os.path.dirname(os.path.abspath(__file__)), "ML_and_Ensemble_models", "countvec_multiNB.pkl")
    ensemble_model = os.path.join(os.path.dirname(os.path.abspath(__file__)), "ML_and_Ensemble_models", "countvec_voteCLF.pkl")

    binary_classes = {0: 'Cyberbullying', 1: 'Not'}
    multiple_classes_bert = {0: 'Hate', 1: 'None', 2: 'Offensive', 3: 'Profane'}

    tsv_dataset_1 = os.path.join(os.path.dirname(os.path.abspath(__file__)), "Datasets", "2019_english_dataset", "english_dataset.tsv")
    tsv_dataset_2 = os.path.join(os.path.dirname(os.path.abspath(__file__)), "Datasets", "2019_english_dataset", "hasoc2019_en_test-2919.tsv")
    xlsx_dataset_3 = os.path.join(os.path.dirname(os.path.abspath(__file__)), "Datasets", "2020_english_dataset", "english.xlsx")
    csv_dataset_4 = os.path.join(os.path.dirname(os.path.abspath(__file__)), "Datasets", "2020_english_dataset", "english_test_1509.csv")
    csv_dataset_5 = os.path.join(os.path.dirname(os.path.abspath(__file__)), "Datasets", "2020_english_dataset", "hasoc_2020_en_train.csv")
    txt_dataset_6 = os.path.join(os.path.dirname(os.path.abspath(__file__)), "Datasets", "Dataset_from_kaggle", "si650winter11", "training.txt")
    csv_dataset_7 = os.path.join(os.path.dirname(os.path.abspath(__file__)), "Datasets", "t-davidson_dataset", "labeled_data.csv")
    csv_dataset_8 = os.path.join(os.path.dirname(os.path.abspath(__file__)), "Datasets", "ZeerakW_dataset", "NAACL_SRW_2016.csv")
    csv_dataset_9 = os.path.join(os.path.dirname(os.path.abspath(__file__)), "Datasets", "ZeerakW_dataset", "tweetID_text_class.csv")
    combined_dataset = os.path.join(os.path.dirname(os.path.abspath(__file__)), "Datasets", "combined_dataset", "combined_dataset.csv")
    new_features = os.path.join(os.path.dirname(os.path.abspath(__file__)), "Datasets", "new_features_dataset", "new_features.csv")

    existing_column_name_list = ['text', 'task_1', 'task_2']
    existing_column_name_list_2 = ['text', 'task1', 'task2']
    existing_column_name_list_3 = ['tweet', 'class']
    existing_column_name_list_4 = ['text', 'multiple_classes']
    new_column_names_list = ['text', 'binary_classes', 'multiple_classes']


class ProductionConfig(Config):  # inherit the parent class Config
    pass


class DevelopmentConfig(Config):
    DEBUG = True


class TestingConfig(Config):
    TESTING = True