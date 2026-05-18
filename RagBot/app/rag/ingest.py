from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_chroma import Chroma
from langchain_community.document_loaders import PyPDFLoader
from app.models.embedding import Embed_function


loader=PyPDFLoader("app/data/sample.pdf")
document=loader.load()


splitter=RecursiveCharacterTextSplitter(chunk_size=500,chunk_overlap=100)
chunks=splitter.split_documents(document)

    
db=Chroma.from_documents(documents=chunks,embedding=Embed_function(),persist_directory="app/db")

print("PDF embedded successfully")
