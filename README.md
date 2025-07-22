# Loan Approval Prediction and deployment using Flask and RESTful API

## Overview

This project aims to predict the likelihood of loan approval to individuals or organizations from a lending institution based on the financial records and associated information as given in the dataset. Also the model is being deployed using Flask RESTful API and tested using Postman tool.

## Dataset

The loan approval dataset, sourced from Kaggle, includes various factors such as Loan Applicant's education and employment status, cibil score, annual income, loan term, loan amount, assets value and loan status.

## Requirements

- pandas
- numpy
- matplotlib
- seaborn
- scikit-learn
- imbalanced-learn
- flask
- RESTful API

## Prediction Process

1. Start with downloading the loan approval dataset from the repository
2. Install the required libraries in Jupyter Notebook
3. Check for any inconsistencies, missing or null values and outliers in the data and fix them
4. Visualize and explore the data, uncover patterns and identify potential issues
5. Check for any existing imbalance in the data and sample it
6. Train the model and find the best-match ML Algorithm using various performance metrics
7. Fit the best-performing model and save it as pickle file
8. Develop the Flask app with Loan Approval Prediction Form being shown on the index html page and the Loan Approval Status being displayed on the results page.
9. Test the RESTful API using Postman tool
