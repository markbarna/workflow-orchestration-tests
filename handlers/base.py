from abc import ABC

class BaseHandler(ABC):
    
    def __init__(self) -> None:
        super().__init__()
        
    def handle(self, request: dict):
        return request