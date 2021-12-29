from handlers.base import BaseHandler
import logging
import numpy as np


class MyConsumerHandler(BaseHandler):
    
    def __init__(self) -> None:
        super().__init__()
        
    def handle(self, request: dict):
        read_path = request["array_path"]
        x = np.load(read_path)
        logging.info(f"Read array from {read_path}:\n\n{x}")
        return request  
