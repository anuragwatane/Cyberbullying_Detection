import torch
import numpy as np
from transformers import BertTokenizer
from transformers import BertForSequenceClassification
from config import ProductionConfig as cfg

class classify_sentence_bert_cls:

    def __init__(self):
        self.output_dir = cfg.bert_model_and_tokenizer_path
        self.MAX_LENGTH = 40

    def classify_sentence(self, sentence):
        input_id_sentence = []
        attention_mask_sentence = []

        model = BertForSequenceClassification.from_pretrained(self.output_dir)

        print(f"\nThe model can predict {model.num_labels} different classes\n")

        tokenizer = BertTokenizer.from_pretrained(self.output_dir)

        encoded_dict = tokenizer.encode_plus(
            sentence,                    # Sentence to encode.
            add_special_tokens=True,     # Add '[CLS]' and '[SEP]'
            max_length=self.MAX_LENGTH,       # Pad & truncate all sentences.
            pad_to_max_length=True,
            return_attention_mask=True,  # Construct attn. masks.
            return_tensors='pt',         # Return pytorch tensors.
        )

        # Add the encoded sentence to the list.
        input_id_sentence.append(encoded_dict['input_ids'])
        # And its attention mask (simply differentiates padding from non-padding).
        attention_mask_sentence.append(encoded_dict['attention_mask'])

        input_id_sentence = torch.cat(input_id_sentence, dim=0)
        attention_mask_sentence = torch.cat(attention_mask_sentence, dim=0)

        with torch.no_grad():
            outputs = model(input_id_sentence, token_type_ids=None, attention_mask=attention_mask_sentence)

        logits = outputs[0]

        print("\n The normalized probability for each class is")
        print(logits.softmax(dim=-1).tolist())
        pred_class_prob = logits.softmax(dim=-1).tolist()

        pred_label_from_prob = np.argmax(pred_class_prob)
        print(f"\nThe predicted class is: {pred_label_from_prob}")

        return pred_label_from_prob


if __name__ == "__main__":
    text = """
    I really dont want to start my weekend off this way - yet here I am. This vile post should be labeled a lie
    """

    obj = classify_sentence_bert_cls()

    print(obj.classify_sentence(text))