# CoursesRater_API_Django

# Business requirements as per the mockup 

1- Course list screen has the foloowing information
    - Course name
    - Course number of stars 
    - Courses average rate 
    - Login 
    - Register
    - showing already logged in user 

2- Popup error if the user already rated 

3- Add rate scree, stars 1 to 5 only and SAVE


# Technical requirements 
Using Django REST frame work please implement the followings

1- Models 
    - Course
    - Stars 
    - User

2- validation if the user already rated the Course 

3- validation to rate min 1 and max 5 

4- CRUD API for Courses 
    http://127.0.0.1:8000/api/Courses
    it should return the average rating and number of rating a long with the Course name and detail

5- CRUD API for Stars 
    http://127.0.0.1:8000/api/stars
    no one should be able to use this crud for rating !!

6- Rate API 
    http://127.0.0.1:8000/api/Courses/Course_pk/rate_Course
    create and update API 

7- Token authentication 

8- Login and register API 

9- Token request API 

10- Deploy to Heroku 

