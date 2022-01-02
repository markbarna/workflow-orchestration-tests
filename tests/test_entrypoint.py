from handlers.entrypoint import main
from pathlib import Path
import sys


class TestEntrypoint:
    
    def test_entrypoint(self, tmp_path: Path):
        save_path = (tmp_path / "array.npy").as_posix()
        args = [
            "MyHandler",
            "-a",
            "(2,3)",
            save_path
        ]
        main(args)
