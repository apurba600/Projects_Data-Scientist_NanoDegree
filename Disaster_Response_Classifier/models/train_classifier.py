# Import Libraries
import sys
import pickle
import pandas as pd
import numpy as np
from sqlalchemy import create_engine
import re
import nltk
nltk.download("punkt")
nltk.download("stopwords")
nltk.download("wordnet")
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem.wordnet import WordNetLemmatizer
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.multioutput import MultiOutputClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.pipeline import Pipeline
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix, classification_report
from sklearn.model_selection import GridSearchCV



def load_data(database_filepath):

    """
    Creates a function to load data

    Input: database filepath

    Output: Two dataframes X,Y and dataframe category names
    """
    
    # Creates an instance of the database 
    engine = create_engine(f'sqlite:///{database_filepath}')

    # reads from the SQL database
    df = pd.read_sql_table("disaster_messages", con=engine)

    # Drops the original column from the dataframe
    df.drop("original",axis = 1,inplace = True)

    # drops all the nan values from the dataframe
    df.dropna(inplace = True)

    category_names = df.columns

    # Assigns values to X and Y to use for ML algorithm
    X = df["message"].values
    Y = df.drop(["message","genre","id"], axis = 1).values
    
    return X,Y,category_names


def tokenize(text):

    """
    Creates a function to tokenize the sentences, remove common words etc

    Input: text messages

    Output: list of cleaned words
    """
    
    # Removes all the punctuations and lowers the words for consistency
    text = re.sub(r"[^a-zA-Z0-9]"," ",text.lower().strip())
    
    # tokenizes the sentences to words saved in a list
    tokens = word_tokenize(text)
    
    # Used to remove common words and also change the words to its root form
    tokens = [WordNetLemmatizer().lemmatize(word) for word in tokens if word not in stopwords.words("english")]
   
    return tokens


def build_model():

    """
    Creates a function to build machine learning model

    output: Trained model
    """
    
    # Creates a pipeline to build ML model
    pipeline = Pipeline([
        ("vect",CountVectorizer(tokenizer=tokenize)),
        ('tfidf',TfidfTransformer()),
        ('clf',MultiOutputClassifier(RandomForestClassifier()))
    ])
    
    # parameters to test out while using grid search
    parameters = {
        'clf__estimator__n_estimators': [50,75,100]
    }
    # model instance 
    model = GridSearchCV(pipeline,param_grid=parameters)
    
    return model


def evaluate_model(model, X_test, Y_test):

    """
    Function that takes in model,X,Y in order to outout the models performance

    Input: model, dataset

    Output: Classification report to evaluate the model
    """

    # Predicts the values for given X_test
    y_pred = model.predict(X_test)
    for index, column in enumerate(Y_test):
        print(column, classification_report(Y_test[column], y_pred[:, index]))


def save_model(model, model_filepath):

    """
    Function to save the model
    
    Input: model and the model filepath
    
    Output: Saves the model at the filepath using pickle 
    """
    pickle.dump(model,open(model_filepath,"wb"))


def main():

    """
    Builds the model, trains and evaluates the model and finally saves it
    """
    if len(sys.argv) == 3:
        database_filepath, model_filepath = sys.argv[1:]
        print('Loading data...\n    DATABASE: {}'.format(database_filepath))
        X, Y, category_names = load_data(database_filepath)
        X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2)
        
        print('Building model...')
        model = build_model()
        
        print('Training model...')
        model.fit(X_train, Y_train)
        
        print('Evaluating model...')
        evaluate_model(model, X_test, Y_test)

        print('Saving model...\n    MODEL: {}'.format(model_filepath))
        save_model(model, model_filepath)

        print('Trained model saved!')

    else:
        print('Please provide the filepath of the disaster messages database '\
              'as the first argument and the filepath of the pickle file to '\
              'save the model to as the second argument. \n\nExample: python '\
              'train_classifier.py ../data/DisasterResponse.db classifier.pkl')


if __name__ == '__main__':
    main()