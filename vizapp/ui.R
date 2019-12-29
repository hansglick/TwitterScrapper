source("packages.R")
source("config.R")

ui <- dashboardPage(
  skin = "black",
  
  # le DASHBOARD HEADER
  dashboardHeader(title = "Dashboard"),
  
  
  # le DASHBOARD SIDEBAR
  dashboardSidebar(
    
    
    
    
    # les options sidebar
    tags$head(
      tags$link(rel = "stylesheet", type = "text/css", href = "custom.css")
    ),
    
    
    
    
    sidebarMenu(
      menuItem("Community", tabName = "ONGLET_draft", icon = icon("plane")),
      menuItem("DATAFRAME", tabName = "ONGLET_offset", icon = icon("plane")),
      # menuItem("HABITS", tabName = "ONGLET_habits", icon = icon("plane")),
      # menuItem("RECHERCHE", tabName = "ONGLET_recherche", icon = icon("plane")),
      
      selectInput(
        inputId = "selected_filename",
        label = "Selectionnez une dataset",
        choices = DatasSetsChoices,
        selected = DatasSetsChoices[1],
        selectize = TRUE
      ),
      
      sliderInput(inputId = "selected_poids",
                  label ="RT Minimum du link", 
                  min = 1,
                  max = 100,
                  value = 5
                  ),
      
      sliderInput(inputId = "selected_followers",
                  label ="Followers Minimum", 
                  min = 500,
                  max = 50000,
                  value = 1000
                  ),
      
      actionButton("selected_go",
                   "Run"
                   )
      
      
      
      # actionButton(inputId = "button_next",label ="Suivant"),
      # radioButtons(inputId="decision",
      #              label="Faites votre choix",
      #              choices = c("match","doubt","unmatch","cont diff"),
      #              selected = NULL,
      #              inline = FALSE,
      #              width = NULL,
      #              choiceNames = NULL,
      #              choiceValues = NULL),
      # actionButton("goButton", "Save")
      
      
      
      
    ) # fin de la sidebar menu
    
    
    
    
  ), # fin de la dashboardsidebar
  
  
  
  
  
  # LE DASHBOARD BODY
  dashboardBody(
    
    # Les styles
    tags$style(type="text/css",
               ".shiny-output-error { visibility: hidden; }",
               ".shiny-output-error:before { visibility: hidden; }"
    ),
    
    
    
    
    
    
    
    tabItems(
      
      
      
      
      
      
      
      # Debut onglet draft
      tabItem(
        tabName = "ONGLET_draft",
        
        
        # ROW 1 - Onglet draft
        # Nouvelle Fluidrow pour afficher
        fluidRow(
          box(
            collapsible = TRUE,
            collapsed = FALSE,
            solidHeader = TRUE,
            status = "primary",
            title="Graph",
            width=12,
            visNetworkOutput("network",height = "900px")
          )
        ),
        fluidRow(
        ),
        fluidRow(
        ),
        fluidRow(
        ),
        fluidRow(
        ),
        fluidRow(
        ),
        fluidRow(
        )
        
      ), # FIN ONGLET draft
      
      
      
      
      
      
      # Debut onglet offset
      tabItem(
        tabName = "ONGLET_offset",
        
        # ROW 1 - Onglet offset
        fluidRow(
        )
      ) # FIN ONGLET OFFSET, rajouter virgule apres parenthese si autre onglet
      
      
      
      
      
      # # début Onglet habits
      # tabItem(
      #   tabName = "ONGLET_habits",
      #   
      #   # ROW 1 - Onglet HABITS
      #   fluidRow(
      #   ),
      #   fluidRow(
      #   ),
      #   fluidRow(
      #   ),
      #   fluidRow(
      #   ),
      #   fluidRow(
      #   ),
      #   fluidRow(
      #   ),
      #   fluidRow(
      #   )
      # ), # fin onglet habits
      
      
      
      
      
      # Debut onglet RECHERCHE
      # tabItem(
      #   tabName = "ONGLET_recherche",
      #   # R1 - Onglet recherche
      #   fluidRow(
      #   )
      # ) # Fin ONGLET RECHERCHE
      
      
      
      
      
      
      
      
      
    ) # fin de tabitems global
    
    
    
    
    
    
  ) # fin dashboard body
  
  
) # fin dashboard page














