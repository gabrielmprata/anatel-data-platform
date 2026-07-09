# Changelog

Todas as mudanças relevantes deste projeto serão documentadas neste arquivo.

O formato é baseado em **Keep a Changelog** e segue os princípios do **Semantic Versioning (SemVer)**.

---

## [0.1.0] - 2026-07-08

### Added

* Estrutura inicial do projeto.
* Organização das pastas (`src`, `tests`, `docs`, `data` e `notebooks`).
* Criação do ambiente virtual (`venv`).
* Configuração inicial do projeto Python (`pyproject.toml`).
* Arquivo `requirements.txt` com as dependências do projeto.
* Arquivo `.gitignore`.
* Estrutura inicial dos módulos:

  * `config.py`
  * `downloader.py`
  * `extractor.py`
  * `dataset.py`
  * `logger.py`
  * `exceptions.py`
* Definição da arquitetura inicial da plataforma.

---

## Próximas versões

### [0.2.0] - Planejado

* Implementação do módulo `config.py`.
* Implementação do módulo `downloader.py`.

### [0.3.0] - Planejado

* Implementação do módulo `extractor.py`.
* Criação da classe `Dataset`.

### [0.4.0] - Planejado

* Transformações dos dados.
* Validações.

### [0.5.0] - Planejado

* Exportação para Parquet.

### [0.6.0] - Planejado

* Integração com PostgreSQL.

### [0.7.0] - Planejado

* Automação utilizando GitHub Actions.

### [1.0.0]

Primeira versão estável da plataforma contendo:

* Download automático dos dados da ANATEL.
* ETL completo.
* Banco PostgreSQL.
* Integração com Power BI.
* Documentação completa.
* Testes automatizados.
