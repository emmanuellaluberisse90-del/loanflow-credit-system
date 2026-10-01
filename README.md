LoanFlow — Credit System

A web application for credit pre-analysis, loan simulation, and appointment scheduling.

This project was developed as an educational and portfolio prototype using FastAPI, React, and SQLite.

Disclaimer: LoanFlow does not represent the actual rules of any financial institution. All business rules and data used in this project are fictional and intended for educational purposes only.

Features
Customer registration
Financial profile registration
Credit request creation
Rule-based credit pre-analysis
Loan simulation
Installment affordability verification
Bank branch registration and consultation
Available time slot consultation
Appointment scheduling
Appointment cancellation
Web interface integrated with the backend
System Flow
Identification
      ↓
Registration Verification
      ↓
Credit Pre-analysis
      ↓
Loan Simulation
      ↓
Appointment Scheduling
      ↓
Customer Service
Architecture
React Frontend
       ↓
FastAPI Backend
       ↓
Business Rules
       ↓
SQLite Database
Technologies
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
HTML
CSS
Tools
Git
GitHub
VS Code
Modules

The system is organized into the following modules:

Customer
Financial Profile
Credit Request
Credit Pre-analysis
Loan Simulation
Bank Branch
Time Slot
Appointment
Simulation Example

Example used during system testing:

Information	Value
Requested amount	R$ 20,000.00
Term	24 months
Monthly rate	2%
Approximate installment	R$ 1,057.42
Approximate total amount	R$ 25,378.08

The values above are examples for testing purposes only.

Appointment Scheduling

The user can:

Select a bank branch;
View available time slots;
Select a time slot;
Confirm the appointment.

After an appointment is created, the selected time slot becomes unavailable.

An appointment can also be cancelled. When this happens, the time slot becomes available again.

Project Structure
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
├── .gitignore
└── README.md
How to Run
1. Backend

Open PowerShell in the project directory:

cd C:\Users\aluno\Documents\loanflow

Run:

py -3.12 -m uvicorn backend.app.main:app --reload

The API will be available at:

http://127.0.0.1:8000

Swagger API documentation:

http://127.0.0.1:8000/docs
2. Frontend

Open another PowerShell terminal:

cd C:\Users\aluno\Documents\loanflow\frontend

Run:

npm.cmd run dev

The application will be available at:

http://localhost:5173
Example Workflow
1. Enter the credit request ID
            ↓
2. Run credit pre-analysis
            ↓
3. Enter amount, term, and interest rate
            ↓
4. Run loan simulation
            ↓
5. Load bank branches
            ↓
6. Select a branch
            ↓
7. Select an available time slot
            ↓
8. Schedule the appointment
Project Goals

The goal of LoanFlow is to demonstrate practical knowledge of:

REST API development;
Python and FastAPI;
Database modeling;
SQLAlchemy;
Business rules;
Financial calculations;
React frontend development;
Frontend/backend integration;
Data validation;
Availability management;
Git and GitHub.
Future Improvements

Possible future improvements include:

User authentication;
Administrative dashboard;
Credit request history;
Improved user experience;
Automated tests;
Integration with external services;
Experimental Machine Learning features;
Large Language Model (LLM) integration.
Project Status

Functional MVP.

The project currently includes a FastAPI backend, SQLite database, and React frontend integrated through REST APIs.

Data

All data used in this project is fictional or test data.

No real banking or personal data should be used in this repository.