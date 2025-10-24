### **Project 05**  
**Project Title**: LinkVault API – Bookmark & Tag Management System  
**Project Description**:  
Constructed a self-hosted bookmarking API that enables users to save, tag, and retrieve web links programmatically. The system supports duplicate detection, tag-based filtering, and CLI-based import/export in standard formats, functioning as a privacy-focused alternative to commercial bookmarking services.

**Objective**:  
- Design an API to store URLs with optional title, notes, and multiple tags  
- Implement duplicate URL detection using normalized URL hashing  
- Support filtering by tag, keyword, or archived status  
- Model `Bookmark` and `Tag` with a many-to-many relationship in SQLAlchemy  
- Create a CLI to export bookmarks in Netscape HTML format (standard for browsers)  
- Optionally auto-extract page titles using `requests` + `BeautifulSoup`  
- Return consistent, paginated JSON responses for large datasets  

**Tools Used**:  
- **Backend Framework**: Flask, Flask-SQLAlchemy, Flask-Migrate  
- **Web Scraping (optional)**: `requests`, `BeautifulSoup4`  
- **CLI**: Click for import/export operations  
- **Data Handling**: URL normalization (`urllib.parse`), hashing (`hashlib`)  
- **Database**: SQLite for simplicity and file-based persistence  

**Weeks (during training)**: 1-4 (both inclusive)  
**Project Type**: Lightweight data curation API focused on URL management, tagging, and interoperability  
**Outcome**:  
Delivered a functional, extensible bookmarking API with CLI interoperability and duplicate prevention. The system empowers users to own their link data and demonstrates practical Flask API development with real utility for developers and researchers.