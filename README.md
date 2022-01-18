# Python-Challenge
_____________________________________________________

### Contributor: 

**Valense Acquah-Louis**

## Background

Python is an integrated high level computer programming language which is versatile and uses data, mathematical computatitions and lines of code. 

This project is made up of two challenges
* PyBank
* PyPoll
 
**Source of data:**

The source data is in the form of a raw data, so the data will first be processed and used to fit the machine learning models. The is no known classification system, hence the use of unsupervised learning. Several clustering algorithms will be used to explore whether the cryptocurrencies can be grouped together with other similar cryptocurrencies and data visualization will be used to share the findings with the investment bank.

The data was obtained from https://min-api.cryptocompare.com/data/all/coinlist (CryptoCompare)

## PyBank
_____________________________________________________
![image](https://user-images.githubusercontent.com/82990618/150007537-2ebb54e3-3677-4c71-ab93-124370edefc0.png)


### Analysis

**Data Preparation**

Using a series of steps, the data was prepared for the analysis. The steps are listed below.
*	Reading
*	Cleaning (filtering, elimination)
*	Standardize 
*	Reduction

## PyPoll
_____________________________________________________
![image](https://user-images.githubusercontent.com/82990618/150009576-53d656fd-6062-429a-bb8c-35305afaaec1.png)

**Reading & Cleaning**
* Read crypto_data.csv into Pandas. 
*  Discard all cryptocurrencies that are not being traded. Filter for currencies that are currently being traded. Once done this, drop the IsTrading column from the dataframe.
*  Remove all rows that have at least one null value.
*  Filter for cryptocurrencies that have been mined. That is, the total coins mined should be greater than zero.
*  Since the coin names do not contribute to the analysis of the data, delete the CoinName from the original dataframe to make the data comprehensible to a machine learning algorithm.
*  Convert the remaining features with text values, Algorithm and ProofType, into numerical data using Pandas to create dummy variables. Examine the number of rows and columns of your dataset now. How did they change?

**Standardize**

* Standardize your dataset so that columns that contain larger values do not unduly influence the outcome.

**Dimensionality Reduction and Models**

* Creating dummy variables dramatically increased the number of features in the dataset. Dimensionality reduction with **PCA** was performed. Rather than specify the number of principal components when the **PCA** model is instantiated, the desired **explained variance was stated**. For example, say that a dataset has 100 features. Using **PCA**(n_components=0.99) creates a model that will preserve approximately 99% of the explained variance, whether that means reducing the dataset to 80 principal components or 3. For this project, 90% of the explained variance in dimensionality reduction was preserved. 
*  Next, further reduction of the dataset dimensions with **t-SNE** was performed  and the results visually inspected. To accomplish this task, **t-SNE** was run on the principal components: the output of the **PCA** transformation. Then a scatter plot of the **t-SNE** output was created. 

**Scatter Plot**

![image](https://user-images.githubusercontent.com/82990618/136716217-bd3c964f-4ad8-456f-a690-95a537df3d0d.png)

**Observation**

Observe whether there are distinct clusters or not?

There appears to be about 4 distinct clusters with 2 outliers

**Cluster Analysis with k-Means**

An elbow plot (**k-Means**) was created to identify the best number of clusters. Using a for-loop the inertia for each **k** between 1 through 10 was determined. The value of **k** where the elbow of the plot lies was determined, that is  at which value of **k** it appears. 

**Elbow Curve Plot**

![image](https://user-images.githubusercontent.com/82990618/136716645-464f6ced-b623-4864-8171-c864091dd08a.png)

**Observation**

From the elbow curve the k appears around 4 which is indicative of 4 clusters as seen in the scatter plot.

### Observations and Recommendation

**Observations:**

*Scatter Plot from PCA and t-SNE analysis*

* There appears to be about 4 distinct clusters with 2 outliers. 

*k-Means Elbow Curve*

* From the elbow curve the k appears around 4 which is indicative of 4 clusters as seen in the scatter plot.

**Recommendation:**

Since clustering is used in Unsupervised Machine Learning to classify data into structures to make it possible for easy manipulation as well as make the data easy to understand. Clustering minimizes the variance of data point within the cluster and combine data that are like each other. The Scatter plot was a little unclear of the number of possible clusters, so the elbow curve was employed. 
The Elbow Curve is used to determine the optimal number of possible clusters. From the elbow curve the value of k=4 (the point where there is an improvement in distortion) which means further division of the data into clusters are not necessary. 
The Cryptocurrency data can therefore be clustered into 4 groups for analysis.  
