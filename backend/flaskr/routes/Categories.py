from flask import Blueprint, request, jsonify, abort
from db import Question, Category
from flaskr.utils import helper


categories = Blueprint('categories', __name__)
helperUtils = helper()


@categories.route('/categories', methods=['GET'])
def get_categories():
    catergories = Category.query.all()
    if len(catergories) == 0:
        abort(404, 'not found')
    return jsonify({
        'categories': [catergory.format()
                       for catergory
                       in helperUtils.paganation
                       (request, catergories)],
    })


@categories.route('/categories/<int:ct_id>/questions', methods=['GET'])
def get_specif_questions_category(ct_id):
    questions = Question.query.filter(Question.category == ct_id).all()
    return jsonify({
        'questions': [q.format() for q
                      in helperUtils.paganation
                      (request, questions)],
        'total_questions': len(questions),
        'current_category': ct_id
    })
