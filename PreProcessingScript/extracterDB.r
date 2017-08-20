# Data Frame exploration.
# Extract data from Documents and document summaries into new subset and prepare them for extarction to table in DB.

# Extract Documents from df > dfData
counter = 1
while(counter <= 25){
  for (m in doc) {
    if ((exists("dfData"))==TRUE) {
      dfEdit=data.frame(with(df, paste0(df[[m]])), stringsAsFactors=FALSE)
      colnames(dfEdit)="Documents"
      dfData=rbind(dfData,dfEdit)
    } else {
      dfData=data.frame(with(df, paste0(df[[m]])),stringsAsFactors=FALSE)
      colnames(dfData)="Documents"
    }
    counter = counter + 1
    
  }
}


# Extract Document names from df > dfDataNames

docNames = c('DocumentName1', 'DocumentName2', 'DocumentName3', 'DocumentName4', 'DocumentName5', 'DocumentName6', 'DocumentName7', 'DocumentName8', 'DocumentName9', 'DocumentName10', 'DocumentName11', 'DocumentName12', 'DocumentName13', 'Document14', 'DocumentName15', 'DocumentName16', 'DocumentName17', 'DocumentName18', 'DocumentName19', 'DocumentName20', 'DocumentName21', 'DocumentName22', 'DocumentName23', 'DocumentName24', 'DocumentName25')
counter = 1
while(counter <= 25){
  for (w in docNames) {
    if ((exists("dfDataNames"))==TRUE) {
      dfEditNames=data.frame(with(df, paste0(df[[w]])), stringsAsFactors=FALSE)
      colnames(dfEditNames)="DocSum"
      dfDataNames=rbind(dfDataNames,dfEditNames)
    } else {
      dfDataNames=data.frame(with(df, paste0(df[[w]])),stringsAsFactors=FALSE)
      colnames(dfDataNames)="DocSum"
    }
    counter = counter + 1
    
  }
}

#Merge data frames together
dfData$DocSum = dfDataNames$DocSum

# Status echo
cat('Extracting completed. Moving to another stage...')

