from dataclasses import dataclass
from typing import List
from enum import Enum

class QuestionType(Enum):
    MULTIPLE_CHOICE = "multiple_choice"
    RATING_SCALE = "rating_scale"
    OPEN_ENDED = "open_ended"

@dataclass(frozen=True)
class Question:
    question_type: QuestionType
    text: str
    options: List[str] = None
    scale: int = None

class Survey:
    def __init__(self, title: str):
        self.title = title
        self.questions = []
        self.responses = []

    def add_question(self, question_type: QuestionType, text: str, options=None, scale=None):
        question = Question(question_type=question_type, text=text, options=options, scale=scale)
        self.questions.append(question)

    def submit_response(self, response: List):
        if len(response) != len(self.questions):
            raise ValueError("Invalid response length")
        self.responses.append(response)

    def get_results(self):
        results = {}
        for i, question in enumerate(self.questions):
            if question.question_type == QuestionType.MULTIPLE_CHOICE:
                results[question.text] = self._get_multiple_choice_results(i)
            elif question.question_type == QuestionType.RATING_SCALE:
                results[question.text] = self._get_rating_scale_results(i)
            elif question.question_type == QuestionType.OPEN_ENDED:
                results[question.text] = self._get_open_ended_responses(i)
        return results

    def _get_multiple_choice_results(self, question_index: int):
        results = {}
        for response in self.responses:
            answer = response[question_index]
            if answer in results:
                results[answer] += 1
            else:
                results[answer] = 1
        return results

    def _get_rating_scale_results(self, question_index: int):
        results = [0] * (self.questions[question_index].scale + 1)
        for response in self.responses:
            answer = response[question_index]
            results[answer] += 1
        return results

    def _get_open_ended_responses(self, question_index: int):
        return [response[question_index] for response in self.responses]