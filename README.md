# Projects_Data-Scientist_NanoDegree
This Repo consists projects completed for the Nano Degree Program

## IBM Recommendation System
The IBM articles recommendation system was created to provide personalized recommendations to users based on their reading history. Multiple approaches were used, including knowledge-based, collaborative-based, and matrix factorization using SVD. The data cleaning process was performed using Python libraries, including Pandas, to prepare the data for model creation.

The recommendation model was created using a combination of matrix factorization and collaborative filtering techniques. SVD was used for matrix factorization to decompose the user-item matrix into latent features, which were then used to make predictions. In addition, collaborative filtering was used to make recommendations based on the similarity between users and items.

The recommendation system was further refined using various techniques, such as removing outliers and implementing bias correction methods, to improve the overall accuracy of the recommendations. Python libraries, including Scikit-learn and Surprise, were used to implement the recommendation algorithms and evaluate the performance of the model.

For new users, the best way to recommend articles was to first use content-based filtering to recommend items that are similar to the user's interests. This was done by using NLP techniques to extract features from the articles and calculate their similarity to the user's reading history.

In conclusion, the IBM articles recommendation system was developed using a combination of various approaches and techniques to provide accurate and personalized recommendations to users. The use of matrix factorization and collaborative filtering, along with data cleaning and bias correction methods, contributed to the success of the model.


## Disaster Response Classifier

In this disaster response classifier project, various technical approaches were used to create an effective machine learning model. The following were the main technical aspects involved in the project:

- ETL Pipeline: An ETL pipeline was developed using Python, Pandas, and SQLalchemy for data extraction, transformation, and loading of the disaster response message dataset.

- NLP Techniques: Natural Language Processing (NLP) techniques were used to process and understand the text of the disaster response messages. This involved cleaning the text data, tokenizing, stemming and lemmatizing, and vectorizing the text data.

- Model Development: The machine learning model was developed using the Python library, Scikit-learn. The model was trained on a labeled dataset of disaster response messages and was able to categorize messages into 36 different categories.

- Model Selection: The model was built using a text processing and machine learning pipeline. GridSearchCV was used to tune the model and select the best parameters.

- Model Deployment: The final model was exported as a pickle file and deployed in a Flask web app. This provided a user-friendly interface for emergency workers to classify messages and view data visualizations.

- Model Evaluation: The model was evaluated using various metrics such as accuracy

In conclusion, the disaster response classifier project demonstrated the use of NLP techniques and machine learning to classify disaster response messages into 36 different categories. The model was trained and evaluated using various techniques and libraries, and the final model was deployed in a user-friendly Flask web app.

## House SalePrice Regression

In this project, a house sale price regression model was developed using various machine learning techniques. The main objective was to predict the sale price of a house based on its various features. The dataset consisted of a range of house features such as number of bedrooms, square footage, location, etc.

The project involved various steps such as data cleaning, feature engineering, and model building. To clean the data, missing values were filled and outliers were removed to ensure that the data was free of any inconsistencies. In the feature engineering step, new features were created from the existing ones, and the categorical variables were transformed into numerical ones.

For model building, a range of regression algorithms were tested including linear regression, decision tree regression, and random forest regression. The best performing model was selected based on the root mean squared error (RMSE) and R-squared values. The model was then optimized using GridSearchCV, which is a powerful technique for tuning the hyperparameters of a model.

In addition to the model building, the project also involved data visualization, which was carried out using popular libraries such as Matplotlib and Seaborn. A heatmap was created to visualize the correlation between the various features and the target variable. This helped to better understand the relationship between the features and the sale price of a house.

In conclusion, this project showed the use of machine learning algorithms for regression problems, and how the performance of a model can be improved by tuning its hyperparameters. The results of this project can be used as a starting point for further work on predicting house sale prices.


<img width="965" alt="Screen Shot 2023-02-12 at 2 15 02 PM" src="https://user-images.githubusercontent.com/90535174/218298138-7a630471-0f7d-4982-9c72-fcb7fa6059e0.png">
