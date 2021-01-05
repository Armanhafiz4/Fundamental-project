# Fundamental-project


## GYM Workouts App


### Contents
* [Brief](https://github.com/Armanhafiz4/Fundamental-project/blob/main/README.md#brief) 
  * [Requirements](https://github.com/Armanhafiz4/Fundamental-project/blob/main/README.md#requirements)
  * [My Idea](https://github.com/Armanhafiz4/Fundamental-project/blob/main/README.md#my-idea)
* [Architecture](https://github.com/Armanhafiz4/Fundamental-project/blob/main/README.md#architecture)
  * [ERD](https://github.com/Armanhafiz4/Fundamental-project/blob/main/README.md#erd)
* [Project Tracking](https://github.com/Armanhafiz4/Fundamental-project/blob/main/README.md#project-tracking)
* [Risk Assessment](https://github.com/Armanhafiz4/Fundamental-project/blob/main/README.md#risk-assessment)
* [Testing](https://github.com/Armanhafiz4/Fundamental-project/blob/main/README.md#testing)
* [Front-End Design](https://github.com/Armanhafiz4/Fundamental-project/blob/main/README.md#front-end-design)
* [Known Issues](https://github.com/Armanhafiz4/Fundamental-project/blob/main/README.md#known-issues)
* [Future Improvements](https://github.com/Armanhafiz4/Fundamental-project/blob/main/README.md#future-improvements)
* [Acknowledgements](https://github.com/Armanhafiz4/Fundamental-project/blob/main/README.md#acknowledgements)
* [Authors](https://github.com/Armanhafiz4/Fundamental-project/blob/main/README.md#authors)

### Brief 
The objective for this Fundamental project is to create a CRUD application with using all core modules covered during my training so far at QA. I have created an application that has the functions of create, read, update and delete in order to operate a Gym Workouts App for users to use as their own workout planner.

#### Requirements
Aswell as operating and making a CRUD application there are also other requirements such as:

* A Kanban board with full expansion on user stories and project tracking. For this I have used a   Trello board.
* A relational database consisting of at least 2 tables that have a relationship
* A clear documentation of the design phase, application architecture and a risk assessment 
* A functioning CRUD application created in Python
* Shown testing for my application which uses automated tests for the application I created
* A functioning front-end website that I must create using Flask
* A code integrated into a Version Control System which would be built through a CI server and deployed to a cloud-based virtual machine

#### My Idea

My idea is to create an app that allows users to have a gym workout planner where users can create gym workouts, add exercises, view, update and delete their workouts within these days. The application must allow users to carry out the following: 

* Create: 
  * Workout title 
  * Exercise names 
  * How many repetitions
  * The date that the workout day was created
* Read: 
  * Workouts that have been created
  * Exercises that are under each workout day
  * Repetitions that are under each workout day
  * The date and time the workout was created
* Update: 
  * Workouts
* Delete: 
  * Workouts
  
### Architecture 

#### ERD
Below is 2 entity relationship diagrams (ERD) which shows the structure of the database I am using. The first ERD is my original ERD however as my project progressed I chose certain things to not implement into my app, so therefore the second ERD is my final ERD for my app as it includes everything I implemented. 
<br>
![alt text](https://github.com/Armanhafiz4/Fundamental-project/blob/main/Original%20ERD%20Diagram.png) 
<br>
My original ERD which is above shows a many to many relationship. This idea included me creating an app where users create an account with a user id and password. Then they create their workout and then their exercises which would be attached to their workouts. The application would also allow users to view their friends workouts and exercises planned, this idea also allows users to share their workouts too. 
<br>
![alt_text](https://github.com/Armanhafiz4/Fundamental-project/blob/main/ERD%20new%20Diagram.png)
<br>
However as my project progressed I stuck to this ERD and idea where there was no create a username function etc and no sharing workouts with friends. Now a one to many relationship is shown in this ERD and I chose this idea as I saw my criteria that I needed to fulfill for this project and as this ERD allowed me to have a relational database between 2 tables and be able to create an application with CRUD functionality. My old ERD was quite complex so I decided to trim my idea and ERD to ensure that the MVP CRUD functionality was met. Any trimmed fields could be re-introduced for a future improvement of my application. My new ERD shows my idea on how users create a workout and add exercises and repetitions to the workout etc.

### Project Tracking

I tracked my progress using a trello board which is made [here](https://trello.com/b/ihNNyfj3/qa-fundamental-project). This trello board I made includes project requirements, a product backlog, detailed user stories, tasks on my current to do list from the date of making my trello board, tasks in progress from the date of making my trello board and completed tasks from the date of making my trello board.
<br>
![image](https://user-images.githubusercontent.com/74771197/103489502-db415c80-4e0c-11eb-8e31-b97b1b835a4e.png)

### Risk Assessment


My risk assessment table:

![image](https://user-images.githubusercontent.com/74771197/103491155-3ed18700-4e19-11eb-8cbd-e694ebf70e1d.png)
<br>
![image](https://user-images.githubusercontent.com/74771197/103492775-22d3e280-4e25-11eb-97af-c14bb9c07876.png)
<br>
My risk assessments include the description of the risk, the assessment of the risk, the probability, the level of impact, who has the responsibility of the risk, the current mitigation, the proposed mitigation and the response. My first risk assessment table includes the risks that I identified at the start of the project however as my project progressed I identified more risks which I placed in a second risk assessment. 

### Testing

The following screenshots shows my unit-testing and how I achieved 84% total coverage in my unit tests. 

![image](https://user-images.githubusercontent.com/74771197/103464355-f045bf00-4d2a-11eb-938e-396fef918d83.png)
<br><br>
To start my unit tests the relevant imports must be made which are the unittest module from Python, flask and flask_testing that allows us to import url_for and TestCase. TestCase is the basis needed to run all my unit tests which is used after setting up TestBase to use TestCase. Also app and the database is imported along with my models which are to be tested (Workout, Exercises). After all the required imports are imported, the TestBase is set up and the first function that is run allocates properties to the database for the temporary database to use. SQLite was used so the main database wasn't affected. After this SetUp and tearDown functions are allocated with the self argument passed through these. The SetUp and tearDown functions create and also populate the database and also remove the database. These are run seperately for each test and this makes sure that each test would be working with the same set of data.
<br><br>
![image](https://user-images.githubusercontent.com/74771197/103464362-14090500-4d2b-11eb-8a40-d865d1268046.png)
<br><br>
After the set up is completed, now we want to test flask so we can see if the routes are working and sending back the correct status codes. The status code 200 means a successful get request. These tests are to see if when a user navigates to the url_for ('name of the page') that they are sent there and that the app recognises this. The delete get requests have to allow redirects as the delete function we have contains a redirect to the home page of my application which allows the user to delete as many workouts on the homepage without the page changing or refreshing. After our routes are tested, I tested the read functionality within flask. This function passes through the home page through a get request and assumes that specific data will be in the response data. I tested this by seeing if "Workout1" was present on the home page and this would show me that the database is working correctly and flask is displaying the correct information.    
<br><br>
![image](https://user-images.githubusercontent.com/74771197/103464375-208d5d80-4d2b-11eb-936b-b0d471b1892a.png)
<br><br>
The createworkout functionality of my app was tested by my test acts like a user and would send a post request to the createworkout route which would enter the data that is required by the user in order to create a workout. It would then see if it directs to the home page and seeing whether the data entered in the post request is now included in the response data of the home page. I also tested the remaining functions of the CRUD application which is Update and Delete. The test for the Update function is when the user navigates to the update link and performs an update on their workout, the previous workout title should change to the new workout title entered in the post request, also using the get request to show the new workout title on the home page. The delete route was tested by seeing if the user navigates to the delete route then it should delete the workout with the associated workout title that the user has chosen to delete and that it would be no longer present when redirecting to the home page.
<br><br>
![image](https://user-images.githubusercontent.com/74771197/103591682-bb7f6680-4ee8-11eb-9940-914c70b4d779.png)
<br><br>
As this screenshot shows, the unit tests have tested majority of my application with 100% of lines within init, forms and models being tested and 71% being tested within the routes. This gave an overall of 84% being tested and I used the missing terms command to see which lines from my routes that are missing which would allow me to see what needs to be tested in order to achieve 100% of lines being tested in my unit tests in the future. 

### Build

The CI pipeline for this project revolved around Jenkins and Git. Below are screenshots provided on my jenkins console output and after I automated a pytest as it shows which tests I passed and failed. Jenkins produces console outputs that tells the developer how many tests the code passes and also which tests that the code failed. Again it shows that 84% of my application was tested and we use Jenkins as a way to automate our tests by using builds. The first screenshot provided is my Jenkins script in the command section when executing my shell and the second screenshot is the test coverage shown in my console output. 
![image](https://user-images.githubusercontent.com/74771197/103557342-f367b900-4eaa-11eb-83b0-125b872b7789.png)
<br><br>
![image](https://user-images.githubusercontent.com/74771197/103637102-df6f9600-4f42-11eb-936a-326d296d8b89.png)


### Front-End Design
<br><br>
![image](https://user-images.githubusercontent.com/74771197/103638221-856fd000-4f44-11eb-92e8-66764e055160.png)
<br><br>
![image](https://user-images.githubusercontent.com/74771197/103638403-c667e480-4f44-11eb-9832-50624566d66b.png)
<br><br>

### Known Issues
The main issue that my application has is that the add function is still faulty. There is a button there for the user to add their chosen exercise however it doesnt redirect itself to the home page in order for the exercise to be shown under the users chosen workout. However my application has its CRUD functionality and working tests.

### Future Improvements
Future improvements I would like to implement into my project would be another form of testing for example selenium integration testing. This would be done using chromedrivers and it would give another way in testing the system. The more tests the better as I would be more confident that I was able to make a functioning application. Another future improvement I would like to make is that I would like to get 100% coverage in my unit testing, this should be attainable due to the missing terms command as I can see which lines are not being covered in my routes page. Also I would fix my add function so it is a completely working application where users can add their exercises to their workouts.

### Acknowledgements
Harry Volker for providing the base of the CRUD project and guiding us throughout the project. Nathan Forester for providing guidance throughout the project specifically with Jenkins. Jay Grindrod guiding us throughout the project specifically with database models and logistics. Sam Birchall for guiding us throughout the project.

### Authors
Arman Hafiz
