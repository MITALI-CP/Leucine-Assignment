from fastapi import APIRouter, Depends
from app.utils.auth import verify_token
from app.services.rag_service import save_document
from app.models.document import Document

router = APIRouter()


@router.post("/documents")
def upload_document(
    document: Document,
    user=Depends(verify_token)
):
    return save_document(
        filename=document.filename,
        content=document.content,
        user_email=user["email"]
    )