# Source control script for complete dataset processing

setwd('~/summCode')

# LIBRARIES
library(RSQLite)
library(tm)
library(reshape2)
library(gsubfn)


# FUNCTIONS
# Connection to DB
connDB = function(z) {
  # Initiate Connection to DB
  conn = dbConnect(dbDriver("SQLite"), z)
  return(conn)
}

# Disconnect from DB
disDB = function(w) {
  dbDisconnect = dbDisconnect(w)
  return()
}



# CONTROL
# READ DATA FROM DATABASE
# Status echo
cat('Connecting to database and dataset extracing...')

# Initiate connection to DB
conn = connDB('Data/DUCDataset.db')

# Extract data from the table in DB
df = dbGetQuery(conn, "select * from summDUC")

# Disconnect from DB
dis = disDB(conn)

# Status echo
cat("Stage 1: Dataset explorarion\n")
cat("Dataset exploration...\n")

# Call dataset exploration script ()
source('PreProcessingScript/explorationDF.r')

# Status echo
cat("Stage 2: Dataset processing...\n")
# Call dataset processing script ()
source('PreProcessingScript/processingDF.r')

# Status echo
cat("Extracting preprocessed documents and summaries from DF...")
source('PreProcessingScript/extracterDB.r')



# WRITE CHANGES BACK TO DATABASE
# Status echo
cat("Writing all changes back to DB")
# Initiate Connection to DB
conn = connDB('Data/DUCDataset.db')

# Write changes back to DB
# Wright query to database. Create new table and write new data
dbSendQuery(conn, "CREATE TABLE rewsum1(Documents TEXT, Summaries TEXT)")
dbWriteTable(conn, name="rewsum1", dfEdited, append=T, row.names=F, col.names=T)

# Extract data from 'rewsum1' table and write them to .csv file
raw = dbGetQuery(conn, 'SELECT * FROM rewsum1')
write.csv(raw, 'Data/rewsum.csv', row.names = F)

# Disconnect from DB
dis = disDB(conn)

cat("Dataset processed. Changes saved. Completed this stage. Moving forward...")
