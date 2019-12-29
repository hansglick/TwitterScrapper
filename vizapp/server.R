shinyServer(function(input, output, session) {
  
  StoredValues <- reactiveValues(graph = NULL)
  
  observeEvent(input$selected_go, {
    df = CleanDf(input$selected_filename,input$selected_poids,input$selected_followers)
    nodesdf = BuildNodesDf(df)
    edgesdf = BuildEdgesDf(df,nodesdf)
    clusterobj = ClusteringGraph(nodesdf,edgesdf)
    edgesdf = clusterobj[[1]]
    nodesdf = clusterobj[[2]]
    StoredValues$graph =  DefineNetWork(nodesdf,edgesdf)
  })
  
  output$network <- renderVisNetwork({
    StoredValues$graph
  })
  
})