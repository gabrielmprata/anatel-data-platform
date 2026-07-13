# Changelog

Todas as mudanças relevantes deste projeto serão documentadas neste arquivo.

O projeto segue o padrão **Keep a Changelog** e utiliza **Versionamento Semântico (SemVer)**.

---

## [0.1.0] - 2026-07-09

### 🎉 Primeira versão da plataforma

Esta versão estabelece a fundação arquitetural do projeto.

### Adicionado

* Estrutura modular baseada em `src/`
* Organização em módulos:

  * `core`
  * `io`
  * `models`
  * `pipelines`
* Configuração utilizando `pyproject.toml`
* Ambiente virtual (`venv`)
* Projeto instalável com `pip install -e .`
* Classe `Config`
* Hierarquia de exceções personalizadas
* Testes automatizados com `pytest`

### Alterado

* Reorganização completa da arquitetura do projeto.

### Próxima versão

**v0.2.0**

* Sistema de Logging
* Download Manager
* Estrutura de logs da plataforma
