# Fundamental-project


## GYM Workouts App


### Contents
* [Brief](https://github.com/Armanhafiz4/Fundamental-project/blob/main/README.md#brief) 
  * [Requirements](https://github.com/Armanhafiz4/Fundamental-project/blob/main/README.md#requirements)
  * [My Idea](https://github.com/Armanhafiz4/Fundamental-project/blob/main/README.md#my-idea)
* [Architecture](https://github.com/Armanhafiz4/Fundamental-project/blob/main/README.md#architecture)
  * [ERD](https://github.com/Armanhafiz4/Fundamental-project/blob/main/README.md#erd)
  * [CI Pipeline](https://github.com/Armanhafiz4/Fundamental-project/blob/main/README.md#ci-pipeline)
* [Project Tracking](https://github.com/Armanhafiz4/Fundamental-project/blob/main/README.md#project-tracking)
* [Risk Assessment](https://github.com/Armanhafiz4/Fundamental-project/blob/main/README.md#risk-assessment)
* [Testing](https://github.com/Armanhafiz4/Fundamental-project/blob/main/README.md#testing)
* [Front-End Design](https://github.com/Armanhafiz4/Fundamental-project/blob/main/README.md#front-end-design)
* [Known Issues](https://github.com/Armanhafiz4/Fundamental-project/blob/main/README.md#known-issues)
* [Future Improvements](https://github.com/Armanhafiz4/Fundamental-project/blob/main/README.md#future-improvements)
* [Acknowledgements](https://github.com/Armanhafiz4/Fundamental-project/blob/main/README.md#acknowledgements)
* [Authors](https://github.com/Armanhafiz4/Fundamental-project/blob/main/README.md#authors)

### Brief 
GIVE MORE EXPLANATION ON BRIEF

The objective for this project is to create a CRUD application with using all core modules covered during my training so far at QA.
I have created an application that has the functions of create, read, update and delete in order to operate a Gym Workouts App

#### Requirements
CLEAR UP THE REQUIREMENTS

Aswell as operating and making a CRUD application there are also other requirements such as:
* A Trello board for project tracking
* A relational database consisting of at least 2 tables that have a relationship
* A clear documentation of the design phase, application architecture and a risk assessment 
* A functioning CRUD application created in Python
* Shown testing for my application which uses automated tests for the app
* A front-end website that I must create using Flask
* A code integrated into GitHub
* Google Cloud Platform

#### My Idea

My idea is to create an app that allows users to create a gym workout planner where users can create gym workout planned days, add, update and delete exercises within these days. The application must allow users to carry out the following: 

* Create: 
  * Workout name 
  * Exercise names 
  * How many repetitions
  * The date that the workout day was created
* Read: 
  * Workouts that have been created
  * Exercises that are under each workout day
  * Repetitions that are under each workout day
  * The date and time the workout was created
* Update: 
  * Workout days with exercises and repetitions
* Delete: 
  * Workouts
  
### Architecture 
TALK ABOUT YOUR ERD'S AND TALK ABOUT HOW AS TIME PROGRESSED YOUR IDEA CHANGED AND THEREFORE SO DID THE ERDS AND TALK ABOUT ONE TO MANY OR MANY TO MANY ETC
CI PIPELINE

#### ERD
Below is 2 entity relationship diagrams (ERD) which shows the structure of the database I am using. The first ERD is my original ERD however as my project progressed I chose certain things to not implement into my app, so therefore the second ERD is my final ERD for my app as it includes everything I implemented.

![alt text](https://github.com/Armanhafiz4/Fundamental-project/blob/main/Original%20ERD%20Diagram.png) 


My old ERD is above where I had a many to many ERD


![alt_text](https://github.com/Armanhafiz4/Fundamental-project/blob/main/ERD%20new%20Diagram.png)


My new ERD is above which is more simplified and is just a one to many ERD

#### CI Pipeline

### Project Tracking
TALK ABOUT USER STORIES AND MENTION THEM

I tracked my progress using a trello board which is made [here](https://trello.com/b/ihNNyfj3/qa-fundamental-project). This trello board was made using user stories and descriptions and coloured tabs to designate the epics and documentations etc 
<br><br>
![image](https://user-images.githubusercontent.com/74771197/103489502-db415c80-4e0c-11eb-8e31-b97b1b835a4e.png)


### Risk Assessment
TALK ABOUT HOW AS YOU PROGRESSED THROUGH THE PROJECT SO DID THE RISKS

My risk assessment table:

![image](https://user-images.githubusercontent.com/74771197/103491155-3ed18700-4e19-11eb-8cbd-e694ebf70e1d.png)


![image](https://user-images.githubusercontent.com/74771197/103492775-22d3e280-4e25-11eb-97af-c14bb9c07876.png)


### Testing
TALK ABOUT UNIT TESTING AND WHAT ITS USED FOR AND TALK ABOUT EACH SCREENSHOT
ALSO TALK ABOUT THE 94% AND MENTION HOW YOU USED MISSING TERMS
ALSO POSSIBLY SELENIUM CHROMIUMDRIVE INTEGRATION TESTING

![image](https://user-images.githubusercontent.com/74771197/103464355-f045bf00-4d2a-11eb-938e-396fef918d83.png)
<br><br>
![image](https://user-images.githubusercontent.com/74771197/103464362-14090500-4d2b-11eb-8a40-d865d1268046.png)
<br><br>
![image](https://user-images.githubusercontent.com/74771197/103464375-208d5d80-4d2b-11eb-936b-b0d471b1892a.png)
<br><br>
![image](https://user-images.githubusercontent.com/74771197/103489423-5eae7e00-4e0c-11eb-81bb-4935c4e83e44.png)


### Build
JENKINS
![image](https://user-images.githubusercontent.com/74771197/103557342-f367b900-4eaa-11eb-83b0-125b872b7789.png)

![image](https://user-images.githubusercontent.com/74771197/103557405-0e3a2d80-4eab-11eb-99da-ec7e17a99636.png)




### Front-End Design
EXPLAIN EACH STEP AND HOW YOU USED FLASK WITH ROUTES AND MODELS ETC ETC. TALK ABOUT CRUD AND HOW UPDATING COULD HAVE GONE BETTER

![image](https://user-images.githubusercontent.com/74771197/103464266-40705180-4d2a-11eb-90fb-1c540a885e5b.png) 
<br><br>
![image](https://user-images.githubusercontent.com/74771197/103464288-6c8bd280-4d2a-11eb-9935-2081387385cb.png)
<br><br>
![image](https://user-images.githubusercontent.com/74771197/103464298-7dd4df00-4d2a-11eb-89ef-8eb4dc7c2b27.png)
<br><br>
![image](https://user-images.githubusercontent.com/74771197/103464309-8a593780-4d2a-11eb-87b6-cc17d3c0917e.png)
<br><br>
![image](https://user-images.githubusercontent.com/74771197/103464331-ad83e700-4d2a-11eb-95bb-441c319f760a.png)
<br><br>
![image](https://user-images.githubusercontent.com/74771197/103464337-bb396c80-4d2a-11eb-8402-6b71b357ac49.png)


### Known Issues
TALK ABOUT UPDATE FUNCTION AND READ FUNCTION. JENKINS POSSIBLY

### Future Improvements
JENKINS POSSIBLY
SELENIUM INTEGRATION TESTING
MISSING TERMS TO GET 100% COVERAGE
UPDATE AND READ FUNCTION

### Acknowledgements

### Authors
