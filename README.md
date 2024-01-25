## End to End ML project

This is an End to End ML project in which I have used the US Health Insurance Dataset available on Kaggle and created an ML model for predicting the Health Insurance Bill for an individual.

<h2>Install</h2>
<li>Numpy</li>
<li>Pandas</li>
<li>Django</li>
<li>Matplotlib</li>
<li>Scikit-learn</li>
<li>Seaborn</li>
<br>
The link to the Kaggle Dataset used: https://www.kaggle.com/datasets/teertha/ushealthinsurancedataset
<hr>

For training various models like Linear Regression (Ridge and Lasso), KNeighboursRegressor, XGBoost, Decision Tree, Random Forest etc. were tried. In the end a BaggingRegressor with RandomForestRegression has been used.

The machine learning model created is deployed through a django application. In this application a user has to enter his/her details like age, height, weight, gender, no. of children and select in which region of US the person resides. Based on the entered values the predicted cost is displayed to the user.
