from typing import List

from fastapi import APIRouter

from .models import QuestionIn, QuestionOut
from .utils import add_questions
from .crud import get_questions_from_db


app_router = APIRouter()


@app_router.post("/", response_model=List[QuestionOut])
async def get_questions(request: QuestionIn) -> List[QuestionOut]:
    questions_num = request.model_dump()['questions_num']
    questions = await get_questions_from_db(questions_num)
    await add_questions(questions_num)
    return questions
