# House price prediction

### Dataset 
In this dataset we have to predict the sales price of houses in King County, Seattle. It includes homes sold between May 2014 and May 2015. Before doing anything we should first know about the dataset what it contains what are its features and what is the structure of data.

The dataset cantains 20 house features plus the price, along with 21613 observations.

The description for the 20 features is given below:

1. `id`: It is the unique numeric number assigned to each house being sold.
2. `date`: It is the date on which the house was sold out.
3. `price`: It is the price of house which we have to predict so this is our target variable and aprat from it are our features.
4. `bedrooms`: It determines number of bedrooms in a house.
5. `bathrooms`: It determines number of bathrooms in a bedroom of a house.
6. `sqft_living`: It is the measurement variable which determines the measurement of house in square foot.
7. `sqft_lot`: It is also the measurement variable which determines square foot of the lot.
8. `floors`: It determines total floors means levels of house.
9. `waterfront`: This feature determines whether a house has a view to waterfront 0 means no 1 means yes.
10. `view`: This feature determines whether a house has been viewed or not 0 means no 1 means yes.
11. `condition`: It determines the overall condition of a house on a scale of 1 to 5.
12. `grade`: It determines the overall grade given to the housing unit, based on King County grading system on a scale of 1 to 11.
13. `sqft_above`: It determines square footage of house apart from basement.
14. `sqft_basement`: It determines square footage of the basement of the house.
15. `yr_built`: It detrmines the date of building of the house.
16. `yr_renovated`: It detrmines year of renovation of house.
17. `zipcode`: It determines the zipcode of the location of the house.
18. `lat`: It determines the latitude of the location of the house.
19. `long`: It determines the longitude of the location of the house.
20. `sqft_living15`: Living room area in 2015(implies-- some renovations)
21. `sqft_lot15`: lotSize area in 2015(implies-- some renovations) 

### Model
After EDA several features were picked and four different models compared in effectivness. The best model appeared to be the Gradient Boosting one. All training and EDA are included in Jypiter Notebook file

### How to launch
1. Clone repositry
2. Install docker
3. Run `docker compose up --build`
4. Access service via browser at `localhost:5000`

### Work instrcutions
For model prediction it is required to upload file in html form from local machine. The Specification of file is described on the page, as well as example file `test.txt` provided.
