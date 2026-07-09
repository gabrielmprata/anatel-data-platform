"""
Módulo de configuração da plataforma.

Centraliza os caminhos do projeto e garante que a estrutura de diretórios
necessária exista antes da execução dos pipelines.
"""

from dataclasses import dataclass, field
from pathlib import Path


@dataclass(frozen=True)
class Config:
    """Representa a configuração estrutural da plataforma."""

    project_root: Path = field(init=False)

    data_dir: Path = field(init=False)
    raw_data_dir: Path = field(init=False)
    processed_data_dir: Path = field(init=False)
    exports_data_dir: Path = field(init=False)

    logs_dir: Path = field(init=False)
    docs_dir: Path = field(init=False)
    tests_dir: Path = field(init=False)
    notebooks_dir: Path = field(init=False)

    def __post_init__(self) -> None:
        root = Path(__file__).resolve().parents[3]

        object.__setattr__(self, "project_root", root)

        object.__setattr__(self, "data_dir", root / "data")
        object.__setattr__(self, "raw_data_dir", root / "data" / "raw")
        object.__setattr__(self, "processed_data_dir",
                           root / "data" / "processed")
        object.__setattr__(self, "exports_data_dir", root / "data" / "exports")

        object.__setattr__(self, "logs_dir", root / "logs")
        object.__setattr__(self, "docs_dir", root / "docs")
        object.__setattr__(self, "tests_dir", root / "tests")
        object.__setattr__(self, "notebooks_dir", root / "notebooks")

        self._create_directories()

    def _create_directories(self) -> None:
        """Cria automaticamente os diretórios necessários."""

        directories = (
            self.data_dir,
            self.raw_data_dir,
            self.processed_data_dir,
            self.exports_data_dir,
            self.logs_dir,
        )

        for directory in directories:
            directory.mkdir(parents=True, exist_ok=True)
            # parents=True cria toda a hierarquia se necessário | exist_ok=True não gera erro se a pasta já existir
