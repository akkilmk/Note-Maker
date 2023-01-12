from models.note import Note, NoteWrite
from fastapi import APIRouter

router = APIRouter()

@router.post("/")
async def root():
    return await Note.find().to_list()


@router.post("/create")
async def save(payload: NoteWrite):
    await Note(note=payload.note).save()
