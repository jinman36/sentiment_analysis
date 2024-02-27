# External Libraries
import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

# import from normalize text
from normalize_text import process_tweet

def fit_lr(X_train, y_train):
    model = LogisticRegression()
    model.fit(X_train, y_train)
    return model

def fit_tfid(tweet_corpus):
    tf_vect = TfidfVectorizer(preprocessor=lambda x: x, tokenizer=lambda x: x, token_pattern=None)
    tf_vect.fit(tweet_corpus)
    return tf_vect

def fit_cv(tweet_corpus):
    cv_vect = CountVectorizer(tokenizer=lambda x: x, preprocessor=lambda x: x, token_pattern=None)
    cv_vect.fit(tweet_corpus)
    return  cv_vect

def predict_tweet(prediction):
    if prediction == 1:
        return "positive"
    else:
        return "negative"
    
def model(text):
    df = pd.read_csv("tweet_data.csv")
    df["tokens"] = df["tweet_text"].apply(process_tweet)
    df["tweet_sentiment"] = df["sentiment"].apply(lambda i: 1 if i == 'positive' else 0)
    X = df["tokens"].tolist()
    y = df["tweet_sentiment"].tolist()
    X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=0, train_size=0.80)
    
    # console log - train test split
    print("----training set-----")
    print("Size of X_train: {}".format(len(X_train)))
    print("Size of y_train: {}".format(len(y_train)))
    print("\n")
    print("----testing set-----")
    print("Size of X_test: {}".format(len(X_test)))
    print("Size of y_test: {}".format(len(y_test)))
    print("\n")
    print("Train proportion: {:.0%}".format(len(X_train)/(len(X_train)+len(X_test))))
    print("----Model Accuracy-----")
        
    # # Count Vector Model
    # cv = fit_cv(X_train)
    # X_train_cv = cv.transform(X_train)
    # X_test_cv = cv.transform(X_test)
    # model_lr_cv = fit_lr(X_train_cv, y_train)
    # cv = fit_cv(X_train)
    # X_train_cv = cv.transform(X_train)
    # X_test_cv = cv.transform(X_test)
    # model_lr_cv = fit_lr(X_train_cv, y_train)
    # y_pred_lr_cv = model_lr_cv.predict(X_test_cv)
    # print("CV Model Accuracy: {:.2%}".format(accuracy_score(y_test, y_pred_lr_cv)))
    
    # # TF-IDF Model
    tf = fit_tfid(X_train)
    X_train_tf = tf.transform(X_train)
    X_test_tf = tf.transform(X_test)
    model_lr_tf = fit_lr(X_train_tf, y_train)
    model_lr_tf = fit_lr(X_train_tf, y_train)
    y_pred_lr_tf = model_lr_tf.predict(X_test_tf)
    print("TFIDF Model Accuracy: {:.2%}".format(accuracy_score(y_test, y_pred_lr_tf)))
    
    processed_tweet = process_tweet(text)
    
    # #Using CountVector
    
    # # Using TF-IDF
    transformed_tweet = tf.transform([processed_tweet])
    prediction = model_lr_tf.predict(transformed_tweet)
    return predict_tweet(prediction)
