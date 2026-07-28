from fastapi import APIRouter, Depends
from app.models.document import ChatRequest
from app.services.rag_service import generate_answer
from app.utils.auth import verify_token

router = APIRouter()


@router.post("/chat")
def chat(
    request: ChatRequest,
    user=Depends(verify_token)
):

    answer = generate_answer(request.question)

    return {
        "question": request.question,
        "answer": answer
    }