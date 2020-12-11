# Full Stack Trivia API Backend

## Getting Started

### Installing Dependencies

#### Python 3.7

Follow instructions to install the latest version of python for your platform in the [python docs](https://docs.python.org/3/using/unix.html#getting-and-installing-the-latest-version-of-python)

#### Virtual Enviornment

We recommend working within a virtual environment whenever using Python for projects. This keeps your dependencies for each project separate and organaized. Instructions for setting up a virual enviornment for your platform can be found in the [python docs](https://packaging.python.org/guides/installing-using-pip-and-virtual-environments/)

#### PIP Dependencies

Once you have your virtual environment setup and running, install dependencies by naviging to the `/backend` directory and running:

```bash
pip install -r requirements.txt
```

This will install all of the required packages we selected within the `requirements.txt` file.

##### Key Dependencies

- [Flask](http://flask.pocoo.org/)  is a lightweight backend microservices framework. Flask is required to handle requests and responses.

- [SQLAlchemy](https://www.sqlalchemy.org/) is the Python SQL toolkit and ORM we'll use handle the lightweight sqlite database. You'll primarily work in app.py and can reference models.py. 

- [Flask-CORS](https://flask-cors.readthedocs.io/en/latest/#) is the extension we'll use to handle cross origin requests from our frontend server. 

## Database Setup
With Postgres running, restore a database using the trivia.psql file provided. From the backend folder in terminal run:
```bash
psql trivia < trivia.psql
```

## Running the server

From within the `backend` directory first ensure you are working using your created virtual environment.

To run the server, execute:

```bash
export FLASK_APP=flaskr
export FLASK_ENV=development
flask run
```

Setting the `FLASK_ENV` variable to `development` will detect file changes and restart the server automatically.

Setting the `FLASK_APP` variable to `flaskr` directs flask to use the `flaskr` directory and the `__init__.py` file to find the application. 

## API Referance
### Getting Started
- BaseUrl : at the present the this app can locally at ``` http://127.0.0.1:5000 ```
- Authentication : this version of the appliaction does not require authentication or api keys
### Error Handling
Errors are returned as Json objects Example
``` 
{
"error": 405,
"message": "The method is not allowed for the requested URL.",
"success": false
}
```
The Api Contain The Following Errors
- 422 -> Unprocessed [ Cannot do This Action ]
- 404 -> Not Found
- 400 -> Bad Request
- 422 -> Unprocessed

### EndPoints

### POST '/quizzes'
- General
    - Returns one of the randomly chosen questions in the given category and success value.
    - If `previous_questions` is provided in request body, they are excluded from selecting process. 
    - `question` is returned as `null` if there is no more questions which has not previously played in the category. 
- Sample 

`curl -X POST http://127.0.0.1:5000/quizzes -H "Content-Type: application/json" -d '{"quiz_category":{"type":"Science","id":1},"previous_questions":[20]}'`  

```
{
    "question": {
        "answer": "Blood",
        "category": 1,
        "difficulty": 4,
        "id": 22,
        "question": "Hematology is a branch of medicine involving the study of what?"
    }
}
```




#### GET /questions
- General
    - Return a List Of Questions with List Of Categories ,total_questions, Question
    - Result are paginated into a groups of 10 . Include a request argument to choose page number,page size
    - Error of status code 404 is thrown when there is not question on the given page.
- Sample
    - ``` curl -X GET http://127.0.0.1:5000/questions ```    
```
{
  "categories": [
    {
      "id": 1,
      "type": "Science"
    },
    {
      "id": 2,
      "type": "Art"
    },
    {
      "id": 3,
      "type": "Geography"
    },
    {
      "id": 4,
      "type": "History"
    },
    {
      "id": 5,
      "type": "Entertainment"
    },
    {
      "id": 6,
      "type": "Sports"
    }
  ],
  "current_category": null,
  "questions": [
    {
      "answer": "Tom Cruise",
      "category": 5,
      "difficulty": 4,
      "id": 4,
      "question": "What actor did author Anne Rice first denounce, then praise in the role of her beloved Lestat?"
    },
    {
      "answer": "Edward Scissorhands",
      "category": 5,
      "difficulty": 3,
      "id": 6,
      "question": "What was the title of the 1990 fantasy directed by Tim Burton about a young man with multi-bladed appendages?"
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
    },
    {
      "answer": "Mona Lisa",
      "category": 2,
      "difficulty": 3,
      "id": 17,
      "question": "La Giaconda is better known as what?"
    },
    {
      "answer": "One",
      "category": 2,
      "difficulty": 4,
      "id": 18,
      "question": "How many paintings did Van Gogh sell in his lifetime?"
    },
    {
      "answer": "Jackson Pollock",
      "category": 2,
      "difficulty": 2,
      "id": 19,
      "question": "Which American artist was a pioneer of Abstract Expressionism, and a leading exponent of action painting?"
    }
  ],
  "total_questions": 20
}

```
#### Post /questions
- General
  - Creates a new question using the submitted question, answer, difficulty and category. All the parameters are required. Returns the created question and success value
- Sample 
```
curl -X POST http://127.0.0.1:5000/questions -H "Content-Type: application/json" -d '{"question":"Best Player in The World?","answer":"Ronaldo","difficulty":4,"category":1}'
```    

```
{
    "question": {
        "answer": "Ronaldo",
        "category": 1,
        "difficulty": 3,
        "id": 35,
        "question": "Best Player in The World?"
    }
}
```
#### Post /search/question
- General
   - If search_term is included in request body, the result of search for questions based on the given search term is returned, which returns a list of matched questions, success value, total number of result, and current category as null
   - Error of status code 404 is thrown when there is not question on the given page.
- Sample 
```
curl -X POST http://127.0.0.1:5000/questions -H "Content-Type: application/json" -d '{"searchTerm":"question"}'
```    

```
{
    "current_category": null,
    "questions": [
        {
            "answer": "Ronaldo",
            "category": 1,
            "difficulty": 3,
            "id": 35,
            "question": "Best Player in The World?"
        }
    ],
    "total_questions": 1
}}
```

### DELETE '/questions/`question_id`'
- General
    - Deletes the question of the given ID if it exists. Returns {} when deleted
    - If the question of the given ID does not exist, error of status code 422 is returned.
- Sample 

`curl -X DELETE http://127.0.0.1:5000/questions/1`  

```
{}
```





```    
1. Use Flask-CORS to enable cross-domain requests and set response headers. 
2. Create an endpoint to handle GET requests for questions, including pagination (every 10 questions). This endpoint should return a list of questions, number of total questions, current category, categories. 
3. Create an endpoint to handle GET requests for all available categories. 
4. Create an endpoint to DELETE question using a question ID. 
5. Create an endpoint to POST a new question, which will require the question and answer text, category, and difficulty score. 
6. Create a POST endpoint to get questions based on category. 
7. Create a POST endpoint to get questions based on a search term. It should return any questions for whom the search term is a substring of the question. 
8. Create a POST endpoint to get questions to play the quiz. This endpoint should take category and previous question parameters and return a random questions within the given category, if provided, and that is not one of the previous questions. 
9. Create error handlers for all expected errors including 400, 404, 422 and 500. 

REVIEW_COMMENT
```
This README is missing documentation of your endpoints. Below is an example for your endpoint to get all categories. Please use it as a reference for creating your documentation and resubmit your code. 

Endpoints
GET '/categories'
GET ...
POST ...
DELETE ...

### GET '/categories'
- Fetches a dictionary of categories in which the keys are the ids and the value is the corresponding string of the category
- Request Arguments: None
- Returns: An object with a single key, categories, that contains a object of id: category_string key:value pairs. 
``` 
{
    "categories": [
        {
            "id": 1,
            "type": "Science"
        },
        {
            "id": 2,
            "type": "Art"
        },
        {
            "id": 3,
            "type": "Geography"
        },
        {
            "id": 4,
            "type": "History"
        },
        {
            "id": 5,
            "type": "Entertainment"
        },
        {
            "id": 6,
            "type": "Sports"
        }
    ]
}
```
### GET '/categories/{ct_id}/questions'
- Fetches a dictionary of questions to specific category  `ct_id`
``` 
{
    "current_category": 1,
    "questions": [
        {
            "answer": "The Liver",
            "category": 1,
            "difficulty": 4,
            "id": 20,
            "question": "What is the heaviest organ in the human body?"
        },
        {
            "answer": "Alexander Fleming",
            "category": 1,
            "difficulty": 3,
            "id": 21,
            "question": "Who discovered penicillin?"
        },
        {
            "answer": "Blood",
            "category": 1,
            "difficulty": 4,
            "id": 22,
            "question": "Hematology is a branch of medicine involving the study of what?"
        },
        {
            "answer": "yes",
            "category": 1,
            "difficulty": 5,
            "id": 25,
            "question": "Mario love marina ?"
        },
        {
            "answer": "yes",
            "category": 1,
            "difficulty": 5,
            "id": 26,
            "question": "Mario love marina ?"
        },
        {
            "answer": "yes",
            "category": 1,
            "difficulty": 5,
            "id": 27,
            "question": "Mario love marina ?"
        },
        {
            "answer": "yes",
            "category": 1,
            "difficulty": 5,
            "id": 28,
            "question": "Mario love marina ?"
        },
        {
            "answer": "OK",
            "category": 1,
            "difficulty": 3,
            "id": 34,
            "question": "??"
        },
        {
            "answer": "Ronaldo",
            "category": 1,
            "difficulty": 3,
            "id": 35,
            "question": "Best Player in The World?"
        }
    ],
    "total_questions": 9
}
```



## Testing
To run the tests, run
```
dropdb trivia_test
createdb trivia_test
psql trivia_test < trivia.psql
python test_flaskr.py
```