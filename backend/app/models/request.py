from pydantic import BaseModel


class ArgumentRequest(BaseModel):
    argument: str