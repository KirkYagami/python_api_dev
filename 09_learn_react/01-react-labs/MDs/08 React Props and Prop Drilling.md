# React Props and Prop Drilling: Comprehensive Guide

## Introduction to Props

### What are Props?

**Props** (short for "properties") are the mechanism for passing data from parent components to child components in React. They enable component communication and data flow throughout your application.

**Key Characteristics:**

- **Read-only:** Props cannot be modified by the receiving component
- **Unidirectional:** Data flows from parent to child (top-down)
- **Dynamic:** Props can contain any JavaScript value (strings, numbers, objects, functions, etc.)
- **Reusability:** Allow components to be reused with different data

### Component Hierarchy

```
App (Parent)
├── Header (Child)
├── Content (Child)
└── Footer (Child)
```

In this hierarchy, App is the parent component that can pass props to its children: Header, Content, and Footer.

---

## Basic Props Usage

### Passing Props from Parent to Child

#### Step 1: Define Props in Parent Component

**App.js (Parent):**

```javascript
import Header from './Header';

function App() {
  return (
    <div className="App">
      <Header title="Grocery List" />
    </div>
  );
}

export default App;
```

**Syntax:**

```jsx
<ComponentName propName="value" />
```

#### Step 2: Receive Props in Child Component

**Header.js (Child):**

```javascript
function Header(props) {
  return (
    <header className="header">
      <h1>{props.title}</h1>
    </header>
  );
}

export default Header;
```

**Access Pattern:** `props.propertyName`

### Props Destructuring

Instead of repeatedly typing `props.propertyName`, you can destructure props directly in the function parameters.

#### Without Destructuring

```javascript
function Header(props) {
  return (
    <header>
      <h1>{props.title}</h1>
      <p>{props.subtitle}</p>
    </header>
  );
}
```

#### With Destructuring (Preferred)

```javascript
function Header({ title, subtitle }) {
  return (
    <header>
      <h1>{title}</h1>
      <p>{subtitle}</p>
    </header>
  );
}
```

**Advantages:**

- Cleaner, more readable code
- Immediately see which props the component expects
- Less repetitive code
- Modern JavaScript best practice

### Multiple Props Example

```javascript
// Parent Component
function App() {
  return (
    <div>
      <UserCard 
        name="John Doe"
        age={30}
        email="john@example.com"
        isActive={true}
      />
    </div>
  );
}

// Child Component
function UserCard({ name, age, email, isActive }) {
  return (
    <div className="user-card">
      <h2>{name}</h2>
      <p>Age: {age}</p>
      <p>Email: {email}</p>
      <p>Status: {isActive ? 'Active' : 'Inactive'}</p>
    </div>
  );
}
```

---

## Default Props

### What are Default Props?

Default props provide fallback values when a prop is not passed from the parent component. This prevents errors and makes components more robust during development.

### Setting Default Props

**Method 1: Using defaultProps (Class Component Legacy)**

```javascript
function Header({ title }) {
  return (
    <header>
      <h1>{title}</h1>
    </header>
  );
}

Header.defaultProps = {
  title: "Default Title"
};

export default Header;
```

**Method 2: Default Parameters (Modern Approach)**

```javascript
function Header({ title = "Default Title" }) {
  return (
    <header>
      <h1>{title}</h1>
    </header>
  );
}

export default Header;
```

### Default Props in Action

```javascript
// Parent Component
function App() {
  return (
    <div>
      <Header title="Grocery List" />  {/* Uses provided prop */}
      <Header />                        {/* Uses default prop */}
    </div>
  );
}

// Child Component
function Header({ title = "Default Title" }) {
  return <h1>{title}</h1>;
}
```

**Output:**

```
Grocery List
Default Title
```

### Complex Default Props

```javascript
function UserProfile({
  name = "Guest User",
  age = 0,
  location = "Unknown",
  hobbies = [],
  isVerified = false
}) {
  return (
    <div>
      <h2>{name}</h2>
      <p>Age: {age}</p>
      <p>Location: {location}</p>
      <p>Hobbies: {hobbies.join(", ") || "None listed"}</p>
      <p>Verified: {isVerified ? "Yes" : "No"}</p>
    </div>
  );
}
```

### When to Use Default Props

**Use Cases:**

1. **Development/Prototyping:** Provide sample data while building components
2. **Optional Props:** Props that aren't always required
3. **Fallback Values:** Ensure component doesn't break if data is missing
4. **Documentation:** Show expected prop types and structure

---

## Understanding Prop Drilling

### What is Prop Drilling?

**Prop drilling** is the process of passing data from a parent component down through multiple levels of nested child components to reach a deeply nested component that needs the data.

### The Problem Prop Drilling Solves

Components that are siblings cannot directly share data. Data must flow through their common parent.

```
App (has data)
├── Content (sibling 1)
└── Footer (sibling 2 - needs data from Content)
```

**Solution:** Move data to the common parent (App) and pass it down to both children.

### Prop Drilling Example: Single Level

```javascript
// App.js (Parent - Level 0)
function App() {
  const [items, setItems] = useState([
    { id: 1, item: "Bread", checked: false },
    { id: 2, item: "Milk", checked: true },
    { id: 3, item: "Eggs", checked: false }
  ]);

  return (
    <div>
      <Content items={items} setItems={setItems} />
    </div>
  );
}
```

```javascript
// Content.js (Child - Level 1)
function Content({ items, setItems }) {
  return (
    <main>
      <ul>
        {items.map(item => (
          <li key={item.id}>{item.item}</li>
        ))}
      </ul>
    </main>
  );
}
```

### Prop Drilling Example: Multiple Levels

```javascript
// App.js (Level 0 - Top Parent)
function App() {
  const [items, setItems] = useState([
    { id: 1, item: "Bread", checked: false },
    { id: 2, item: "Milk", checked: true }
  ]);

  const handleCheck = (id) => {
    const updatedItems = items.map(item =>
      item.id === id ? { ...item, checked: !item.checked } : item
    );
    setItems(updatedItems);
  };

  const handleDelete = (id) => {
    const filteredItems = items.filter(item => item.id !== id);
    setItems(filteredItems);
  };

  return (
    <div className="App">
      <Header title="Grocery List" />
      <Content 
        items={items}
        handleCheck={handleCheck}
        handleDelete={handleDelete}
      />
      <Footer length={items.length} />
    </div>
  );
}
```

```javascript
// Content.js (Level 1 - Middle Component)
function Content({ items, handleCheck, handleDelete }) {
  return (
    <main>
      {items.length ? (
        <ItemList 
          items={items}
          handleCheck={handleCheck}
          handleDelete={handleDelete}
        />
      ) : (
        <p>Your list is empty</p>
      )}
    </main>
  );
}
```

```javascript
// ItemList.js (Level 2 - Another Middle Component)
function ItemList({ items, handleCheck, handleDelete }) {
  return (
    <ul>
      {items.map(item => (
        <LineItem
          key={item.id}
          item={item}
          handleCheck={handleCheck}
          handleDelete={handleDelete}
        />
      ))}
    </ul>
  );
}
```

```javascript
// LineItem.js (Level 3 - Final Component)
function LineItem({ item, handleCheck, handleDelete }) {
  return (
    <li>
      <input
        type="checkbox"
        checked={item.checked}
        onChange={() => handleCheck(item.id)}
      />
      <label>{item.item}</label>
      <button onClick={() => handleDelete(item.id)}>
        Delete
      </button>
    </li>
  );
}
```

### Prop Drilling Visualization

```
App (Level 0)
└── items, handleCheck, handleDelete
    │
    ├─→ Content (Level 1)
    │   └── items, handleCheck, handleDelete
    │       │
    │       └─→ ItemList (Level 2)
    │           └── items, handleCheck, handleDelete
    │               │
    │               └─→ LineItem (Level 3)
    │                   └── Uses: item, handleCheck, handleDelete
    │
    └─→ Footer (Level 1)
        └── length (items.length)
```

---

## Passing Different Data Types as Props

### Strings

```javascript
<Component title="Hello World" />

// In component
function Component({ title }) {
  return <h1>{title}</h1>;
}
```

### Numbers

```javascript
<Component count={42} age={25} />

// In component
function Component({ count, age }) {
  return (
    <div>
      <p>Count: {count}</p>
      <p>Age: {age}</p>
    </div>
  );
}
```

### Booleans

```javascript
<Component isActive={true} isVisible={false} />

// In component
function Component({ isActive, isVisible }) {
  return (
    <div>
      {isActive && <p>Active</p>}
      {isVisible && <p>Visible</p>}
    </div>
  );
}
```

### Arrays

```javascript
const fruits = ["Apple", "Banana", "Orange"];

<Component items={fruits} />

// In component
function Component({ items }) {
  return (
    <ul>
      {items.map((item, index) => (
        <li key={index}>{item}</li>
      ))}
    </ul>
  );
}
```

### Objects

```javascript
const user = {
  name: "John Doe",
  age: 30,
  email: "john@example.com"
};

<Component user={user} />

// In component
function Component({ user }) {
  return (
    <div>
      <h2>{user.name}</h2>
      <p>{user.age}</p>
      <p>{user.email}</p>
    </div>
  );
}
```

### Functions

```javascript
function App() {
  const handleClick = (message) => {
    alert(message);
  };

  return <Button onClick={handleClick} />;
}

function Button({ onClick }) {
  return (
    <button onClick={() => onClick("Button clicked!")}>
      Click Me
    </button>
  );
}
```

### State and State Setters

```javascript
function App() {
  const [count, setCount] = useState(0);

  return (
    <Counter count={count} setCount={setCount} />
  );
}

function Counter({ count, setCount }) {
  return (
    <div>
      <p>Count: {count}</p>
      <button onClick={() => setCount(count + 1)}>
        Increment
      </button>
    </div>
  );
}
```

---

## Practical Example: Grocery List Application

### Complete Implementation

#### Step 1: App Component (Parent - State Management)

```javascript
import { useState } from 'react';
import Header from './Header';
import Content from './Content';
import Footer from './Footer';

function App() {
  const [items, setItems] = useState([
    { id: 1, item: "Bread", checked: false },
    { id: 2, item: "Milk", checked: true },
    { id: 3, item: "Eggs", checked: false }
  ]);

  const handleCheck = (id) => {
    const updatedItems = items.map(item =>
      item.id === id ? { ...item, checked: !item.checked } : item
    );
    setItems(updatedItems);
  };

  const handleDelete = (id) => {
    const filteredItems = items.filter(item => item.id !== id);
    setItems(filteredItems);
  };

  return (
    <div className="App">
      <Header title="Grocery List" />
      <Content 
        items={items}
        handleCheck={handleCheck}
        handleDelete={handleDelete}
      />
      <Footer length={items.length} />
    </div>
  );
}

export default App;
```

#### Step 2: Header Component

```javascript
function Header({ title = "Default Title" }) {
  return (
    <header className="header">
      <h1>{title}</h1>
    </header>
  );
}

export default Header;
```

#### Step 3: Content Component

```javascript
import ItemList from './ItemList';

function Content({ items, handleCheck, handleDelete }) {
  return (
    <main className="content">
      {items.length ? (
        <ItemList 
          items={items}
          handleCheck={handleCheck}
          handleDelete={handleDelete}
        />
      ) : (
        <p style={{ marginTop: '2rem' }}>Your list is empty</p>
      )}
    </main>
  );
}

export default Content;
```

#### Step 4: ItemList Component

```javascript
import LineItem from './LineItem';

function ItemList({ items, handleCheck, handleDelete }) {
  return (
    <ul>
      {items.map(item => (
        <LineItem
          key={item.id}
          item={item}
          handleCheck={handleCheck}
          handleDelete={handleDelete}
        />
      ))}
    </ul>
  );
}

export default ItemList;
```

#### Step 5: LineItem Component (Reusable)

```javascript
import { FaTrashAlt } from 'react-icons/fa';

function LineItem({ item, handleCheck, handleDelete }) {
  return (
    <li className="item">
      <input
        type="checkbox"
        checked={item.checked}
        onChange={() => handleCheck(item.id)}
      />
      <label
        style={(item.checked) ? { textDecoration: 'line-through' } : null}
        onDoubleClick={() => handleCheck(item.id)}
      >
        {item.item}
      </label>
      <FaTrashAlt
        role="button"
        tabIndex="0"
        onClick={() => handleDelete(item.id)}
        aria-label={`Delete ${item.item}`}
      />
    </li>
  );
}

export default LineItem;
```

#### Step 6: Footer Component

```javascript
function Footer({ length }) {
  return (
    <footer className="footer">
      <p>
        {length} List {length === 1 ? "Item" : "Items"}
      </p>
    </footer>
  );
}

export default Footer;
```

---

## Component Abstraction and Organization

### Why Abstract Components?

**Benefits:**

1. **Reusability:** Components can be used in multiple places
2. **Maintainability:** Easier to locate and fix issues
3. **Readability:** Smaller, focused components are easier to understand
4. **Testing:** Isolated components are easier to test
5. **Collaboration:** Team members can work on different components

### When to Abstract a Component

**Consider abstraction when:**

- Component has more than 100-150 lines of code
- JSX contains repetitive patterns (like list items)
- Logic or UI can be reused elsewhere
- Component has multiple responsibilities
- Code becomes hard to read or maintain

### Abstraction Example

**Before Abstraction (Content.js):**

```javascript
function Content({ items, handleCheck, handleDelete }) {
  return (
    <main>
      {items.length ? (
        <ul>
          {items.map(item => (
            <li key={item.id}>
              <input
                type="checkbox"
                checked={item.checked}
                onChange={() => handleCheck(item.id)}
              />
              <label>{item.item}</label>
              <button onClick={() => handleDelete(item.id)}>
                Delete
              </button>
            </li>
          ))}
        </ul>
      ) : (
        <p>Your list is empty</p>
      )}
    </main>
  );
}
```

**After Abstraction:**

```javascript
// Content.js
function Content({ items, handleCheck, handleDelete }) {
  return (
    <main>
      {items.length ? (
        <ItemList 
          items={items}
          handleCheck={handleCheck}
          handleDelete={handleDelete}
        />
      ) : (
        <p>Your list is empty</p>
      )}
    </main>
  );
}

// ItemList.js
function ItemList({ items, handleCheck, handleDelete }) {
  return (
    <ul>
      {items.map(item => (
        <LineItem
          key={item.id}
          item={item}
          handleCheck={handleCheck}
          handleDelete={handleDelete}
        />
      ))}
    </ul>
  );
}

// LineItem.js
function LineItem({ item, handleCheck, handleDelete }) {
  return (
    <li>
      <input
        type="checkbox"
        checked={item.checked}
        onChange={() => handleCheck(item.id)}
      />
      <label>{item.item}</label>
      <button onClick={() => handleDelete(item.id)}>
        Delete
      </button>
    </li>
  );
}
```

---

## The `key` Prop in Lists

### Why Keys are Required

When rendering lists in React, each child element must have a unique `key` prop. This helps React identify which items have changed, been added, or removed.

### Key Prop Usage

```javascript
function ItemList({ items }) {
  return (
    <ul>
      {items.map(item => (
        <LineItem key={item.id} item={item} />
      ))}
    </ul>
  );
}
```

**Key Requirements:**

- Must be unique among siblings
- Should be stable (not change between renders)
- Should not use array index if list can be reordered

### Good vs Bad Key Examples

**❌ Bad: Using Array Index**

```javascript
{items.map((item, index) => (
  <li key={index}>{item.name}</li>
))}
```

**Why it's bad:** If items are reordered, React can't properly track them.

**✓ Good: Using Unique ID**

```javascript
{items.map(item => (
  <li key={item.id}>{item.name}</li>
))}
```

**Why it's good:** Each item has a stable, unique identifier.

**✓ Acceptable: Using Index (When List is Static)**

```javascript
{items.map((item, index) => (
  <li key={index}>{item.name}</li>
))}
```

**When it's acceptable:** List never reorders, filters, or receives new items.

### Key Prop Error

**Error Message:**

```
Warning: Each child in a list should have a unique "key" prop.
```

**Solution:** Add a unique `key` prop to the top-level element in your map.

---

## Accessibility: ARIA Labels

### What are ARIA Labels?

ARIA (Accessible Rich Internet Applications) labels provide additional context for screen readers and assistive technologies.

### Using ARIA Labels in React

```javascript
function LineItem({ item, handleDelete }) {
  return (
    <li>
      <label>{item.item}</label>
      <button
        onClick={() => handleDelete(item.id)}
        aria-label={`Delete ${item.item}`}
      >
        <FaTrashAlt />
      </button>
    </li>
  );
}
```

**Why it's important:** The button only contains an icon (no text), so screen readers need the aria-label to announce what the button does.

### Common ARIA Attributes in React

```javascript
// aria-label: Provides a label when none is visible
<button aria-label="Close dialog">
  <CloseIcon />
</button>

// aria-labelledby: References another element's ID
<div aria-labelledby="dialog-title">
  <h2 id="dialog-title">Confirm Delete</h2>
</div>

// aria-describedby: Provides additional description
<input
  type="text"
  aria-describedby="password-help"
/>
<span id="password-help">
  Password must be at least 8 characters
</span>

// role: Defines the element's purpose
<div role="button" tabIndex="0" onClick={handleClick}>
  Click me
</div>

// aria-hidden: Hides decorative elements from screen readers
<span aria-hidden="true">★★★★★</span>
```

---

## Props Best Practices

### 1. Use Descriptive Prop Names

**❌ Bad:**

```javascript
<Component d="John" n={5} />
```

**✓ Good:**

```javascript
<Component displayName="John" itemCount={5} />
```

### 2. Destructure Props Immediately

**❌ Less Preferred:**

```javascript
function Component(props) {
  return <h1>{props.title}</h1>;
}
```

**✓ Preferred:**

```javascript
function Component({ title }) {
  return <h1>{title}</h1>;
}
```

### 3. Provide Default Props When Appropriate

```javascript
function Button({ 
  text = "Click me", 
  variant = "primary",
  disabled = false 
}) {
  return <button disabled={disabled}>{text}</button>;
}
```

### 4. Document Expected Props

```javascript
/**
 * UserCard Component
 * @param {string} name - User's full name
 * @param {number} age - User's age
 * @param {string} email - User's email address
 * @param {boolean} isVerified - Whether user is verified
 */
function UserCard({ name, age, email, isVerified }) {
  // Component implementation
}
```

### 5. Keep Prop Drilling Shallow

**Problem:** Drilling props through many levels becomes hard to maintain.

**Solution:** Consider these alternatives for deep prop drilling:

- **Context API** (covered in advanced tutorials)
- **State Management Libraries** (Redux, Zustand, etc.)
- **Component Composition**

### 6. Don't Mutate Props

**❌ Wrong:**

```javascript
function Component({ items }) {
  items.push(newItem); // Never mutate props!
  return <ul>...</ul>;
}
```

**✓ Correct:**

```javascript
function Component({ items, setItems }) {
  const addItem = () => {
    setItems([...items, newItem]); // Create new array
  };
  return <ul>...</ul>;
}
```

### 7. Use Prop Type Validation (Optional but Recommended)

```javascript
import PropTypes from 'prop-types';

function Header({ title, subtitle }) {
  return (
    <header>
      <h1>{title}</h1>
      <h2>{subtitle}</h2>
    </header>
  );
}

Header.propTypes = {
  title: PropTypes.string.isRequired,
  subtitle: PropTypes.string
};

Header.defaultProps = {
  subtitle: "Default Subtitle"
};
```

---

## Common Pitfalls and Solutions

### Pitfall 1: Forgetting to Pass Required Props

**Problem:**

```javascript
// Parent
<Header />  // Missing title prop

// Child
function Header({ title }) {
  return <h1>{title}</h1>;  // title is undefined
}
```

**Solution:** Use default props or check for existence

```javascript
function Header({ title = "Default Title" }) {
  return <h1>{title}</h1>;
}
```

### Pitfall 2: Passing Props with Wrong Names

**Problem:**

```javascript
// Parent passes "heading"
<Header heading="My Title" />

// Child expects "title"
function Header({ title }) {
  return <h1>{title}</h1>;  // undefined
}
```

**Solution:** Ensure prop names match

```javascript
<Header title="My Title" />
```

### Pitfall 3: Not Drilling Functions Correctly

**Problem:**

```javascript
// Calling function immediately instead of passing reference
<Button onClick={handleClick()} />  // ❌ Calls immediately
```

**Solution:**

```javascript
<Button onClick={handleClick} />     // ✓ Passes reference
<Button onClick={() => handleClick()} />  // ✓ Passes function that calls it
```

### Pitfall 4: Forgetting Key Prop in Lists

**Problem:**

```javascript
{items.map(item => (
  <li>{item.name}</li>  // Warning: missing key
))}
```

**Solution:**

```javascript
{items.map(item => (
  <li key={item.id}>{item.name}</li>
))}
```

### Pitfall 5: Prop Name Conflicts with HTML Attributes

**Problem:**

```javascript
function Image({ class, for }) {  // Reserved words!
  return <img className={class} />;
}
```

**Solution:** Use different names

```javascript
function Image({ imageClass, labelFor }) {
  return <img className={imageClass} />;
}
```

---

## Lab Exercise: Building a Todo Application

### Exercise Overview

Build a complete todo application using props and prop drilling.

### Requirements

1. Display a list of todo items
2. Each item shows text and completion status
3. User can mark items as complete
4. User can delete items
5. Footer shows total item count
6. Header displays the app title

### Project Structure

```
src/
├── App.js
├── components/
│   ├── Header.js
│   ├── TodoList.js
│   ├── TodoItem.js
│   └── Footer.js
```

### Step 1: App.js (Parent Component)

```javascript
import { useState } from 'react';
import Header from './components/Header';
import TodoList from './components/TodoList';
import Footer from './components/Footer';
import './App.css';

function App() {
  const [todos, setTodos] = useState([
    { id: 1, text: "Learn React", completed: false },
    { id: 2, text: "Build a project", completed: false },
    { id: 3, text: "Master props", completed: true }
  ]);

  const toggleTodo = (id) => {
    setTodos(todos.map(todo =>
      todo.id === id 
        ? { ...todo, completed: !todo.completed }
        : todo
    ));
  };

  const deleteTodo = (id) => {
    setTodos(todos.filter(todo => todo.id !== id));
  };

  return (
    <div className="App">
      <Header title="My Todo App" />
      <TodoList 
        todos={todos}
        toggleTodo={toggleTodo}
        deleteTodo={deleteTodo}
      />
      <Footer 
        totalCount={todos.length}
        completedCount={todos.filter(t => t.completed).length}
      />
    </div>
  );
}

export default App;
```

### Step 2: Header.js

```javascript
function Header({ title = "Todo Application" }) {
  return (
    <header style={{
      backgroundColor: '#282c34',
      padding: '1rem',
      color: 'white',
      textAlign: 'center'
    }}>
      <h1>{title}</h1>
    </header>
  );
}

export default Header;
```

### Step 3: TodoList.js

```javascript
import TodoItem from './TodoItem';

function TodoList({ todos, toggleTodo, deleteTodo }) {
  return (
    <main style={{ padding: '2rem' }}>
      {todos.length ? (
        <ul style={{ listStyle: 'none', padding: 0 }}>
          {todos.map(todo => (
            <TodoItem
              key={todo.id}
              todo={todo}
              toggleTodo={toggleTodo}
              deleteTodo={deleteTodo}
            />
          ))}
        </ul>
      ) : (
        <p>No todos yet! Add one to get started.</p>
      )}
    </main>
  );
}

export default TodoList;
```

### Step 4: TodoItem.js (Reusable Component)

```javascript
function TodoItem({ todo, toggleTodo, deleteTodo }) {
  return (
    <li style={{
      padding: '1rem',
      marginBottom: '0.5rem',
      backgroundColor: '#f5f5f5',
      borderRadius: '4px',
      display: 'flex',
      justifyContent: 'space-between',
      alignItems: 'center'
    }}>
      <div style={{ display: 'flex', alignItems: 'center', gap: '1rem' }}>
        <input
          type="checkbox"
          checked={todo.completed}
          onChange={() => toggleTodo(todo.id)}
          aria-label={`Mark "${todo.text}" as ${todo.completed ? 'incomplete' : 'complete'}`}
        />
        <span style={{
          textDecoration: todo.completed ? 'line-through' : 'none',
          color: todo.completed ? '#999' : '#000'
        }}>
          {todo.text}
        </span>
      </div>
      <button
        onClick={() => deleteTodo(todo.id)}
        aria-label={`Delete "${todo.text}"`}
        style={{
          backgroundColor: '#dc3545',
          color: 'white',
          border: 'none',
          padding: '0.5rem 1rem',
          borderRadius: '4px',
          cursor: 'pointer'
        }}
      >
        Delete
      </button>
    </li>
  );
}

export default TodoItem;
```

### Step 5: Footer.js

```javascript
function Footer({ totalCount, completedCount }) {
  return (
    <footer style={{
      backgroundColor: '#282c34',
      padding: '1rem',
      color: 'white',
      textAlign: 'center',
      marginTop: 'auto'
    }}>
      <p>
        {completedCount} of {totalCount} {totalCount === 1 ? 'task' : 'tasks'} completed
      </p>
    </footer>
  );
}

export default Footer;
```

### Exercise Challenges

**Challenge 1:** Add a prop to filter todos (show all, active, or completed)

**Challenge 2:** Pass a custom style prop to TodoItem for different priorities

**Challenge 3:** Add a prop to Header for a subtitle

**Challenge 4:** Create an "Edit" feature by passing an edit function through props

---

## Summary

### Key Concepts Covered

**Props Fundamentals:**

- ✓ Props pass data from parent to child components
- ✓ Props are read-only and cannot be modified
- ✓ Use destructuring for cleaner code
- ✓ Any JavaScript value can be passed as a prop

**Default Props:**

- ✓ Provide fallback values for missing props
- ✓ Prevent errors during development
- ✓ Document expected component interface
- ✓ Use default parameters for modern approach

**Prop Drilling:**

- ✓ Pass data through multiple component levels
- ✓ Enables sibling components to share data via common parent
- ✓ State and functions can be drilled down
- ✓ Necessary for component communication in small to medium apps

**Component Abstraction:**

- ✓ Create reusable components for repeated patterns
- ✓ Keep components focused and maintainable
- ✓ Abstract when code exceeds 100-150 lines
- ✓ Improve readability and testability

**Lists and Keys:**

- ✓ Always provide unique `key` prop in lists
- ✓ Keys help React identify changes efficiently
- ✓ Use stable IDs, not array indices (when possible)
- ✓ Keys must be unique among siblings

**Accessibility:**

- ✓ Use `aria-label` for icon-only buttons
- ✓ Provide context for screen readers
- ✓ Implement proper ARIA attributes
- ✓ Ensure all interactive elements are accessible

### Component Communication Patterns

```
Parent Component (App)
  ↓ Props Down ↓
Child Components (Header, Content, Footer)
  ↓ Props Down ↓
Grandchild Components (ItemList)
  ↓ Props Down ↓
Great-grandchild Components (LineItem)
```

### Props Flow Summary

1. **Define state** in the highest common parent component
2. **Pass state and functions** as props to child components
3. **Destructure props** in child components for cleaner code
4. **Drill down** through multiple levels as needed
5. **Maintain unidirectional data flow** (top-down)

### When to Lift State Up

Move state to a parent component when:

- Multiple children need access to the same data
- Siblings need to communicate
- Data needs to be shared across the component tree
- A child needs to update parent state

### Next Steps

With a solid understanding of props and prop drilling, you're ready to:

1. Explore the Context API (eliminates deep prop drilling)
2. Learn about controlled components and forms
3. Implement custom hooks for reusable logic
4. Work with external data sources (APIs)
5. Master state management patterns
6. Build complex, multi-level component hierarchies
7. Optimize performance with React.memo and useCallback
8. Explore state management libraries (Redux, Zustand)

### Common Interview Questions

**Q1: What are props in React?** Props (properties) are the mechanism for passing data from parent to child components. They are read-only and enable component reusability.

**Q2: What is prop drilling?** Prop drilling is the process of passing data through multiple levels of nested components to reach a deeply nested component that needs the data.

**Q3: How do you pass functions as props?** Pass the function reference (without calling it) as a prop value:

```javascript
<Child onUpdate={handleUpdate} />
```

**Q4: Why is the key prop important in lists?** The key prop helps React identify which items have changed, been added, or removed, enabling efficient re-rendering of list items.

**Q5: Can props be modified in a child component?** No, props are read-only. To modify data, pass a state setter function from the parent as a prop.

**Q6: What are default props?** Default props provide fallback values when a prop is not passed from the parent, preventing undefined errors.

**Q7: How is prop drilling different from Context API?** Prop drilling passes data through every level explicitly, while Context API allows consuming components to access data directly without intermediate components passing it down.

### Additional Resources

**Official Documentation:**

- [React Props Documentation](https://react.dev/learn/passing-props-to-a-component)
- [Lifting State Up](https://react.dev/learn/sharing-state-between-components)
- [Context API](https://react.dev/learn/passing-data-deeply-with-context)

**Best Practices:**

- Keep components small and focused
- Use descriptive prop names
- Provide default props for optional values
- Document expected props with comments or PropTypes
- Consider Context API for deeply nested props
- Validate props in development with PropTypes or TypeScript

**Performance Tips:**

- Avoid creating new objects/functions in render
- Use React.memo for expensive child components
- Pass only necessary props to children
- Consider useCallback for function props

### Conclusion

Props and prop drilling are fundamental concepts in React that enable component communication and data flow. While prop drilling is essential for small to medium applications, be aware that deeply nested prop drilling can become cumbersome. As your application grows, consider alternative patterns like the Context API or state management libraries.

The key to mastering props is understanding:

- How data flows unidirectionally from parent to child
- When to lift state up to enable sibling communication
- How to abstract components for reusability
- When prop drilling becomes a maintenance burden

With these foundations, you're well-equipped to build complex, maintainable React applications that efficiently manage data flow throughout the component tree.