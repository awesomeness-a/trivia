import os
from types import ClassMethodDescriptorType
from flask import Flask, request, abort, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
import random

from models import setup_db, Question, Category

QUESTIONS_PER_PAGE = 10


def paginate_questions(request, selection):
    page = request.args.get('page', 1, type=int)
    start = (page - 1) * QUESTIONS_PER_PAGE
    end = start + QUESTIONS_PER_PAGE

    questions = [question.format() for question in selection]
    current_questions = questions[start:end]

    return current_questions


def create_app(test_config=None):
    # Create and configure the app
    app = Flask(__name__)
    setup_db(app)
    # Set up CORS with * for origins
    cors = CORS(app, resources={r"/trivia/*": {"origins": "*"}})
    # Enable cross-domain requests and set respense headers
    @app.after_request
    def after_request(response):
        response.headers.add('Access-Control-Allow-Headers',
                             'Content-Type, Authorization, true')
        response.headers.add('Access-Control-Allow-Methods',
                             'GET, PUT, POST, DELETE, OPTIONS')

        return response


# ------------------------------------------------------------------------- #
# Endpoints
# ------------------------------------------------------------------------- #

    # Create an endpoint to handle GET requests for all available categories
    @app.route('/categories')
    def retrieve_categories():
        try:
            categories = Category.query.order_by(Category.type).all()

            return jsonify({
              'success': True,
              'categories': {category.id: category.type
                             for category in categories}
            })
        except Exception as e:
            print(e)
            abort(500)


    # Create an endpoint to handle GET requests for questions,
    # including pagination. Returns a list of questions,
    # number of total questions, current category, categories.
    @app.route('/questions')
    def retrieve_questions():
        try:
            selection = Question.query.order_by(Question.id).all()
            current_questions = paginate_questions(request, selection)
            categories = Category.query.order_by(Category.type).all()

            if len(current_questions) == 0:
                abort(404)

            return jsonify({
                'success': True,
                'questions': current_questions,
                'total_questions': len(selection),
                'categories': {category.id: category.type
                               for category in categories},
                'current_category': None
              })
        except Exception as e:
            print(e)
            abort


    # Create an endpoint to DELETE a question using a question ID
    @app.route('/questions/<int:question_id>', methods=['DELETE'])
    def delete_question(question_id):
        try:
            question = Question.query.filter(
              Question.id == question_id).one_or_none()

            if question is None:
                abort(404)

            question.delete()

            return jsonify({
              'success': True,
              'deleted': question_id
            })

        except Exception as e:
            if '404' in str(e):
                abort(404)
            else:
                abort(422)


    # Create an endpoint to POST a new question, which will require
    # the question and answer text, category, and difficulty score.
    @app.route('/questions', methods=['POST'])
    def create_question():
        body = request.get_json()
        new_question = body.get('question', None)
        new_answer = body.get('answer', None)
        new_difficulty = body.get('difficulty', None)
        new_category = body.get('category', None)

        try:
            question = Question(question=new_question,
                                answer=new_answer,
                                difficulty=new_difficulty,
                                category=new_category)
            question.insert()

            return jsonify({
              'success': True,
              'created': question.id
            })
        except Exception as e:
            print(e)
            abort(500)


    # Create a GET endpoint to get questions based on category
    @app.route('/categories/<int:category_id>/questions', methods=['GET'])
    def retrieve_questions_by_category(category_id):
        try:
            questions = Question.query.filter(
              Question.category == str(category_id)).all()

            return jsonify({
              'success': True,
              'questions': [question.format() for question in questions],
              'total_questions': len(questions),
              'current_category': category_id
            })
        except Exception as e:
            print(e)
            abort(404)


    # Create a POST endpoint to get questions based on a search term.
    # It returns any questions for whom the search term is
    # a substring of the question.
    @app.route('/search', methods=['POST'])
    def search_questions():
        body = request.get_json()
        search_term = body.get('searchTerm', None)

        try:
            questions = Question.query.filter(
              Question.question.ilike(f'%{search_term}%')).all()

            return jsonify({
              'success': True,
              'questions': [question.format() for question in questions],
              'total_questions': len(questions),
              'current_category': None
            })
        except Exception as e:
            print(e)
            abort(404)


    # Create a POST endpoint to get questions to play the quiz.
    # This endpoint takes category and previous question parameters
    # and returns a random questions within the given category,
    # if provided, and that is not one of the previous questions.
    @app.route('/quizzes', methods=['POST'])
    def play_quiz():
        try:
            body = request.get_json()
            category = body.get('quiz_category')
            previous_questions = body.get('previous_questions')

            if category['type'] == 'click':
                available_questions = Question.query.filter(
                    Question.id.notin((previous_questions))).all()
            else:
                available_questions = Question.query.filter_by(
                  category=category['id']).filter(
                    Question.id.notin_((previous_questions))).all()

            new_question = available_questions[
              random.randrange(0,
                               len(available_questions))
              ].format() if len(available_questions) > 0 else None

            return jsonify({
              'success': True,
              'question': new_question
            })
        except Exception as e:
            print(e)
            abort(422)


    # ----------------------------------------------------------------------- #
    # Error Handlers
    # ----------------------------------------------------------------------- #

    @app.errorhandler(400)
    def bad_request(error):
        return jsonify({
            'success': False,
            'error': 400,
            'message': 'Bad request'
        }), 400

    @app.errorhandler(404)
    def not_found(error):
        return jsonify({
            'success': False,
            'error': 404,
            'message': 'Resource not found'
        }), 404

    @app.errorhandler(422)
    def unprocessable(error):
        return jsonify({
            'success': False,
            'error': 404,
            'message': 'Unprocessable request'
        }), 422

    @app.errorhandler(500)
    def server_error(error):
        return jsonify({
            'success': False,
            'error': 500,
            'message': 'Internal server error'
        }), 500

    return app
