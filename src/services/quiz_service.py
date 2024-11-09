# src/services/quiz_service.py
from ..models.quiz_model import QuizModel

class QuizService:
    def create_quiz(self, quiz_data):
        # INCOMPLETE: Extract `title` and `questions` from `quiz_data`
        # TODO: Retrieve "title" and "questions" from `quiz_data` dictionary
        title = quiz_data.get("title")
        questions = quiz_data.get("questions")
        
        # INCOMPLETE: Create a new QuizModel instance
        # TODO: Initialize a QuizModel with `title` and `questions` (Hint: quiz = QuizModel(title, questions))
        quiz = QuizModel(title, questions)
        
        # INCOMPLETE: Save the quiz and return its ID
        # TODO: Call `save()` on the quiz instance and return `quiz.id`
        quiz.save()
        return quiz.id
        # pass  # REMOVE when implementing

    def get_quiz(self, quiz_id):
        # INCOMPLETE: Retrieve a quiz by its ID using the model
        # TODO: Use QuizModel's `get_quiz` method to retrieve the quiz and return it
        # pass  # REMOVE when implementing
        return QuizModel.get_quiz(quiz_id)
    
    def evaluate_quiz(self, quiz_id, user_answers):
        # INCOMPLETE: Retrieve the quiz by its ID
        # TODO: Call `get_quiz` with `quiz_id` and store the result in `quiz`
        quiz = self.get_quiz(quiz_id)
        
        # INCOMPLETE: Check if the quiz exists
        # TODO: If `quiz` is None, return None and "Quiz not found"
        if quiz is None:
            return {"score": None, "message": "Quiz not found"}
        
        # INCOMPLETE: Calculate the score based on correct answers
        # TODO: Compare `user_answers` with `quiz.questions`, count correct answers, and return the score
        # pass  # REMOVE when implementing
        score = 0
        for i in range(len(quiz.questions)):
            if quiz.questions[i]["answer"] == user_answers[i]:
                score += 1

        return {"score": score, "message": "Quiz evaluated successfully"}
