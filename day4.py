from langgraph.graph import MessagesState, START, END, StateGraph
from typing import TypedDict

def first(state):
    return {"messages": ["salom"]}


def second(state):
    return {"messages": ["salom2"]}


builder = StateGraph(MessagesState)
builder.add_node("first", first)
builder.add_node("second", second)

builder.add_edge(START, "first")
builder.add_edge("first", "second")
builder.add_edge("second", END)

graph = builder.compile()

response = graph.invoke({
    "messages": [],
})
print(response)