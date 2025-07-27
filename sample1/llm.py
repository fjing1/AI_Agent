class LLM:
    def __init__(self, document_store):
        self.document_store = document_store

    def query(self, nlp_query):
        documents = self.document_store.fetch_response(nlp_query)
        return f"Relevant documents: {documents}"

