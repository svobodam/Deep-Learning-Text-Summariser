# Script to perform data visualisation
# All visualise stored in dataVisualisation/Plots

# Load required libraries
library(wordcloud)
library(ggplot2)
library(SnowballC)
library(plyr)
library(RColorBrewer)
library(sentimentr)
library(tm)
library(data.table)


# ***Functions***
# Sentiment Analysis
# return sentiment
sentimentAnalysis = function(data_frame, column1, column2) {
  sentiment=with(data_frame, sentiment_by(data_frame$column1, list(data_frame$column2)))
  png('dataVisualisation/Plots/sentiment.png')
  plot(sentiment)
  dev.off()
  return()
}

# Wordcloud
corpusFunction = function(data_frame) {
  c = Corpus(VectorSource(data_frame))
  return(c)
  
}

# Word Frequency
wordFreq = function(corpus) {
  tdm = TermDocumentMatrix(corpus)
  m = as.matrix(tdm)
  #Calculate frequency
  v = sort(rowSums(m), decreasing = TRUE)
  d = data.frame(word = names(v), freq = v)
  d$word = gsub("-", "", d$word)
  png('dataVisualisation/Plots/wordcloud.png')
  wordcloud(words = d$word, freq = d$freq, min.freq = 50,
            max.words = 500, random.order = FALSE,
            rot.per = 0.2, colors = brewer.pal(8, "Dark2"))
  dev.off()
}

# Number of words
wordsNO = function(corpus) {
  tdm = TermDocumentMatrix(corpus)
  wordsNO = data.frame(rowSums(as.matrix(tdm)))
  return(wordsNO)
}

# Visualise Number of Words

visualWordNO = function(i) {
  top_word = i[order(i$Frequency, decreasing = TRUE)]
  top_word = head(top_word, 10)
  d = ggplot(top_word)
  d = d + aes(Words, Frequency)
  d = d + geom_point(alpha = 1 / 3)
  d = d + geom_text_repel(aes(label = Words), size =7)
  png('dataVisualisation/Plots/wordFrequency.png')
  dev.off()
}


# ***Call Functions***
# Sentiment Analysis
sentiment = sentimentAnalysis(dfData, Documents, Summaries)

# Corpus Documents
corpusDoc = corpusFunction(dfData$Documents)

# Wordcloud Documents
wordcloudDoc = wordFreq(corpusDoc)

# Number of words
numWCorpus = corpusFunction(dfData$Documents)
numW = wordsNO(numWCorpus)
numW = setDT(numW, keep.rownames = TRUE)[]
setnames(numW, old = c('rn', 'rowSums.as.matrix.tdm..'), new = c('Words', 'Frequency'))
# Call Visualise function
visualWordNO(numW)
