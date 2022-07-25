import logging
import logging.handlers
import pprint
import sys
import traceback
from argparse import ArgumentParser
from dataclasses import dataclass
from dataclasses import field
from dataclasses import fields
from pathlib import Path
from typing import Any, List, Optional, Sequence, Type, TypeVar

import wx

import configurator
import configurator.gui.configurator

T = TypeVar("T")


@dataclass(frozen=True)
class Arguments:
    verbose: bool = field(
        metadata={
            "name_or_flags": ["-v", "--verbose"],
            "default": False,
            "required": False,
            "action": "store_true",
            "help": "Show verbose output",
        }
    )
    settings: Path = field(
        metadata={
            "name_or_flags": ["-c", "--settings"],
            "default": "./settings.json",
            "required": False,
            "help": 'The path to the settings file. [default: "./settings.json"]',
            "convert": (lambda string: Path(string).resolve()),
        }
    )

    @classmethod
    def from_args(cls: Type[T], args: Sequence[str]) -> T:
        """Generate the Settings from parsed arguments."""
        parser = ArgumentParser(prog=f"{configurator.__title__} {cls.__name__.lower()}")

        for cls_field in fields(cls):
            metadata = dict(cls_field.metadata)
            metadata.pop("convert", None)
            name_or_flags = tuple(
                metadata.pop("name_or_flags") if "name_or_flags" in metadata else []
            )
            parser.add_argument(*name_or_flags, **metadata)

        parsed = vars(parser.parse_args(args))

        for cls_field in fields(cls):
            metadata = cls_field.metadata
            if "convert" in metadata and (value := parsed[cls_field.name]) is not None:
                parsed[cls_field.name] = metadata["convert"](value)

        return cls(**parsed)


# logger = logging.getLogger(__name__)
# logger.parent = logging.getLogger(configurator.__title__)


def main(*args: str) -> Optional[Any]:
    formatter = logging.Formatter(
        fmt="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
        datefmt="%Y-%m-%d %I:%M:%S",  # yyyy-MM-dd HH:mm:ss
        style="%",
        validate=True,
    )

    console_handler = logging.StreamHandler(stream=sys.stdout)
    console_handler.setFormatter(formatter)
    console_handler.setLevel(logging.INFO)

    log_file_path: Path = Path("./configurator.log")
    log_file_exists = log_file_path.exists()

    file_handler = logging.handlers.RotatingFileHandler(
        log_file_path, mode="w", backupCount=5
    )
    file_handler.setFormatter(formatter)
    file_handler.setLevel(logging.INFO)
    if log_file_exists:
        file_handler.doRollover()

    root_logger = logging.getLogger(configurator.__title__)
    root_logger.propagate = True
    root_logger.setLevel(logging.DEBUG)
    root_logger.handlers = [console_handler, file_handler]

    arguments: Arguments = Arguments.from_args(args)

    if arguments.verbose:
        console_handler.setLevel(logging.DEBUG)
        file_handler.setLevel(logging.DEBUG)

    root_logger.info(pprint.pformat(arguments))

    try:
        app = wx.App()
        configurator.gui.configurator.Configurator(None).Show(True)
        return app.MainLoop()
    except Exception as e:
        root_logger.critical(
            f"An Exception caused the program to exit:"
            f"\n{''.join(traceback.format_exception(e))}"
        )
        return 1


if __name__ == "__main__":
    sys.exit(main(*sys.argv[1:]))
