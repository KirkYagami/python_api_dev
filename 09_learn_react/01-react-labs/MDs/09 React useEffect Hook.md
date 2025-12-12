# React useEffect Hook: Comprehensive Guide

## Table of Contents

1. Introduction
2. Fundamental Concepts
3. useEffect Anatomy
4. Implementation Patterns
5. Practical Examples
6. Best Practices

---

## Introduction

The `useEffect` hook is a fundamental React hook that enables developers to perform side effects in functional components. Side effects are operations that occur as consequences of state changes or component lifecycle events, such as data fetching, DOM manipulation, event listener management, and subscription handling.

### What are Side Effects?

In React terminology, a side effect is any operation that affects something outside the scope of the current function being executed. Common side effects include:

- Fetching data from APIs
- Directly manipulating the DOM
- Setting up event listeners
- Managing timers and intervals
- Subscribing to external data sources
- Performing cleanup operations

---

## Fundamental Concepts

### Import Statement

Before using `useEffect`, you must import it from React:

```javascript
import { useEffect } from 'react';
```

For projects using multiple hooks:

```javascript
import React, { useState, useEffect } from 'react';
```

### Basic Syntax

The `useEffect` hook accepts two arguments:

```javascript
useEffect(() => {
  // Effect logic goes here
}, [dependencies]);
```

**First Argument**: A function containing the side effect code **Second Argument**: An optional dependency array that controls when the effect runs

---

## useEffect Anatomy

### Three Core Components

#### 1. Effect Function (Required)

The effect function contains the code you want to execute as a side effect. This can be:

- An arrow function
- An anonymous function
- A callback function

```javascript
useEffect(() => {
  // Your side effect code here
  console.log('Effect executed');
});
```

#### 2. Dependency Array (Optional but Critical)

The dependency array tells React when to re-run the effect. It determines the execution pattern:

```javascript
useEffect(() => {
  // Effect code
}, [dependency1, dependency2]); // Runs when these values change
```

#### 3. Cleanup Function (Optional)

A function returned from the effect that handles cleanup operations:

```javascript
useEffect(() => {
  // Setup code
  
  return () => {
    // Cleanup code
  };
}, [dependencies]);
```

---

## Implementation Patterns

### Pattern 1: Run on Every Render

**Syntax**: No dependency array provided

```javascript
useEffect(() => {
  console.log('Component rendered');
});
```

**Behavior**: Executes after every component render, including the initial mount.

**Use Case**: Rarely used in production; primarily for debugging or specific synchronization needs.

**Example**:

```javascript
function Counter() {
  const [count, setCount] = useState(0);

  useEffect(() => {
    document.title = `Count: ${count}`;
  }); // No dependency array - runs on every render

  return (
    <button onClick={() => setCount(count + 1)}>
      Increment
    </button>
  );
}
```

---

### Pattern 2: Run Only on Mount

**Syntax**: Empty dependency array `[]`

```javascript
useEffect(() => {
  console.log('Component mounted');
}, []); // Empty array - runs once on mount
```

**Behavior**: Executes only once when the component first mounts to the DOM.

**Use Cases**:

- Initial data fetching
- Setting up event listeners
- One-time DOM manipulation
- Initializing third-party libraries

**Example**:

```javascript
function App() {
  useEffect(() => {
    document.title = 'My Application';
    console.log('App initialized');
  }, []); // Runs only once on mount

  return <div>Welcome</div>;
}
```

---

### Pattern 3: Run on Specific Dependencies

**Syntax**: Array with specific values `[dep1, dep2]`

```javascript
useEffect(() => {
  // Effect code
}, [value1, value2]); // Runs when value1 or value2 changes
```

**Behavior**: Executes when the component mounts AND whenever any listed dependency changes.

**Use Cases**:

- Responding to state changes
- Reacting to prop updates
- Conditional side effects

**Example**:

```javascript
function UserProfile() {
  const [userId, setUserId] = useState(1);
  const [userData, setUserData] = useState(null);

  useEffect(() => {
    // Fetch user data when userId changes
    fetch(`/api/users/${userId}`)
      .then(res => res.json())
      .then(data => setUserData(data));
  }, [userId]); // Runs on mount and when userId changes

  return <div>{userData?.name}</div>;
}
```

---

## Practical Examples

### Example 1: Counter with Document Title Update

This example demonstrates basic state tracking with side effects.

**Step 1: Initial Setup**

```javascript
import { useState, useEffect } from 'react';

function Counter() {
  const [count, setCount] = useState(0);

  return (
    <div>
      <p>Count: {count}</p>
      <button onClick={() => setCount(count + 1)}>Add</button>
    </div>
  );
}

export default Counter;
```

**Step 2: Add useEffect to Update Document Title**

```javascript
function Counter() {
  const [count, setCount] = useState(0);

  useEffect(() => {
    document.title = `Count: ${count}`;
  }, [count]); // Runs when count changes

  return (
    <div>
      <p>Count: {count}</p>
      <button onClick={() => setCount(count + 1)}>Add</button>
    </div>
  );
}
```

**Explanation**:

- The effect runs on mount (initial title set to "Count: 0")
- Every time `count` changes, the effect re-runs
- The document title updates to reflect the current count

**Step 3: Add Multiple State Variables**

```javascript
function Counter() {
  const [count, setCount] = useState(0);
  const [color, setColor] = useState('green');

  useEffect(() => {
    document.title = `Count: ${count} ${color}`;
  }, [count, color]); // Runs when count OR color changes

  function addCount() {
    setCount(prevCount => prevCount + 1);
  }

  function subtractCount() {
    setCount(prevCount => prevCount - 1);
  }

  function changeColor() {
    setColor(prevColor => prevColor === 'green' ? 'red' : 'green');
  }

  return (
    <div>
      <p style={{ color: color }}>Count: {count}</p>
      <button onClick={addCount}>Add</button>
      <button onClick={subtractCount}>Subtract</button>
      <button onClick={changeColor}>Change Color</button>
    </div>
  );
}
```

**Key Points**:

- Multiple dependencies in array: `[count, color]`
- Effect runs when ANY dependency changes
- Document title reflects both state values

---

### Example 2: Window Resize Tracker with Event Listeners

This advanced example demonstrates event listener management and cleanup.

**Step 1: Setup State Variables**

```javascript
import { useState, useEffect } from 'react';

function WindowDimensions() {
  const [width, setWidth] = useState(window.innerWidth);
  const [height, setHeight] = useState(window.innerHeight);

  return (
    <div>
      <p>Window Width: {width}px</p>
      <p>Window Height: {height}px</p>
    </div>
  );
}

export default WindowDimensions;
```

**Step 2: Create Resize Handler Function**

```javascript
function WindowDimensions() {
  const [width, setWidth] = useState(window.innerWidth);
  const [height, setHeight] = useState(window.innerHeight);

  function handleResize() {
    setWidth(window.innerWidth);
    setHeight(window.innerHeight);
  }

  return (
    <div>
      <p>Window Width: {width}px</p>
      <p>Window Height: {height}px</p>
    </div>
  );
}
```

**Step 3: Add Event Listener with useEffect (INCORRECT APPROACH)**

```javascript
function WindowDimensions() {
  const [width, setWidth] = useState(window.innerWidth);
  const [height, setHeight] = useState(window.innerHeight);

  // ⚠️ PROBLEMATIC: This adds a new listener on every render
  window.addEventListener('resize', handleResize);
  console.log('EVENT LISTENER ADDED');

  function handleResize() {
    setWidth(window.innerWidth);
    setHeight(window.innerHeight);
  }

  return (
    <div>
      <p>Window Width: {width}px</p>
      <p>Window Height: {height}px</p>
    </div>
  );
}
```

**Problem**: This approach adds a new event listener every time the component re-renders, leading to memory leaks and performance degradation. After a few resizes, hundreds or thousands of listeners may be attached.

**Step 4: Correct Implementation with useEffect**

```javascript
function WindowDimensions() {
  const [width, setWidth] = useState(window.innerWidth);
  const [height, setHeight] = useState(window.innerHeight);

  useEffect(() => {
    window.addEventListener('resize', handleResize);
    console.log('EVENT LISTENER ADDED');
  }, []); // Empty array - add listener only on mount

  function handleResize() {
    setWidth(window.innerWidth);
    setHeight(window.innerHeight);
  }

  return (
    <div>
      <p>Window Width: {width}px</p>
      <p>Window Height: {height}px</p>
    </div>
  );
}
```

**Improvement**: The event listener is added only once when the component mounts.

**Step 5: Add Cleanup Function (COMPLETE SOLUTION)**

```javascript
function WindowDimensions() {
  const [width, setWidth] = useState(window.innerWidth);
  const [height, setHeight] = useState(window.innerHeight);

  useEffect(() => {
    window.addEventListener('resize', handleResize);
    console.log('EVENT LISTENER ADDED');

    // Cleanup function
    return () => {
      window.removeEventListener('resize', handleResize);
      console.log('EVENT LISTENER REMOVED');
    };
  }, []);

  function handleResize() {
    setWidth(window.innerWidth);
    setHeight(window.innerHeight);
  }

  return (
    <div>
      <p>Window Width: {width}px</p>
      <p>Window Height: {height}px</p>
    </div>
  );
}
```

**Step 6: Add Second useEffect for Title Updates**

```javascript
function WindowDimensions() {
  const [width, setWidth] = useState(window.innerWidth);
  const [height, setHeight] = useState(window.innerHeight);

  // First useEffect: Event listener management
  useEffect(() => {
    window.addEventListener('resize', handleResize);
    console.log('EVENT LISTENER ADDED');

    return () => {
      window.removeEventListener('resize', handleResize);
      console.log('EVENT LISTENER REMOVED');
    };
  }, []);

  // Second useEffect: Update document title
  useEffect(() => {
    document.title = `Size: ${width} x ${height}`;
  }, [width, height]);

  function handleResize() {
    setWidth(window.innerWidth);
    setHeight(window.innerHeight);
  }

  return (
    <div>
      <p>Window Width: {width}px</p>
      <p>Window Height: {height}px</p>
    </div>
  );
}

export default WindowDimensions;
```

**Key Insights**:

- Multiple `useEffect` hooks can coexist in one component
- First effect: Manages event listener lifecycle (mount/unmount)
- Second effect: Responds to state changes (width/height updates)
- Each effect has its own dependencies and cleanup logic

---

## Understanding Cleanup Functions

### Cleanup Function Lifecycle

The cleanup function returned from `useEffect` runs in two scenarios:

1. **Before the effect re-runs**: When dependencies change, React cleans up the previous effect before executing the new one
2. **On component unmount**: When the component is removed from the DOM

### Visualization of Execution Order

```javascript
useEffect(() => {
  console.log('The count is:', count);

  return () => {
    console.log('I am being cleaned up!');
  };
}, [count]);
```

**Execution Sequence**:

```
Component Mount:
  → Effect runs: "The count is: 0"

Count changes to 1:
  → Cleanup runs: "I am being cleaned up!"
  → Effect runs: "The count is: 1"

Count changes to 2:
  → Cleanup runs: "I am being cleaned up!"
  → Effect runs: "The count is: 2"

Component Unmount:
  → Cleanup runs: "I am being cleaned up!"
```

### Common Cleanup Scenarios

#### 1. Removing Event Listeners

```javascript
useEffect(() => {
  const handleClick = () => console.log('Clicked');
  document.addEventListener('click', handleClick);

  return () => {
    document.removeEventListener('click', handleClick);
  };
}, []);
```

#### 2. Clearing Timers

```javascript
useEffect(() => {
  const timer = setTimeout(() => {
    console.log('Delayed action');
  }, 1000);

  return () => {
    clearTimeout(timer);
  };
}, []);
```

#### 3. Canceling Subscriptions

```javascript
useEffect(() => {
  const subscription = dataSource.subscribe(data => {
    setData(data);
  });

  return () => {
    subscription.unsubscribe();
  };
}, []);
```

#### 4. Aborting Fetch Requests

```javascript
useEffect(() => {
  const controller = new AbortController();

  fetch('/api/data', { signal: controller.signal })
    .then(res => res.json())
    .then(data => setData(data))
    .catch(err => {
      if (err.name !== 'AbortError') {
        console.error(err);
      }
    });

  return () => {
    controller.abort();
  };
}, []);
```

---

## Best Practices

### 1. Always Specify Dependencies Correctly

React and most code editors will warn you about missing dependencies:

```javascript
// ❌ BAD: Missing dependency
useEffect(() => {
  console.log(count);
}, []); // Warning: React Hook useEffect has a missing dependency: 'count'

// ✅ GOOD: All dependencies listed
useEffect(() => {
  console.log(count);
}, [count]);
```

### 2. Avoid Unnecessary Re-renders

```javascript
// ❌ BAD: Runs on every render
useEffect(() => {
  document.title = 'My App';
});

// ✅ GOOD: Runs once on mount
useEffect(() => {
  document.title = 'My App';
}, []);
```

### 3. Use Multiple useEffect Hooks for Separation of Concerns

```javascript
// ✅ GOOD: Separate effects for different concerns
function UserProfile({ userId }) {
  useEffect(() => {
    // Concern 1: Data fetching
    fetchUserData(userId);
  }, [userId]);

  useEffect(() => {
    // Concern 2: Analytics tracking
    trackPageView('user-profile');
  }, []);

  useEffect(() => {
    // Concern 3: Event listeners
    window.addEventListener('resize', handleResize);
    return () => window.removeEventListener('resize', handleResize);
  }, []);
}
```

### 4. Always Clean Up Side Effects

```javascript
// ✅ GOOD: Proper cleanup prevents memory leaks
useEffect(() => {
  const interval = setInterval(() => {
    console.log('Tick');
  }, 1000);

  return () => clearInterval(interval);
}, []);
```

### 5. Understand Strict Mode Behavior

In React Strict Mode (development only), effects run twice:

- Mount → Effect → Cleanup → Effect

This is intentional to help identify missing cleanup functions:

```javascript
useEffect(() => {
  console.log('Effect'); // Logs twice in development

  return () => {
    console.log('Cleanup'); // Also logs for development-only setup cycle
  };
}, []);
```

### 6. Handle Async Operations Properly

```javascript
// ❌ BAD: Cannot make effect callback async directly
useEffect(async () => {
  const data = await fetchData();
  setData(data);
}, []);

// ✅ GOOD: Define async function inside effect
useEffect(() => {
  async function loadData() {
    const data = await fetchData();
    setData(data);
  }
  
  loadData();
}, []);

// ✅ ALSO GOOD: Using .then()
useEffect(() => {
  fetchData()
    .then(data => setData(data))
    .catch(err => console.error(err));
}, []);
```

---

## Complete Working Examples

### Example 1: Counter with Cleanup Logging

```javascript
import { useEffect, useState } from 'react';

function Demo() {
  const [count, setCount] = useState(0);

  useEffect(() => {
    // The code that we want to run
    console.log('The count is:', count);

    // Optional return function
    return () => {
      console.log('I am being cleaned up!');
    };
  }, [count]); // The dependency array

  return (
    <div className='tutorial'>
      <h1>Count: {count}</h1>
      <button onClick={() => setCount(count - 1)}>
        Decrement
      </button>
      <button onClick={() => setCount(count + 1)}>
        Increment
      </button>
    </div>
  );
}

export default Demo;
```

### Example 2: Window Dimensions Tracker

```javascript
import React, { useState, useEffect } from "react";

function MyComponent() {
  const [width, setWidth] = useState(window.innerWidth);
  const [height, setHeight] = useState(window.innerHeight);

  useEffect(() => {
    window.addEventListener("resize", handleResize);
    console.log("EVENT LISTENER ADDED");

    return () => {
      window.removeEventListener("resize", handleResize);
      console.log("EVENT LISTENER REMOVED");
    };
  }, []);

  useEffect(() => {
    document.title = `Size: ${width} x ${height}`;
  }, [width, height]);

  function handleResize() {
    setWidth(window.innerWidth);
    setHeight(window.innerHeight);
  }

  return (
    <>
      <p>Window Width: {width}px</p>
      <p>Window Height: {height}px</p>
    </>
  );
}

export default MyComponent;
```

---

## Summary

The `useEffect` hook is essential for managing side effects in React functional components. Key takeaways:

1. **Purpose**: Execute code in response to component lifecycle events and state changes
2. **Syntax**: `useEffect(effectFunction, [dependencies])`
3. **Execution Patterns**:
    - No dependency array: Runs on every render
    - Empty array `[]`: Runs once on mount
    - With dependencies `[dep1, dep2]`: Runs on mount and when dependencies change
4. **Cleanup**: Return a function to clean up resources before re-running or unmounting
5. **Best Practices**: Specify dependencies correctly, separate concerns with multiple effects, and always clean up side effects

Understanding `useEffect` thoroughly enables you to build robust, efficient React applications with proper resource management and predictable behavior.