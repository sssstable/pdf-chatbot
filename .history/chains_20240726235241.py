import logging
from langchain_community.embeddings import OpenAIEmbeddings
from langchain_openai import ChatOpenAI
from langchain_community.chat_models import ChatOllama


from langchain.chains import RetrievalQAWithSourcesChain
from langchain.chains.qa_with_sources import load_qa_with_sources_chain

import logging
from langchain_community.embeddings import OllamaEmbeddings

# Initialize logger
logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO)

def load_embedding_model(embedding_model_name: str, logger=logger, config={}):
    if embedding_model_name == "ollama":
        embeddings = OllamaEmbeddings(
            base_url=config["ollama_base_url"], model="llama2"
        )
        dimension = 4096
        logger.info("Embedding: Using Ollama")
    elif embedding_model_name == "openai":
        embeddings = OpenAIEmbeddings()
        dimension = 1536
        logger.info("Embedding: Using OpenAI")
    else:
        raise ValueError(f"Unknown embedding model name: {embedding_model_name}")
    return embeddings, dimension

def load_llm(llm_name: str, logger=logger, config={}):
    if llm_name == "gpt-4":
        logger.info("LLM: Using GPT-4")
        return ChatOpenAI(temperature=0, model_name="gpt-4", streaming=True)
    elif llm_name == "gpt-3.5":
        logger.info("LLM: Using GPT-3.5")
        return ChatOpenAI(temperature=0, model_name="gpt-3.5-turbo", streaming=True)
    elif len(llm_name):
        logger.info(f"LLM: Using Ollama: {llm_name}")
        return ChatOllama(
            temperature=0,
            base_url=config["ollama_base_url"],
            model=llm_name,
            streaming=True,
            top_k=10,
            top_p=0.3,
            num_ctx=3072,
        )
    logger.info("LLM: Using GPT-3.5")
    return ChatOpenAI(temperature=0, model_name="gpt-3.5-turbo", streaming=True)
