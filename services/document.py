from infraestructure import VectorStore, EmbeddingModel
from langchain_experimental.text_splitter import SemanticChunker
from langchain_community.document_loaders import PyPDFLoader
from schemas import DocumentSchema, RetrieveSchema # Para importar todos los archivos desde el Schema
from fastapi import HTTPException
#Aquí se guarda la lógica de negocios

class DocumentService:
    def __init__(self) -> None:
        self.vector_store = VectorStore()
        self.embedding = EmbeddingModel.get_model_embedding()

    def add_documents(self, data: DocumentSchema): #Recibe una instancia de DocumentSchema
        
        splitter = SemanticChunker (
            embeddings= self.embedding
        )
        document = PyPDFLoader(str(data.path)).load()

        chunks= splitter.split_documents(document)
        
        results = self.vector_store.add_document(collection_name=data.collection_name, docs=chunks)

        #
        if not results:
            raise HTTPException(
                detail="Error al indexar los documentos",
                status_code=500
            )

        return results
    
    def retrieve(self, data: RetrieveSchema):
        return self.vector_store.search_documents(
            collection_name=data.collection_name,
            query=data.query,
            k=data.k,
        )