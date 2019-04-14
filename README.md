# Aduhan
CodeathonX Kuala Lumpuer April 2019 - Team Aduhan  

This is a project created during the CodeathonX KL on 13-14 April 2019. 

Aduhan was created by 4 passionate youths from different backgrounds interested in using tech to improve the world for societies and communities. Aduhan aims to improve the well-being of communities by facilitating the maintenance of public amenities and infrastructure. Our goal is inline with the United Nation's [Sustainable Development Goals](https://www.un.org/sustainabledevelopment/sustainable-development-goals/), specifically [Goal 11: Sustainable Cities and Communities](https://www.un.org/sustainabledevelopment/cities/). 

We begin the project by first targeting the Kuala Lumpur metropolitan area.

# Problem statement

1. How can we ensure that everyone has access to good public facilities? 
2. How can we help the underserved communities / communities with special needs to get their needs heard?
3. How can we get more citizens involved in making important decisions for their city? 
4. How can we improve the transparency of government?
5. How can we facilitate conversations between government and citizens?

# The Idea

# Details
## Format of data consumed
We will be getting user data from multiple platform which will then be transformed into a csv file with the following columns:
1. Date
2. Longitude
3. Latitude
4. Problem description
5. Category (traffic, housing, park, etc..)
6. Involving undeserved group? (Decided by algorithm, see next section)
7. Criticality (E.g. issues with traffic light in busy roads)

## How our algorithm determine if the problem involve undeserved group? 
We use a simple rule-based system:
1. We check if it has been specifically marked as involving identified underserved / special need communities, i.e. handicaped, children, women etc. **{If yes --> underserved group}**
2. We identify the location of the problem & check if belongs to a region with high populations of low income. **{If yes --> underserved group}**
3. We scan the problem description and determine it should be marked as underserved group, keywords model, e.g. "ramp for wheelchair", etc.. **{If yes --> underserved group}**

*For all other problems posted, we let volunteers mark them and have another volunteer to verify it, feeding the data to model for better prediction next time*

## Running prototype
- Go to https://ludwighoon.github.io/Aduhan/App%20Prototype%20V3/index.html#/screens/01de8dc3-c48f-4553-911e-d84823348ec5 for mockups 
- Demo at https://youtu.be/9rsxbqe5Dtw 
- python serve.py //Just for PoC for getting data, etc..
- Others are still under development - check Jupyter notebook --> Data wrangling --> Possibly training model with WEKA (depends on time)
- Currently visualisation is done in Tableau (remove dependency later)

## Data used
Our test cases is in Malaysia and we made use of open data provided by Malaysian government. The data is stored in *data* (creative common - open data licence). There may be other useful data that we have missed, visit http://www.data.gov.my to see a full list of data available.  

# More information
For more information, please check our slides at: <Insert later(**Change permision to view only)>
