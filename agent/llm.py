from langchain_groq import ChatGroq
import logging

class GroqLLM:
    def __init__(self, model_id: str = "llama-3.1-8b-instant", temperature: float = 0.5) -> None:
        self.model_id = model_id
        self.temperature = temperature

    def get_llm(self):
        try:
            logging.info("Initializing llm....")
            return ChatGroq(model=self.model_id, temperature=self.temperature)

        except Exception as e:
            raise RuntimeError(
                "Failed to initialize model: {self.model_id}") from e


if __name__ == "__main__":
    obj = GroqLLM()
    llm = obj.get_llm()
    result = llm.invoke("What is machine learning?")

    print(result)
