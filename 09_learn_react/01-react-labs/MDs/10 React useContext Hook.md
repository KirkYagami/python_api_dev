# React useContext Hook - Comprehensive Guide

## Table of Contents

1. Introduction
2. Understanding Prop Drilling
3. The Problem with Prop Drilling
4. Introduction to Context API
5. Implementing useContext
6. Creating Custom Context Hooks
7. Best Practices

---

## Introduction

The React Context API provides a way to share data across the component tree without having to pass props manually through every level. The `useContext` hook is the modern way to consume context values in functional components.

**Key Concept**: Context allows you to store data that can be accessed by any component in your application tree without prop drilling.

---

## Understanding Prop Drilling

### What is Prop Drilling?

Prop drilling occurs when you pass data from a parent component through multiple intermediate components that don't need the data themselves, just to get it to a deeply nested child component.

### Example: Application Without Context

Let's build a simple user dashboard application to demonstrate the problem.

#### Step 1: Create the Basic Components

**File: `App.js`**

```javascript
import React, { useState } from 'react';
import Dashboard from './Dashboard';

function App() {
  const [user] = useState({
    name: 'John Doe',
    isSubscribed: true
  });

  return (
    <div>
      <Dashboard user={user} />
    </div>
  );
}

export default App;
```

**File: `Dashboard.js`**

```javascript
import React from 'react';
import Sidebar from './Sidebar';
import Profile from './Profile';

function Dashboard({ user }) {
  return (
    <div style={{ padding: '20px' }}>
      <h1>Dashboard</h1>
      <Sidebar user={user} />
      <Profile user={user} />
    </div>
  );
}

export default Dashboard;
```

**File: `Sidebar.js`**

```javascript
import React from 'react';

function Sidebar({ user }) {
  return (
    <div style={{ border: '1px solid #ccc', padding: '10px', margin: '10px 0' }}>
      <h2>Sidebar</h2>
      <div>User: {user.name}</div>
      <div>Subscription Status: {user.isSubscribed ? 'Active' : 'Inactive'}</div>
    </div>
  );
}

export default Sidebar;
```

**File: `Profile.js`**

```javascript
import React from 'react';

function Profile({ user }) {
  return (
    <div style={{ border: '1px solid #ccc', padding: '10px', margin: '10px 0' }}>
      <h2>Profile</h2>
      <div>Welcome, {user.name}!</div>
    </div>
  );
}

export default Profile;
```

---

## The Problem with Prop Drilling

### Analyzing the Issue

In the example above, notice that:

1. **App component** has the `user` state
2. **Dashboard component** receives `user` as a prop but doesn't use it directly
3. Dashboard only passes `user` to **Sidebar** and **Profile**
4. Only Sidebar and Profile actually need the `user` data

**The Problem:**

```javascript
// Dashboard doesn't need user, but must receive and pass it
function Dashboard({ user }) {
  return (
    <div>
      <Sidebar user={user} />  {/* Passing through */}
      <Profile user={user} />  {/* Passing through */}
    </div>
  );
}
```

### Why This is Problematic

1. **Maintenance Difficulty**: If you need to add more user properties, you must update props at every level
2. **Component Coupling**: Dashboard is tightly coupled to components below it
3. **Reduced Reusability**: Dashboard can't be reused without providing the user prop
4. **Code Bloat**: More props means more code and complexity
5. **Refactoring Challenges**: Moving components around requires rewiring all prop chains

### Visualizing the Problem

```
App (has user data)
  ↓ (passes user)
Dashboard (doesn't use user)
  ↓ (passes user)          ↓ (passes user)
Sidebar (uses user)      Profile (uses user)
```

The data travels through Dashboard unnecessarily, creating a maintenance burden.

---

## Introduction to Context API

### What is Context?

Context provides a way to pass data through the component tree without having to pass props down manually at every level. It's designed to share data that can be considered "global" for a tree of React components.

### Core Concepts

1. **createContext**: Creates a Context object
2. **Context.Provider**: Makes context value available to child components
3. **useContext**: Consumes the context value in a component

---

## Implementing useContext

Let's refactor our application to use Context instead of prop drilling.

### Step 1: Create the Context

**File: `UserContext.js`**

```javascript
import { createContext } from 'react';

// Create a context with undefined as default value
const UserContext = createContext(undefined);

export default UserContext;
```

**Explanation:**

- `createContext(undefined)` creates a new context
- We use `undefined` as the default because we don't have access to the user data at this point
- The actual value will be provided by the Provider component

### Step 2: Wrap Components with Provider

**File: `App.js`** (Updated)

```javascript
import React, { useState } from 'react';
import Dashboard from './Dashboard';
import UserContext from './UserContext';

function App() {
  const [user] = useState({
    name: 'John Doe',
    isSubscribed: true
  });

  return (
    <div>
      <UserContext.Provider value={user}>
        <Dashboard />
      </UserContext.Provider>
    </div>
  );
}

export default App;
```

**Key Changes:**

- Import `UserContext`
- Wrap `Dashboard` with `UserContext.Provider`
- Pass `user` as the `value` prop to the Provider
- Remove `user` prop from `Dashboard` (no longer needed!)

### Step 3: Update Dashboard (Remove Props)

**File: `Dashboard.js`** (Updated)

```javascript
import React from 'react';
import Sidebar from './Sidebar';
import Profile from './Profile';

function Dashboard() {
  // No props needed anymore!
  return (
    <div style={{ padding: '20px' }}>
      <h1>Dashboard</h1>
      <Sidebar />
      <Profile />
    </div>
  );
}

export default Dashboard;
```

**Benefits:**

- Dashboard no longer receives or passes props
- It's now decoupled from the user data
- Much cleaner and more maintainable

### Step 4: Consume Context in Child Components

**File: `Sidebar.js`** (Updated)

```javascript
import React, { useContext } from 'react';
import UserContext from './UserContext';

function Sidebar() {
  // Access user directly from context
  const user = useContext(UserContext);

  return (
    <div style={{ border: '1px solid #ccc', padding: '10px', margin: '10px 0' }}>
      <h2>Sidebar</h2>
      <div>User: {user.name}</div>
      <div>Subscription Status: {user.isSubscribed ? 'Active' : 'Inactive'}</div>
    </div>
  );
}

export default Sidebar;
```

**File: `Profile.js`** (Updated)

```javascript
import React, { useContext } from 'react';
import UserContext from './UserContext';

function Profile() {
  // Access user directly from context
  const user = useContext(UserContext);

  return (
    <div style={{ border: '1px solid #ccc', padding: '10px', margin: '10px 0' }}>
      <h2>Profile</h2>
      <div>Welcome, {user.name}!</div>
    </div>
  );
}

export default Profile;
```

**How useContext Works:**

1. `useContext(UserContext)` looks up the component tree
2. Finds the nearest `UserContext.Provider`
3. Returns the `value` passed to that Provider
4. Component re-renders when the context value changes

### New Component Tree Structure

```
App (provides user via Provider)
  ↓
Dashboard (no props needed)
  ↓                    ↓
Sidebar              Profile
(consumes context)   (consumes context)
```

---

## Creating Custom Context Hooks

### The Problem with Direct useContext Usage

The current implementation has a potential issue:

```javascript
const user = useContext(UserContext);
// user could be undefined if used outside Provider
```

If a component uses `useContext(UserContext)` outside of the Provider, it will receive `undefined`, which could cause runtime errors.

### Solution: Custom Hook with Error Handling

**File: `UserContext.js`** (Final Version)

```javascript
import { createContext, useContext } from 'react';

const UserContext = createContext(undefined);

// Custom hook with built-in error handling
export function useUserContext() {
  const user = useContext(UserContext);

  // Throw error if used outside Provider
  if (user === undefined) {
    throw new Error(
      'useUserContext must be used within a UserContext.Provider'
    );
  }

  return user;
}

export default UserContext;
```

**Benefits of Custom Hook:**

1. **Error Prevention**: Catches usage outside Provider immediately
2. **Better Developer Experience**: Clear error message explains the problem
3. **Type Safety**: Guarantees user is never undefined
4. **Reusability**: Single source of truth for accessing context
5. **Cleaner Code**: No need for null checks in components

### Step 5: Update Components to Use Custom Hook

**File: `Sidebar.js`** (Final Version)

```javascript
import React from 'react';
import { useUserContext } from './UserContext';

function Sidebar() {
  const user = useUserContext(); // Using custom hook

  return (
    <div style={{ border: '1px solid #ccc', padding: '10px', margin: '10px 0' }}>
      <h2>Sidebar</h2>
      <div>User: {user.name}</div>
      <div>Subscription Status: {user.isSubscribed ? 'Active' : 'Inactive'}</div>
    </div>
  );
}

export default Sidebar;
```

**File: `Profile.js`** (Final Version)

```javascript
import React from 'react';
import { useUserContext } from './UserContext';

function Profile() {
  const user = useUserContext(); // Using custom hook

  return (
    <div style={{ border: '1px solid #ccc', padding: '10px', margin: '10px 0' }}>
      <h2>Profile</h2>
      <div>Welcome, {user.name}!</div>
    </div>
  );
}

export default Profile;
```

### Complete File Structure

```
src/
  ├── App.js                 (Provider wrapper)
  ├── UserContext.js         (Context + custom hook)
  ├── Dashboard.js           (No props needed)
  ├── Sidebar.js            (Consumes context)
  └── Profile.js            (Consumes context)
```

---

## Best Practices

### 1. Context Scope

**Do:** Create context for related data

```javascript
// Good: Focused context
const UserContext = createContext();
const ThemeContext = createContext();
```

**Don't:** Put everything in one context

```javascript
// Bad: Kitchen sink context
const AppContext = createContext(); // Contains user, theme, settings, etc.
```

### 2. Provider Placement

Place the Provider at the appropriate level in your tree:

```javascript
// Good: Provider wraps only components that need it
function Dashboard() {
  return (
    <UserContext.Provider value={user}>
      <DashboardContent />
    </UserContext.Provider>
  );
}

// Also Good: Provider at app level for global data
function App() {
  return (
    <AuthContext.Provider value={auth}>
      <Router />
    </AuthContext.Provider>
  );
}
```

### 3. Always Create Custom Hooks

```javascript
// Good: Custom hook with validation
export function useUserContext() {
  const context = useContext(UserContext);
  if (context === undefined) {
    throw new Error('useUserContext must be used within UserProvider');
  }
  return context;
}

// Bad: Direct useContext usage
const user = useContext(UserContext); // No validation
```

### 4. Naming Conventions

```javascript
// Context name
export const UserContext = createContext();

// Provider component (optional wrapper)
export function UserProvider({ children }) {
  const [user, setUser] = useState(null);
  return (
    <UserContext.Provider value={{ user, setUser }}>
      {children}
    </UserContext.Provider>
  );
}

// Custom hook
export function useUser() {
  return useContext(UserContext);
}
```

### 5. Performance Optimization

Context triggers re-renders for all consumers. Optimize by:

**Split contexts by update frequency:**

```javascript
// Frequently updated
const UserActionsContext = createContext();

// Rarely updated
const UserProfileContext = createContext();
```

**Memoize context values:**

```javascript
const value = useMemo(() => ({ user, updateUser }), [user]);

<UserContext.Provider value={value}>
  {children}
</UserContext.Provider>
```

### 6. When to Use Context

**Use Context for:**

- Theme/styling data
- User authentication
- Language/localization
- Global settings
- UI state (modals, sidebars)

**Don't Use Context for:**

- Frequent updates (use state management library)
- Server state (use React Query, SWR)
- Form data (use local state)
- Everything (avoid context overuse)

---

## Summary

### Key Takeaways

1. **Prop Drilling**: Passing props through components that don't use them is inefficient and hard to maintain
    
2. **Context API**: Provides a way to share data across component trees without prop drilling
    
3. **useContext Hook**: Modern way to consume context values in functional components
    
4. **Custom Hooks**: Wrap context consumption in custom hooks for better error handling and developer experience
    
5. **Provider Pattern**: Wrap components with Provider to make context available to descendants
    

### Complete Solution Pattern

```javascript
// 1. Create Context with custom hook
const MyContext = createContext(undefined);

export function useMyContext() {
  const context = useContext(MyContext);
  if (context === undefined) {
    throw new Error('useMyContext must be used within Provider');
  }
  return context;
}

// 2. Provide context value
function App() {
  const [data] = useState({ /* data */ });
  return (
    <MyContext.Provider value={data}>
      <Components />
    </MyContext.Provider>
  );
}

// 3. Consume in any child component
function ChildComponent() {
  const data = useMyContext();
  return <div>{data.something}</div>;
}
```

This pattern eliminates prop drilling while maintaining clean, maintainable code with proper error handling.