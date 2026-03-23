from langchain_openai import ChatOpenAI
from langgraph.checkpoint.memory import MemorySaver
from langchain.agents import create_agent

from config import Settings, SYSTEM_PROMPT
from tools import web_search, read_url, write_report, knowledge_search

settings = Settings()

llm = ChatOpenAI(
    model=settings.model_name,
    api_key=settings.api_key.get_secret_value(),
)

tools = [web_search, read_url, knowledge_search, write_report]

memory = MemorySaver()

agent = create_agent(
    model=llm,
    tools=tools,
    system_prompt=SYSTEM_PROMPT,
    checkpointer=memory,
)

