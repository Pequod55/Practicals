library(igraph)
g<- as.data.frame(cbind(matrix(c(1,2,1,3,1,4,3,4,2,4), byrow =TRUE, ncol = 2 )))
print(g)
g<-graph.data.frame(g, directed = FALSE)
plot(g)
g<- g+vertices(5)
plot(g)
g["1","2"]<-NULL
plot(g)
g<-g+edge("1","5")
g<-g+edge("2","5")
plot(g)


library(igraph)
G<-graph.tree(n=13,children = 2)
V(G)$name<-LETTERS[1:length(V(G))]
lay<-layout.reingold.tilford(G,params=list(root='A'))
plot(G,layout=lay,vertex.size=25)
G<-G+vertices('O')
G<-G+edge('G','O')
lay<-layout.reingold.tilford(G,params = list(root='A'))
plot(G,layout=lay,vertex.size=25)