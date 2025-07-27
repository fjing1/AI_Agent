class CodeExecutor:
    def execute(self, code):
        try:
            # Dangerous: use restricted environment in real systems!
            exec_globals = {}
            exec(code, exec_globals)
            return f"Execution result: {exec_globals}"
        except Exception as e:
            return f"Code execution error: {e}"

