from typing import List

from asyncpg import exceptions

from . import utils
from .tables import Question


async def save_qestions(questions: List[dict]) -> None:
    repeated_questions = 0
    for question in questions:
        try:
            new_question = Question(
                {
                    Question.number: question['id'],
                    Question.text: question['question'],
                    Question.answer: question['answer'],
                }
            )
            await new_question.save()
        except exceptions.UniqueViolationError:
            repeated_questions += 1

    if repeated_questions:
        await utils.fetch_questions(questions_num=repeated_questions)


async def get_questions_from_db(limit: int) -> List[dict]:
    questions = await Question.select(
        Question.number, Question.text, Question.answer).order_by(
        Question.created_at, ascending=False).limit(limit)
    return questions
