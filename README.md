# Full Stack API Trivia

Udacity is invested in creating bonding experiences for its employees and students. A bunch of team members got the idea to hold trivia on a regular basis and created a webpage to manage the trivia app and play the game.<br> 
The application does:

1. Display questions - both all questions and by category. Questions should show the question, category and difficulty rating by default and can show/hide the answer.
2. Delete questions.
3. Add questions and require that they include question and answer text.
4. Search for questions based on a text query string.
5. Play the quiz game, randomizing either all questions or within a specific category.

This project is a part of Udacity [Full-stack Nanodegree program](https://www.udacity.com/course/full-stack-web-developer-nanodegree--nd0044).

All backend code follows [PEP8 style guidelines](https://www.python.org/dev/peps/pep-0008/). 

## About the Stack

### Frontend
The `./frontend` directory contains a complete React frontend to consume the data from the Flask server. 

### Installing dependencies for the Frontend

**Installing Node and NPM**
This project depends on Node.js and Node Package Manager (NPM). Before continuing, you must download and install Node (the download includes NPM) from https://nodejs.com/en/download.

This project uses NPM to manage software dependencies. NPM Relies on the `package.json` file located in the frontend directory of this repository. 

From the frontend folder, run the following commands to start the client: 
```
npm install // only once to install dependencies
npm start 
```

By default, the frontend will run on `localhost:3000`.

### Backend
The `./backend` directory contains Flask and SQLAlchemy server. `__init__.py` defines your endpoints and can reference `models.py` for DB and SQLAlchemy setup.

### Installing Dependencies for the Backend

1. **Python 3.7** - Follow instructions to install the latest version of python for your platform in the [python docs](https://docs.python.org/3/using/unix.html#getting-and-installing-the-latest-version-of-python)

2. **Virtual Enviornment** - We recommend working within a virtual environment whenever using Python for projects. This keeps your dependencies for each project separate and organaized. Instructions for setting up a virual enviornment for your platform can be found in the [python docs](https://packaging.python.org/guides/installing-using-pip-and-virtual-environments/)

3. **PIP Dependencies** - Once you have your virtual environment setup and running, install dependencies by naviging to the `/backend` directory and running:
```bash
pip install -r requirements.txt
```
This will install all of the required packages we selected within the `requirements.txt` file.

4. **Key Dependencies**
 - [Flask](http://flask.pocoo.org/)  is a lightweight backend microservices framework. Flask is required to handle requests and responses.

 - [SQLAlchemy](https://www.sqlalchemy.org/) is the Python SQL toolkit and ORM we'll use handle the lightweight sqlite database. You'll primarily work in app.py and can reference models.py. 

 - [Flask-CORS](https://flask-cors.readthedocs.io/en/latest/#) is the extension we'll use to handle cross origin requests from our frontend server. 


### Database Setup
With Postgres running, restore a database using the `trivia.psql` file provided. From the backend folder in terminal run:
```bash
psql trivia < trivia.psql
```

### Running the server

From within the `./src` directory first ensure you are working using your created virtual environment.

To run the server, execute:

```bash
flask run --reload
```

The `--reload` flag will detect file changes and restart the server automatically.


### Testing 

In order to run tests navigate to the backend folder and run the following commands:
```bash
dropdb trivia_test
createdb trivia_test
psql trivia_test < trivia.psql
python test_flaskr.py
```
The first time you run the tests, omit the dropdb command. 

All tests are kept in that file and should be maintained as updates are made to app functionality. 


## API Reference

### Getting Started
- Base URL: At present this app can only be run locally and is not hosted as a base URL. The backend app is hosted at the default, `http://127.0.0.1:5000/`, which is set as a proxy in the frontend configuration. 
- Authentication: This version of the application does not require authentication or API keys. 

### Error Handling
Errors are returned as JSON objects in the following format:
```
{
    "success": False, 
    "error": 400,
    "message": "bad request"
}
```

The API will return three error types when requests fail:
- 400: Bad Request
- 404: Resource Not Found
- 422: Not Processable 
- 500: Internal Server Error

### Endpoints 

#### GET /categories
- General:
    - Returns a dictionary of categories in which keys are ids and values are corresponding strings of categories.
    - Request arguments: None.
    - Returns: An object with keys:
      - `success`: The success flag
      - `categories`: Contains an object of `id:category_string` and `key:value`. 
- Sample: `curl http://127.0.0.1:5000/categories`

``` 
{
    "success": True,
    "categories": {
        "1": "Science",
        "2": "Art",
        "3": "Geography",
        "4": "History",
        "5": "Entertainment",
        "6": "Sports"
    }
}
```

#### GET /questions
- General:
    - Fetches a list of questions, number of total questions, current category, and a dictionary of categories.
    - Results are paginated in groups of 10. Include a request argument to choose page number, starting from 1.
    - Request arguments: `page`(integer), a current page.
    - Returns an object with keys: `success` (the success flag), `questions` (a list of questions, paginated by 10),
    `categories` (a dictionary of categories), `total_questions` (number of total questions), `current_category`.
- Sample: `curl http://127.0.0.1:5000/questions`

```
{
  "categories": {
    "1": "Science", 
    "2": "Art", 
    "3": "Geography", 
    "4": "History", 
    "5": "Entertainment", 
    "6": "Sports"
  }, 
  "current_category": null, 
  "questions": [
    {
      "answer": "Maya Angelou", 
      "category": 4, 
      "difficulty": 2, 
      "id": 5, 
      "question": "Whose autobiography is entitled 'I Know Why the Caged Bird Sings'?"
    }, 
    {
      "answer": "Edward Scissorhands", 
      "category": 5, 
      "difficulty": 3, 
      "id": 6, 
      "question": "What was the title of the 1990 fantasy directed by Tim Burton about a young man with multi-bladed appendages?"
    }, 
    {
      "answer": "Muhammad Ali", 
      "category": 4, 
      "difficulty": 1, 
      "id": 9, 
      "question": "What boxer's original name is Cassius Clay?"
    }, 
    {
      "answer": "Brazil", 
      "category": 6, 
      "difficulty": 3, 
      "id": 10, 
      "question": "Which is the only team to play in every soccer World Cup tournament?"
    }, 
    {
      "answer": "Uruguay", 
      "category": 6, 
      "difficulty": 4, 
      "id": 11, 
      "question": "Which country won the first ever soccer World Cup in 1930?"
    }, 
    {
      "answer": "George Washington Carver", 
      "category": 4, 
      "difficulty": 2, 
      "id": 12, 
      "question": "Who invented Peanut Butter?"
    }, 
    {
      "answer": "Lake Victoria", 
      "category": 3, 
      "difficulty": 2, 
      "id": 13, 
      "question": "What is the largest lake in Africa?"
    }, 
    {
      "answer": "The Palace of Versailles", 
      "category": 3, 
      "difficulty": 3, 
      "id": 14, 
      "question": "In which royal palace would you find the Hall of Mirrors?"
    }, 
    {
      "answer": "Agra", 
      "category": 3, 
      "difficulty": 2, 
      "id": 15, 
      "question": "The Taj Mahal is located in which Indian city?"
    }, 
    {
      "answer": "Escher", 
      "category": 2, 
      "difficulty": 1, 
      "id": 16, 
      "question": "Which Dutch graphic artist\u2013initials M C was a creator of optical illusions?"
    }
  ], 
  "success": true, 
  "total_questions": 20
}
```

#### DELETE /questions/<question_id>
- General:
    - Request arguments: `question_id` (integer)
    - Deletes the question of the given ID if it exists. Returns the id of the deleted question and success value
- Sample: `curl -X DELETE http://127.0.0.1:5000/questions/13?page=2`
```
{
    "deleted": 1,
    "success": true
}
```

#### POST /questions
- General:
    - Creates a new question using the question and answer text, category, and difficulty score.
    - Request arguments: `question` (string), `answer` (string), `difficulty` (string), `category` (string).
    - Returns the id of the created question and success value 
- Sample: `curl http://127.0.0.1:5000/questions?page=2 -X POST -H "Content-Type: application/json" -d '{"question":"What is the title of the first movie?", "answer":"Roundhay Garden Scene", "difficulty":"5", "category":"Entertainment"}'`
```
{
  "success": true,
  "created": 20
}
```

#### GET /categories/<category_id>/questions
- General:
    - Fetches a list of questions based on category.
    - Request arguments: `category_id` (integer).
    - Returns an object with keys: `success` (the success flag), `questions` (a list of questions, paginated by 10 items),
    `total_questions` (number of total questions), `current_category`.
- Sample: `curl http://127.0.0.1:5000/categories/4/questions`

{
    "success": true,
    "questions": [
        {
            "answer": "Brazil",
            "category": 6,
            "difficulty": 3,
            "id": 10,
            "question": "Which is the only team to play in every soccer World Cup tournament?"
        },
        {
            "answer": "Uruguay",
            "category": 6,
            "difficulty": 4,
            "id": 11,
            "question": "Which country won the first ever soccer World Cup in 1930?"
        },

    ],
    "total_questions": 10,
    "current_category": 6
}

#### POST /search
- General:
    - Retrieves questions based on a search term.
    - Request arguments: `search_term` (the term to search).
    - Returns an object with keys: `success` (the success flag), `questions` (a list of questions),
    `total_questions` (number of total questions), `current_category`.

{
    "success": true,
    "questions": [
        {
            "answer": "Brazil",
            "category": 6,
            "difficulty": 3,
            "id": 10,
            "question": "Which is the only team to play in every soccer World Cup tournament?"
        },
        {
            "answer": "Uruguay",
            "category": 6,
            "difficulty": 4,
            "id": 11,
            "question": "Which country won the first ever soccer World Cup in 1930?"
        },

    ],
    "total_questions": 10,
    "current_category": null
}

#### POST /quizzes
- General:
    - Fetches one random question within a specified category.
    - Request arguments: `quiz_category` (dictionary, the quiz category with the type and id), `previous_questions` (a list of the previous questions ids).
    - Returns an object with keys: `success` (the success flag), `question` (a random question to play the quiz).

{
    "answer": "Tom Cruise",
    "category": 5,
    "difficulty": 4,
    "id": 4,
    "question": "What actor did author Anne Rice first denounce, then praise in the role of her beloved Lestat?"
}
