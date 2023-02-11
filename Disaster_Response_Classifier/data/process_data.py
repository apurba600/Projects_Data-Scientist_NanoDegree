# Import libraries
import sys
import pandas as pd
import numpy as np
from sqlalchemy import create_engine

def load_data(messages_filepath, categories_filepath):
    
    """
    Read both the csv files(containing messages and categories) using pandas library 
    and merge them together to output one dataframe (df)
    """
    
    # Load the csv files
    messages = pd.read_csv(messages_filepath)
    categories = pd.read_csv(categories_filepath)
    
    # Merge the two csv files
    df = pd.merge(messages,categories,on = "id",how ='outer')
    
    return df


def clean_data(df):
    
    
    """
    Takes in the raw dataframe and gives out clean dataframe
    
    Parameter: dataframe (df)
    
    input: Raw dataframe
    
    Output: Cleaned dataframe
    
    """
    # splits the category series into its variables and creates a new column of the variables
    categories = df["categories"].str.split(";",expand = True)
    # Selects the first row of the dataframe
    row = categories.iloc[1]
    # To create column names
    category_colnames = row.apply(lambda x: x[:-2])
    categories.columns = category_colnames
    
    # Uses for loop 
    for column in categories:
        # set each value to be the last character of the string
        categories[column] = categories[column].apply(lambda x: x[-1])
    
        # convert column from string to numeric
        categories[column] = categories[column].apply(int)

    categories['related'] = categories['related'].replace(to_replace=2, value=1)    
    
    # Drops the categories column from the dataframe
    df.drop("categories",inplace = True, axis = 1)
    
    # concats the categories dataframe with the main dataframe
    df = pd.concat([df,categories], axis = 1)
    
    # Drops the dublicate dataframe
    df.drop_duplicates(["message","original"],keep = False, inplace = True)
    
    return df
    
def save_data(df, database_filepath):

    """
    Stores Dataframe in a SQLite database
    Input: takes in dataframe and database filepath
    
    """
    engine = create_engine(f'sqlite:///{database_filepath}')
    df.to_sql('disaster_messages', engine, index=False, if_exists='replace') 
    
def main():

    """
    Main function loads the data, cleans the data and outputs a clean dataframe 
    to save it to a SQL database
    """
    if len(sys.argv) == 4:

        messages_filepath, categories_filepath, database_filepath = sys.argv[1:]

        print('Loading data...\n    MESSAGES: {}\n    CATEGORIES: {}'
              .format(messages_filepath, categories_filepath))
        df = load_data(messages_filepath, categories_filepath)

        print('Cleaning data...')
        df = clean_data(df)
        
        print('Saving data...\n    DATABASE: {}'.format(database_filepath))
        save_data(df, database_filepath)
        
        print('Cleaned data saved to database!')
    
    else:
        print('Please provide the filepaths of the messages and categories '\
              'datasets as the first and second argument respectively, as '\
              'well as the filepath of the database to save the cleaned data '\
              'to as the third argument. \n\nExample: python process_data.py '\
              'disaster_messages.csv disaster_categories.csv '\
              'DisasterResponse.db')


if __name__ == '__main__':
    main()