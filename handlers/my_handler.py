from handlers.base import BaseHandler
import logging
import numpy as np

class MyHandler(BaseHandler):
    
    def __init__(self, array_shape: tuple) -> None:
        self.shape = array_shape
    
    def handle(self, request: dict):
        x = np.zeros(self.shape)
        logging.info(f"Here's my array:\n\n{x}")
        return request