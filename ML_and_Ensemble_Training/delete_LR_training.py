import pandas as pd

from sklearn.feature_extraction import text
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics import f1_score

from imblearn.over_sampling import RandomOverSampler

from config import ProductionConfig as cfg

df = pd.read_csv(cfg.new_features, nrows=5000)
print(df.sample(10).to_string())

print(df.tweet_raw_text.isna().sum())
print(df.segmented_hashtags.isna().sum())
df.dropna(subset=['tweet_raw_text','segmented_hashtags'], how='any', inplace=True)

# convert labels (categorical values) into numbers
LE = LabelEncoder()
df['binary_classes'] = LE.fit_transform(df['binary_classes'])
binary_classes = dict(zip(LE.classes_, LE.transform(LE.classes_)))
print(binary_classes)

X = df[['tweet_raw_text', 'segmented_hashtags']]
y = df[['binary_classes']]

# Split data in train and test with 0.2 factor
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)

# Oversample the data
print(X_train.shape)
ros = RandomOverSampler(random_state=0)
X_train_oversampled, y_train_oversampled = ros.fit_resample(X_train, y_train)
print(X_train_oversampled.shape)
print(X_train_oversampled.sample(10).to_string())

#X_train = X_train_oversampled.squeeze()
#y_train = y_train_oversampled.squeeze()

#X_test = X_test.squeeze()
#y_test = y_test.squeeze()

# Create customized stopping words set by including english stop words and @USER and {{URL}}
my_additional_stop_words = {'@USER', '{{URL}}', 'url', 'user'}
stop_words = text.ENGLISH_STOP_WORDS.union(my_additional_stop_words)

# Bag of Words and delete stopping words
countvec = CountVectorizer(stop_words=stop_words)

del df, LE, binary_classes, X, y

# https://towardsdatascience.com/natural-language-processing-on-multiple-columns-in-python-554043e05308

X_train_raw_text_counts = countvec.fit_transform(X_train_oversampled.tweet_raw_text)
X_train_raw_text_df = pd.DataFrame( data = X_train_raw_text_counts.todense(), columns = countvec.get_feature_names() )

X_test_raw_text_counts = countvec.transform(X_test.tweet_raw_text)
X_test_raw_text_df = pd.DataFrame( data = X_test_raw_text_counts.todense(), columns = countvec.get_feature_names() )


X_train_segmented_hashtags_counts = countvec.fit_transform(X_train_oversampled.segmented_hashtags)
X_train_segmented_hashtags_df = pd.DataFrame( data = X_train_segmented_hashtags_counts.todense(), columns = countvec.get_feature_names() )

X_test_segmented_hashtags_counts = countvec.transform(X_test.segmented_hashtags)
X_test_segmented_hashtags_df = pd.DataFrame( data = X_test_segmented_hashtags_counts.todense(), columns = countvec.get_feature_names() )

train = pd.concat( [X_train_raw_text_df, X_train_segmented_hashtags_df], axis=1)
test = pd.concat( [X_test_raw_text_df, X_test_segmented_hashtags_df], axis=1)

print(type(train))
print(train.shape)
print(type(y_train_oversampled))
print(y_train_oversampled.shape)

# Initialize classifiers
log_clf = LogisticRegression(n_jobs=-1)

log_clf.fit( train, y_train_oversampled.squeeze() )
y_pred = log_clf.predict(test)
print(log_clf.__class__.__name__, f1_score(y_test, y_pred, average = 'macro'))