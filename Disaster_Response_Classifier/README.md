# Disaster-Response-Classifier


## PURPOSE:
Used my data engineering skillset ( Extract, Transform, Load ) along with my NLP and Machine leaning skillset to successfully classify 
Figure eight messages into 36 different categories to solve a real world problem.

## SUMMARY
In this project, a machine learning model was developed to classify disaster response messages into 36 different categories. These categories include things like water, shelter, medical aid, etc. The model was trained using a dataset of labeled disaster response messages, and NLP techniques were used to process and understand the text of the messages.

During the training process, the model learned to identify key words and phrases that are indicative of each category. Once trained, the model was able to take in new disaster response messages and accurately predict which category they belonged to.

Having a model that can accurately classify disaster response messages is important for disaster response organizations, as it allows them to quickly identify the needs of those affected by a disaster and allocate resources accordingly. This can help to save lives and improve the overall efficiency of the response effort. Overall, the use of machine learning and NLP in this project has the potential to make a significant impact in disaster response efforts.

## Files Description

- APP ( run.py, go.html, master.html): This folder consists of 3 files and consist of scripts for the backend and frontend to run the web application.
- Model: This folder consists of train_classifier.py, which is the python script to train the dataset
- Data: This folder consists of 3 files; messages.csv, categories.csv and process.py. process.py is a script used to Extract the data, clean and load it into Sqlite database.
- requirements.txt: Consists of all the versions needed to run the application

## PROJECT COMPONENTS

In this project, an ETL (extract, transform, load) pipeline was developed to process and clean data from two datasets: one containing disaster response messages and the other containing the categories for those messages. The Python script, process_data.py, loads the datasets, merges them, performs data cleaning, and stores the cleaned data in a SQLite database. A jupyter notebook, ETL Pipeline Preparation, was also used to explore and prepare the data for the ETL pipeline.

The project also includes an ML (machine learning) pipeline, which is written in the Python script train_classifier.py. This pipeline loads data from the SQLite database, splits it into training and test sets, builds a machine learning model using a text processing and machine learning pipeline, trains and tunes the model using GridSearchCV, and outputs the results on the test set. The final model is also exported as a pickle file. A jupyter notebook, ML Pipeline Preparation, was used to explore and prepare the data for the ML pipeline.

Finally, the project includes a Flask web app that allows an emergency worker to input a new message and receive classification results in multiple categories. The web app also displays visualizations of the data. This provides a user-friendly interface for emergency workers to quickly classify and understand the needs of those affected by a disaster.

## Instructions on How to Interact With the Project:

-Run the following commands in the project's root directory to set up your database and model.
-To run ETL pipeline that cleans data and stores in database python data/process_data.py data/disaster_messages.csv data/disaster_categories.csv data/DisasterResponse.db
-To run ML pipeline that trains classifier and saves python models/train_classifier.py data/DisasterResponse.db models/classifier.pkl
Run the following command in the app's directory to run your web app. python run.py
-Go to http://0.0.0.0:3000/

## Screenshots of some outputs in the Web App
<img width="1426" alt="trial message" src="https://user-images.githubusercontent.com/90535174/210775190-1b2250d3-a931-4c38-b0bd-15003c34f4f4.png">

![disaster-response-project1](https://user-images.githubusercontent.com/90535174/210775549-16b1f986-0c11-4248-b2e2-30703229490d.png)![disaster-response-project2](https://user-images.githubusercontent.com/90535174/210775574-ca23a297-6505-4609-a11b-cfa19bbd528e.png)

<img width="1440" alt="Screen Shot 2023-02-11 at 9 07 09 PM" src="https://user-images.githubusercontent.com/90535174/218263791-d5084fcf-0597-4b4b-9bae-2605921aaa4a.png">
