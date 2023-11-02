################################ Importing packedgs ##########################################

import networkx as nx
import matplotlib.pyplot as plt
from random import randint



################################ Importing DATASET ##########################################
FielName="fb-messages.edges"
Graphtype = nx.Graph()   # use net.Graph() for undirected graph
G = nx.read_edgelist(

    FielName,
    create_using=Graphtype,
    nodetype=int,
    delimiter=',',
    data=(('time',int),)
)
#print(G)
#degreeG=nx.degree_centrality(G)
#nx.draw(G,with_labels=False, node_size=[ i * 1 for i in degreeG.values()])
#plt.show()
#G.subgraph(out)
########################################## fuction ##########################################


def subgraphi(G,t,t_):
    out = []
    for u, v in list(nx.edges(G)):
        if G[u][v]['time'] >= t and G[u][v]['time'] <= t_ :
            out.extend([u, v])
    return G.subgraph(out)
"""
n=[]
for j in list(nx.edges(G)):
    neighbor=nx.all_neighbors(G,j)
    n.append(len(list(neighbor)))
"""
#nous avons choisi de calculer le degré de centralité pour les graphes instantanés
#graph à l'instantat T
G1=subgraphi(G,1080090715,1085084784)
#degree1=[val for (node, val) in G1.degree()]
degree1=nx.degree_centrality(G1)
print(degree1)
plt.title("Graph à l'instant T")
#subax1 = plt.subplot(121)
nx.draw(G1, with_labels=False, node_size=[ i * 1000 for i in degree1.values()], node_color='black')
plt.show()

#graph à l'instantat T+1

#subax2 = plt.subplot(122)
G2=subgraphi(G,1085084784,1098769942)
degree2=nx.degree_centrality(G2)
print(degree2)
plt.title("Graph à l'instant T+1")
nx.draw(G2, with_labels=False, node_size=[ i * 1000 for i in degree2.values()], node_color='black')
plt.show()


#le résultat
R = G2.copy()
R.remove_nodes_from(n for n in G2 if n in G1)
degreeR=nx.degree_centrality(R)
print(degreeR)
plt.title("graph presente les nodes influents")
nx.draw(R, with_labels=False, node_size=[ i * 1500 for i in degree2.values()], node_color='green')
plt.show()
