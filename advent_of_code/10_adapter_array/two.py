import pandas as pd
import numpy as np
from functools import reduce
import networkx as nx

df = pd.read_csv('advent_of_code/10_adapter_array/input.txt', header=None, names=['jolts'])

df.loc[-1, :] = [0] #Base adapter
df = df.sort_values(by='jolts', ascending=True)
df.loc[df.shape[0], :] = [df.iloc[-1] + 3] #phone adapter
vals = df['jolts'].astype(int).values.tolist()

# Build graph, separate in 'bridges', single possible connection components.
G = nx.DiGraph()
G.add_nodes_from(vals)
for i, value in enumerate(vals):
    for j, sig in enumerate(vals[i+1:i+4]):
        diff = sig - value
        if diff > 3 or (diff == 3 and j < 2):
            break
        G.add_edge(value, sig, weight=1)

# Generate the subgraphs and count the possible paths between them
sub_graphs = list(nx.weakly_connected_components(G))
accu = []
for sg_t in sub_graphs:
    if len(sg_t) <= 1:
        continue
    sg = nx.subgraph(G, sg_t)
    paths = nx.all_simple_paths(sg, source=min(sg.nodes), target=max(sg.nodes))
    count = len(list(paths))
    accu.append(count)

# Product of every count of possible paths for each subgraph gives total possible paths
# counting every path in the full graph would be intractable (I tried, sigh)
# This solution takes into account the toppology of the graph: litle mesh-like groups and 1-way bridges
print(accu)
print(np.prod(accu))
