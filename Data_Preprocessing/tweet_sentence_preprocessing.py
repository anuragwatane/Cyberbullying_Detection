from ekphrasis.classes.segmenter import Segmenter
seg_tw = Segmenter(corpus = "twitter")  # to leverage word statistics from Twitter

import emoji
import csv
import regex
import pandas as pd
import preprocessor as tweet_proc
from config import ProductionConfig as cfg


class tweet_text_preprocessing_cls:

    def __init__(self, df):

        self.new_df = df.copy()

        # start - add new column to the dataframe
        self.new_df['hashtags'] = ""
        self.new_df['hashtags'] = self.new_df['hashtags'].astype('object')

        self.new_df['segmented_hashtags'] = ""
        self.new_df['segmented_hashtags'] = self.new_df['segmented_hashtags'].astype('object')

        self.new_df['emojis'] = ""
        self.new_df['emojis'] = self.new_df['emojis'].astype('object')

        self.new_df['emoji_words'] = ""
        self.new_df['emoji_words'] = self.new_df['emoji_words'].astype('object')

        self.new_df['urls'] = ""
        self.new_df['urls'] = self.new_df['urls'].astype('object')

        self.new_df['mentions'] = ""
        self.new_df['mentions'] = self.new_df['mentions'].astype('object')

        self.new_df['numbers'] = ""
        self.new_df['numbers'] = self.new_df['numbers'].astype('object')

        self.new_df['reserved_word'] = ""
        self.new_df['reserved_word'] = self.new_df['reserved_word'].astype('object')

        self.new_df['tweet_raw_text'] = ""
        self.new_df['tweet_raw_text'] = self.new_df['tweet_raw_text'].astype('object')
        # end - add new column to the dataframe


    def make_list(self, proc_obj):

        if proc_obj == None:
            return []  # must return empty list

        store = []

        for unit in proc_obj:
            store.append(unit.match)

        return store

    def strip_list(self, listie):

        if listie == []:
            return ""
        else:
            stripped = []

            for item in listie:
                stripped.append(item.strip())
            return stripped


    def extract_features_from_text(self, df):

        for idx, text in df['text'].iteritems():
            parse_obj = tweet_proc.parse(text.replace("\n", " "))

            df.at[idx, 'hashtags'] = self.strip_list( self.make_list(parse_obj.hashtags) )
            df.at[idx, 'segmented_hashtags'] = self.segment_hashtags( df['hashtags'][idx] )

            df.at[idx, 'emojis'] = self.get_emoji_list(text.replace("\n", " "))
            df.at[idx, 'emoji_words'] = self.generating_emoji_words( df['emojis'][idx] )

            df.at[idx, 'urls'] = self.strip_list( self.make_list(parse_obj.urls) )

            df.at[idx, 'mentions'] = self.strip_list( self.make_list(parse_obj.mentions) )

            df.at[idx, 'numbers'] = self.strip_list( self.make_list(parse_obj.numbers) )

            df.at[idx, 'reserved_word'] = self.strip_list( self.make_list(parse_obj.reserved) )

            df.at[idx, 'tweet_raw_text'] = tweet_proc.clean( text.replace("\n", " ") )

        return df


    def generating_emoji_words(self, emo_list):
        words = []

        if len(emo_list) > 0:
            for icon in emo_list:
                text = emoji.demojize(icon).replace(",", "").replace(":", "").replace("_", " ")
                words.append(text)

            return words
        else:
            return ""


    def get_emoji_list(self, text):

        emoji_list = []
        data = regex.findall(r'\X', text)

        for word in data:
            if any(char in emoji.UNICODE_EMOJI['en'] for char in word):
                emoji_list.append(word)

        if len(emoji_list)>0:
            return emoji_list
        else:
            return ""


    def segment_hashtags(self, hashtags):
        segmented_set = []

        if len(hashtags)>0:
            for tag in hashtags:
                word = tag[1:]  # removing the hash symbol
                segmented_set.append(seg_tw.segment(word))

            return segmented_set
        else:
            return ""


if __name__ == "__main__":

    df = pd.read_csv(cfg.combined_dataset)

    obj = tweet_text_preprocessing_cls(df)
    new_features_df = obj.extract_features_from_text(obj.new_df)

    new_features_df.to_csv(cfg.new_features, index=False)