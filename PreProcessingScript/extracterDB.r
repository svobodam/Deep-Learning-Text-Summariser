# Author: Matej Svoboda
# Data Frame exploration.
# Extract data from Documents and summaries into rewsum1 to table in DB


# SUBSET CREATION

# Create Subset and merge all columns into one column called "Documents". Column "Summaries" = summary of document
dfData = with(df, paste0(Document1, Document2, Document3, Document4, Document5, Document6, Document7, Document8, Document9, Document10, Document11, Document12, Document13, Document14, Document15, Document16, Document17, Document18, Document19, Document20, Document21, Document21, Document22, Document23, Document24, Document25))
#
#
dfEdited = data.frame(dfData)
# Create new column named "Documents"
colnames(dfEdited) ="Documents"
dfEdited$Summaries = df$Sum1

# Status echo
cat('Extracting completed.')

