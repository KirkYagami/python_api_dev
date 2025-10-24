### **Project 01**  
**Project Title**: TaskFlow API – RESTful Task Management System  
**Project Description**:  
Designed and implemented a modern, API-first task management system using Flask and SQLAlchemy, enabling users to create, track, update, and organize tasks through a clean, well-documented REST interface. The system supports user assignment, status tracking, filtering, and CLI-based utilities for automation and data management, adhering to REST conventions and modern backend engineering practices.

**Objective**:  
- Develop a fully RESTful task management API with standardized endpoints and HTTP status codes  
- Implement robust data models for `User` and `Task` using SQLAlchemy ORM (SQLite/PostgreSQL)  
- Enforce input validation and structured error responses using Pydantic or Marshmallow  
- Support filtering, pagination, and query parameters for flexible task retrieval  
- Create a CLI tool (using Click) for administrative tasks like listing overdue items or bulk operations  
- Ensure database portability with Flask-Migrate for schema versioning  
- Design the system to be easily consumable by frontends, mobile apps, or automation scripts  

**Tools Used**:  
- **Backend Framework**: Flask, Flask-RESTful (optional), Flask-SQLAlchemy, Flask-Migrate  
- **Validation & Serialization**: Pydantic or Marshmallow  
- **Database**: SQLite (development), PostgreSQL (production-ready)  
- **CLI & Utilities**: Click, logging, datetime  
- **Testing & DevOps**: pytest, python-dotenv, HTTPie/curl for API testing  

**Weeks (during training)**: 2–3 (both inclusive)  
**Project Type**: Intermediate backend API project focusing on REST design, data modeling, request validation, and CLI integration  
**Outcome**:  
Delivered a production-structured, testable, and maintainable task management API with comprehensive endpoints, input validation, error handling, and CLI utilities. The system demonstrates strong Flask and SQLAlchemy proficiency and serves as a foundation for scalable microservices or full-stack applications.