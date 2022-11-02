# google_spreadsheets_read_write_data
Python code for fetching and update gogle spreadsheets data 


-------------------------------------------------------------------------------------------------------------
-------------------------------------------------------------------------------------------------------------
-------------------------------------------------------------------------------------------------------------

Learn how to use Python and Google Sheets API to read and write data to a spreadsheet with a service account. 

Resources:

https://www.youtube.com/watch?v=4ssigWmExak



-------------------------------------------------------------------------------------------------------------
-------------------------------------------------------------------------------------------------------------
-------------------------------------------------------------------------------------------------------------


Read and Update Google Spreadsheets with Python!
download
Share
Lakshay Arora — Published On July 30, 2020 and Last Modified On June 16th, 2022
Beginner Excel Programming Python
Overview
Learn how to setup a Google service account
Read and Write data in Google Spreadsheets using Python
 

Introduction
Automation of work has been one of the quickest ways to reach functional efficiency. Moreover, in today’s era where success is dependent on speed, automation of myriad repetitive tasks play a key role in any industry and at the most basic level of functionality. But many of us fail to understand how to automate some tasks and end in the loop of manually doing the same things again.

google spreadsheets with python

For instance, we often spend hours daily extracting data and then copy-pasting to spreadsheets and creating reports leading to excessive time consumption. Consequently, it would be great if we just run a script, and data is uploaded in the spreadsheet and the report is prepared with just a click. There are multiple advantages of report automation like you would be able to save time on data collection and removing typos and focus would be more on the analysis part.

In this article, we will see a step by step process to set up a Google service account. We will make use of the Google APIs to read google spreadsheets data using python and we will also update the data in the spreadsheet using python. We are going to read the cricket commentary data from the spreadsheet and find out the number of runs scored by each batsman and then upload the results into a separate spreadsheet.

In case you are unfamiliar with Python, do have a look at our free course Introduction to Python

Loading Image
100+ Data Science Job Openings
Lenovo, TVS, Convergytics, Ripik.AI and many more are hiring | Open to all Data Science Enthusiasts.
 

Table of Contents
Create Google Service Account
Read Data from Google Sheets
Update Data in Google Sheets
 

Create Google Service Account
In order to read and update the data from google spreadsheets in python, we will have to create a Service Account. It is a special type of account that is used to make authorized API calls to Google Cloud Services. First of all, make sure that you have a google account. If you have a Google account, you can follow these steps to create a Google service account.

Go to the developer’s console.  Now, you will see something like this. Click on the Create Project button.google spreadsheets with python : Create project
Then provide the project name and the organization name which is optional. Then click on the create button.google spreadsheets with python : new project name
Now, that our project is created we need to enable the APIs that we require in this project. Click on the Enable APIs and Services button to search for the APIs that Google provides.google spreadsheets with python: APIs and servicesConsequently, we will add two APIs for our project.
Google Sheets API
Google Drive API
 

Then, in the search bar, search for these APIs and click on the enable button.google spreadsheets with python: API search bar
 Google Sheets API will look something like this. It will allow you to access Google Spreadsheets. You would be able to read and modify the content present in the Spreadsheets.google spreadsheets with python: enable
Google Drive API will look something like this. It will allow you to access the resources from Google Drive.google spreadsheets with python
Once you have enabled the required APIs in your project then it’s time to create credentials for the service account. Click on the Create Credentials button to continue.google spreadsheets with python:overview
 
Now, select Google Drive API in the type of API required question. We will be calling the API from a non UI based platform so select Other non-UI (e.g. cron job, daemon). Select the Application Data in the next question as we do not require any user data to run our application. And also we are not using any cloud-based compute engine for our application. Finally, click on the What credentials do I need? button.
Then, share the google spreadsheets with other people and provide permission like edit or view only. Similarly, we will provide access to our service account. We will give it the complete access so that we will be able to read as well as write the spreadsheets and download the JSON file of the credentials.
 

Now, a JSON file will be downloaded which contains the keys to access the API. Our google service account is ready to use. In the next section, we will read and modify the data in the spreadsheet.

 

Read Data from Google Sheets
We will read the commentary data of the India Bangladesh cricket match. You can access the data here.

google spreadsheets with python : data

We have a ball by ball data of the complete match in the spreadsheet. Now, we will do a very basic task and calculate how many runs are scored by each of the batsmen. We can do this by using a simple groupby in pandas. And finally, we will upload the results in a separate sheet.

Provide access to the Google Sheet
Now, we need to provide access to the google sheet so that the API can access it. Open the JSON file that we downloaded from the developer’s console. Look for the client_email in the JSON file and copy it.

google spreadsheets with python: client email

Then click on the Share button on the Spreadsheet and provide access to this client email.

google spreadsheets with python : Provide access to google sheet

Now, we are ready to code and access the sheet using python. The following are the steps-

1. Importing the Libraries
We will use the gspread and oauth2client service to authorize and make API calls to Google Cloud Services.

You can install the libraries using the following commands.
