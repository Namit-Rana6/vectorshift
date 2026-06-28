from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import List

app = FastAPI()

# Allow requests from any origin so the dev server works regardless of
# whether it is accessed via localhost, 127.0.0.1, or a LAN IP address.
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=False,
    allow_methods=["*"],
    allow_headers=["*"],
)


class Node(BaseModel):
    id: str


class Edge(BaseModel):
    source: str
    target: str


class Pipeline(BaseModel):
    nodes: List[Node]
    edges: List[Edge]


def is_dag(nodes: List[Node], edges: List[Edge]) -> bool:
    """
    Returns True if the graph formed by nodes/edges is a Directed Acyclic Graph.
    Uses Kahn's algorithm (BFS topological sort).
    A graph with no edges is trivially a DAG.
    Nodes referenced only in edges (not in the nodes list) are also handled.
    """
    node_ids = {n.id for n in nodes}

    # Build adjacency list and in-degree map for all known node ids
    in_degree = {n: 0 for n in node_ids}
    adjacency = {n: [] for n in node_ids}

    for edge in edges:
        src, tgt = edge.source, edge.target
        # Guard against edges referencing unknown node ids
        if src not in adjacency:
            adjacency[src] = []
            in_degree[src] = 0
        if tgt not in in_degree:
            adjacency[tgt] = []
            in_degree[tgt] = 0
        adjacency[src].append(tgt)
        in_degree[tgt] += 1

    # Kahn's algorithm
    queue = [n for n, deg in in_degree.items() if deg == 0]
    visited = 0

    while queue:
        node = queue.pop(0)
        visited += 1
        for neighbor in adjacency.get(node, []):
            in_degree[neighbor] -= 1
            if in_degree[neighbor] == 0:
                queue.append(neighbor)

    return visited == len(in_degree)


@app.get('/')
def read_root():
    return {'Ping': 'Pong'}


@app.post('/pipelines/parse')
def parse_pipeline(pipeline: Pipeline):
    num_nodes = len(pipeline.nodes)
    num_edges = len(pipeline.edges)
    dag = is_dag(pipeline.nodes, pipeline.edges)

    return {
        'num_nodes': num_nodes,
        'num_edges': num_edges,
        'is_dag': dag,
    }
