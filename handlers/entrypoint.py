from argparse import ArgumentParser
import logging
from importlib import import_module
import sys

def main(args: list):
    parser = ArgumentParser(description="Entrypoint for pipeline handlers")
    parser.add_argument(
        "handler_name",
        choices=["MyHandler", "MyConsumerHandler"]
    )
    parser.add_argument(
        "-a", "--args",
        nargs="*",
        default=tuple()
    )
    parser.add_argument(
        "-r", "--request",
        nargs="*",
        default=dict()
    )
    parsed = parser.parse_args(args)
    logging.info(f"parsed args {parsed}")
    
    handler_cls = getattr(import_module(name="handlers"), parsed.handler_name)
    hander = handler_cls(*parsed.args)
    request = dict(**parsed.request)
    hander.handle(request)

if __name__ == "__main__":
    main(sys.argv[1:])
