# React Coding Interview Lab

**Components · State · Forms · Layout**  
_(Vite + React)_

---

## Learning Outcomes

By the end of this lab, students will be able to:

- Set up a **clean React project using Vite**
    
- Build **interview-grade React components**
    
- Explain **state, controlled inputs, conditional rendering**
    
- Implement a **classic layout problem (Holy Grail)**
    
- Confidently answer **“How would you build this?”** in interviews
    

---

# Project Setup (Once)

```bash
npm create vite@latest react-interview-lab
cd react-interview-lab
npm install
npm run dev
```

Open the browser at the shown URL.

---

# 0. Clean Slate (MANDATORY)

We **remove all Vite boilerplate** to avoid confusion.

### Step 0.1 – Clear CSS

- Open `src/App.css` → **delete everything**
    
- Open `src/index.css` → **delete everything**
    

---

### Step 0.2 – Empty App Shell

Replace `src/App.jsx` completely:

```jsx
// src/App.jsx
export default function App() {
  return (
    <div style={{ padding: '20px', fontFamily: 'sans-serif' }}>
      <h1>React Interview Lab</h1>
      {/* Components will be injected here */}
    </div>
  );
}
```

✅ **Browser Check**  
You should see only:

```
React Interview Lab
```

---

# 1. Accordion Component

**(Most asked React interview question)**

> ❓ _“Build an accordion where only one section is open at a time.”_

---

## 1.1 Static Accordion (No State)

### Create File

`src/Accordion.jsx`

```jsx
// src/Accordion.jsx
const data = [
  { id: 1, title: "What is Vite?", content: "A lightning-fast build tool." },
  { id: 2, title: "What is State?", content: "An object that holds UI data." }
];

export default function Accordion() {
  return (
    <div style={{ border: '1px solid #ccc', marginTop: '10px' }}>
      {data.map((item) => (
        <div key={item.id} style={{ borderBottom: '1px solid #ccc' }}>
          <div style={{ padding: '10px', background: '#f4f4f4' }}>
            {item.title}
          </div>
          <div style={{ padding: '10px' }}>
            {item.content}
          </div>
        </div>
      ))}
    </div>
  );
}
```

---

### Inject into App

Update `src/App.jsx`:

```jsx
import Accordion from './Accordion';

export default function App() {
  return (
    <div style={{ padding: '20px' }}>
      <h1>React Interview Lab</h1>
      <Accordion />
    </div>
  );
}
```

✅ **Browser Check**  
Both accordion items are visible.

---

## 1.2 Add Toggle Logic (Core Interview Skill)

> 🎯 **Concept:** Single Source of Truth

### Update `Accordion.jsx`

```jsx
import { useState } from 'react';

const data = [
  { id: 1, title: "What is Vite?", content: "A lightning-fast build tool." },
  { id: 2, title: "What is State?", content: "An object that holds UI data." }
];

export default function Accordion() {
  const [openId, setOpenId] = useState(null);

  return (
    <div style={{ border: '1px solid #ccc' }}>
      {data.map((item) => (
        <div key={item.id}>
          <div
            onClick={() =>
              setOpenId(openId === item.id ? null : item.id)
            }
            style={{
              padding: '10px',
              cursor: 'pointer',
              background: '#eee'
            }}
          >
            {item.title} {openId === item.id ? '−' : '+'}
          </div>

          {openId === item.id && (
            <div style={{ padding: '10px' }}>
              {item.content}
            </div>
          )}
        </div>
      ))}
    </div>
  );
}
```

✅ **Browser Check**

- Click a title → it expands
    
- Click again → it collapses
    
- Only **one item open at a time**
    

---

### 🧠 Interview Explanation

- `openId` controls **entire UI**
    
- No DOM manipulation
    
- Conditional rendering using `&&`
    
- React decides what appears
    

---

# 2. Contact Form

**Controlled Inputs (Very High Frequency Question)**

> ❓ _“How do you handle forms in React?”_

---

## 2.1 Basic Controlled Form

### Create File

`src/ContactForm.jsx`

```jsx
import { useState } from 'react';

export default function ContactForm() {
  const [form, setForm] = useState({
    name: '',
    email: ''
  });

  function handleChange(e) {
    setForm({
      ...form,
      [e.target.name]: e.target.value
    });
  }

  function handleSubmit(e) {
    e.preventDefault();
    alert(JSON.stringify(form));
  }

  return (
    <form
      onSubmit={handleSubmit}
      style={{
        marginTop: '30px',
        display: 'flex',
        flexDirection: 'column',
        gap: '10px',
        maxWidth: '300px'
      }}
    >
      <input
        name="name"
        placeholder="Name"
        value={form.name}
        onChange={handleChange}
      />

      <input
        name="email"
        placeholder="Email"
        value={form.email}
        onChange={handleChange}
      />

      <button type="submit">Submit</button>
    </form>
  );
}
```

---

### Inject into App

```jsx
import Accordion from './Accordion';
import ContactForm from './ContactForm';

export default function App() {
  return (
    <div style={{ padding: '20px' }}>
      <h1>React Interview Lab</h1>
      <Accordion />
      <ContactForm />
    </div>
  );
}
```

✅ **Browser Check**

- Typing updates state
    
- Submit shows JSON alert
    

---

### 🧠 Interview Explanation

- Inputs are **controlled**
    
- React is the **single source of truth**
    
- One handler for multiple inputs
    
- Scales to large forms
    

---

# 3. Holy Grail Layout

**Classic Frontend Interview Problem**

> ❓ _“Build a header, footer, and three-column layout.”_

---

## 3.1 CSS Grid Setup

Open `src/App.css`

```css
.grid-container {
  display: grid;
  grid-template-columns: 150px 1fr 150px;
  grid-template-rows: 60px 1fr 60px;
  grid-template-areas:
    "header header header"
    "nav main aside"
    "footer footer footer";
  height: 50vh;
  margin-top: 40px;
  border: 2px solid black;
}

.header { grid-area: header; background: coral; }
.nav    { grid-area: nav; background: lightblue; }
.main   { grid-area: main; background: #fff; }
.aside  { grid-area: aside; background: lightblue; }
.footer { grid-area: footer; background: coral; }
```

---

## 3.2 Component Creation

`src/HolyGrail.jsx`

```jsx
import './App.css';

export default function HolyGrail() {
  return (
    <div className="grid-container">
      <header className="header">Header</header>
      <nav className="nav">Navigation</nav>
      <main className="main">Main Content</main>
      <aside className="aside">Sidebar</aside>
      <footer className="footer">Footer</footer>
    </div>
  );
}
```

---

## 3.3 Final App Integration

```jsx
import Accordion from './Accordion';
import ContactForm from './ContactForm';
import HolyGrail from './HolyGrail';

export default function App() {
  return (
    <div style={{ padding: '20px' }}>
      <h1>React Interview Lab</h1>

      <Accordion />
      <ContactForm />
      <HolyGrail />
    </div>
  );
}
```

✅ **Browser Check**

You now see:

1. Interactive Accordion
    
2. Controlled Contact Form
    
3. Holy Grail Layout
    

---

# Interview Wrap-Up (For Students)

### You can now confidently answer:

- How state controls UI
    
- Why controlled components matter
    
- How conditional rendering works
    
- How layouts should be structured
    
- Why React avoids direct DOM manipulation
    
