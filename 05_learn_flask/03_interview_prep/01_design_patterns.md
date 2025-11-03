# Design Patterns in Python

## Overview

**Design Patterns** are reusable, proven solutions to common software design problems. They represent best practices evolved over time by experienced developers.

### Benefits of Design Patterns
- **Reusability**: Proven solutions that can be applied across projects
- **Maintainability**: Clean, organized code structure
- **Scalability**: Patterns that grow with your application
- **Communication**: Common vocabulary for developers


**Three Main Categories:**

1. **Creational** - Object creation mechanisms
2. **Structural** - Object composition and relationships
3. **Behavioral** - Communication between objects

---
## Singleton Pattern

### Definition
The **Singleton Pattern** ensures a class has only one instance and provides a global point of access to it.

### Use Cases
- Database connections
- Configuration managers
- Logging systems
- Caching mechanisms

### Implementation Methods in Python

#### 1. Module-Level Singleton
```python
# database.py
class DatabaseConnection:
    def __init__(self):
        self.connection_string = "postgresql://localhost:5432/mydb"
    
    def query(self, sql):
        print(f"Executing: {sql}")
        return f"Results for: {sql}"

# Module-level instance
db_instance = DatabaseConnection()
```

#### 2. Decorator Singleton
```python
def singleton(cls):
    instances = {}
    
    def get_instance(*args, **kwargs):
        if cls not in instances:
            instances[cls] = cls(*args, **kwargs)
        return instances[cls]
    
    return get_instance
```

### Flask Singleton Example

```python
# config_manager.py
from flask import Flask

class ConfigManager(metaclass=SingletonMeta):
    def __init__(self):
        self.config = {
            'DEBUG': True,
            'SECRET_KEY': 'your-secret-key',
            'DATABASE_URI': 'sqlite:///app.db'
        }
    
    def get(self, key):
        return self.config.get(key)
    
    def set(self, key, value):
        self.config[key] = value

# app.py
from flask import Flask, jsonify

app = Flask(__name__)

# Initialize config manager
config_manager = ConfigManager()

@app.route('/config')
def get_config():
    return jsonify(config_manager.config)

@app.route('/config/<key>')
def get_config_value(key):
    value = config_manager.get(key)
    return jsonify({key: value})

if __name__ == '__main__':
    app.run(debug=config_manager.get('DEBUG'))
```

## Factory Pattern

### Definition
The **Factory Pattern** provides an interface for creating objects in a superclass, but allows subclasses to alter the type of objects that will be created.

### Types of Factory Patterns
1. **Simple Factory**: A single method that creates objects based on parameters
2. **Factory Method**: Subclasses override the creation method
3. **Abstract Factory**: Creates families of related objects

### Use Cases
- Object creation logic is complex
- Need to create different types of objects based on conditions
- Want to decouple object creation from usage

### Implementation

#### Simple Factory Pattern
```python
class Notification:
    def send(self, message):
        pass

class EmailNotification(Notification):
    def send(self, message):
        return f"Sending email: {message}"

class SMSNotification(Notification):
    def send(self, message):
        return f"Sending SMS: {message}"

class PushNotification(Notification):
    def send(self, message):
        return f"Sending push notification: {message}"

class NotificationFactory:
    @staticmethod
    def create_notification(notification_type):
        if notification_type == "email":
            return EmailNotification()
        elif notification_type == "sms":
            return SMSNotification()
        elif notification_type == "push":
            return PushNotification()
        else:
            raise ValueError(f"Unknown notification type: {notification_type}")
```

### Flask Factory Pattern Example

```python
# notification_factory.py
from flask import Flask, request, jsonify

class NotificationFactory:
    @staticmethod
    def create_notifier(notifier_type):
        if notifier_type == 'email':
            return EmailNotifier()
        elif notifier_type == 'sms':
            return SMSNotifier()
        elif notifier_type == 'slack':
            return SlackNotifier()
        else:
            raise ValueError(f"Unknown notifier type: {notifier_type}")

class EmailNotifier:
    def notify(self, message, recipient):
        # Simulate email sending
        return f"Email sent to {recipient}: {message}"

class SMSNotifier:
    def notify(self, message, recipient):
        # Simulate SMS sending
        return f"SMS sent to {recipient}: {message}"

class SlackNotifier:
    def notify(self, message, channel):
        # Simulate Slack message
        return f"Slack message to {channel}: {message}"

# app.py
app = Flask(__name__)

@app.route('/notify', methods=['POST'])
def send_notification():
    data = request.json
    notifier_type = data.get('type')
    message = data.get('message')
    recipient = data.get('recipient')
    
    try:
        notifier = NotificationFactory.create_notifier(notifier_type)
        result = notifier.notify(message, recipient)
        return jsonify({'status': 'success', 'result': result})
    except ValueError as e:
        return jsonify({'status': 'error', 'message': str(e)}), 400

# Usage example:
# POST /notify
# {
#   "type": "email",
#   "message": "Hello World!",
#   "recipient": "user@example.com"
# }
```

## Advanced Flask Example: Combined Patterns

```python
# database_factory.py
from abc import ABC, abstractmethod

class Database(ABC):
    @abstractmethod
    def connect(self):
        pass
    
    @abstractmethod
    def execute(self, query):
        pass

class PostgreSQLDatabase(Database):
    def connect(self):
        return "Connected to PostgreSQL"
    
    def execute(self, query):
        return f"PostgreSQL: {query}"

class MySQLDatabase(Database):
    def connect(self):
        return "Connected to MySQL"
    
    def execute(self, query):
        return f"MySQL: {query}"

class SQLiteDatabase(Database):
    def connect(self):
        return "Connected to SQLite"
    
    def execute(self, query):
        return f"SQLite: {query}"

class DatabaseFactory:
    _instances = {}  # Singleton storage
    
    @classmethod
    def get_database(cls, db_type):
        if db_type not in cls._instances:
            if db_type == "postgresql":
                cls._instances[db_type] = PostgreSQLDatabase()
            elif db_type == "mysql":
                cls._instances[db_type] = MySQLDatabase()
            elif db_type == "sqlite":
                cls._instances[db_type] = SQLiteDatabase()
            else:
                raise ValueError(f"Unsupported database type: {db_type}")
        return cls._instances[db_type]

# app.py
from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/database/<db_type>/connect')
def connect_database(db_type):
    try:
        db = DatabaseFactory.get_database(db_type)
        result = db.connect()
        return jsonify({'status': 'success', 'result': result})
    except ValueError as e:
        return jsonify({'status': 'error', 'message': str(e)}), 400

@app.route('/database/<db_type>/query', methods=['POST'])
def execute_query(db_type):
    data = request.json
    query = data.get('query')
    
    try:
        db = DatabaseFactory.get_database(db_type)
        result = db.execute(query)
        return jsonify({'status': 'success', 'result': result})
    except ValueError as e:
        return jsonify({'status': 'error', 'message': str(e)}), 400
```

## Best Practices

### When to Use Singleton
- ✅ When exactly one instance of a class is needed
- ✅ When you need controlled access to a shared resource
- ✅ For logging, configuration, caching systems

### When to Use Factory
- ✅ When object creation logic is complex
- ✅ When you want to decouple client code from concrete classes
- ✅ When you need to create different objects based on conditions

### Anti-Patterns to Avoid
- **Singleton**: Overusing for everything (can make testing difficult)
- **Factory**: Creating unnecessary abstraction layers
- **Both**: Using patterns where simple solutions would suffice

## Testing Examples

```python
# test_singleton.py
import pytest
from your_app import ConfigManager

def test_singleton_pattern():
    instance1 = ConfigManager()
    instance2 = ConfigManager()
    assert instance1 is instance2  # Same instance

# test_factory.py
from your_app import NotificationFactory

def test_factory_pattern():
    email_notifier = NotificationFactory.create_notifier('email')
    sms_notifier = NotificationFactory.create_notifier('sms')
    
    assert isinstance(email_notifier, EmailNotifier)
    assert isinstance(sms_notifier, SMSNotifier)
```
