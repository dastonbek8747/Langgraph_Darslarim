from langgraph.graph import START, END, StateGraph
from typing import TypedDict


class State(TypedDict):
    text: str


builder = StateGraph(State)


def add_hello(state):
    return {"text": state["text"] + " Salom"}


def add_world(state):
    return {"text": state["text"] + " Dunyo"}


builder.add_node("hello", add_hello)
builder.add_node("world", add_world)

builder.add_edge(START, "hello")
builder.add_edge("hello", "world")
builder.add_edge("world", END)

graph = builder.compile()

response = graph.invoke({
    "text": "Doston",
})

print(response)