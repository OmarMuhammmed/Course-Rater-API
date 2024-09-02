
# Course Rater API

Course Rater API is a RESTful API that allows users to rate and review courses. The project aims to provide a system where users can evaluate courses, helping others make informed decisions about whether to enroll in a particular course.

## Features

- **Add Courses:** Users can add new course information.
- **Rate Courses:** Users can rate and review courses.
- **View Ratings:** Users can view course ratings and reviews.
- **Manage Ratings:** Administrators can manage course ratings and reviews.
- **Custom Permissions:** Admin only list users and user olny edit your pofile .
- **auth With Token :** can user Login with token genrated by system  .


## Requirements

- Python 3.8 or higher
- Django 4.x
- Django REST Framework
- SQLite3 (you can switch to PostgreSQL for production)

## Local Setup

Follow these steps to set up and run the project locally:

1. **Clone the repository:**

   ```bash
   git clone https://github.com/OmarMuhammmed/Course-Rater-API.git
   cd Course-Rater-API
   ```

2. **Create and activate a virtual environment:**

   ```bash
   python -m venv venv
   
   venv\Scripts\activate
   ```

3. **Install the dependencies:**

   ```bash
   pip install -r requirements.txt
   ```

4. **Set up the database:**

   ```bash
   python manage.py migrate
   ```

5. **Run the local server:**

   ```bash
   python manage.py runserver
   ```

   You can access the API at `http://127.0.0.1:8000/`.

