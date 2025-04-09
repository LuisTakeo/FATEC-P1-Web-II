# 🌐 PROVA DESENVOLVIMENTO WEB1

📌 Projeto desenvolvido por **Luis Takeo** e **Vinicius Lima**  

---

## 📝 Resumo

Este repositório contém uma aplicação web baseada na arquitetura **MVC (Model-View-Controller)**, voltada para o gerenciamento de **produtos e usuários**. O sistema implementa operações completas de **CRUD**, com persistência de dados em um banco **MySQL**. As interfaces de cadastro incluem **validação rigorosa de dados**, assegurando integridade e consistência. A estrutura do projeto foi segmentada em pastas específicas para facilitar manutenção e escalabilidade.

---

## 🎯 Cenário

Uma empresa necessita de um sistema funcional para **cadastrar, consultar, atualizar e excluir** produtos. O projeto foi desenvolvido como uma solução prática para essa necessidade, com suporte também à gestão de usuários.

---

## 🛠️ Tecnologias e Arquitetura

- **Linguagem Backend:** Python  
- **Framework:** FastAPI  
- **Banco de Dados:** MySQL  
- **Arquitetura:** MVC  
- **API:** RESTful  

### 📁 Estrutura de Pastas

- **controllers/** – Responsável por processar requisições, chamar os models e retornar as respostas.  
- **models/** – Define as estruturas de dados e realiza operações no banco (ex: Produto, Usuário).  
- **views/** – Contém as páginas HTML renderizadas para o usuário final.  
- **database/** – Guarda a lógica de conexão com o banco e scripts SQL necessários.  
- **templates/** – Armazena layouts base, cabeçalhos, rodapés e partes reutilizáveis nas views.  
- **main.py** – Inicializa a aplicação e configura as rotas principais.


---

## ⚙️ Funcionalidades

### 📦 Produtos

| Método | Rota               | Descrição                        |
|--------|--------------------|----------------------------------|
| GET    | /produtos          | Retorna todos os produtos        |
| GET    | /produtos/{id}     | Busca produto específico         |
| POST   | /produtos          | Cria novo produto (validação)   |
| PUT    | /produtos/{id}     | Atualiza produto existente       |
| DELETE | /produtos/{id}     | Remove produto                   |

### 👤 Usuários

| Método | Rota              | Descrição                          |
|--------|-------------------|------------------------------------|
| GET    | /usuarios         | Lista todos os usuários            |
| GET    | /usuarios/{id}    | Retorna um usuário específico      |
| POST   | /usuarios         | Adiciona novo usuário              |
| PUT    | /usuarios/{id}    | Edita dados de usuário             |
| DELETE | /usuarios/{id}    | Deleta usuário                     |

---

## ✅ Regras de Validação

### Produto

- **nome**: mínimo de 3 caracteres  
- **preço**: valor positivo obrigatório  
- **estoque**: número inteiro ≥ 0  

### Usuário

- Verificação de **nome**, **e-mail** e **senha**  
- Em caso de erro, o sistema retorna mensagens claras de correção  

---

## 🚧 Desafios Enfrentados e Soluções

🔹 **Reestruturação do Código-Fonte**  
Com o crescimento do projeto, a base de código foi modularizada, separando responsabilidades entre **Controllers**, **Models**, **Serviços** e **Rotas**, garantindo organização e manutenção facilitada.

🔹 **Tratamento de Requisições Inválidas**  
Para evitar falhas em atualizações e exclusões, foram criadas verificações de existência do registro, retornando **HTTP 404** quando necessário.

🔹 **Validações no Servidor**  
Foram criadas **camadas de verificação centralizadas** para garantir que apenas dados válidos chegassem ao banco, promovendo consistência e segurança.

🔹 **Configuração da Conexão com MySQL**  
Dificuldades iniciais foram resolvidas com consulta à documentação e ajustes precisos na **string de conexão e configuração do ORM**.

---

## 📚 Fontes e Materiais de Apoio

- [Documentação do MySQL](https://dev.mysql.com/doc/)  
- [FastAPI – Documentação Oficial](https://fastapi.tiangolo.com/) 
[Martin Fowler – GUI Architectures (MVC explanation)](https://martinfowler.com/eaaDev/uiArchs.html) 

---

## 🏁 Considerações Finais

A construção deste sistema proporcionou uma vivência completa no desenvolvimento de aplicações web com foco em **organização de código, padronização de rotas e segurança dos dados**. O uso da arquitetura **MVC** se mostrou essencial para manter o projeto limpo, coeso e fácil de escalar.

Além da consolidação de conceitos técnicos, a experiência trouxe aprendizados valiosos sobre:

- A importância de **dividir responsabilidades** entre camadas da aplicação  
- Como **boas práticas de validação** evitam inconsistências no banco de dados  
- A relevância de um projeto bem estruturado para futuras **evoluções e integrações**# FATEC-P1-Web-II
