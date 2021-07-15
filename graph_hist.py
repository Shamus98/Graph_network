import community
import networkx as nx
import matplotlib.cm as cm
import matplotlib.pyplot as plt

G = nx.read_edgelist('email-Eu-core.txt', create_using=nx.DiGraph())
G_strong = G.subgraph(max(nx.strongly_connected_components(G), key=len))
G_weak = G.subgraph(max(nx.weakly_connected_components(G), key=len))
print ('Диаметр: ', nx.diameter(G_strong))
print ('Среднее расстояние в компоненте сильной связности: ', nx.average_shortest_path_length(G_strong))
print ('Среднее расстояние в компоненте слабой связности: ', nx.average_shortest_path_length(G_weak))

degree = dict(G.degree())
degree_values = sorted(set(degree.values()))
hist = [list(degree.values()).count(x) for x in degree_values]
plt.figure(figsize=(10, 10))
plt.plot(degree_values, hist, 'ro-')
plt.legend(['Degree'])
plt.xlabel('Degree')
plt.ylabel('Number of nodes')
plt.show()