import logging
from dataclasses import dataclass
from pathlib import Path


@dataclass
class AppConfig:
    """Central configuration for the application paths and settings."""

    input_dir: Path
    output_dir: Path
    log_file: Path | None = None
    log_level: str = "INFO"

    def __post_init__(self):
        """Ensure directories exist."""
        self.input_dir = Path(self.input_dir).resolve()
        self.output_dir = Path(self.output_dir).resolve()

        self.output_dir.mkdir(parents=True, exist_ok=True)

        if self.log_file:
            self.log_file = Path(self.log_file).resolve()
            self.log_file.parent.mkdir(parents=True, exist_ok=True)

    def setup_logging(self):
        """Configures the logging system based on the current config."""
        handlers: list[logging.Handler] = [logging.StreamHandler()]

        if self.log_file:
            handlers.append(logging.FileHandler(self.log_file))

        logging.basicConfig(
            level=getattr(logging, self.log_level.upper(), logging.INFO),
            format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
            handlers=handlers,
        )
        logging.info("Logging initialized.")
