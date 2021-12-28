from numpy.lib.npyio import save
from handlers import MyHandler, MyConsumerHandler
import numpy as np
from pathlib import Path

def test_my_handler(tmp_path: Path):
    save_path = (tmp_path / "array.npy").as_posix()
    handler = MyHandler((4,2), out_path=save_path)
    handler.handle({})
    
def test_my_consumer(tmp_path: Path):
    x = np.ones((5,5))
    array_path = (tmp_path / "array.npy").as_posix()
    np.save(array_path, x)
    handler = MyConsumerHandler()
    handler.handle({"array_path": array_path})