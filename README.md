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

#### CI Pipeline

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
My first risk assessment table 

### Testing
TALK ABOUT UNIT TESTING AND WHAT ITS USED FOR AND TALK ABOUT EACH SCREENSHOT
ALSO TALK ABOUT THE 84% AND MENTION HOW YOU USED MISSING TERMS

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

![image](https://user-images.githubusercontent.com/74771197/103574785-73e8e280-4ec8-11eb-9cc9-5fe6e8bcde95.png)




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
TALK ABOUT UPDATE FUNCTION AND READ FUNCTION. Add function was faulty

### Future Improvements
SELENIUM INTEGRATION TESTING
MISSING TERMS TO GET 100% COVERAGE
Add FUNCTION

### Acknowledgements

### Authors
Arman Hafiz
