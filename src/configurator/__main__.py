import logging
import sys
import traceback
from typing import Any, Optional

import configurator


def main(*argv: str) -> Optional[Any]:
    try:
        print(argv)
        return 0
    except Exception as e:
        logger = logging.getLogger(configurator.__title__)
        logger.critical(
            f"An Exception caused the program to exit:"
            f"\n{''.join(traceback.format_exception(e))}"
        )
        return 1


if __name__ == "__main__":
    sys.exit(main(*sys.argv[1:]))
