from fastapi import APIRouter, Form
from schemas import LLMSchema
from services import LLMService

router = APIRouter()
llm_service = LLMService()


@router.post("/response")
def response(
    collection_name: str = Form(...),
    input: str = Form(...),
):
    result = llm_service.response(
        data=LLMSchema(
            collection_name=collection_name,
            query=input,
        )
    )
    return result