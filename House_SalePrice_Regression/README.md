MEDIUM POST: https://medium.com/@apurbapandey60/how-to-pick-a-house-for-investment-purposes-ff27e03062f9

# House-SalePrice-Analysis

Analyzing house features to find the most correlated features which can be helpful for real estate purposes.
This project also covers using machine learning model to predict the saleprice of the house.

## CRISP-DM process consists of six phases, as follows, which we will be utiziling:

- Business Understanding: In this phase, the objective of the project and the business problem to be solved are defined. The data mining goals and success criteria are also established in this phase.

- Data Understanding: In this phase, the data is collected and explored to gain an understanding of its quality, completeness, and structure. This phase includes tasks such as data exploration, data quality assessment, and data cleaning.

- Data Preparation: In this phase, the data is transformed and cleaned so that it is in a format that can be used for analysis. This phase includes tasks such as missing value imputation, feature scaling, and data normalization.

- Modeling: In this phase, statistical and machine learning models are developed to analyze the data and solve the business problem. This phase includes tasks such as model selection, feature selection, and model evaluation.

- Evaluation: In this phase, the results of the models are evaluated to determine their performance and accuracy. This phase includes tasks such as performance measurement, model comparison, and model tuning.

- Deployment: In this phase, the model is deployed to the production environment and put into use. This phase includes tasks such as model deployment, monitoring, and maintenance.

## The following libraries were used in the project:

- Pandas: for data wrangling and analysis
- Numpy: for working with arrays
- Matplotlib and Seaborn: for data visualization, such as bar charts and heat maps
- Sklearn: for preprocessing the data, training machine learning models, and evaluating performance using various metrics
- Ipython.display: for displaying images within the notebook


## FILES IN THE REPOSITORY:

- Dataset (CSV Files): Training dataset, Testing dataset, Submission sample sataset, Final_submission ( this is the predicted prices for the test set)
- Description file (txt file): Features detailed description
- README.md: Contains the details and summary of the project

## QUESTIONS

- What are the most correlated features in a house to the sale price?
- What year were most of the houses built and does it have any correlation with the saleprice? is there variation in saleprice based on month?
- Can we use ML model to predict house saleprice given the same features with good axxuracy?

## SUMMARY
- The most correlated features with sale price were Overall quality of the house, Ground level living area, number of Car garage.
- Most of the houses were built in the year 2005, 2006. On average the houses built after 1980 have higher Saleprice. There is also no significance    difference in terms of average saleprice based on month. September taking the lead.
- Cross validation and Gridsearch were used to find the best performing ML model with best performing hyper-parameter. The model chosen was gradient boosting regressor (Best_hyperparameter :  {'learning_rate': 0.1, 'loss': 'squared_error', 'n_estimators': 300}) to predict the house sale price. Which gave a decent RMSE score of 0.025 on the training set and 0.13 on the test dataset.

## Acknowledgement And References

I am grateful to the libraries used in this project, such as Pandas, Numpy, matplotlib, Seaborn, Sklearn, and Ipython.display for making the data wrangling, analysis, visualization, and machine learning process much easier and smoother.

- Kaggle Community. (n.d.). Kaggle: Your Home for Data Science. [Online]. Available at: https://www.kaggle.com/ [Accessed: 11th February 2023].

- Stack Overflow Community. (n.d.). Stack Overflow: Where Developers Learn, Share, & Build Careers. [Online]. Available at: https://stackoverflow.com/ [Accessed: 11th February 2023].

- Udacity. (n.d.). Online Learning Platform for Programming, Data Science, AI, and More | Udacity. [Online]. Available at: https://www.udacity.com/ [Accessed: 11th February 2023].

- Bishop, C. M. (2006). Pattern Recognition and Machine Learning (1st ed.). New York: Springer.
