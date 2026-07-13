from pathlib import Path
from datetime import datetime
import logging


class LoggerFactory:

    @staticmethod
    def create(pipeline_name: str) -> logging.Logger:

        # ======================================================
        # Pasta de logs
        # ======================================================

        log_dir = Path("logs")
        log_dir.mkdir(parents=True, exist_ok=True)

        # ======================================================
        # Nome do arquivo
        # ======================================================

        timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")

        log_file = log_dir / f"{pipeline_name}_{timestamp}.log"

        # ======================================================
        # Logger
        # ======================================================

        logger = logging.getLogger(pipeline_name)

        logger.setLevel(logging.INFO)

        # ======================================================
        # Evita adicionar múltiplos handlers
        # ======================================================

        if not logger.handlers:

            file_handler = logging.FileHandler(
                filename=log_file,
                encoding="utf-8"
            )

            formatter = logging.Formatter(
                fmt="%(asctime)s | %(levelname)s | %(name)s | %(message)s",
                datefmt="%Y-%m-%d %H:%M:%S"
            )

            file_handler.setFormatter(formatter)

            logger.addHandler(file_handler)

        return logger
