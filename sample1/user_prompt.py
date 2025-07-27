from ai_agent import AIAgent
from document_store import DocumentStore
from llm import LLM
from ml_model import MLModel
from code_executor import CodeExecutor

if __name__ == "__main__":
    document_store = DocumentStore()
    llm = LLM(document_store)
    ml_model = MLModel()
    code_executor = CodeExecutor()

    agent = AIAgent(llm, ml_model, code_executor, document_store)

    # Simulated user input
    user_prompt = "predict house price based on features"
    output = agent.handle_prompt(user_prompt)
    print("Task Output:", output)

