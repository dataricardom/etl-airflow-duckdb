from pydantic import BaseModel, Json

class PokemonSchema(BaseModel):
    name: str
    type: str

    class Config:
        from_attributes = True