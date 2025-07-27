class AIAgent:
    def __init__(self, llm, ml_model, code_executor, document_store):
        self.llm = llm
        self.ml_model = ml_model
        self.code_executor = code_executor
        self.document_store = document_store

    def handle_prompt(self, prompt):
        print(f"Received prompt: {prompt}")
        task = self._understand_prompt(prompt)
        return self._execute_task(task)

    def _understand_prompt(self, prompt):
        # Naive implementation of NLP-driven task identification
        if "predict" in prompt:
            return {"type": "ml_query", "query": prompt}
        elif "document" in prompt:
            return {"type": "document_query", "query": prompt}
        elif "code" in prompt:
            return {"type": "code_execution", "code": prompt}
        else:
            return {"type": "default", "query": prompt}

    def _execute_task(self, task):
        if task["type"] == "ml_query":
            return self.ml_model.query(task["query"])
        elif task["type"] == "document_query":
            return self.llm.query(task["query"])
        elif task["type"] == "code_execution":
            return self.code_executor.execute(task["code"])
        else:
            return "Unknown task type."

