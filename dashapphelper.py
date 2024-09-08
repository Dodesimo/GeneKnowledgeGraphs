import pandas as pd
import networkx as nx
import plotly.graph_objects as go
import networkx as nx

def fullTripleGeneration(data):
    relationships = []
    for a, b, c in zip(data['ENTITYA'], data['EFFECT'], data['ENTITYB']):
        relationships.append((a, b, c))
    return relationships

def sparseTripleGeneration(data):
    relationships = []
    counter = 0
    for a, b, c in zip(data['ENTITYA'], data['EFFECT'], data['ENTITYB']):
        if counter == 50:
            return relationships
        else:
            relationships.append((a, b, c))
            counter += 1

    return relationships

def graphGeneration(relationships):
    graph = nx.DiGraph();

    for relationship in relationships:
        graph.add_edge(relationship[0], relationship[2], label=relationship[1])

    pos = nx.spring_layout(graph, seed=2, k=3)

    edge_traces = []

    edge_label_trace = go.Scatter(

        x=[(pos[edge[0]][0] + pos[edge[1]][0]) / 2 for edge in graph.edges()],
        y=[(pos[edge[0]][1] + pos[edge[1]][1]) / 2 for edge in graph.edges()],
        mode='text',
        text=[graph[edge[0]][edge[1]]['label'] for edge in graph.edges()],
        textposition='middle center',
        hoverinfo='none',
        textfont=dict(size=7)

    )

    for edge in graph.edges():
        x0, y0 = pos[edge[0]]
        x1, y1 = pos[edge[1]]
        edge_trace = go.Scatter(
            x=[x0, x1, None],
            y=[y0, y1, None],
            mode='lines',
            line=dict(width=2, color='gray'),
            hoverinfo='none'
        )
        edge_traces.append(edge_trace)

    node_trace = go.Scatter(

        x=[pos[node][0] for node in graph.nodes()],
        y=[pos[node][1] for node in graph.nodes()],
        mode='markers+text',
        marker=dict(size=15, color='lightblue'),
        text=[node for node in graph.nodes()],
        textposition='top center',
        hoverinfo='text',
        textfont=dict(size=7)

    )

    # Create layout
    layout = go.Layout(
        title='Knowledge Graph',
        titlefont_size=16,
        title_x=0.5,
        showlegend=False,
        hovermode='closest',
        margin=dict(b=20, l=5, r=5, t=40),
        xaxis_visible=False,
        yaxis_visible=False
    )

    return go.Figure(data=edge_traces + [node_trace, edge_label_trace], layout=layout)
