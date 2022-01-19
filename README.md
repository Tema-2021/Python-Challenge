# Python-Challenge
_____________________________________________________

### Contributor: 

**Valense Acquah-Louis**

## Background

Python is an integrated high level computer programming language which is versatile and uses data, mathematical computatitions and lines of code. 

This project is made up of two challenges
* PyBank
* PyPoll

Two different sets of csv's a read and lists, dictionaries, and tuples are used to analyze the data and create output files.
The files for each analysis are saved in main.py files.
 
**Source of data:**

The source data is in a form of a csv 

* budget_data.csv for the PyBank analysis  
* election_data.csv for the PyPoll analysis

## PyBank
_____________________________________________________
![image](https://user-images.githubusercontent.com/82990618/150007537-2ebb54e3-3677-4c71-ab93-124370edefc0.png)

For this analysis, financial records/ dataset of a company was analyzed. The dataset is composed of two columns: Date and Profit/Losses.

This Python script analysis the dataset to calculate:

* The total number of months included in the dataset
* The net total amount of "Profit/Losses" over the entire period
* Calculate the changes in "Profit/Losses" over the entire period, then find the average of those changes
* The greatest increase in profits (date and amount) over the entire period
* The greatest decrease in profits (date and amount) over the entire period

The final script prints the analysis to the terminal and export a text file with the results.


The analysis should look like below:

Finacial Analysis

----------------------------
Total Months: 86

Total: $38382578

Average  Change: $-2315.12

Greatest Increase in Profits: Feb-2012 ($1926159)

Greatest Decrease in Profits: Sep-2013 ($-2196167)

## PyPoll
_____________________________________________________
![image](https://user-images.githubusercontent.com/82990618/150009576-53d656fd-6062-429a-bb8c-35305afaaec1.png)

In this next analysis ascript is written to help a small rural town to modernize its vote counting process. '

A set of poll data called election_data.csv is used in the analysis. The dataset is composed of three columns: Voter ID, County, and Candidate and this script analyzes the votes and calculates each of the following:

* The total number of votes cast
* A complete list of candidates who received votes
* The percentage of votes each candidate won
* The total number of votes each candidate won
* The winner of the election based on popular vote.

The final script for this analysis should also print the analysis to the terminal and export a text file with the results.

Election Results

-------------------------

Total Votes: 3521001

-------------------------
Khan: 63.000% (2218231)

Correy: 20.000% (704200)

Li: 14.000% (492940)

O'Tooley: 3.000% (105630)

-------------------------

Winner: Khan
-------------------------








