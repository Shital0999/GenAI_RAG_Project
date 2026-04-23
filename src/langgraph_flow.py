from langgraph.graph import StateGraph
from typing import TypedDict

# ✅ Correct State Definition
class State(TypedDict):
    query: str
    pipeline: object
    answer: str


# ✅ Process Node
def process_node(state: State):
    query = state["query"]
    pipeline = state["pipeline"]

    answer = pipeline(query)

    # HITL condition
    if "don't know" in answer.lower() or len(answer.strip()) < 20:
        print("\n⚠️ Escalating to Human...")
        human = input("Enter human response: ")
        return {"answer": human}

    return {"answer": answer}


# ✅ Output Node
def output_node(state: State):
    print("\n✅ Answer:", state["answer"])
    return state


# ✅ Build Graph
def build_graph():
    graph = StateGraph(State)

    graph.add_node("process", process_node)
    graph.add_node("output", output_node)

    graph.set_entry_point("process")
    graph.add_edge("process", "output")

    return graph.compile()