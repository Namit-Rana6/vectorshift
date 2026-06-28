# VectorShift Pipeline Builder

A visual pipeline builder built with a **React** frontend and **FastAPI** backend as part of the VectorShift Frontend Technical Assessment.

---

# Prerequisites

* Node.js (v16 or later)
* Python (v3.8 or later)
* pip

---

# Backend Setup

Open a terminal inside the `backend` directory:

```bash
cd backend
pip install -r requirements.txt
uvicorn main:app --reload
```

If your frontend is served through a network address (for example, when using WSL/Hyper-V), start the backend using:

```bash
uvicorn main:app --reload --host 0.0.0.0
```

The backend will run on port **8000**.

---

# Frontend Setup

Open a second terminal inside the `frontend` directory:

```bash
cd frontend
npm install
npm start
```

The React development server will display both a **Local** and an **On Your Network** URL.

If `http://localhost:3000` does not respond in your environment, use the **On Your Network** URL printed by `npm start` (for example, `http://172.x.x.x:3000`).

> `npm install` only needs to be run once (or whenever project dependencies change).

---

# Features

### Part 1 – Node Abstraction

* Shared `BaseNode` component for common node layout and handle rendering.
* Configuration-driven `createNode` factory for creating reusable node types.
* Reusable field rendering system for text inputs, dropdowns, number inputs, and textareas.
* Five additional node types:

  * API
  * Filter
  * Delay
  * Merge
  * Note

---

### Part 2 – Styling

* Unified light theme with consistent typography and spacing.
* Color-coded node categories.
* Redesigned toolbar and analysis dialog.
* Customized React Flow controls and canvas styling.

---

### Part 3 – Text Node Logic

* Dynamic width adjustment based on content.
* Dynamic height adjustment.
* Automatic detection of variables written as `{{variable}}`.
* Dynamic creation and removal of corresponding React Flow input handles.
* Duplicate variable detection.

---

### Part 4 – Backend Integration

* Frontend submits the current pipeline to the FastAPI backend.
* Backend calculates:

  * Number of nodes
  * Number of edges
  * Whether the graph forms a Directed Acyclic Graph (DAG) using Kahn's Algorithm
* Results displayed in a custom analysis dialog.
* Cycle visualization through highlighted edges.

---

# Project Structure

```
VectorShift/
├── backend/
│   ├── main.py
│   └── requirements.txt
│
└── frontend/
    ├── public/
    ├── src/
    │   ├── nodes/
    │   ├── App.js
    │   ├── store.js
    │   ├── toolbar.js
    │   ├── ui.js
    │   └── submit.js
    ├── package.json
    └── README.md
```

---

# Usage

1. Start both the frontend and backend.
2. Drag nodes from the toolbar onto the canvas.
3. Connect nodes to build a pipeline.
4. Click **Analyse Pipeline**.
5. The backend returns:

   * Total number of nodes
   * Total number of edges
   * Whether the pipeline forms a valid Directed Acyclic Graph (DAG)

The analysis results are displayed in a modal within the application.
