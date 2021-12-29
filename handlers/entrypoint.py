from argparse import ArgumentParser
from importlib import import_module
import pathlib


def main():
    parser = ArgumentParser(description="Entrypoint for pipeline handlers")
    parser.add_argument(
        "handler_name",
        choices=["MyHandler", "MyConsumerHandler"]
    )
    parser.add_argument(
        "-a", "--args",
        nargs="*"
    )
    parser.add_argument(
        "-r", "--request",
        nargs="*"
    )
    parsed = parser.parse_args()
    print(parsed)
    
    handler_cls = import_module(name=parsed.handler_name, package="my_handler")
    hander = handler_cls(parsed.args)
    request = dict(**parsed.request)
    hander.handle(request)

if __name__ == "__main__":
    main()
