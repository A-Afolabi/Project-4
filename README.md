# General Assembly Project 4 - Horse Outdoors

## Project Overview

Horse Outdoors was the fourth and final project of General Assembly’s Software Engineering Immersive course. This project required us to build a full-stack application using **Python Django API** and using **Django REST Framework**. With a combination of everything we had learnt throughout the course, we had 9 days to do the project before presenting it to our instructors and peers. This project built upon some of the things I had previously done in other projects, and I decided to take the opportunity to experience working in a pair for the first time with [Elena Gicheva](https://github.com/ElenaGicheva/).

The two of us settled on the idea of a horse-riding vacation app. This would allow users to view horse riding vacations in different locations worldwide, post reviews and more. We chose this for our project due to the vast amount of ideas and things we wanted to implement, however, we had to reduce the amount we wanted due to time constraints. Choosing to work in a pair rather than a group was a decision I was adamant about. I enjoyed working in a group for my last project but I was keen to put myself in a position where I would learn more from struggling through problems before coming up with solutions.


## Deployed Project

[Horse Outdoors](https://horseoutdoors.herokuapp.com/)


## Brief

* Build a full-stack application by making your own backend and your own front-end.
* Use a Python Django API using Django REST Framework to serve your data from a Postgres database.
* Consume your API with a separate front-end built with React.
* Be a complete product with multiple relationships and CRUD functionality for at least two models.


## Concept

Seeing how well an extensive plan did for my third project, I insisted that the same amount of detail went into this project. Doing an extensive plan helped both of us eliminate some of our ideas straight away, due to only having 9 days to complete the project. After writing down a few things between us, we moved on to the wireframe where we could really put the workings and usability of the app together.

Horse Outdoors is intended to be a place where a user can view different horse riding holidays and activities in different countries around the world. As well as this, users will be able to post reviews on destinations, log in and out, add an event, and have their own profile page.


## Technologies Used

#### Front-end:
* HTML
* CSS/SCSS
* JavaScript (ES6)
* React
* JSX
* Axios
* Google Font
#### Back-end:
* Python
* Django
* Python REST Framework
* Pyjwt
* PostgreSQL
* Psycopg2
#### Development Tools:
* VS code
* Insomnia
* Git & GitHub
* Zoom
* Slack
* Trello
* Excalidraw
* Heroku


## Approach Taken

### Day 1-2
#### Planning
The two of us exchanged some ideas for our app and reviewed how other vacation websites have been done. After doing so we moved straight on to our wireframe. 

The wireframe helped us both combine our ideas and get a real sense of feeling for how the website would look and work. Here we were able to eliminate some of our ideas from the start due to time constraints, but still had a lot of work to try and achieve within it.

![Screenshot 2023-02-28 at 14 09 51](https://user-images.githubusercontent.com/95321738/221878516-93840c8d-93bb-42cb-b3b0-d113b5ce62dd.png)

Upon completion of the wireframe via Excalidraw, we used it as a reference while building out our model relationships. This was done using the Entity Relationship Diagram below, although challenging to visually understand as it was very new to us, the time spent on doing so helped when we started the back-end. The ERD helped us decide to use tags in our project, this was due to the ability of the relationship to be a many-to-many one. The ERD helped show all the relationships, either many-to-many or one-to-many, as well as some of the data within each app.

![Screenshot 2023-02-28 at 14 12 11](https://user-images.githubusercontent.com/95321738/221879042-52fcd162-92f5-43b7-9293-24455a9d25c4.png)

After completing our ERD we then made a quick Trello board which we would use during the project to add all ideas and tick off what we could achieve within the timeframe. This was not simply limited to features that would be added, but also what we were doing to help with our understanding of Django. This enabled us to keep track of what the other one was doing and potentially help.

![Screenshot 2023-02-28 at 14 14 40](https://user-images.githubusercontent.com/95321738/221879701-67fade36-633f-4054-936c-8cb75e8524ff.png)


### Day 3-6
#### Back-end
Having some prior knowledge of SQL before the course felt very beneficial to me when using the PostgreSQL database. Despite this, like many others on our course, we ran into problems trying to build out our backend in Django. This was mostly due to still understanding Django and the workings and use of things such as Serializer. Fortunately, most issues were easy to understand when explained and some were rectified quite quickly between the two of us. However, due to this, building out our backend took longer than we had originally planned for and therefore impacted what we felt was both achievable, and realistic on the front-end.

#### Models
Our backend consisted of 5 apps, continents, destinations, jwt_auth, reviews and tags. When going through each app, we started with the models and were not met with any real issues when building them. The foreign keys were used as a reference when creating relationships between models in different apps.

![Screenshot 2023-02-28 at 14 18 59](https://user-images.githubusercontent.com/95321738/221880769-1eac1063-38fd-40fc-9791-d075d387e320.png)

#### Serializers
Once this was done we moved on to our serializers. These were used for each of our apps in order for Django to be able to communicate with our PostgreSQL database. The serializers enable our seeded data to be read by JavaScript on the front-end. With our data being stored in JSON format, the serializer would convert and store the data in our database correctly, as well as retrieve data correctly. When we created the serializers, we created both `.common` and `.populated` files with the models they have a relationship with, as shown below for our Destination Serializer.

![Screenshot 2023-02-28 at 14 20 45](https://user-images.githubusercontent.com/95321738/221881257-d7450ce6-c59f-455f-a0f5-5f124e75d041.png)

#### Views
Our `views.py` file was where we implemented Django REST Framework to add CRUD functionality when making requests to our database. The serializers were used here to convert the data returned. Once created we would then test the requests within Insomnia, with the admin checking we were getting back the correct JSON responses.

![Screenshot 2023-02-28 at 14 23 27](https://user-images.githubusercontent.com/95321738/221881943-25c2aa5b-de43-4a36-991f-4bf0767dea59.png)

![Screenshot 2023-02-28 at 14 26 04](https://user-images.githubusercontent.com/95321738/221882669-e5b34f50-3eaf-4bfb-b7c6-56286a64de31.png)

#### Authentication
In order for us to add authentication, we made an `authentication.py` file inside of our jwt_auth app, where we defined a function that extended the Basic Authentication from the Django REST Framework, with the use of JSON Web Token to decode it.

This also meant adding validation functions for our UserSerializer to ensure the hash passwords of the users are correct.


### Day 7-9
#### Front-end
As the back-end took longer than we had anticipated, it ate into our front-end time and we quickly decided on how we would prioritise things. With our back-end complete, we knew in the future we could return and implement more of what we wanted after the project deadline.

Despite the limited time, we decided to first start working on the homepage together, before splitting up and working on individual pages. The home page was fairly straightforward once we used `axios.get` to retrieve the continent data from our API. After this we pulled the data we wanted from the continent and formed it as part of a card. After completing the home page, we split up to work on individual pages. This was done while both on zoom and able to call on the other if needed. I worked on the Destinations page, Destination page, App.js page for the routes and SiteNave page. I was also able to help out with parts of the Register and Login page.

Once the continent was selected, I then had to filter the destinations to only show those that matched the same continent `id`. This would then only present the destinations that matched in a card as shown below.

![Screenshot 2023-02-28 at 14 30 48](https://user-images.githubusercontent.com/95321738/221883976-b0d2529f-0037-40c0-9333-738b22cca921.png)

![Screenshot 2023-02-28 at 14 31 37](https://user-images.githubusercontent.com/95321738/221884204-01d2b2e4-5388-4052-8798-a4c53183efb7.png)

Our destination page used two different `axios.get` requests, one for the destination chosen and the other for the reviews on our API that already exist. In order to get the reviews for each specific location, we used the `id` of the destination which would have a relationship with the reviews. This meant that only reviews which also matched the destination `id` would appear on the relevant destinations page. This was all done within our `handleReviewSubmit` function where we also ensured new reviews, via a POST request, would be submitted in the right place. The user would also need to be logged in and authenticated in order to submit a review.

![Screenshot 2023-02-28 at 14 35 03](https://user-images.githubusercontent.com/95321738/221885101-5e5ad8e2-e324-4184-bd43-bd5b31fb4704.png)

This then gave us the following review section which allowed us to show multiple reviews relating to the specific destination and post a review, as long as we were logged in, on the correct destination page.

![Screenshot 2023-02-28 at 14 36 22](https://user-images.githubusercontent.com/95321738/221885452-7dfaa5e7-2c51-4354-ae9b-640e40fb1c7f.png)

In terms of authentication on the front-end, we used an auth.js file that would get the token from the local storage and check if it matches our format, then return it back in JSON format. After this, the payload would be checked to make sure it both exists and is still valid with the expiry date we set for the token.

![Screenshot 2023-02-28 at 14 38 26](https://user-images.githubusercontent.com/95321738/221886018-d22f5f3d-82e9-47be-9f72-ec8bf8c7225f.png)

When we reached the deadline of our project, a few of the functions and some of the styling were not yet completed. I spent some time after presenting what we had done so far, to complete the project, in terms of fixing some of the functionality and improving the styling. This is to the point I am currently content with before planning to go back and truly bring the project to where it was envisioned to be.

I chose to work in a pair as opposed to a group to really push myself through difficult moments that would arise, and find solutions to them more independently. Although help was always available if needed, I found I was able to find answers to things through a much-improved ability to google and go through notes I had made on my front-end. The project also enabled me to learn a lot more as I took on more responsibility as each day passed.


## Wins

* Despite the difficulties found with Django, I managed to understand and resolve a lot of the issues together.
  * The two of us found Django a bit tricky partly due to having taken so much information in while doing the course. Going over things again did help and eventually, things became easier to understand and implement.
* Improvement in my ability while writing JavaScript.
  * I wasn’t too confident in my JavaScript skills before the project as it had been a steady improvement. This project reach showed how much of an improvement I had made and was still making, as I coded out most of the front-end
* Becoming more comfortable with React.
* Working well together and taking on more responsibility during the project.
  * I was really adamant I did not work in a group, but at the same time, I was conscious of not walking solo due to both my difficulties in Django and JavaScript. I took the opportunity to do pair programming for the experience which pushed me to solve more individually. I am really happy with the progress it enabled me to make.
* The opportunity to learn and practise my newly acquired Python skills.
  * Learning Python was something I was really looking forward to, and I was happy that it did not disappoint when learning and then using it for this project.


## Challenges

* This was the first time we built a back-end project in Django Python, as such, there was a learning curve for both of us when implementing, learning and getting all the components (models, serializers, views, etc) working. However, doing this during the project really helped and is something I will be going back over to further solidify the fundamentals and understanding of Django.
* Implementing all of our ideas became something we simply could not do within the timeframe of both understanding Django having just learnt it the week prior and the duration of the project length.


## Key Learnings

* Continued improvement and understanding of Django as the project went on.
* Whenever I do a plan, I also take into consideration with more detail how long the backend could take to build, and areas of confusion.
* Having a stricter MVP and stretch goals list. This will be to the point of ensuring I do not need to go over what can be achieved and what can not during production.
* My previous knowledge of SQL helped a lot and gave me confidence going into Python which I thoroughly enjoyed. I was able to use my already-acquired knowledge of JavaScript to help.
* Building another full-stack project was less daunting and gave me the self-belief that it was achievable for me.


## Future Features

* We currently have an enquire button that does nothing due to not having enough time to implement functionality for it. The plan for this button would be to take the user to a form where they could submit their enquiry.
* Adding a profile page for the user as originally planned. This would mean changing the register fields to incorporate more data it requires.
* Making the search feature on the homepage that was originally in our wireframe.
* Further styling improvements, including a strict border on the overall page depending on screen sizing.
