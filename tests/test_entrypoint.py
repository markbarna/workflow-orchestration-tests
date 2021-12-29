from handlers import entrypoint
from pathlib import Path
import sys


# TODO: Mock the parser -->
# Namespace(handler_name='MyHandler', args=['(2,3)'], request=None)

class TestEntrypoint:
    
    def test_entrypoint(self, tmp_path: Path):
        save_path = (tmp_path / "array.npy").as_posix()
        entrypoint.main()
