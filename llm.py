# Install dependencies (run this manually in your environment if needed):
# pip install langchain langgraph langchain-community tavily-python

# ✅ Step 1: Set up Tavily API
from tavily import TavilyClient

# Set your Tavily API key
tavily_client = TavilyClient(api_key="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")

# ✅ Step 2: LangGraph Node - Classifier
def classifier_node(state):
    keywords = ["finance", "stock", "balance sheet", "revenue", "EBITDA", "debt", "equity", "cash flow"]
    is_finance = any(k.lower() in state["question"].lower() for k in keywords)
    return {**state, "is_finance": is_finance}

# ✅ Step 3: LangGraph Node - Finance Answer using Tavily
def finance_tavily_node(state):
    question = state["question"]
    # Perform a search using Tavily API
    response = tavily_client.search(
        query=f"finance {question}",
        search_depth="basic",
        max_results=5
    )
    # Extract relevant content from search results
    answer = ""
    for result in response["results"]:
        answer += result["content"] + "\n"
    if not answer:
        answer = "No relevant finance information found."
    return {**state, "answer": answer}

# ✅ Step 4: LangGraph Node - Fallback Answer
def fallback_node(state):
    return {**state, "answer": "I'm trained to answer finance-related questions only. Please ask something about finance."}

# ✅ Step 5: LangGraph Node - Output
def output_node(state):
    print(f"\n📌 Question: {state['question']}\n💡 Answer: {state['answer']}\n")
    return state

# ✅ Step 6: Build LangGraph with dict-based state
from langgraph.graph import StateGraph

# Define the graph with dict-based state
graph = StateGraph(dict)

# Add nodes
graph.add_node("Classifier", classifier_node)
graph.add_node("FinanceTavily", finance_tavily_node)
graph.add_node("Fallback", fallback_node)
graph.add_node("Output", output_node)

# Set entry point
graph.set_entry_point("Classifier")

# Define conditional routing function
def route_classifier(state):
    return "FinanceTavily" if state.get("is_finance", False) else "Fallback"

# Add conditional edges
graph.add_conditional_edges(
    "Classifier",
    route_classifier,
    {
        "FinanceTavily": "FinanceTavily",
        "Fallback": "Fallback"
    }
)

# Add direct edges
graph.add_edge("FinanceTavily", "Output")
graph.add_edge("Fallback", "Output")

# Set finish point
graph.set_finish_point("Output")

# Compile the workflow
workflow = graph.compile()

# ✅ Step 7: Run interactive input
if __name__ == "__main__":
    while True:
        input_question = input("Enter your question (or type 'exit' to quit): ")
        if input_question.lower() == "exit":
            print("Exiting...")
            break
        workflow.invoke({"question": input_question})