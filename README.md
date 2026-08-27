# Em desenvolvimento

```mermaid
flowchart LR

    subgraph Fonte
        A["Portal de Dados Abertos da ANATEL"]
    end

    subgraph ETL
        B["Download do ZIP"]
        C["BytesIO"]
        D["ZipFile"]
        E["Leitura dos CSVs"]
    end

    subgraph Processamento
        F["DataFrame_<<param_ano>>"]
        G["DataFrame_<<param_ano>>"]
        H["Tratamento"]
        I["Padronização"]
    end

    subgraph Saída
        J["Power BI"]
        K["Parquet"]
        L["Análises Estatísticas"]
    end

    A --> B
    B --> C
    C --> D
    D --> E
    E --> F
    E --> G
    F --> H
    G --> H
    H --> I
    I --> J
    I --> K
    I --> L
```

```mermaid
architecture-beta
    group sources(cloud)[Sources]
        service src_a(server)[SCM] in sources
        service src_b(server)[Reclamacoes] in sources
        service src_c(server)[SMP] in sources

    group storage(database)[Storage]
        service db_one(database)[Aiven] in storage
        service db_two(database)[Neon] in storage
        service db_three(database)[Aiven] in storage

    group output(disk)[Output]
        service brief(disk)[Brief] in output
        service analyst(server)[Analyst] in output
        service delivery(cloud)[Delivery] in output

    src_a:B --> T:db_one
    src_b:B --> T:db_two
    src_c:B --> T:db_three
    db_two:B --> T:brief
    brief:R --> L:analyst
    analyst:R --> L:delivery

    align row src_a src_b src_c
    align row db_one db_two db_three
    align row brief analyst delivery

    align column src_a db_one
    align column src_b db_two brief
    align column src_c db_three
```

# Painel Telefonia Móvel

---

# Fase 1 — Fundação da Plataforma

## Sprint 1.1 ✅

* [x] Estrutura inicial do projeto
* [x] Ambiente virtual
* [x] Git
* [x] Requirements
* [x] .gitignore
* [x] Arquitetura inicial

---

## Sprint 1.2 ✅

Objetivo:

Construir a infraestrutura básica da biblioteca.

Entregas:

* [x] `config.py`
* [x] `log.py`
* [x] `extract.py`
* [x] `transform.py`

---

## Sprint 1.3 

Objetivo:

Construir o modelo relacional (Star Schema).

Entregas:

* [x] df_acessos_movel
* [x] df_reclamacao
* [x] dm_geracao
* [x] dm_tipo_produto
* [x] dm_porte_prestadora
* [x] dm_populacao
* [x] dm_modalidade_cobranca
* [x] dm_calendario

---
