import os
from pydantic import BaseModel, PrivateAttr
from typing import Literal, Optional
from utils.config_loader import ConfigLoader
from langchain_groq import ChatGroq   
from langchain_community.chat_models import ChatOpenAI



class ModelLoader(BaseModel):
    model_provider: Literal["groq", "openai"] = "groq"
    
    # Use PrivateAttr for config — NOT a normal field
    _config: Optional[ConfigLoader] = PrivateAttr(default_factory=ConfigLoader)

    def __init__(self, **data):
        super().__init__(**data)
        # Initialize config explicitly if needed
        self._config = ConfigLoader()

    def load_llm(self):
        print("LLM loading...")
        print(f"Loading model from provider: {self.model_provider}")
        if self.model_provider == "groq":
            groq_api_key = os.getenv("GROQ_API_KEY")
            model_name = self._config["llm"]["groq"]["model_name"]
            llm = ChatGroq(model=model_name, api_key=groq_api_key)
        elif self.model_provider == "openai":
            openai_api_key = os.getenv("OPENAI_API_KEY")
            model_name = self._config["llm"]["openai"]["model_name"]
            llm = ChatOpenAI(model_name=model_name, api_key=openai_api_key)
        return llm
