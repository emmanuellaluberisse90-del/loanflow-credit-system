LoanFlow
Sistema de Pré-análise, Simulação e Agendamento de Crédito

O LoanFlow é um protótipo de sistema financeiro desenvolvido para demonstrar um fluxo simplificado de pré-análise de crédito, simulação de empréstimo e agendamento de atendimento em agência.

O projeto foi desenvolvido com foco em integração entre frontend, backend, regras de negócio e banco de dados.

Aviso: o LoanFlow é um projeto educacional e de portfólio. As regras de análise de crédito utilizadas são fictícias e não representam critérios reais de instituições financeiras.

Funcionalidades

O sistema permite:

Cadastro e consulta de clientes
Cadastro de perfil financeiro
Criação de solicitações de crédito
Pré-análise de crédito
Cálculo de comprometimento de renda
Simulação de empréstimos
Cálculo do valor das parcelas
Verificação de compatibilidade da parcela
Cadastro de agências
Consulta de horários disponíveis
Agendamento de atendimento
Cancelamento de agendamento
Interface web integrada à API
Fluxo do sistema
Cliente
   ↓
Solicitação
   ↓
Pré-análise
   ↓
Simulação
   ↓
Escolha da agência
   ↓
Escolha do horário
   ↓
Agendamento
   ↓
Confirmação
Arquitetura
React
   ↓
FastAPI
   ↓
Regras de negócio
   ↓
SQLAlchemy
   ↓
SQLite
Tecnologias utilizadas
Backend
Python
FastAPI
SQLAlchemy
SQLite
Uvicorn
Frontend
React
Vite
JavaScript
CSS
Ferramentas
Git
GitHub
Visual Studio Code
Swagger / OpenAPI
Principais módulos
Cliente

Armazena informações básicas do cliente, como:

Nome
CPF representado por hash fictício
Data de nascimento
Telefone
E-mail
Cidade
Status do cadastro
Perfil financeiro

Armazena informações utilizadas pela pré-análise:

Renda mensal
Tipo de renda
Tempo de renda
Outras rendas
Despesas mensais
Dívidas ativas
Histórico de pagamentos
Atrasos nos últimos 12 meses
Pré-análise

O sistema aplica regras simplificadas para verificar:

Renda mínima
Comprometimento de renda
Histórico de pagamentos
Atrasos recentes

O resultado pode ser:

aprovado

ou

nao_aprovado
Simulação

O usuário informa:

Valor desejado
Prazo em meses
Taxa mensal

O sistema calcula:

Valor da parcela
Valor total
Compatibilidade da parcela com a capacidade financeira simulada

Exemplo:

Valor: R$ 20.000,00
Prazo: 24 meses
Taxa: 2% ao mês

Parcela aproximada: R$ 1.057,42
Valor total: R$ 25.378,08
Agendamento

Depois da simulação, o usuário pode:

Selecionar uma agência
Consultar horários disponíveis
Selecionar um horário
Confirmar o atendimento

A confirmação apresenta:

Agência
Data
Horário
Status
ID do agendamento

O sistema também impede que uma mesma solicitação tenha mais de um agendamento ativo.

Estrutura do projeto
loanflow/
│
├── backend/
│   └── app/
│       ├── routes/
│       ├── rules/
│       ├── services/
│       ├── database.py
│       ├── models.py
│       ├── schemas.py
│       └── main.py
│
├── frontend/
│   ├── src/
│   │   ├── App.jsx
│   │   ├── App.css
│   │   └── main.jsx
│   ├── package.json
│   └── vite.config.js
│
├── loanflow.db
└── README.md
Como executar o projeto
1. Backend

Abra um terminal na pasta:

C:\Users\aluno\Documents\loanflow

Execute:

py -3.12 -m uvicorn backend.app.main:app --reload

A API estará disponível em:

http://127.0.0.1:8000

Documentação Swagger:

http://127.0.0.1:8000/docs
2. Frontend

Abra outro terminal e entre na pasta:

cd C:\Users\aluno\Documents\loanflow\frontend

Execute:

npm.cmd run dev

O frontend estará disponível em:

http://localhost:5173
Exemplo de fluxo

Um exemplo de utilização do sistema:

Solicitação: 1

Pré-análise
→ análise do perfil financeiro

Simulação
→ R$ 20.000
→ 24 meses
→ 2% ao mês

Agendamento
→ Agência Jandaia
→ 01/10/2026
→ 14:00 às 14:30

Resultado
→ Agendamento confirmado
Objetivo do projeto

O projeto foi desenvolvido como parte de um estudo prático envolvendo:

Desenvolvimento de APIs
Desenvolvimento frontend
Banco de dados
Regras de negócio
Integração entre sistemas
Desenvolvimento de aplicações financeiras
Organização de projetos para portfólio
Melhorias futuras

Algumas funcionalidades podem ser adicionadas futuramente:

Autenticação de usuários
Dashboard administrativo
Histórico de solicitações
Notificações
Testes automatizados
Docker
Deploy em nuvem
Integração com modelos de Machine Learning
Integração com LLMs para análise e explicação de dados
Status

Projeto funcional — MVP

O fluxo principal de pré-análise, simulação e agendamento está implementado e integrado entre frontend e backend.

Observação sobre dados

Os dados utilizados no projeto são fictícios e destinados exclusivamente a fins educacionais e de demonstração.