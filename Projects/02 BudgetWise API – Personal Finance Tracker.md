### **Project 02**  
**Project Title**: BudgetWise API – Personal Finance Tracker  
**Project Description**:  
Built a secure, JSON-based personal finance API that enables users to log income and expenses, categorize transactions, and retrieve financial summaries via programmatic endpoints. The system leverages SQL aggregation for insightful reporting and includes a CLI utility for importing bank statements, emphasizing data integrity, query efficiency, and developer-friendly API design.

**Objective**:  
- Design a transaction logging API with support for income/expense types and custom categories  
- Implement financial aggregation endpoints (e.g., monthly totals, category-wise spending)  
- Use SQLAlchemy to model `Transaction` and `Category` with proper relationships  
- Enable filtering by date range, category, or transaction type via query parameters  
- Develop a CLI tool to parse and import CSV bank/export files into the database  
- Ensure consistent numeric handling (e.g., `Decimal` for monetary values)  
- Provide structured JSON responses suitable for charting or external consumption  

**Tools Used**:  
- **Backend Framework**: Flask, Flask-SQLAlchemy, Flask-Migrate  
- **Data Handling**: Python `Decimal`, `datetime`, CSV parsing (`csv` module)  
- **Database**: SQLite (for portability), PostgreSQL (for scalability)  
- **CLI**: Click for command-line data import and reporting  
- **Validation**: Manual or Pydantic-based request validation  

**Weeks (during training)**: 2–3 (both inclusive)  
**Project Type**: Intermediate data-centric API project emphasizing SQL aggregation, financial data modeling, and automation via CLI  
**Outcome**:  
Delivered a reliable, query-optimized finance tracking API with real-world utility. The system supports automated data ingestion, accurate financial summaries, and clean JSON output—ideal for integration with dashboards, mobile apps, or personal automation workflows.
