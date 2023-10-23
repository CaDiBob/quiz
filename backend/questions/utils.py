from aiohttp import ClientSession

from .crud import save_qestions
from config import settings


async def fetch_questions(questions_num: int | None) -> None:
    async with ClientSession(raise_for_status=True) as session:
        params = {"count": questions_num}
        url = settings.api_url
        async with session.get(url, params=params) as response:
            questions = await response.json()
        return questions


async def add_questions(questions_num: int | None) -> None:
    new_questions = await fetch_questions(questions_num)
    await save_qestions(new_questions)
