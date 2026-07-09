# Roadmap

Este documento apresenta o planejamento da evolução da plataforma.

O objetivo é construir uma solução completa de Engenharia de Dados para consumo dos dados públicos da ANATEL, preparada para automação, integração contínua e visualização no Power BI.

---

# Fase 1 — Fundação da Plataforma

## Sprint 1.1 ✅

* [x] Estrutura inicial do projeto
* [x] Ambiente virtual
* [x] Git
* [x] Requirements
* [x] pyproject.toml
* [x] .gitignore
* [x] Arquitetura inicial

---

## Sprint 1.2

Objetivo:

Construir a infraestrutura básica da biblioteca.

Entregas:

* [ ] `config.py`
* [ ] `logger.py`
* [ ] `exceptions.py`

---

## Sprint 1.3

Objetivo:

Implementar a camada de obtenção dos dados.

Entregas:

* [ ] Download automático do ZIP
* [ ] Leitura em memória
* [ ] Tratamento de exceções
* [ ] Testes

---

## Sprint 1.4

Objetivo:

Implementar a leitura dos arquivos CSV.

Entregas:

* [ ] Classe `Dataset`
* [ ] Leitura dinâmica por ano
* [ ] Múltiplos DataFrames

---

# Fase 2 — Processamento

## Sprint 2.1

* [ ] Padronização de colunas
* [ ] Conversão de tipos
* [ ] Limpeza dos dados

## Sprint 2.2

* [ ] Validação automática
* [ ] Controle de qualidade
* [ ] Relatório de inconsistências

---

# Fase 3 — Persistência

## Sprint 3.1

* [ ] Exportação para Parquet

## Sprint 3.2

* [ ] PostgreSQL
* [ ] Criação automática das tabelas
* [ ] Carga incremental

---

# Fase 4 — Automação

## Sprint 4.1

* [ ] GitHub Actions
* [ ] Atualização automática

## Sprint 4.2

* [ ] Agendamento diário
* [ ] Logs automáticos
* [ ] Notificações

---

# Fase 5 — Business Intelligence

## Sprint 5.1

* [ ] Conexão do Power BI ao PostgreSQL

## Sprint 5.2

* [ ] Atualização automática do Dashboard

---

# Fase 6 — Plataforma

## Versão 1.0

Objetivo final da plataforma:

* ETL totalmente automatizado
* Banco de dados centralizado
* Atualização sem intervenção manual
* Dashboard conectado diretamente ao banco
* Código modular e reutilizável
* Testes automatizados
* Documentação completa
* Integração contínua com GitHub Actions
