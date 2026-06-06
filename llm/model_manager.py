from llama_cpp import Llama

class ModelManager:

    #static variable
    MODEL_PATH = {
        "qwen2.5": "models/qwen2.5-1.5b-instruct-q4_k_m.gguf",
        "typhoon": "models/llama3.2-typhoon2-t1-3b-q4_k_m.gguf",
    }
    current_model_name = None
    current_model = None

    #non-static variable
    def __init__(self):
        pass

    def load_model(self, model_name: str):

        if self.current_model_name == model_name:
            # Check if the model is already loaded
            print(f"[ModelManager] '{model_name}' is already loaded.")
            return
        
        # Unload the current model if it's different from the new one
        self._unload()

        # Load the new model
        print(f"[ModelManager] Loading {model_name}...")
        self.current_model = Llama(
            model_path=self.MODEL_PATHS[model_name],
            n_ctx=2048,
            n_threads=4,
        )

        # Update the current model name after loading
        self.current_model_name = model_name
        print(f"[ModelManager] '{model_name}' loaded successfully.")

    def _unload(self):
        if self.current_model:
            print(f"[ModelManager] '{self.current_model_name}' unloaded.")
            self.current_model = None
            self.current_model_name = None

    def generate_response(self, prompt: str, stream: bool = False):
        if not self.current_model:
            raise RuntimeError("No model is currently loaded.")
        
        output = self.current_model(prompt,
            max_tokens=2048,
            temperature=0.7,
            top_p=0.9,
            stop=["\n\n"],
        ).choices[0].text.strip()

        return output

    




