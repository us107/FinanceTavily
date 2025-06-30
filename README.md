Finance Question Answering with Tavily and LangGraph
====================================================

Overview
--------

This Python script implements an interactive finance question-answering system using the Tavily API and LangGraph. It classifies user questions as finance-related or non-finance-related, fetches answers for finance questions via Tavily search, and provides a fallback response for non-finance questions. Users input questions in the terminal, and answers are printed there.

Features
--------

*   **Interactive Input**: Users type questions in the terminal and receive immediate answers.
    
*   **Finance Classification**: Questions are classified using finance-related keywords (e.g., "EBITDA", "stock").
    
*   **Tavily API Integration**: Finance questions are answered using aggregated search results from the Tavily API.
    
*   **LangGraph Workflow**: A directed graph routes questions through classification, answer generation, and output nodes.
    
*   **Exit Option**: Type exit to quit the program.
    

Prerequisites
-------------

*   Python 3.8+
    
*   pip install langchain langgraph langchain-community tavily-python
    
*   A valid Tavily API key (included in the script: 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).
    

Setup
-----

1.  pip install langchain langgraph langchain-community tavily-python
    
2.  **Secure the API Key** (optional but recommended):
    
    *   export TAVILY\_API\_KEY="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"
        
    *   import ostavily\_client = TavilyClient(api\_key=os.environ\["TAVILY\_API\_KEY"\])
        
3.  **Save the Script**:
    
    *   Save the code to m\_tavily\_with\_key.py.
        

Usage
-----

1.  python m\_tavily\_with\_key.py
    
2.  **Interact in the Terminal**:
    
    *   Enter a question when prompted (e.g., "Can you explain the concept of EBITDA in corporate finance?").
        
    *   The system classifies the question and either fetches an answer via Tavily (for finance questions) or returns a fallback message.
        
    *   Type exit to quit.
        

Example Interaction
-------------------

Plain textANTLR4BashCC#CSSCoffeeScriptCMakeDartDjangoDockerEJSErlangGitGoGraphQLGroovyHTMLJavaJavaScriptJSONJSXKotlinLaTeXLessLuaMakefileMarkdownMATLABMarkupObjective-CPerlPHPPowerShell.propertiesProtocol BuffersPythonRRubySass (Sass)Sass (Scss)SchemeSQLShellSwiftSVGTSXTypeScriptWebAssemblyYAMLXML`   Enter your question (or type 'exit' to quit): Can you explain the concept of EBITDA in corporate finance?  📌 Question: Can you explain the concept of EBITDA in corporate finance?  💡 Answer: [Aggregated Tavily search results explaining EBITDA...]  Enter your question (or type 'exit' to quit): What is the weather?  📌 Question: What is the weather?  💡 Answer: I'm trained to answer finance-related questions only. Please ask something about finance.  Enter your question (or type 'exit' to quit): exit  Exiting...   `

LangGraph Workflow Diagram
--------------------------

Below is a simplified ASCII diagram of the LangGraph workflow:

Plain textANTLR4BashCC#CSSCoffeeScriptCMakeDartDjangoDockerEJSErlangGitGoGraphQLGroovyHTMLJavaJavaScriptJSONJSXKotlinLaTeXLessLuaMakefileMarkdownMATLABMarkupObjective-CPerlPHPPowerShell.propertiesProtocol BuffersPythonRRubySass (Sass)Sass (Scss)SchemeSQLShellSwiftSVGTSXTypeScriptWebAssemblyYAMLXML`   Start    |    v  [Classifier] ----is_finance=True----> [FinanceTavily]    |                                      |    | is_finance=False                     |    v                                      v  [Fallback] ----------------------------> [Output]    |    v  [End]   `

### Diagram Explanation

*   **Start**: User inputs a question in the terminal.
    
*   **Classifier**: Checks for finance keywords (e.g., "finance", "EBITDA") in the question.
    
*   **FinanceTavily**: Queries the Tavily API for finance-related answers and aggregates results.
    
*   **Fallback**: Returns a message for non-finance questions.
    
*   **Output**: Prints the question and answer to the terminal.
    
*   **End**: Completes the workflow for the current question; user can input another or exit.
    

Library Usage
-------------

This project uses langchain, langgraph, and langchain-community. Below is an explanation of each library and why it’s used:

*   **langchain**:
    
    *   **Purpose**: Provides a framework for building applications with language models and external tools.
        
    *   **Usage in Project**: Although the original code used langchain for LLM integration, in this version, it’s included for compatibility with langgraph and langchain-community. It provides the foundation for state management and node execution in the LangGraph workflow.
        
    *   **Why Used**: LangChain’s abstractions simplify integrating external APIs (like Tavily) and managing state in complex workflows, ensuring modularity and scalability.
        
*   **langgraph**:
    
    *   **Purpose**: A library for building directed acyclic graph (DAG) workflows, allowing conditional routing and state management.
        
    *   **Usage in Project**: Defines the workflow with nodes (Classifier, FinanceTavily, Fallback, Output) and conditional edges to route questions based on finance classification. The StateGraph manages the question-processing pipeline.
        
    *   **Why Used**: LangGraph enables structured, conditional workflows, making it ideal for routing questions to either the Tavily API or a fallback response based on classification.
        
*   **langchain-community**:
    
    *   **Purpose**: Contains community-contributed tools and integrations for LangChain, including utilities for external APIs.
        
    *   **Usage in Project**: Provides the TavilyClient integration (via tavily-python) to fetch search results for finance questions. In the original code, it was used for Hugging Face LLM integration, but here it supports the Tavily API.
        
    *   **Why Used**: The langchain-community package extends LangChain with tools like Tavily, allowing seamless integration of search capabilities without custom API handling.
        

Code Structure
--------------

*   **Classifier Node**: Checks if the question contains finance keywords.
    
*   **FinanceTavily Node**: Queries the Tavily API and aggregates up to 5 search results.
    
*   **Fallback Node**: Returns a message for non-finance questions.
    
*   **Output Node**: Prints the question and answer.
    
*   **LangGraph Workflow**: Routes questions through nodes based on classification.
    

Notes
-----

*   **Tavily API Limits**: The free tier allows ~1,000 searches/month. Monitor usage via [tavily.com](https://tavily.com/).
    
*   **Security**: Avoid sharing the API key publicly. Use environment variables for production.
    
*   **Improvements**: Consider summarizing Tavily results for concise answers or adding error handling for API failures.
    

