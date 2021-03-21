#Formacao Inteligencia Artificial e Machine Learning - Fernando Amaral

library(shiny)
library(bnlearn)
idade =unique(insurance$Age)
risco = unique(insurance$RiskAversion)
modelo = unique(insurance$MakeModel)

ui <- fluidPage(
  titlePanel("Avalicao Riscos Seguradora ABC"),
  sidebarLayout(
    sidebarPanel(
      
      selectInput("Idade","Selecione a Idade:",choices = idade),
      selectInput("Risco","Gosto de Risco:",choices = risco),
      selectInput("Modelo","Modelo do Veiculo:",choices = modelo),
      actionButton("Processar","Processar")
    ),
    mainPanel(
      
      plotOutput("coolplot"),
      br(),
      
      
     h1(textOutput("Resultado"))
      
    )
  )
)
# selectInput("Condisele","Selecione Codicao Economica:",choices = condicaoeconomica)


server <- function(input, output) {
  
  
  
 
 calcula <- function(){
    res <- hc(insurance)
    output$coolplot = renderPlot({plot(res)})
    modelo <- bn.fit(res, data = insurance)
    
    varidade = input$Idade
    varrisco = input$Risco
    varmodelo = input$Modelo
    
    ev = paste("(Age== '", varidade, "' & RiskAversion=='", varrisco, "' & MakeModel == '", varmodelo, "')",",n=10000000", sep = "")
    
    cmd = paste("cpquery(modelo, event =( Accident=='Moderate' | Accident=='Severe' ),evidence=", ev, ")", sep = "")
    ret = eval(parse(text = cmd))


    
    
    return(ret)
  }
  
  
  observeEvent(input$Processar, {
    
   
    xc =  paste("Risco Avaliado: " ,round(calcula(), digits = 2 ))
   
    output$Resultado = renderText({ xc})
    
  })
  
  
  
  
  
}
shinyApp(ui = ui, server = server)

