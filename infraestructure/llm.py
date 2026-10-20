from langchain_ollama import OllamaLLM

class LLModel:
    def get_model() -> OllamaLLM:
        return OllamaLLM(
            model="qwen3.5.4b-Q4_K_M:latest",
            temperature=0.0,
            reasoning=False,
        )