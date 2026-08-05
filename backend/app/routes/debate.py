from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
import traceback

from app.services.agent import generate_rebuttal

router = APIRouter()


class DebateRequest(BaseModel):
    argument: str
    history: list = []


@router.post("/debate")
def debate(request: DebateRequest):

    try:

        return generate_rebuttal(
            argument=request.argument,
            history=request.history
        )

    except Exception as e:

        traceback.print_exc()

        raise HTTPException(
            status_code=500,
            detail=str(e)
        )