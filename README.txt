#	***Abstractive Text Summariser***
#
#	Author: Matej Svoboda
#
#	***All Rights Reserved***
#
################################################################################
#
# CONTENT OF THE FOLDER
#
#
# Data > 
#	DUC Dataset in original .txt form
#	DUCDatat.db - SQLite database file
#	rewsum.csv - extracted data from DUCDataset.db
#
# PreProcessingScript > 
#	checkpoint.py - script which saves checkpoint after certain steps
#	data2tensor.py - script which transfer data to tensors
#	explorationDF.r - script which do basic exploration of dataset stored in .db file
#	extracterDF.r - script which extracts documents and summaries from .db to .csv
#	dbConn.py - script to initiate connection to .db file for it's manipulation
#	Python Script to preprocess data
# 
# dataVisualisation >
#	visualisationDF.r
#
# Evaluation >
#
#
#
# Models >
#	lstm_simple.py - initiate deep learning process
#	sequenceNet.py - neural network
#	simple.py - neural network
#
# Results >
#	lstm >
#		output.csv - results of the summarisation process.
#
# runSCripts >
#	trainLSTM-ATTN.py - script to initiate lstm training with attention
#	trainLSTM-noATTN.py - script to initiate lstm training without attention
# 
# startup.sh - starup script which automatise program
#
#
#
