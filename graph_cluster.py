import community
import networkx as nx
import matplotlib.cm as cm
import matplotlib.pyplot as plt

G = nx.read_edgelist('email-Eu-core.txt', create_using=nx.DiGraph())
G_strong = G.subgraph(max(nx.strongly_connected_components(G), key=len))
G_weak = G.subgraph(max(nx.weakly_connected_components(G), key=len))

print ('Кластеризация: ', nx.transitivity(G_strong))
print ('Кластерный коэффициент: ', nx.average_clustering(G_strong))
print ('Количество центральных узлов: ', len(nx.center(G_strong)))
print ('Количество узлов на периферии: ', len(nx.periphery(G_strong)))

G_undirected = G_weak.to_undirected()
partition = community.best_partition(G_undirected)
communities = set(partition.values())
communities_dict = {c: [k for k, v in partition.items() if v == c] for c in communities}
highest_degree = {k: sorted(v, key=lambda x: G.degree(x))[-5:] for k, v in communities_dict.items()}
print('Количество сообществ: ', len(highest_degree))
print('Количество элементов в выделенных сообществах:', ', '.join([str(len(highest_degree[key])) for key in highest_degree]))

pos = nx.spring_layout(G)
plt.figure(figsize=(15, 15))
cmap = cm.get_cmap('gist_rainbow', max(partition.values()) + 1)
nx.draw_networkx_nodes(G, pos, partition.keys(), node_size=20, cmap=cmap, node_color=list(partition.values()))
nx.draw_networkx_edges(G, pos, alpha=0.5)
plt.show()