# 🕊️ Aconchego Social

> **Trabalho de Banco de Dados — Sistema Web com CRUD Acessível**  
> **Professora:** Camille Braga  
> **Tecnologias:** Python, Flask, SQLite, HTML5 e CSS3

---

## 📌 1. Sobre o Projeto e Justificativa

O **Aconchego Social** é uma aplicação web desenvolvida para gerenciar doações (brinquedos, roupas, alimentos e itens de higiene) destinadas a casas de acolhimento e abrigos parceiros.

### 💡 Justificativa
Centros de acolhimento muitas vezes enfrentam dificuldades na organização e controle do fluxo de doações recebidas e das demandas pendentes[cite: 1]. O sistema resolve esse problema ao permitir a gestão centralizada do inventário de recursos vinculados a cada abrigo, possibilitando cadastrar, consultar com filtros, atualizar o status e excluir doações de forma intuitiva e acessível[cite: 1].

---

## 🗄️ 2. Modelagem do Banco de Dados

O banco de dados foi construído em **SQLite** e conta com duas entidades (tabelas) em um relacionamento **1:N (Um-para-Muitos)**[cite: 1]:

### Diagrama Lógico / Tabelas

1. **`abrigo`** (Ponto de Acolhimento):
   - `id` (INTEGER, PRIMARY KEY, AUTOINCREMENT)[cite: 1]
   - `nome` (TEXT, NOT NULL)[cite: 1]
   - `cidade` (TEXT, NOT NULL)[cite: 1]
   - `responsavel` (TEXT)[cite: 1]
   - `telefone` (TEXT)[cite: 1]

2. **`doacao`** (Recursos / Suprimentos):
   - `id` (INTEGER, PRIMARY KEY, AUTOINCREMENT)[cite: 1]
   - `item` (TEXT, NOT NULL)[cite: 1]
   - `categoria` (TEXT, NOT NULL) — Ex: Brinquedo, Roupa, Alimento[cite: 1]
   - `detalhes` (TEXT) — Observações como tamanho ou validade[cite: 1]
   - `quantidade` (INTEGER, NOT NULL)[cite: 1]
   - `status` (TEXT, NOT NULL) — Ex: Pendente, Recebido, Entregue[cite: 1]
   - `abrigo_id` (INTEGER, FOREIGN KEY -> `abrigo(id)`)[cite: 1]

---

## ♿ 3. Diretrizes de Acessibilidade Implementadas (WCAG)

A interface foi projetada para garantir a melhor usabilidade para todos os públicos, seguindo as normas da WCAG[cite: 1]:

- **Contraste de Cores:** Combinação de texto escuro (`#111827`) sobre fundo claro (`#FAF9F5`) com taxa de contraste superior a **15:1** (superando o mínimo exigido de 4.5:1)[cite: 1].
- **Rótulos nos Formulários:** Todos os elementos `<input>` e `<select>` possuem tags `<label>` associadas diretamente com a propriedade `for`[cite: 1].
- **Navegação por Teclado:** Foco visível destacado (`outline: 3px solid #0284C7`) em botões e links durante a navegação pelas teclas <kbd>Tab</kbd> e <kbd>Enter</kbd>[cite: 1].
- **Área de Clique:** Botões e links possuem dimensão mínima clicável de **44x44px** para facilitar a interação em telas sensíveis ao toque[cite: 1].
- **Mensagens Informativas:** Avisos de erro, sucesso ou exclusão combinam cores, textos explicativos e ícones/símbolos indicativos[cite: 1].
- **HTML Semântico:** Estruturação através das tags `<header>`, `<nav>`, `<main>`, `<table>` e `<footer>`[cite: 1].

---

## 🛠️ 4. Estrutura do Projeto

```text
Aconchego-Social/
├── app.py                  # Servidor Flask e definição de rotas do CRUD[cite: 1]
├── banco.db                # Banco de dados relacional SQLite[cite: 1]
├── criar_banco.py          # Script SQL para criação das tabelas e carga inicial[cite: 1]
├── static/
│   └── css/
│       └── style.css       # Estilização global com regras de acessibilidade[cite: 1]
└── templates/
    ├── base.html           # Layout base e navegação[cite: 1]
    ├── index.html          # Página principal (Home)[cite: 1]
    ├── cadastrar.html      # Formulário de cadastro (Create)[cite: 1]
    ├── consultar.html      # Tabela de listagem e busca (Read & Delete)[cite: 1]
    └── editar.html         # Formulário de atualização (Update)[cite: 1]