#!/usr/bin/env python
# Author: Matej Svoboda
# Database connection for DB manipulation

# Import libraries
import sqlite3
sqlConnection = sqlite3.connect('Data/DUCDataset.db')

c = sqlConnection.cursor()

c.execute("DELETE from summDUC WHERE TopicNo = 'D0702A'")

# Save changes
sqlConnection.commit()

# Close connection to DB
sqlConnection.close()
