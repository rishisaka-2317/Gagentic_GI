from dotenv import load_dotenv

from langchain.agents import create_agent

from langchain.tools import tool

from langchain_core.messages import HumanMessage

from langchain_openai import ChatOpenAI




import os
load_dotenv()


def search(query:str) -> str:
    """
    Tool that searches over internet
    Args:
        query: The query to search for
    Returns:
         The search result
    """
    print(f"Searching for {query}")
    return "Tokyo weather is sunny"      

llm = ChatOpenAI()
tools = [search]
agent = create_agent(model=llm, tools=tools)


def main():
    print("Hello from gagentic-gi!")
    result = agent.invoke({"messages": HumanMessage(content="Whats the weather in Tokyo")})
    print(result)


if __name__ == "__main__":
    main()


