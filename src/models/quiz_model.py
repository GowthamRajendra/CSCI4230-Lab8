# src/models/quiz_model.py
from ..database import db

# INCOMPLETE: Define the QuizModel class
# TODO: Create a class named QuizModel that inherits from db.Model
class QuizModel(db.Model):
    # INCOMPLETE: Set up the table name
    # TODO: Define `__tablename__` as 'quizzes'
    __tablename__ = 'quizzes'
    
    # INCOMPLETE: Define table columns
    # TODO: Define an integer primary key column named `id`
    id = db.Column(db.Integer, primary_key=True)
    # TODO: Define a string column named `title` that cannot be null
    title = db.Column(db.String(100), nullable=False)
    # TODO: Define a column named `questions` with PickleType to store a list
    questions = db.Column(db.PickleType)
    
    def __init__(self, title, questions):
        # INCOMPLETE: Initialize the model with title and questions
        # TODO: Assign `self.title` and `self.questions` with `title` and `questions`
        # pass  # REMOVE when implementing
        self.title = title
        self.questions = questions

    def save(self):
        # INCOMPLETE: Save the quiz to the database
        # TODO: Use `db.session.add(self)` and `db.session.commit()` to save the instance
        # pass  # REMOVE when implementing
        db.session.add(self)
        db.session.commit()

    @classmethod
    def get_quiz(cls, quiz_id):
        # INCOMPLETE: Retrieve a quiz by its ID
        # TODO: Use `cls.query.get(quiz_id)` to retrieve a quiz and return it
        # pass  # REMOVE when implementing
        return cls.query.get(quiz_id)
