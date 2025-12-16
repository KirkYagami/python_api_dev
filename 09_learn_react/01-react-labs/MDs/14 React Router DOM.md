# React Router DOM: Interactive Step-by-Step Tutorial

## Welcome! 🚀

This tutorial will teach you React Router DOM by building a **Book Library App** from scratch. You'll see your progress in the browser after every step!

---

## Setup: Getting Started

### Step 1: Create Your Project

Open your terminal and run:

```bash
npm create vite@latest book-library -- --template react
cd book-library
npm install
npm install react-router-dom
```

### Step 2: Start the Development Server

```bash
npm run dev
```

Your browser should open to `http://localhost:5173`. You'll see the default Vite + React page.

---

## Part 1: Your First Route

Let's replace the default content with our own routing setup!

### Step 3: Create a Simple Home Page

**Create: `src/pages/Home.jsx`**

```jsx
export function Home() {
  return (
    <div>
      <h1>📚 Book Library</h1>
      <p>Welcome to your personal book collection!</p>
    </div>
  );
}
```

### Step 4: Set Up Basic Routing

**Update: `src/App.jsx`**

```jsx
import { Routes, Route } from 'react-router-dom';
import { Home } from './pages/Home';

function App() {
  return (
    <Routes>
      <Route path="/" element={<Home />} />
    </Routes>
  );
}

export default App;
```

### Step 5: Wrap Your App with BrowserRouter

**Update: `src/main.jsx`**

```jsx
import React from 'react';
import ReactDOM from 'react-dom/client';
import { BrowserRouter } from 'react-router-dom';
import App from './App.jsx';
import './index.css';

ReactDOM.createRoot(document.getElementById('root')).render(
  <React.StrictMode>
    <BrowserRouter>
      <App />
    </BrowserRouter>
  </React.StrictMode>
);
```

**✅ CHECK YOUR BROWSER:** You should now see "📚 Book Library" and "Welcome to your personal book collection!"

---

## Part 2: Adding More Pages

### Step 6: Create a Books Page

**Create: `src/pages/BookList.jsx`**

```jsx
export function BookList() {
  return (
    <div>
      <h1>📖 All Books</h1>
      <p>Your book collection will appear here.</p>
    </div>
  );
}
```

### Step 7: Add the Books Route

**Update: `src/App.jsx`**

```jsx
import { Routes, Route } from 'react-router-dom';
import { Home } from './pages/Home';
import { BookList } from './pages/BookList';

function App() {
  return (
    <Routes>
      <Route path="/" element={<Home />} />
      <Route path="/books" element={<BookList />} />
    </Routes>
  );
}

export default App;
```

**✅ TEST IT:**

- Visit `http://localhost:5173/` - you see the Home page
- Manually change URL to `http://localhost:5173/books` - you see the Books page

But we can't navigate between pages yet! Let's fix that.

---

## Part 3: Navigation with Links

### Step 8: Add Navigation Bar

**Update: `src/App.jsx`**

```jsx
import { Routes, Route, Link } from 'react-router-dom';
import { Home } from './pages/Home';
import { BookList } from './pages/BookList';

function App() {
  return (
    <>
      <nav style={{
        padding: '1rem',
        borderBottom: '2px solid #ddd',
        marginBottom: '2rem'
      }}>
        <Link to="/" style={{ marginRight: '1rem' }}>🏠 Home</Link>
        <Link to="/books">📚 Books</Link>
      </nav>

      <div style={{ padding: '0 1rem' }}>
        <Routes>
          <Route path="/" element={<Home />} />
          <Route path="/books" element={<BookList />} />
        </Routes>
      </div>
    </>
  );
}

export default App;
```

**✅ CHECK YOUR BROWSER:**

- Click "🏠 Home" and "📚 Books" links
- Notice the page changes WITHOUT a full reload!
- The navigation bar stays visible on both pages

**💡 Key Concept:** The navigation is OUTSIDE `<Routes>`, so it persists across all pages.

---

## Part 4: Dynamic Routes (URL Parameters)

Now let's display individual books!

### Step 9: Create Individual Book Page

**Create: `src/pages/Book.jsx`**

```jsx
import { useParams } from 'react-router-dom';

export function Book() {
  const { id } = useParams();
  
  return (
    <div>
      <h1>Book #{id}</h1>
      <p>Details for book {id} will go here.</p>
    </div>
  );
}
```

### Step 10: Add Dynamic Route

**Update: `src/App.jsx`**

```jsx
import { Routes, Route, Link } from 'react-router-dom';
import { Home } from './pages/Home';
import { BookList } from './pages/BookList';
import { Book } from './pages/Book';

function App() {
  return (
    <>
      <nav style={{
        padding: '1rem',
        borderBottom: '2px solid #ddd',
        marginBottom: '2rem'
      }}>
        <Link to="/" style={{ marginRight: '1rem' }}>🏠 Home</Link>
        <Link to="/books">📚 Books</Link>
      </nav>

      <div style={{ padding: '0 1rem' }}>
        <Routes>
          <Route path="/" element={<Home />} />
          <Route path="/books" element={<BookList />} />
          <Route path="/books/:id" element={<Book />} />
        </Routes>
      </div>
    </>
  );
}

export default App;
```

**✅ TEST IT:**

- Visit `http://localhost:5173/books/1` - you see "Book #1"
- Visit `http://localhost:5173/books/42` - you see "Book #42"
- Visit `http://localhost:5173/books/hello` - you see "Book #hello"

The `:id` captures ANY value from the URL!

### Step 11: Add Links to Specific Books

**Update: `src/pages/BookList.jsx`**

```jsx
import { Link } from 'react-router-dom';

export function BookList() {
  const books = [
    { id: 1, title: 'The Great Gatsby' },
    { id: 2, title: '1984' },
    { id: 3, title: 'To Kill a Mockingbird' }
  ];

  return (
    <div>
      <h1>📖 All Books</h1>
      <ul>
        {books.map(book => (
          <li key={book.id}>
            <Link to={`/books/${book.id}`}>{book.title}</Link>
          </li>
        ))}
      </ul>
    </div>
  );
}
```

**✅ CHECK YOUR BROWSER:**

- Click on "📚 Books"
- You'll see a list of books
- Click any book title to see its detail page
- Use browser back button to return

---

## Part 5: Better Book Details

### Step 12: Display Real Book Information

**Update: `src/pages/Book.jsx`**

```jsx
import { useParams, Link } from 'react-router-dom';

export function Book() {
  const { id } = useParams();
  
  const books = {
    1: { title: 'The Great Gatsby', author: 'F. Scott Fitzgerald', year: 1925 },
    2: { title: '1984', author: 'George Orwell', year: 1949 },
    3: { title: 'To Kill a Mockingbird', author: 'Harper Lee', year: 1960 }
  };

  const book = books[id];

  if (!book) {
    return (
      <div>
        <h1>❌ Book Not Found</h1>
        <Link to="/books">← Back to all books</Link>
      </div>
    );
  }

  return (
    <div>
      <h1>📕 {book.title}</h1>
      <p><strong>Author:</strong> {book.author}</p>
      <p><strong>Published:</strong> {book.year}</p>
      <Link to="/books">← Back to all books</Link>
    </div>
  );
}
```

**✅ TEST IT:**

- Visit a valid book (1, 2, or 3) - see full details
- Visit `http://localhost:5173/books/999` - see "Book Not Found"

---

## Part 6: Adding New Books

### Step 13: Create New Book Form

**Create: `src/pages/NewBook.jsx`**

```jsx
import { useState } from 'react';
import { Link } from 'react-router-dom';

export function NewBook() {
  const [title, setTitle] = useState('');
  const [author, setAuthor] = useState('');

  return (
    <div>
      <h1>➕ Add New Book</h1>
      <form style={{ display: 'flex', flexDirection: 'column', maxWidth: '400px', gap: '1rem' }}>
        <div>
          <label>Title:</label><br />
          <input 
            type="text" 
            value={title}
            onChange={(e) => setTitle(e.target.value)}
            style={{ width: '100%', padding: '0.5rem' }}
          />
        </div>
        <div>
          <label>Author:</label><br />
          <input 
            type="text" 
            value={author}
            onChange={(e) => setAuthor(e.target.value)}
            style={{ width: '100%', padding: '0.5rem' }}
          />
        </div>
        <button type="submit" style={{ padding: '0.5rem' }}>Add Book</button>
      </form>
      <br />
      <Link to="/books">← Back to all books</Link>
    </div>
  );
}
```

### Step 14: Add Route for New Books

**Update: `src/App.jsx`**

```jsx
import { Routes, Route, Link } from 'react-router-dom';
import { Home } from './pages/Home';
import { BookList } from './pages/BookList';
import { Book } from './pages/Book';
import { NewBook } from './pages/NewBook';

function App() {
  return (
    <>
      <nav style={{
        padding: '1rem',
        borderBottom: '2px solid #ddd',
        marginBottom: '2rem'
      }}>
        <Link to="/" style={{ marginRight: '1rem' }}>🏠 Home</Link>
        <Link to="/books" style={{ marginRight: '1rem' }}>📚 Books</Link>
        <Link to="/books/new">➕ New Book</Link>
      </nav>

      <div style={{ padding: '0 1rem' }}>
        <Routes>
          <Route path="/" element={<Home />} />
          <Route path="/books" element={<BookList />} />
          <Route path="/books/new" element={<NewBook />} />
          <Route path="/books/:id" element={<Book />} />
        </Routes>
      </div>
    </>
  );
}

export default App;
```

**✅ CHECK YOUR BROWSER:** Click "➕ New Book" to see the form.

**💡 Important:** Notice `/books/new` comes BEFORE `/books/:id`. This ensures `/books/new` matches exactly, not as an `id`!

---

## Part 7: Programmatic Navigation

### Step 15: Navigate After Form Submission

**Update: `src/pages/NewBook.jsx`**

```jsx
import { useState } from 'react';
import { Link, useNavigate } from 'react-router-dom';

export function NewBook() {
  const [title, setTitle] = useState('');
  const [author, setAuthor] = useState('');
  const navigate = useNavigate();

  const handleSubmit = (e) => {
    e.preventDefault();
    
    if (!title || !author) {
      alert('Please fill in all fields');
      return;
    }

    // In real app: save to database
    console.log('Saving book:', { title, author });
    
    // Navigate back to books list
    navigate('/books');
  };

  return (
    <div>
      <h1>➕ Add New Book</h1>
      <form onSubmit={handleSubmit} style={{ display: 'flex', flexDirection: 'column', maxWidth: '400px', gap: '1rem' }}>
        <div>
          <label>Title:</label><br />
          <input 
            type="text" 
            value={title}
            onChange={(e) => setTitle(e.target.value)}
            style={{ width: '100%', padding: '0.5rem' }}
          />
        </div>
        <div>
          <label>Author:</label><br />
          <input 
            type="text" 
            value={author}
            onChange={(e) => setAuthor(e.target.value)}
            style={{ width: '100%', padding: '0.5rem' }}
          />
        </div>
        <button type="submit" style={{ padding: '0.5rem' }}>Add Book</button>
      </form>
      <br />
      <Link to="/books">← Cancel</Link>
    </div>
  );
}
```

**✅ TEST IT:**

- Click "➕ New Book"
- Fill out the form
- Click "Add Book"
- You're automatically redirected to the books list!

---

## Part 8: 404 Page

### Step 16: Create Not Found Page

**Create: `src/pages/NotFound.jsx`**

```jsx
import { Link } from 'react-router-dom';

export function NotFound() {
  return (
    <div style={{ textAlign: 'center', padding: '3rem' }}>
      <h1>404</h1>
      <h2>Page Not Found</h2>
      <p>The page you're looking for doesn't exist.</p>
      <Link to="/">← Go Home</Link>
    </div>
  );
}
```

### Step 17: Add Catch-All Route

**Update: `src/App.jsx`**

```jsx
import { Routes, Route, Link } from 'react-router-dom';
import { Home } from './pages/Home';
import { BookList } from './pages/BookList';
import { Book } from './pages/Book';
import { NewBook } from './pages/NewBook';
import { NotFound } from './pages/NotFound';

function App() {
  return (
    <>
      <nav style={{
        padding: '1rem',
        borderBottom: '2px solid #ddd',
        marginBottom: '2rem'
      }}>
        <Link to="/" style={{ marginRight: '1rem' }}>🏠 Home</Link>
        <Link to="/books" style={{ marginRight: '1rem' }}>📚 Books</Link>
        <Link to="/books/new">➕ New Book</Link>
      </nav>

      <div style={{ padding: '0 1rem' }}>
        <Routes>
          <Route path="/" element={<Home />} />
          <Route path="/books" element={<BookList />} />
          <Route path="/books/new" element={<NewBook />} />
          <Route path="/books/:id" element={<Book />} />
          <Route path="*" element={<NotFound />} />
        </Routes>
      </div>
    </>
  );
}

export default App;
```

**✅ TEST IT:** Visit `http://localhost:5173/random-page` - you'll see the 404 page!

---

## Part 9: Active Navigation Links

### Step 18: Style Active Links

**Update: `src/App.jsx`**

```jsx
import { Routes, Route, NavLink } from 'react-router-dom';
import { Home } from './pages/Home';
import { BookList } from './pages/BookList';
import { Book } from './pages/Book';
import { NewBook } from './pages/NewBook';
import { NotFound } from './pages/NotFound';

function App() {
  const navLinkStyle = ({ isActive }) => ({
    marginRight: '1rem',
    textDecoration: 'none',
    color: isActive ? '#ff6b6b' : '#333',
    fontWeight: isActive ? 'bold' : 'normal',
    borderBottom: isActive ? '2px solid #ff6b6b' : 'none',
    paddingBottom: '0.25rem'
  });

  return (
    <>
      <nav style={{
        padding: '1rem',
        borderBottom: '2px solid #ddd',
        marginBottom: '2rem'
      }}>
        <NavLink to="/" style={navLinkStyle}>🏠 Home</NavLink>
        <NavLink to="/books" style={navLinkStyle}>📚 Books</NavLink>
        <NavLink to="/books/new" style={navLinkStyle}>➕ New Book</NavLink>
      </nav>

      <div style={{ padding: '0 1rem' }}>
        <Routes>
          <Route path="/" element={<Home />} />
          <Route path="/books" element={<BookList />} />
          <Route path="/books/new" element={<NewBook />} />
          <Route path="/books/:id" element={<Book />} />
          <Route path="*" element={<NotFound />} />
        </Routes>
      </div>
    </>
  );
}

export default App;
```

**✅ CHECK YOUR BROWSER:** The current page's nav link is now highlighted in red and bold!

---

## Part 10: Nested Routes & Layouts

### Step 19: Create Book Layout Component

**Create: `src/components/BookLayout.jsx`**

```jsx
import { Link, Outlet } from 'react-router-dom';

export function BookLayout() {
  return (
    <div>
      <div style={{ 
        backgroundColor: '#f0f0f0', 
        padding: '1rem', 
        marginBottom: '1rem',
        borderRadius: '4px'
      }}>
        <h3>📚 Books Section</h3>
        <nav>
          <Link to="/books" style={{ marginRight: '1rem' }}>All Books</Link>
          <Link to="/books/new">Add New Book</Link>
        </nav>
      </div>
      
      <Outlet />
    </div>
  );
}
```

### Step 20: Use Nested Routes

**Update: `src/App.jsx`**

```jsx
import { Routes, Route, NavLink } from 'react-router-dom';
import { Home } from './pages/Home';
import { BookList } from './pages/BookList';
import { Book } from './pages/Book';
import { NewBook } from './pages/NewBook';
import { NotFound } from './pages/NotFound';
import { BookLayout } from './components/BookLayout';

function App() {
  const navLinkStyle = ({ isActive }) => ({
    marginRight: '1rem',
    textDecoration: 'none',
    color: isActive ? '#ff6b6b' : '#333',
    fontWeight: isActive ? 'bold' : 'normal',
    borderBottom: isActive ? '2px solid #ff6b6b' : 'none',
    paddingBottom: '0.25rem'
  });

  return (
    <>
      <nav style={{
        padding: '1rem',
        borderBottom: '2px solid #ddd',
        marginBottom: '2rem'
      }}>
        <NavLink to="/" style={navLinkStyle}>🏠 Home</NavLink>
        <NavLink to="/books" style={navLinkStyle}>📚 Books</NavLink>
      </nav>

      <div style={{ padding: '0 1rem' }}>
        <Routes>
          <Route path="/" element={<Home />} />
          
          <Route path="/books" element={<BookLayout />}>
            <Route index element={<BookList />} />
            <Route path="new" element={<NewBook />} />
            <Route path=":id" element={<Book />} />
          </Route>
          
          <Route path="*" element={<NotFound />} />
        </Routes>
      </div>
    </>
  );
}

export default App;
```

**✅ CHECK YOUR BROWSER:**

- Visit any books page
- You'll see the gray "Books Section" box on ALL book-related pages
- The `<Outlet />` is replaced by the current child route's content

**💡 Key Concepts:**

- `<Route path="/books" element={<BookLayout />}>` creates a parent route
- `<Route index>` matches the parent's exact path (`/books`)
- `<Route path="new">` creates `/books/new` (relative path!)
- `<Route path=":id">` creates `/books/:id`
- `<Outlet />` renders the active child route

---

## Part 11: Query Parameters (Search/Filter)

### Step 21: Add Search to Book List

**Update: `src/pages/BookList.jsx`**

```jsx
import { Link, useSearchParams } from 'react-router-dom';

export function BookList() {
  const [searchParams, setSearchParams] = useSearchParams();
  const searchQuery = searchParams.get('search') || '';

  const books = [
    { id: 1, title: 'The Great Gatsby', author: 'F. Scott Fitzgerald' },
    { id: 2, title: '1984', author: 'George Orwell' },
    { id: 3, title: 'To Kill a Mockingbird', author: 'Harper Lee' },
    { id: 4, title: 'Pride and Prejudice', author: 'Jane Austen' },
    { id: 5, title: 'The Hobbit', author: 'J.R.R. Tolkien' }
  ];

  const filteredBooks = books.filter(book =>
    book.title.toLowerCase().includes(searchQuery.toLowerCase()) ||
    book.author.toLowerCase().includes(searchQuery.toLowerCase())
  );

  return (
    <div>
      <h1>📖 All Books</h1>
      
      <input
        type="text"
        placeholder="Search books..."
        value={searchQuery}
        onChange={(e) => setSearchParams({ search: e.target.value })}
        style={{
          width: '100%',
          maxWidth: '400px',
          padding: '0.5rem',
          marginBottom: '1rem',
          fontSize: '1rem'
        }}
      />

      {filteredBooks.length === 0 ? (
        <p>No books found.</p>
      ) : (
        <ul>
          {filteredBooks.map(book => (
            <li key={book.id} style={{ marginBottom: '0.5rem' }}>
              <Link to={`/books/${book.id}`}>
                <strong>{book.title}</strong> by {book.author}
              </Link>
            </li>
          ))}
        </ul>
      )}
    </div>
  );
}
```

**✅ TEST IT:**

- Go to Books page
- Type "great" in the search box
- The URL changes to `/books?search=great`
- Only "The Great Gatsby" shows
- Refresh the page - your search is preserved!

---

## Part 12: Location State (Hidden Data)

### Step 22: Pass Success Message After Adding Book

**Update: `src/pages/NewBook.jsx`**

```jsx
import { useState } from 'react';
import { Link, useNavigate } from 'react-router-dom';

export function NewBook() {
  const [title, setTitle] = useState('');
  const [author, setAuthor] = useState('');
  const navigate = useNavigate();

  const handleSubmit = (e) => {
    e.preventDefault();
    
    if (!title || !author) {
      alert('Please fill in all fields');
      return;
    }

    console.log('Saving book:', { title, author });
    
    // Navigate with success message in state
    navigate('/books', { 
      state: { 
        message: `✅ "${title}" was added successfully!` 
      } 
    });
  };

  return (
    <div>
      <h1>➕ Add New Book</h1>
      <form onSubmit={handleSubmit} style={{ display: 'flex', flexDirection: 'column', maxWidth: '400px', gap: '1rem' }}>
        <div>
          <label>Title:</label><br />
          <input 
            type="text" 
            value={title}
            onChange={(e) => setTitle(e.target.value)}
            style={{ width: '100%', padding: '0.5rem' }}
          />
        </div>
        <div>
          <label>Author:</label><br />
          <input 
            type="text" 
            value={author}
            onChange={(e) => setAuthor(e.target.value)}
            style={{ width: '100%', padding: '0.5rem' }}
          />
        </div>
        <button type="submit" style={{ padding: '0.5rem' }}>Add Book</button>
      </form>
      <br />
      <Link to="/books">← Cancel</Link>
    </div>
  );
}
```

### Step 23: Display Success Message

**Update: `src/pages/BookList.jsx`**

```jsx
import { Link, useSearchParams, useLocation } from 'react-router-dom';

export function BookList() {
  const [searchParams, setSearchParams] = useSearchParams();
  const location = useLocation();
  const searchQuery = searchParams.get('search') || '';
  
  const successMessage = location.state?.message;

  const books = [
    { id: 1, title: 'The Great Gatsby', author: 'F. Scott Fitzgerald' },
    { id: 2, title: '1984', author: 'George Orwell' },
    { id: 3, title: 'To Kill a Mockingbird', author: 'Harper Lee' },
    { id: 4, title: 'Pride and Prejudice', author: 'Jane Austen' },
    { id: 5, title: 'The Hobbit', author: 'J.R.R. Tolkien' }
  ];

  const filteredBooks = books.filter(book =>
    book.title.toLowerCase().includes(searchQuery.toLowerCase()) ||
    book.author.toLowerCase().includes(searchQuery.toLowerCase())
  );

  return (
    <div>
      <h1>📖 All Books</h1>
      
      {successMessage && (
        <div style={{
          backgroundColor: '#d4edda',
          color: '#155724',
          padding: '1rem',
          marginBottom: '1rem',
          borderRadius: '4px',
          border: '1px solid #c3e6cb'
        }}>
          {successMessage}
        </div>
      )}
      
      <input
        type="text"
        placeholder="Search books..."
        value={searchQuery}
        onChange={(e) => setSearchParams({ search: e.target.value })}
        style={{
          width: '100%',
          maxWidth: '400px',
          padding: '0.5rem',
          marginBottom: '1rem',
          fontSize: '1rem'
        }}
      />

      {filteredBooks.length === 0 ? (
        <p>No books found.</p>
      ) : (
        <ul>
          {filteredBooks.map(book => (
            <li key={book.id} style={{ marginBottom: '0.5rem' }}>
              <Link to={`/books/${book.id}`}>
                <strong>{book.title}</strong> by {book.author}
              </Link>
            </li>
          ))}
        </ul>
      )}
    </div>
  );
}
```

**✅ TEST IT:**

- Go to "➕ New Book"
- Fill out the form
- Click "Add Book"
- You'll see a green success message!
- Refresh the page - the message disappears (it's not in the URL!)

---

## Part 13: Better Book Data

### Step 24: Update Book Details Page

**Update: `src/pages/Book.jsx`**

```jsx
import { useParams, Link } from 'react-router-dom';

export function Book() {
  const { id } = useParams();
  
  const books = {
    1: { title: 'The Great Gatsby', author: 'F. Scott Fitzgerald', year: 1925, genre: 'Fiction' },
    2: { title: '1984', author: 'George Orwell', year: 1949, genre: 'Dystopian' },
    3: { title: 'To Kill a Mockingbird', author: 'Harper Lee', year: 1960, genre: 'Fiction' },
    4: { title: 'Pride and Prejudice', author: 'Jane Austen', year: 1813, genre: 'Romance' },
    5: { title: 'The Hobbit', author: 'J.R.R. Tolkien', year: 1937, genre: 'Fantasy' }
  };

  const book = books[id];

  if (!book) {
    return (
      <div>
        <h1>❌ Book Not Found</h1>
        <p>The book you're looking for doesn't exist in our library.</p>
        <Link to="/books">← Back to all books</Link>
      </div>
    );
  }

  return (
    <div>
      <h1>📕 {book.title}</h1>
      <div style={{
        backgroundColor: '#f9f9f9',
        padding: '1.5rem',
        borderRadius: '8px',
        marginTop: '1rem'
      }}>
        <p><strong>Author:</strong> {book.author}</p>
        <p><strong>Published:</strong> {book.year}</p>
        <p><strong>Genre:</strong> {book.genre}</p>
      </div>
      <br />
      <Link to="/books">← Back to all books</Link>
    </div>
  );
}
```

**✅ CHECK YOUR BROWSER:** Click any book to see full details with styling!

---

## 🎉 Congratulations!

You've built a complete React Router application! Here's what you learned:

### Core Concepts ✅

- **Basic routing** with `<Routes>` and `<Route>`
- **Navigation** with `<Link>` and `<NavLink>`
- **Dynamic routes** with URL parameters (`:id`)
- **Programmatic navigation** with `useNavigate()`
- **404 pages** with catch-all routes (`*`)

### Advanced Features ✅

- **Nested routes** and layouts
- **Shared layouts** with `<Outlet>`
- **Query parameters** with `useSearchParams()`
- **Location state** for hidden data
- **Active link styling** with `NavLink`
