import requests as requests
from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from dotenv import load_dotenv
import os

load_dotenv()

app = Flask(__name__)
app.debug = os.getenv("DEBUG")

app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv("DATABASE_URL")
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
db = SQLAlchemy(app)
migrate = Migrate(app, db)


class Question(db.Model):
    question_id = db.Column(db.Integer, primary_key=True)
    id = db.Column(db.Integer, unique=True)
    question = db.Column(db.String(500), unique=True, nullable=False)
    answer = db.Column(db.String(500))
    date = db.Column(db.DateTime)

    def serialize(self):
        return {
            "id": self.id,
            "question": self.question,
            "answer": self.answer,
            "date": self.date
        }


@app.route('/', methods=['POST'])
def add_questions() -> dict:
    count = request.json['questions_num']
    if count > 100:
        raise Exception("questions_num не должно превышать 100")

    response = requests.get('https://jservice.io/api/random?count=' + str(count))
    questions = response.json()
    for i in range(count):
        el = questions[i]
        count_id = Question.query.filter_by(id=el['id']).count()
        count_question = Question.query.filter_by(question=el['question']).count()
        while count_id > 0 or count_question > 0:
            response = requests.get('https://jservice.io/api/random?count=1')
            el = response.json()[0]
            count_id = Question.query.filter_by(id=el['id']).count()
            count_question = Question.query.filter_by(question=el['question']).count()
        new_question = Question(id=el['id'], question=el['question'], answer=el['answer'], date=el['created_at'])
        db.session.add(new_question)
        db.session.commit()

    last_two_questions = Question.query.order_by(Question.question_id.desc()).limit(2).all()
    amount = len(last_two_questions)
    if amount > 1:
        question = last_two_questions[1]
    else:
        question = Question()
    return question.serialize()

