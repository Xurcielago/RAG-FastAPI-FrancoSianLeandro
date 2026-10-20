from pydantic import BaseModel, Field
from pathlib import Path
#Validaciones en base de lo que se ingresa a las funciones

class DocumentSchema(BaseModel):
    collection_name: str = Field(
        description="Este es el nombre de la coleccion"
    )
    path: Path = Field(description="La direccion donde esta el documento")
    #Recibe una instancia de Path para usarse tanto en Windows como Linux


class RetrieveSchema(BaseModel):
    collection_name: str
    query: str
    k: int = 5