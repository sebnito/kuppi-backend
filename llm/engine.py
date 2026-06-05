
class LLMengine:
    def __init__(self):
        self.current_model = None
    
    def generate(self, model_name: str, prompt: str, on_thinking = None):
        if on_thinking:
            on_thinking(f"กำลังโหลด {model_name}...")
        
        