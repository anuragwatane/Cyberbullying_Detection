import os

class Config(object):
    DEBUG = False
    TESTING = False

    #bert_model_and_tokenizer_path = os.path.join( os.path.dirname( os.path.abspath(__file__) ), "model_plus_tokenizer_task1" )

    bert_state_dict_config = os.path.join( os.path.dirname( os.path.abspath(__file__) ), "task1_model_with_state_dict", "config.json" )
    bert_state_dict_model = os.path.join( os.path.dirname( os.path.abspath(__file__) ), "task1_model_with_state_dict", "model_file.bin" )
    bert_state_dict_vocab = os.path.join(os.path.dirname(os.path.abspath(__file__)), "task1_model_with_state_dict", "vocab_file.bin")

    binary_classes_bert = {0: 'Hate/Offensive/Profane', 1: 'None'}
    multiple_classes_bert = {0: 'Hate', 1: 'None', 2: 'Offensive', 3: 'Profane'}


class ProductionConfig(Config):  # inherit the parent class Config
    pass


class DevelopmentConfig(Config):
    DEBUG = True


class TestingConfig(Config):
    TESTING = True