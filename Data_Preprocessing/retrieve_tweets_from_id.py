import pandas as pd
from operator import itemgetter
from multiprocessing import Pool
from twython import Twython, TwythonError
from config import ProductionConfig as cfg
from Data_Preprocessing import twitter_access_token as tat

class retrieve_tweets_from_id_cls:

    def authTwitter(self, consumer_key, consumer_secret, access_token, access_token_secret):
        global twitter
        twitter = Twython(consumer_key, consumer_secret, access_token, access_token_secret)

    def getTweetFromID(self, id):
        try:
            global twitter  # added by anurag
            dump_list = twitter.lookup_status(id=id)
        except TwythonError as e:
            print("TwythonError: {0}".format(e))
        else:
            tweet_dict = dict()
            for i in dump_list:
                tweet_dict[str(i["id"])] = i["text"]
            return tweet_dict

    def split(self, a, n):
        k, m = divmod(len(a), n)
        return (a[i * k + min(i, m):(i + 1) * k + min(i + 1, m)] for i in range(n))

    def get_tweets_from_id(self, path=None):
        df_tweetID_class = pd.read_csv(path, header = None)

        # Modify column names and types
        df_tweetID_class.columns = ["tweet_id", "multiple_classes"]
        df_tweetID_class.tweet_id = df_tweetID_class.tweet_id.astype(str)

        print(df_tweetID_class.duplicated(subset='tweet_id').value_counts())
        df_tweetID_class.drop_duplicates(subset=['tweet_id'], keep='first', inplace=True)

        print(df_tweetID_class['multiple_classes'].value_counts(dropna=False))

        # Authenticate access to Twitter API
        consumer_key = tat.consumer_key
        consumer_secret = tat.consumer_secret
        access_token = tat.access_token
        access_token_secret = tat.access_token_secret

        # Prepare to get tweets from tweet IDs
        l = list( self.split( list(df_tweetID_class.tweet_id), int( df_tweetID_class.shape[0] / 99 ) ) )

        with Pool(16, initializer = self.authTwitter, initargs = (consumer_key, consumer_secret, access_token, access_token_secret,)) as pool:  # what is Pool?
            tweet_dump = pool.map(self.getTweetFromID, l)

        # Flat out tweet_dump into tweet_dict
        tweet_dict = dict()

        for d in tweet_dump:
            tweet_dict.update(d)

        keys = map(str, list(tweet_dict.keys()))

        #Drop the examples whos tweets are not retrived through API
        df_tweetID_class = df_tweetID_class.drop( df_tweetID_class[~df_tweetID_class.tweet_id.isin(keys)].index )

        # Sort the dataset and retrived (id, tweet) items according to IDs
        df_tweetID_class = df_tweetID_class.sort_values(['tweet_id'])
        tweet_tuples = list(tweet_dict.items())
        tweet_id, tweets = zip(*sorted(tweet_tuples, key = itemgetter(0)))
        tweet_id = list(tweet_id)
        tweets = list(tweets)

        # Assert if order of dataset keys match with order of retrived keys
        assert( tweet_id == list(df_tweetID_class.tweet_id) )

        # Add new column 'tweet' to the dataset
        df_tweetID_class['text'] = tweets

        return df_tweetID_class

if __name__ == "__main__":

    obj = retrieve_tweets_from_id_cls()

    df_tweets_with_id = obj.get_tweets_from_id(cfg.csv_dataset_8)

    df_tweets_with_id.to_csv(cfg.csv_dataset_9, index=False)