from langchain_openai import ChatOpenAI
from langchain_core.tools import tool
from langchain_core.messages import HumanMessage
import requests

# tool create

@tool
def multiply(a: int, b: int) -> int:
  """Given 2 numbers a and b this tool returns their product"""
  return a * b

print(multiply.invoke({'a':3, 'b':4}))

# tool binding

llm = ChatOpenAI()
llm_with_tools = llm.bind_tools([multiply])
query = HumanMessage('can you multiply 3 with 1000')
messages = [query]
result = llm_with_tools.invoke(messages)
messages.append(result)
tool_result = multiply.invoke(result.tool_calls[0])
messages.append(tool_result)