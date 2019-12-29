
# Function Random Color * * * 
PickRandomColorVector = function(n){
  qual_col_pals = brewer.pal.info[brewer.pal.info$category == 'qual',]
  col_vector = unlist(mapply(brewer.pal, qual_col_pals$maxcolors, rownames(qual_col_pals)))
  res = sample(col_vector, n)
  return (res)
}

# Clean DF * * * 
CleanDf = function(filename,thresholdf,thresholdp){
  df = read.csv(file = filename,header = T,sep = "," ,stringsAsFactors = F)
  df$A = as.character(df$A)
  df$B = as.character(df$B)
  df = df[df$f>thresholdf,]
  df = df[df$ANFOL>thresholdp,]
  df = df[df$BNFOL>thresholdp,]
  return (df)
}

# Nodes DF * * * 
BuildNodesDf = function(df){
  a = df[,c("ANAME","ANFOL","AFNAME","ADESCRIPTION")]
  b = df[,c("BNAME","BNFOL","BFNAME","BDESCRIPTION")]
  names(a) = c("label","value","flabel","desc")
  names(b) = c("label","value","flabel","desc")
  nodesdf = unique(rbind(a,b))
  nodesdf$id = seq(1,nrow(nodesdf))
  nodesdf$title =  paste0("<p><b>",
                          "ID:",
                          nodesdf$label,
                          "</b><br>",
                          "TITLE:",
                          nodesdf$flabel,
                          "</b><br>",
                          "DESC:",
                          nodesdf$desc,
                          "</p>")
  
  return (nodesdf)
}

# Edges DF * * *
BuildEdgesDf = function(df,nodesdf){
  edgesdf = merge(x = df[,c("ANAME","BNAME","f")],
                  y = nodesdf,
                  by.x ="ANAME",
                  by.y ="label",
                  all.x = TRUE)
  edgesdf = merge(x = edgesdf,
                  y = nodesdf,
                  by.x ="BNAME",
                  by.y ="label",
                  all.x = TRUE)
  edgesdf = edgesdf[,c("id.x","id.y","f")]
  names(edgesdf) = c("from","to","width")
  return(edgesdf)
}

# Run Clustering * * * 
ClusteringGraph = function(nodesdf,edgesdf){
  
  # Walktrap igraph
  nodesdf = nodesdf[,c("id","label","value","flabel","desc","title" )]
  names(edgesdf) = c("from","to","weight")
  g <- graph.data.frame(d = edgesdf,directed = F,vertices = nodesdf)
  clustering = cluster_louvain(g)
  
  
  # Nodes DF et Edges DF updated
  nodesdf$group = as.character(clustering$membership)
  colordf = data.frame(group = unique(as.character(clustering$membership)),
                       color = PickRandomColorVector(length(unique(as.character(clustering$membership)))))
  nodesdf = merge(x = nodesdf,y = colordf,by = "group")
  names(edgesdf) = c("from","to","width")
  
  return(list(edgesdf,nodesdf))
  
}

# Final Network
DefineNetWork = function(nodesdf,edgesdf){
  net = visNetwork(nodesdf, edgesdf,height = "1500", width = "100%") %>%
    visOptions(highlightNearest = TRUE) %>%
    visEdges(smooth = FALSE) %>%
    visPhysics(solver = "forceAtlas2Based",
               stabilization = TRUE,
               forceAtlas2Based = list(gravitationalConstant = -500)) %>%
    visIgraphLayout()
  
  return(net)
}





