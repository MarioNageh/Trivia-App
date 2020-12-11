from flask import Blueprint, request, jsonify, abort
from sqlalchemy.sql.expression import func

from db import Question, Category
from flaskr.utils import helper


quizzes = Blueprint('quizzes', __name__)
helperUtils = helper()


@quizzes.route('/quizzes', methods=['POST'])
def create_quizze():
    requestBody = request.get_json()
    previous_questions = requestBody['previous_questions']
    quiz_category = requestBody['quiz_category']
    if not quiz_category:
        return abort(400, 'Bad Request')
    category_id = int(quiz_category['id'])

    # getting Question That Not included in PreviousQuestion and same Category
    # func.random() to get random rows and get first select
    question = []
    if category_id != 0:
        question = Question.query.filter(Question.category == category_id,
                                         ~Question.id.in_(
                                             previous_questions)).order_by(
                                                func.random()).first()
    else:
        question = Question.query.filter(~Question.id.in_(
                                             previous_questions)).order_by(
                                                func.random()).first()
    return jsonify({'question': question.format()} if question else {})
    pass
