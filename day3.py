from langgraph.graph import *
from typing import TypedDict


class State(TypedDict):
    son: int
    turi: str


def tanla(state):
    if state['son'] >= 100:
        return "yuzlik"

    elif state['son'] >= 10:
        return "onlik"
    else:
        return "birlik"


def onlik(state):
    return {"turi": "onlik"}


def yuzlik(state):
    return {"turi": "yuzlik"}


def birlik(state):
    return {"turi": "birlik"}


builder = StateGraph(State)

builder.add_node("onlik", onlik)
builder.add_node("yuzlik", yuzlik)
builder.add_node("birlik", birlik)

builder.add_conditional_edges(START, tanla)

builder.add_edge("birlik", END)
builder.add_edge("onlik", END)
builder.add_edge("yuzlik", END)

graph = builder.compile()

response = graph.invoke({
    "son": 154,
    'turi': ""

})
print(response)
