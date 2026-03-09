from pathlib import Path
class Agent07:
    def __init__(self, system_prompt_path: str):
        self.system_prompt = self._load_system_prompt(system_prompt_path)

    def _load_system_prompt(self, path:str) -> str:
        file_path = Path(path)
        if not file_path.exists():
            raise FileNotFoundError(f"system prompt not found: {path}")
        return file_path.read_text(encoding="utf-8")
    
    def build_response(self, user_input:str) -> list[dict[str,str]]:
        """
        Constructs response strictly from:
        - system prompt (agent_07_system.md)
        - user input
        """
        return [
            {"role": "system", "content": self.system_prompt},
            {"role":"user", "content": user_input}
        ]
        