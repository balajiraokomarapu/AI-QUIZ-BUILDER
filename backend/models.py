from pydantic import BaseModel

class QuizRequest(BaseModel):
    topic: str
    difficulty: str
    num_questions: int