from pydantic import BaseModel, Field


class Event(BaseModel):
    source: str
    text: str = Field(min_length=5)

    @property
    def visible_text(self) -> str:
        return f'{self.source}: {self.text}'
