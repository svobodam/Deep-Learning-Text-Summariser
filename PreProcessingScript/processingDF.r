# Author: Matej Svoboda
# Data Frame processing
# Dataset used as .db file to allow managing DF from Python and R.
# This process process dataset to remove html tags.



# ***FUNCTIONS***
# Function which transorm DS to Corpus and preprocess it.
dfCorpusFN = function(data_frame) {
  c = Corpus(VectorSource(data_frame))
  
  removeText = function(b) {
    gsub(".*<DATE_TIME>-*|*-</DATE_TIME>", "", b)
  }
  removeTxt = function(a) {
    gsub(".*<CATEGORY>.*usa*.</CATEGORY>", "", a)
  }
  removeURL = function(x) {
    gsub("http[[:alnum:]]*", "", x)
  }
  removeTAGS = function(m) {
    gsub("RT /via ", "", m)
  }
  removeUTAG = function(n) {
    gsub("<.*?>", "", n)
  }
  removeTopicName = function(i) {
    gsub("APW[[:alnum:]]*.[0*]", "", i)
  }
  extractText = function(t) {
    gsub(".*<p>|</p>.*", "", t)
  }
  removeSCH = function(r) {
    gsub("&,^,*,@,#,~,?,$,£", "", r)
  }
  c = tm_map(c, content_transformer(removeText))
  c = tm_map(c, content_transformer(removeTxt))
  c = tm_map(c, content_transformer(removeURL))
  c = tm_map(c, content_transformer(removeTAGS))
  c = tm_map(c, content_transformer(removeUTAG))
  c = tm_map(c, content_transformer(removeTopicName))
  c = tm_map(c, content_transformer(extractText))
  c = tm_map(c, content_transformer(removeSCH))
  c = tm_map(c, removePunctuation)
  c = tm_map(c, content_transformer(tolower))
  return(c)
}

# Convert corpus back to data frame
convert2DF = function(d) {
  dfEd = data.frame(text=unlist(sapply(d, as.character)), stringsAsFactors = F)
  dfEd["Documents"] = NA
  dfEd = melt(dfEd, id.vars=c("Documents"))
  return(dfEd)
}


# ***END OF FUNCTIONS***

# PREPROCESS ALL DOCUMENTS IN DF DATASET
# Run loop over all documents in Dataset
counter = 1 #for testing
doc = c('Document1', 'Document2', 'Document3', 'Document4', 'Document5', 'Document6', 'Document7', 'Document8', 'Document9', 'Document10', 'Document11', 'Document12', 'Document13', 'Document14', 'Document15', 'Document16', 'Document17', 'Document18', 'Document19', 'Document20', 'Document21', 'Document22', 'Document23', 'Document24', 'Document25')
while(counter <= 25){
  for (i in doc) {
    dfCorpus = dfCorpusFN(df[[i]])
    dfNew = convert2DF(dfCorpus)
    df[[i]] = dfNew$value
    counter = counter + 1
  }
}
# Status echo
cat('Preprocessing completed. Moving to another stage...')


