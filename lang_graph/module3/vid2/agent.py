from langchain_core.messages import SystemMessage
from langchain_openai import ChatOpenAI

from langgraph.graph import START, StateGraph, MessagesState, END
from langgraph.prebuilt import tools_condition, ToolNode

def add(a: int, b: int) -> int:
    """Adds a and b.

    Args:
        a: first int
        b: second int
    """
    return a + b

def multiply(a: int, b: int) -> int:
    """Multiplies a and b.

    Args:
        a: first int
        b: second int
    """
    return a * b

def divide(a: int, b: int) -> float:
    """Divide a and b.

    Args:
        a: first int
        b: second int
    """
    return a / b

# NEW: Temperature converter tool
def celsius_to_fahrenheit(celsius: float) -> dict:
    """Convert temperature from Celsius to Fahrenheit.
    
    Args:
        celsius: temperature in Celsius
    """
    fahrenheit = (celsius * 9/5) + 32
    return {
        "celsius": celsius,
        "fahrenheit": fahrenheit,
        "conversion": f"{celsius}°C = {fahrenheit}°F"
    }

tools = [add, multiply, divide]
all_tools = tools + [celsius_to_fahrenheit]  # NEW: Combined tools

# Define LLM with bound tools
llm = ChatOpenAI(model="gpt-4o")
llm_with_tools = llm.bind_tools(all_tools)  # Changed: bind all tools

# System message
sys_msg = SystemMessage(content="You are a helpful assistant tasked with performing arithmetic on a set of inputs and converting temperatures between Celsius and Fahrenheit.")

# Node
def assistant(state: MessagesState):
   return {"messages": [llm_with_tools.invoke([sys_msg] + state["messages"])]}

# NEW: Temperature preprocessing node
def temp_handler(state: MessagesState):
    """Handles temperature queries"""
    return state

# NEW: Custom routing function
def route_from_assistant(state: MessagesState):
    """Route to temp, tools, or end"""
    last_message = state["messages"][-1]
    
    if not hasattr(last_message, 'tool_calls') or not last_message.tool_calls:
        return "end"
    
    tool_name = last_message.tool_calls[0]['name']
    
    if tool_name == 'celsius_to_fahrenheit':
        return "temp"
    else:
        return "tools"

# Build graph
builder = StateGraph(MessagesState)
builder.add_node("assistant", assistant)
builder.add_node("temp", temp_handler)  # NEW: Temperature node
builder.add_node("tools", ToolNode(all_tools))  # Changed: use all_tools

builder.add_edge(START, "assistant")

# NEW: Custom conditional routing
builder.add_conditional_edges(
    "assistant",
    route_from_assistant,
    {
        "temp": "temp",
        "tools": "tools",
        "end": END
    }
)

# NEW: Temp goes to tools
builder.add_edge("temp", "tools")

# Tools go back to assistant
builder.add_edge("tools", "assistant")

# Compile graph
graph = builder.compile(interrupt_before=["temp"])