from pydantic import BaseModel, ConfigDict


class QuestionIn(BaseModel):
    questions_num: int


class QuestionOut(BaseModel):
    number: int
    text: str
    answer: str
    model_config: ConfigDict = ConfigDict()
