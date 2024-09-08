from dash import Dash, html, dcc
import pandas as pd
import networkx as nx
import plotly.graph_objects as go
import networkx as nx
from dashapphelper import fullTripleGeneration, sparseTripleGeneration, graphGeneration

app = Dash()
data = pd.read_csv('/Users/devammondal/PycharmProjects/geneKnowledgeGraphs/all_searched_entities_26_08_24.tsv', sep='\t')

relationships = sparseTripleGeneration(data)
fig = graphGeneration(relationships)

app.layout = [
    fig.show()
]

if __name__ == "__main__":
    app.run_server(debug=True)