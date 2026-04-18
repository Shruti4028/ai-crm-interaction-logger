# ai-crm-interaction-logger
AI-based CRM system to log and manage doctor (HCP) interactions with basic backend and design.
# AI CRM System for Doctor Interaction

## Project Overview

This project is a simple idea of a CRM system for medical representatives. It helps them to store and manage their meetings with doctors.

The main goal is to make it easy to log interactions and also use AI to understand what was discussed in simple language.

---

## How the System Works

The system has different parts working together:

Frontend (React)  
Backend (FastAPI)  
AI Agent (LangGraph + LLM)  
Database  

The user enters data from frontend, backend processes it, AI helps in understanding it, and data is stored in database.

---

## Features

1. Log Interaction  
User can add details of meeting with doctor using a form or simple text.

2. AI Understanding  
If user writes in normal sentence like  
"Met Dr Sharma, discussed diabetes medicine"  
then AI will find:
- Doctor name  
- Topic  
- Short summary  

3. Edit Interaction  
User can update previous records.

4. Search Interaction  
User can find old records easily.

5. Follow-up Suggestion  
System can suggest when to meet doctor again.

6. Summary Report  
User can see summary of their work.

---

## AI Agent (LangGraph)

The system uses an AI agent with different tools:

- Log interaction tool  
- Edit tool  
- Search tool  
- Follow-up tool  
- Report tool  

These tools help in handling user requests step by step.

---

## Database (Basic Idea)

Table: interactions  

Fields:
- id  
- doctor_name  
- date  
- notes  
- summary  

---

## API (Basic)

- GET / → check system  
- POST /log → add data  
- GET /interactions → view data  

---

## Limitations

This is a basic prototype.  
Due to time limit, full system is not built.  
Main focus is on idea, design and understanding.

---

## Future Improvement

- Proper frontend design  
- Full AI integration  
- Real database connection  
- More features  

---


---

## Author

Shruti Durgade  
M.Sc. Computer Science  
