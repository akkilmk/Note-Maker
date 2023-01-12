from beanie import init_beanie, Document, PydanticObjectId
from typing import Optional
import datetime

class NoteWrite(Document):
    id: Optional[PydanticObjectId] = None
    note: str


class Note(NoteWrite):
    date = datetime.datetime.now()
    date: str = str(date.strftime("%d-%b-%Y"))