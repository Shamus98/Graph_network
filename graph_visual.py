#! /usr/bin/env python
# -*- coding: utf-8 -*-
import community
import networkx as nx
import matplotlib.cm as cm
import matplotlib.pyplot as plt

G = nx.read_edgelist('email-Eu-core.txt', create_using=nx.DiGraph())
print('Количество вершин: {}'.format(G.number_of_nodes()))
print('Количество рёбер: {}'.format(G. number_of_edges()))
print(' Среднее количество соседей у узлов в графе: {}'.format(round(G.number_of_edges() / float(G.number_of_nodes()), 4)))

if nx.is_directed(G):
    if nx.is_weakly_connected(G):
        print('Граф является направленным и состоит из одной компоненты слабой связности.')
    else:
        print('Граф является направленным и состоит из нескольких компонент.')
else:
    if nx.is_connected(G):
        print('Граф является ненаправленным и связным.')
    else:
        print('Граф является ненаправленным и состоит из нескольких компонент.')

G_weak = G.subgraph(max(nx.weakly_connected_components(G), key=len))
print('Количество вершин: {}'.format(G_weak.number_of_nodes()))
print('Количество рёбер: {}'.format(G_weak.number_of_edges()))
print('Среднее количество соседей у узла в графе: {}'.format(round(G_weak.number_of_edges() / float(G_weak.number_of_nodes()), 4)))

G_strong = G.subgraph(max(nx.strongly_connected_components(G), key=len))
print('Количество вершин: {}'.format(G_strong.number_of_nodes()))
print('Количество рёбер: {}'.format(G_strong.number_of_edges()))
print('Среднее количество соседей у узла в графе: {}'.format(round(G_strong.number_of_edges() / float(G_strong.number_of_nodes()), 4)))

plt.figure(figsize=(15, 15))
plt.title('E-mails')
nx.draw(G, node_size=5)
plt.show()


