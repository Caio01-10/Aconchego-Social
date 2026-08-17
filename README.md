# 🕊️ Aconchego Social

> **Trabalho de Banco de Dados — Sistema Web com CRUD Acessível**  
> **Professora:** Camille Braga  
> **Tecnologias:** Python, Flask, SQLite, HTML5 e CSS3

---

## 📌 1. Sobre o Projeto e Justificativa

O **Aconchego Social** é uma aplicação web desenvolvida para gerenciar doações (brinquedos, roupas, alimentos e itens de higiene) destinadas a casas de acolhimento e abrigos parceiros.

### 💡 Justificativa
Centros de acolhimento muitas vezes enfrentam dificuldades na organização e controle do fluxo de doações recebidas e das demandas pendentes. O sistema resolve esse problema ao permitir a gestão centralizada do inventário de recursos vinculados a cada abrigo, possibilitando cadastrar, consultar com filtros, atualizar o status e excluir doações de forma intuitiva e acessível.

---

## 🗄️ 2. Modelagem do Banco de Dados

O banco de dados foi construído em **SQLite** e conta com duas entidades (tabelas) em um relacionamento **1:N (Um-para-Muitos)**:

### Diagrama Lógico / Tabelas

1. **`abrigo`** (Ponto de Acolhimento):
   - `id` (INTEGER, PRIMARY KEY, AUTOINCREMENT)
   - `nome` (TEXT, NOT NULL)
   - `cidade` (TEXT, NOT NULL)
   - `responsavel` (TEXT)
   - `telefone` (TEXT)

2. **`doacao`** (Recursos / Suprimentos):
   - `id` (INTEGER, PRIMARY KEY, AUTOINCREMENT)
   - `item` (TEXT, NOT NULL)
   - `categoria` (TEXT, NOT NULL) — Ex: Brinquedo, Roupa, Alimento
   - `detalhes` (TEXT) — Observações como tamanho ou validade
   - `quantidade` (INTEGER, NOT NULL)
   - `status` (TEXT, NOT NULL) — Ex: Pendente, Recebido, Entregue
   - `abrigo_id` (INTEGER, FOREIGN KEY -> `abrigo(id)`)

---

## ♿ 3. Diretrizes de Acessibilidade Implementadas (WCAG)

A interface foi projetada para garantir a melhor usabilidade para todos os públicos, seguindo as normas da WCAG:

- **Contraste de Cores:** Combinação de texto escuro (`#111827`) sobre fundo claro (`#FAF9F5`) com taxa de contraste superior a **15:1** (superando o mínimo exigido de 4.5:1).
- **Rótulos nos Formulários:** Todos os elementos `<input>` e `<select>` possuem tags `<label>` associadas diretamente com a propriedade `for`.
- **Navegação por Teclado:** Foco visível destacado (`outline: 3px solid #0284C7`) em botões e links durante a navegação pelas teclas <kbd>Tab</kbd> e <kbd>Enter</kbd>.
- **Área de Clique:** Botões e links possuem dimensão mínima clicável de **44x44px** para facilitar a interação em telas sensíveis ao toque.
- **Mensagens Informativas:** Avisos de erro, sucesso ou exclusão combinam cores, textos explicativos e ícones/símbolos indicativos.
- **HTML Semântico:** Estruturação através das tags `<header>`, `<nav>`, `<main>`, `<table>` e `<footer>`.

---

## 🛠️ 4. Estrutura do Projeto

```text
Aconchego-Social/
├── app.py                  # Servidor Flask e definição de rotas do CRUD
├── banco.db                # Banco de dados relacional SQLite
├── model.py          # Script SQL para criação das tabelas e carga inicial
├── static/
│   └── css/
│       └── style.css       # Estilização global com regras de acessibilidade
└── templates/
    ├── base.html           # Layout base e navegação
    ├── index.html          # Página principal (Home)
    ├── cadastrar.html      # Formulário de cadastro (Create)
    ├── consultar.html      # Tabela de listagem e busca (Read & Delete)
    └── editar.html         # Formulário de atualização (Update)
...