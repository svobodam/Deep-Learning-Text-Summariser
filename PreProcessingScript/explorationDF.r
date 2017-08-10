# Author: Matej Svoboda
# Data Frame exploration
# Dataset used as .db file to allow managing DF from Python and R.
# This script provides only basic exploration of the DF, including nrow(), ncol(), number of topics, number of documents and number summaries.

# FUNCTIONS
# Dataset preprocessing FUNCTION
dfExplore = function(data_frame) {
  Num_row = nrow(data_frame)
  Num_col = ncol(data_frame)
  NA_val = sum(is.na(df))
  cat("Number of rows in the dataset is:", Num_row, "\n", 
      "and number of columns:", Num_col,"\n", 
      "Number of missing values:", NA_val, "\n")
}

# Topic Explore function
topicExplore = function(data_frame){
  Topic_No = nrow(data_frame)
  
  Doc_per_topicFN = function(data_frame){
    sum(grepl("DocumentNo", colnames(data_frame)))
  }
  
  Doc_per_topic = (Doc_per_topicFN(data_frame) * Topic_No) / Topic_No
  
  Sum_per_topicFN = function(data_frame){
    sum(grepl("Sum", colnames(data_frame)))
  }
  
  Sum_per_topic = (Sum_per_topicFN(data_frame) * Topic_No) / Topic_No
  
  cat("Number of Topics in Dataset:", Topic_No,"\n",
      "Number of documents per topic:", Doc_per_topic,"\n",
      "Number of Summaries per topic:", Sum_per_topic, "\n")
  
}
# END OF FUNCTIONS

# DATASET EXPLORATION
# Call dfExplore function
dfExplore(df)

# Call dfExplore function
topicExplore(df)
cat("Exploration completed, proceeding to next stage. \n")
