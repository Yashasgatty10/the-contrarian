from fastapi import APIRouter, HTTPException
from pydantic import BaseModel

from app.services.agent import generate_rebuttal

router = APIRouter()


class DebateRequest(BaseModel):
    argument: str
    history: list = []


@router.post("/debate")
def debate(request: DebateRequest):

    try:

        result = generate_rebuttal(
            argument=request.argument,
            history=request.history
        )

        return result

    except Exception as e:

        raise HTTPException(
            status_code=500,
            detail=f"Failed to generate rebuttal: {str(e)}"
        )