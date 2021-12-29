from handlers.base import BaseHandler
import logging
import numpy as np

class MyHandler(BaseHandler):
    
    def __init__(self, array_shape: tuple, out_path: str) -> None:
        self.shape = array_shape
        self.out_path = out_path
    
    def handle(self, request: dict):
        x = np.zeros(self.shape)
        np.save(self.out_path, x)
        logging.info(f"Generated array:\n\n{x}\n\nSaved to {self.out_path}")
        request.update({"array_path": self.out_path})
        return request
