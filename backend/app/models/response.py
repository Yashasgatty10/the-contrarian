from pydantic import BaseModel


class Source(BaseModel):
    title: str
    type: str
    score: float


class RebuttalResponse(BaseModel):
    argument: str
    rebuttal: str
    retrieval_used: bool
    used_additional_reasoning: bool
    sources: list[Source]