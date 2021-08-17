# Flight_Price_Prediction

## Table of Content
- Overview
- Description
- Motivation
- Dataset
- Installation
- Technologies used
- Directory Tree
- Demo
- Deployment

## Overview
This project on Flight Fare Price Prediction is based on the flask web app. It is deployed in Heroku.


## Description
ExtraTreeRegressor is used to get the best Features from the dataset.

K-cross validation is used to get the best model from SVM, DecisionTree and Random Forest.

Here, Random Forest Regression is used as it is the best fit for this regression problem.


## Motivation
The motivation behind was to get the hands on experience and to know that how the data scientist approachs and work in an industry end to end. This is my first end to end implementation of machine learning. This oppurtunity was given by inueron internship program.


## Dataset
Link :- https://www.kaggle.com/nikhilmittal/flight-fare-prediction-mh

## Installation
### install python:-
```
conda install python==3.9.6
```
### create env:-
```
conda create --name flightenv
```
### create and add list in requirements.txt file:-
```
conda list e > requirements.txt
```

## Technologies Used
![image](https://user-images.githubusercontent.com/76507095/129721804-e596d45e-2f5d-4390-9d23-061dbc37b7ce.png)

![image](https://user-images.githubusercontent.com/76507095/129721853-6a0f24b2-27de-4826-b36b-57fc8c1a1202.png)

![image](https://user-images.githubusercontent.com/76507095/129721761-b3fee168-4192-4ab8-8441-6bb3c5a15a65.png)


## Directory Tree
```
|--- dataset
|    |--- Data_train.xlsx (unprocessed)
|    |--- Train_preprocesses.csv
|    |--- Test_set.xlsx (unprocessed)
|    |--- Test_preprocessed.csv
|--- model
|    |--- Feature Engineering(Train).ipynb
|    |--- Feature Engineering(Test).ipynb
|    |--- Feature Selection.ipynb
|    |--- Flight_model.ipynb
|--- static 
│    |--- css
|    |--- image
|         |--- flight-1.jpg       
|--- template
│    |--- home.html
|--- Compress_pkl.py
|--- Procfile
|--- README.md
|--- app.py
|--- Price_Regression.pkl
|--- requirements.txt
```


## Demo
### Welcome page
![Screenshot (7)](https://user-images.githubusercontent.com/76507095/129676813-33539395-1b2f-4e18-a5ed-501ef3ff1cd9.png)

Scroll down

### Input page
![Screenshot (9)](https://user-images.githubusercontent.com/76507095/129676878-7a8199ef-1f8b-4b9a-9bf3-8ee060f42d9e.png)

### Output page
![Screenshot (8)](https://user-images.githubusercontent.com/76507095/129676943-fb13238d-57b8-4542-8cca-c6b4da56fb88.png)


## Deployment
Here, I am able to deploy the model but not able to start the link. There is a problem of R15 memory issues, which I don't know how to solve.

As you can see on the right section in Environments, the model is active but I'm not able to start

![Screenshot (2)](https://user-images.githubusercontent.com/76507095/129676282-de84d6fb-9188-48bd-be5a-00e70d401a50.png)

# Please, comment if you have a solution to the R15 memory base error in Heroku!!
