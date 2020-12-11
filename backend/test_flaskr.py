import os
import unittest
import json
from flask_sqlalchemy import SQLAlchemy

from flaskr import create_app
from db import setup_db, Question, Category


class TriviaTestCase(unittest.TestCase):
    """This class represents the trivia test case"""

    def setUp(self):
        """Define test variables and initialize app."""
        self.app = create_app()
        self.client = self.app.test_client
        self.database_name = "trivia_test"
        self.database_path = "postgres://postgres:Mario123!@#@{}/{}".format('localhost:5432', self.database_name)
        setup_db(self.app, self.database_path)

        self.new_question = {
            'question': 'What is Your Name ?',
            'difficulty': 5,
            'category': 1,
            'answer': 'Mario'
        }

        # binds the app to the current context
        with self.app.app_context():
            self.db = SQLAlchemy()
            self.db.init_app(self.app)
            # create all tables
            self.db.create_all()

        # # Init data
        # category = Category('Testing')
        # category.insert()
        # question = Question("New Testing", 'Not', category.id, 5)
        # question.insert()

    def tearDown(self):
        """Executed after reach test"""
        pass

    # Add New Question With Answer Mario
    def test_add_new_question(self):
        reques = self.client().post('/questions', json=self.new_question)
        data = json.loads(reques.data)
        self.assertEqual(data['question']['difficulty'], 5)
        self.assertEqual(data['question']['answer'], 'Mario')

    # Testing Some Nodes Doesn't Exist 422 UnProssed
    def test_add_new_question_error_incorrect_body(self):
        reques = self.client().post('/questions', json={})
        data = json.loads(reques.data)
        self.assertEqual(data['error'], 422)

    # Testing Some Node Are Null Bad Request 400
    def test_add_new_question_error_bad_reqeust(self):
        self.new_question['answer'] = None
        reques = self.client().post('/questions', json=self.new_question)
        data = json.loads(reques.data)
        self.assertEqual(data['error'], 400)

    def test_delete_question(self):
        # This Test Will Remove The Last question
        # This Test Must run after test_add_new_question Test
        lastInsertedQuestion = Question.query.order_by(Question.id.desc()).first()
        reques = self.client().delete(f'/questions/{lastInsertedQuestion.id}')
        self.assertEqual(reques.status_code, 200)

    def test_delete_question_fail(self):
        # 999999999999999999999999999999999999 Is Inavlid Id So Will Generate Error
        reques = self.client().delete(f'/questions/999999999999999999999999999999999999')
        self.assertEqual(reques.status_code, 422)

    # /categories/<int:ct_id>/questions
    def test_get_specific_question_category(self):
        #     We Will Insert New Category , New Question belong to this category and get them
        category = Category('Test')
        category.insert()
        newQuestion = Question('Test Question ?', "True", category.id, 5)
        newQuestion.insert()
        request = self.client().get(f'/categories/{category.id}/questions')
        # Remove Inserted Data
        category.delete()
        newQuestion.delete()
        data = json.loads(request.data)
        self.assertEqual(data['questions'][0]['answer'], "True")

    def test_get_categories_success(self):
        request = self.client().get('/categories')
        self.assertEqual(request.status_code, 200)

    def test_get_categories_fail(self):
        Category.query.delete()
        request = self.client().get('/categories')
        self.assertEqual(request.status_code, 404)

    def test_quizz(self):
        request = self.client().post('/quizzes', json={
            "quiz_category": {'type': 'Science', 'id': 1},
            "previous_questions": []
        })
        self.assertEqual(request.status_code, 200)
    """
    TODO
    Write at least one test for each test for successful operation and for expected errors.
    """


# Make the tests conveniently executable
if __name__ == "__main__":
    unittest.main()
