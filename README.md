# VectorShift Pipeline Builder

A visual pipeline builder with a React frontend and FastAPI backend.

---

## Prerequisites

- [Node.js](https://nodejs.org/) (v16 or higher)
- [Python](https://www.python.org/) (v3.8 or higher)
- pip

---

## Backend Setup

Open a terminal in the `backend` folder:

```bash
cd backend
pip install -r requirements.txt
uvicorn main:app --reload
```

The API will be running at **http://localhost:8000**.

---

## Frontend Setup

Open a **second** terminal in the `frontend` folder:

```bash
cd frontend
npm install
npm start
```

The app will open at **http://localhost:3000**.

> `npm install` downloads all dependencies into `node_modules/` — this only needs to be run once (or whenever dependencies change).

---

## Project Structure

```
VectorShift/
├── backend/
│   ├── main.py            # FastAPI app
│   └── requirements.txt   # Python dependencies
└── frontend/
    ├── public/
    └── src/
        ├── nodes/         # All pipeline node types
        ├── App.js
        ├── ui.js          # Main canvas
        ├── store.js       # Zustand state
        ├── toolbar.js
        └── submit.js      # Pipeline submission to backend
```

---

## How It Works

- Drag nodes from the toolbar onto the canvas and connect them.
- Click **Submit** to send the pipeline to the backend, which returns:
  - Number of nodes
  - Number of edges
  - Whether it forms a valid DAG (Directed Acyclic Graph)
