
### **Project 03**  
**Project Title**: DevLog API – Developer Journal & Code Snippet Manager  
**Project Description**:  
Engineered a lightweight, developer-focused API for managing coding notes, project logs, and reusable code snippets. The system supports tagging, full-text search, and structured retrieval—all exposed through a REST interface—while providing CLI export capabilities for offline backup and version control integration.

**Objective**:  
- Create an API to store and retrieve technical journal entries with Markdown support  
- Implement a code snippet repository with language tagging and search  
- Support filtering by tags, keywords, or programming language  
- Use SQLAlchemy to model `Entry` and `Snippet` with efficient indexing  
- Add CLI functionality to export entries/snippets to Markdown or JSON files  
- Design versioned API endpoints (e.g., `/api/v1/entries`) for future compatibility  
- Return consistent, machine-readable error and success responses  

**Tools Used**:  
- **Backend Framework**: Flask, Flask-SQLAlchemy, Flask-Migrate  
- **Search**: SQLite FTS or PostgreSQL full-text search (basic implementation)  
- **Data Export**: Click CLI, `json`, `pathlib`  
- **Validation**: Pydantic for payload validation  
- **Database**: SQLite (with FTS5) for simplicity and portability  

**Weeks (during training)**: 1-4 (both inclusive)  
**Project Type**: Lightweight knowledge management API focused on developer productivity and data portability  
**Outcome**:  
Delivered a minimal yet powerful API for technical note-taking and snippet organization, complete with CLI export and tag-based retrieval. The system promotes knowledge retention and code reuse while demonstrating clean Flask architecture and data modeling best practices.
