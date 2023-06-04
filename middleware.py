from langchain.document_loaders import UnstructuredURLLoader
import streamlit as st
from langchain.text_splitter import CharacterTextSplitter
from langchain.vectorstores import FAISS
from langchain.embeddings import OpenAIEmbeddings
from langchain.chains import RetrievalQAWithSourcesChain
from langchain.chains.question_answering import load_qa_chain
from langchain import OpenAI
import os

def get_text_from_link(link):
    loaders = UnstructuredURLLoader(urls=[link])
    data = loaders.load()
    return data

def split_text(data):
    text_splitter = CharacterTextSplitter(separator='\n', chunk_size=1000, chunk_overlap=200)
    docs = text_splitter.split_documents(data)
    return docs

def get_embeddings(docs): # will get embeddings from docs and then store them in a vector database
    embeddings = OpenAIEmbeddings()
    vectorSpace_openAI = FAISS.from_documents(docs, embeddings)
    return vectorSpace_openAI

def main():
    os.environ["OPENAI_API_KEY"] = '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'
    loaders = UnstructuredURLLoader(urls=[st.session_state.link])
    data = loaders.load()
    text_splitter = CharacterTextSplitter(separator='\n', chunk_size=1000, chunk_overlap=200)
    docs = text_splitter.split_documents(data)
    print(len(docs))
    embeddings = OpenAIEmbeddings()
    print(embeddings)
    # vectorSpace_openAI = FAISS.from_documents(docs, embeddings)

    # with open('vectorSpace_openAI.pkl', 'wb') as f:
    #     pickle.dump(vectorSpace_openAI, f)

    # with open('vectorSpace_openAI.pkl', 'rb') as f:
    #     vectorSpace_openAI = pickle.load(f)

    llm = OpenAI(temperature=0)
    llm

    



    # print(st.session_state.link)
    # print("helloworld")