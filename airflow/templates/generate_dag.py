import fileinput
from handlers.base import BaseHandler
from pathlib import Path
import shutil
from typing import Type

def process(handler_class: Type[BaseHandler], static_args: dict = None):
    # TODO: create task function by:
    #   replacing "handler_class" with actual handler class
    #   save code text to new file
    template_dir = Path(__file__).parent
    task_wrapper_template_path = template_dir / "task_wrapper.py"
    task_path = template_dir / f"{handler_class.__name__}.py"
    shutil.copy(task_wrapper_template_path, task_path)
    for line in fileinput.input(task_path, inplace=True):
        line.replace()
    # TODO: create python operator:
    #   - import the saved handler 
    #   - put handler into python_callable argument
    #   - save DAG to new file
    # TODO: iterate over as many handlers as were passed in 
    pass


if __name__ == "__main__":
    # TODO: use sys args to get path to handler and args
    # TODO: import handler and call process
    pass