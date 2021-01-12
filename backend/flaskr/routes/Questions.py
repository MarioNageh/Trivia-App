import json

from flask import Blueprint, request, jsonify, Response, abort

from db import Question, Category
from flaskr.utils import helper
questions = Blueprint('questions', __name__)
helperUtils = helper()


@questions.route('/search/question', methods=['POST'])
def search_question():
    try:
        requestBody = request.get_json()
        searchTerm = requestBody['searchTerm']\
            if requestBody is not None \
            and 'searchTerm' in requestBody else ''

        if searchTerm or searchTerm == '':
            #   Here We Will Search
            questions = Question.query.filter(
                Question.question.ilike
                ('%{}%'.format(searchTerm))).all()
            return jsonify({
                'questions': [q.format() for
                              q in helperUtils.paganation
                              (request, questions)],
                'total_questions': len(questions),
                'current_category': None
            })
    except Exception as e:
        print(e)
        abort(422, 'Unprossable')


@questions.route('/questions', methods=['POST'])
def add_new_question():
    requestBody = request.get_json()
    question = ''
    difficulty = ''
    category = ''
    answer = ''
    try:
        question = requestBody['question']
        difficulty = requestBody['difficulty']
        category = requestBody['category']
        answer = requestBody['answer']
    except Exception as e:
        print(e)
        # Error During Parsing The Json
        abort(422, 'incorrect body')
    if not (question and difficulty and category and answer):
        # Error Missing Params data
        abort(400, 'bad request')
    else:
        question = Question(question, answer, category, difficulty)
        question.insert()
        return jsonify({
            'question': question.format()
        })


@questions.route('/questions', methods=['GET'])
def get_questions():
    questions = Question.query.all()
    if len(questions) == 0:
        abort(404, 'Not Found')
    return jsonify({
        'questions': [q.format()
                      for q
                      in helperUtils.paganation(request, questions)],
        'total_questions': len(questions),
        'categories': [cat.format() for cat in Category.query.all()],
        'current_category': None
    })


@questions.route('/questions/<int:question_id>', methods=['DELETE'])
def delete_question(question_id):
    try:
        question = Question.query.filter(
            Question.id == question_id).one_or_none()
        if question is None:
            abort(404, 'Not Found')
        question.delete()
        return jsonify({}), 200
    except Exception as e:
        print(e)
        abort(422, ' Cannot delete question ')
