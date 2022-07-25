import importlib.metadata
import importlib.resources
import json
import logging
import pprint
from dataclasses import asdict
from dataclasses import dataclass
from dataclasses import field
from dataclasses import fields
from pathlib import Path
from typing import Dict, Final, Optional

__all__ = (
    "__metadata_version__",
    "__title__",
    "__version__",
    "__summary__",
    "__author__",
    "__maintainer__",
    "__license__",
    "__url__",
    "__download_url__",
    "__project_urls__",
    "__copyright__",
    "__data_dir__",
)

metadata = importlib.metadata.metadata(__name__)

__metadata_version__: Final[Optional[str]] = metadata.get("metadata-version", None)

__title__: Final[Optional[str]] = metadata.get("name", None)
__version__: Final[Optional[str]] = metadata.get("version", None)
__summary__: Final[Optional[str]] = metadata.get("summary", None)
__author__: Final[Optional[str]] = metadata.get("author", None)
__maintainer__: Final[Optional[str]] = metadata.get("maintainer", __author__)
__license__: Final[Optional[str]] = metadata.get("license", None)
__url__: Final[Optional[str]] = metadata.get("home-page", None)
__download_url__: Final[Optional[str]] = metadata.get("download-url", None)
__project_urls__: Final[Dict[str, str]] = {
    values[0].strip(): values[1].strip()
    for url_str in metadata.get_all("project-url", tuple())
    if (values := url_str.split(","))
}

__copyright__: Final[str] = f"Copyright 2022 {__author__}"

__data_dir__: Final[Path] = (Path(__file__).parent / "data").resolve()

logger = logging.getLogger(__title__)


@dataclass
class Settings:
    version: int = 1
    last_settings_file: Path = field(
        default=Path("instance_settings.json"), metadata={"convert": Path}
    )

    @classmethod
    def load(cls, file: Path) -> None:
        if not file.exists():
            logger.info("Generating Default Settings")
            file.parent.mkdir(parents=True, exist_ok=True)
            file.write_text(json.dumps(asdict(cls()), indent=4))

        # This may error out if the json is malformed
        loaded: Dict[str, str] = json.loads(file.read_text())

        for cls_field in fields(cls):
            metadata = cls_field.metadata
            if cls_field.name not in loaded or loaded[cls_field.name] == "":
                logger.warning(
                    f"Config is missing '{cls_field.name}'. Defaulting to '{cls_field.default}'"
                )
                loaded[cls_field.name] = cls_field.default
            if "convert" in metadata:
                loaded[cls_field.name] = metadata["convert"](loaded[cls_field.name])

        for key, value in loaded.items():
            setattr(cls, key, value)

        logger.info("Config Loaded:\n%s", pprint.pformat(cls(**loaded)))
