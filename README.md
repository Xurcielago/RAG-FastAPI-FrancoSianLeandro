# *Preparación de entorno*  
Ejecutar en orden:  

uv venv env  

env\Scripts\activate  

uv pip install langchain langchain-ollama langchain-chroma langchain-community langchain-text-splitters pypdf langchain-experimental fastapi 'uvicorn[standard]' python-multipart  

uv pip freeze >> requirements.txt  


# *Pruebas*  
uvicorn main:app --reload  
copiar y abrir en el navegador  
http://127.0.0.1:8000  server response  
http://127.0.0.1:8000/docs  
