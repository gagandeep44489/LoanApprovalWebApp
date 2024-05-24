Loan Approval Prediction in Python language
Anaconda Jupyter Notebook is best to open the this kind of file and shift + enter is used to run the each cell.
Table of Contents
Project Description
Libraries Required
Data
Descriptive Statistics and Exploratory Analysis
Prediction
Conclusion
Project Description
LOANS are the major requirement of the modern world. By this only, Banks get a major part of the total profit. It is beneficial for students to manage their education and living expenses, and for people to buy any kind of luxury like houses, cars, etc.
But when it comes to deciding whether the applicant’s profile is relevant to be granted with loan or not. Banks have to look after many aspects.
So, here we will be using Machine Learning with Python to ease their work and predict whether the candidate’s profile is relevant or not using key features like Marital Status, Education, Applicant Income, Credit History, etc.


Libraries Required
Here are the required libraries to run the code properly:


pandas
seaborn
matplotlib
os
joblib
streamlit

Data
I have collced the data from kaggle which is shown downward

The dataset contains 13 features : 

1	Loan	A unique id 
2	Gender	Gender of the applicant Male/female
3	Married	Marital Status of the applicant, values will be Yes/ No
4	Dependents	It tells whether the applicant has any dependents or not.
5	Education	It will tell us whether the applicant is Graduated or not.
6	Self_Employed	This defines that the applicant is self-employed i.e. Yes/ No
7	ApplicantIncome	Applicant income
8	CoapplicantIncome	Co-applicant income
9	LoanAmount	Loan amount (in thousands)
10	Loan_Amount_Term	Terms of loan (in months)
11	Credit_History	Credit history of individual’s repayment of their debts
12	Property_Area	Area of property i.e. Rural/Urban/Semi-urban 
13	Loan_Status	Status of Loan Approved or not i.e. Y- Yes, N-No 
First, we are going to take a look at the data and examine their relationships. In addition, we have to find how many missing values we have and in which variables and replace them with sensible values. We will also use some visualizations in order to better understand the relationships between the variables. Furthermore, we will make several graphs and computations to determine which transformation of variables can be added as new features.

Prediction
Now, we will build and fit some models to the training set and we will compute their accuracy on the test set. For this purpose, we will build seven different models: Decision Tree (DT), Random Forest (RF), Extra-Tree, Gradient Boosting Machine (GBM), XGBoost, Logistic Regression (LR), Support Vector Machine (SVM), kNN (k-Nearest Neighbors) and Neural Network (NN). We reset the random number seed before each run to ensure that each algorithm will be evaluated using the same data partitions. This means that the results will be directly comparable.

More details can be found within the project.

Conclusion : 
Random Forest Classifier is giving the best accuracy with an accuracy score of 82% for the testing dataset. And to get much better results ensemble learning techniques like Bagging and Boosting can also be used.
 In Web Development In this I have used joblib library to save the Random Forest Classifier model and with thinker I have made prediction and now with the help of streamlit library with spyder I have build a web application on to run on localhost this application type stremlit run filename (loanApproval.py) or type this on console
