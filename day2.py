# from langgraph.graph import StateGraph, START, END
# from typing import TypedDict
#
#
# class State(TypedDict):
#     username: str
#     message: list
#
#
# def see_heello(state):
#     print(state["username"] + "hello")
#     return state
#
#
# def see_world(state):
#     print(state["message"] + ["SALOM QANDAY YORDAM BERA OLAMAN !"])
#     return {
#         "message": (state["message"] + ["SALOM QANDAY YORDAM BERA OLAMAN !"])
#     }
#
#
# builder = StateGraph(State)
# builder.add_node("see_hello", see_heello)
# builder.add_node("see_world", see_world)
# builder.add_edge(START, "see_hello")
# builder.add_edge("see_hello", "see_world")
# builder.add_edge("see_world", END)
#
# graph = builder.compile()
#
# response = graph.invoke({
#     "username": "Dostonbek",
#     "message": []
# })
#
# print(response)


from langgraph.graph import StateGraph, START, END
from typing import TypedDict


class State(TypedDict):
    umumiy: int


def sonni_yarmi(state):
    print(state["umumiy"] // 2)
    return {"umumiy": state["umumiy"] // 2}


def songa_on_qosh(state):
    print(state["umumiy"] + 10)
    return {"umumiy": state["umumiy"] + 10}


builder = StateGraph(State)
builder.add_node("yarmi", sonni_yarmi)
builder.add_node("qosh_on", songa_on_qosh)

builder.add_edge(START, "yarmi")
builder.add_edge("yarmi", "qosh_on")
builder.add_edge("qosh_on", END)

graph = builder.compile()

response = graph.invoke({
    "umumiy": 100,
})
print(response)
