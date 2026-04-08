<img width="512" height="122" alt="image" src="https://github.com/user-attachments/assets/501c7a12-66df-4103-b0e9-705825cd0276" />


Curso: Engenharia de Software
Disciplica: Laboratório de Backend
Professor: Fabricio Dias
Aluno: Yago da Costa Jardim Alves Braga
---

# 📝 CRUD FastAPI com MongoDB e Docker

Este projeto consiste em uma aplicação backend para gerenciamento de **Tarefas (Tasks)**, desenvolvida utilizando o framework **FastAPI**, o banco de dados **MongoDB** e totalmente conteinerizada com **Docker**.

O projeto atende aos requisitos de arquitetura modular, utilização de NoSQL e persistência de dados em ambiente isolado.

---

## 🚀 Tecnologias Utilizadas
* **FastAPI:** Framework moderno e rápido para construção de APIs.
* **MongoDB:** Banco de dados NoSQL orientado a documentos.
* **Docker & Docker Compose:** Para orquestração da aplicação e do banco de dados.
* **PyMongo:** Driver oficial para integração entre Python e MongoDB.
* **Pydantic:** Para validação de dados e schemas.

---

## 🏗️ Arquitetura do Projeto
O projeto segue uma **arquitetura modular**, organizada da seguinte forma:

* \`config/\`: Configurações de conexão e variáveis de ambiente.
* \`models/\`: Definição dos Schemas de dados e validações.
* \`repositories/\`: Camada de acesso aos dados (CRUD).
* \`routes/\`: Definição das rotas/endpoints da API.
* \`services/\`: Lógica de negócio da aplicação.

---

## 📋 Schema da Aplicação (Tasks)
Entidade **Task** configurada com os 4 atributos obrigatórios:
1. \`titulo\` (string)
2. \`descricao\` (string)
3. \`prioridade\` (int)
4. \`finalizada\` (bool)

---

## 🛠️ Como Executar a Aplicação

Certifique-se de ter o **Docker** instalado.

1. Clone o repositório:
   \`\`\`bash
   git clone https://github.com/yagojardimm/crud-fastapi-mongodb.git
   cd crud-fastapi-mongodb
   \`\`\`

2. Suba os containers:
   \`\`\`bash
   docker-compose up --build
   \`\`\`

3. Acesse a documentação automática (Swagger):
   * URL: [http://localhost:8000/docs](http://localhost:8000/docs)

---

## 📡 Endpoints Disponíveis
* **POST /tasks/**: Criar tarefa.
* **GET /tasks/**: Listar todas.
* **GET /tasks/{id}**: Buscar por ID.
* **PUT /tasks/{id}**: Atualizar tarefa.
* **DELETE /tasks/{id}**: Remover tarefa.
EOF
