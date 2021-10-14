from argparse import ArgumentParser


def get_parser() -> ArgumentParser:
    parser: ArgumentParser = ArgumentParser()
    parser.add_argument("path", type=str, help="Addressables build layout file path")
    parser.add_argument("-d", action="store_true", help="enable debug functionality")
    parser.add_argument("--address", type=str, default="127.0.0.1", help="App address")
    parser.add_argument("--port", type=int, default=8050, help="App port")
    parser.add_argument("--theme", type=str, default="dark", choices=["dark", "light"], help="app theme")

    return parser
