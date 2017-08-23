# Original script developed by Harshal Priyadarshi https://github.com/harpribot
# Edited for purpose of this project.
import numpy as np
import pandas as pd
from nltk.tokenize import wordpunct_tokenize


class Mapper:
    def __init__(self):
        """

        """
        self.map = dict()
        self.map["GO"] = 0
        self.revmap = dict()
        self.revmap[0] = "GO"
        self.counter = 1
        self.document_max_words = 400000
        self.summary_max_words = 250
        self.doc_sum_pair = None
        self.document_tensor = None
        self.summary_tensor = None
        self.document_tensor_reverse = None


    def generate_vocabulary(self, docSum_file):
        
        #Generate vocabulary from docSum_file

        #Load dataset with header located on the row 1
        self.doc_sum_pair = pd.read_csv(docSum_file, header=0).values

        for Documents,Summaries in self.doc_sum_pair:
            doc_lst = wordpunct_tokenize(Documents)
            sum_lst = wordpunct_tokenize(Summaries)
            self.__add_list_to_dict(doc_lst)
            self.__add_list_to_dict(sum_lst)

        # Now store the "" empty string as the last word of the voacabulary
        self.map[""] = len(self.map)
        self.revmap[len(self.map)] = ""


    def __add_list_to_dict(self, word_lst):
        
        # Add to dictionary 
        for word in word_lst:
            #word = word.lower()
            if word not in self.map:
                self.map[word] = self.counter
                self.revmap[self.counter] = word
                self.counter += 1

    
    def get_tensor(self, reverseflag=False):
        
        self.document_tensor = self.__generate_tensor(is_document=True)
        if reverseflag:
            self.document_tensor_reverse = self.__generate_tensor(is_review=True, reverse=True)

        self.summary_tensor = self.__generate_tensor(is_document=False)

        if reverseflag:
            return self.document_tensor,self.document_tensor_reverse,self.summary_tensor
        else:
            return self.document_tensor, self.summary_tensor


    def __generate_tensor(self, is_document, reverse=False):
        
        # is_review parameter from get_tensor()

        seq_length = self.document_max_words if is_document else self.summary_max_words

        total_doc_summary_pairs = self.doc_sum_pair.shape[0]
        data_tensor = np.zeros([total_doc_summary_pairs,seq_length])

        sample = self.doc_sum_pair[0::, 0] if is_document else self.doc_sum_pair[0::, 1]

        for index, entry in enumerate(sample.tolist()):
            index_lst = np.array([self.map[word.lower()] for word in wordpunct_tokenize(entry)])
            # reverse if want to get backward form
            if reverse:
                index_lst = index_lst[::-1]
            # Pad the list
            if len(index_lst) <= seq_length:
                index_lst = np.lib.pad(index_lst, (0,seq_length - index_lst.size), 'constant', constant_values=(0, 0))
            else:
                index_lst = index_lst[0:seq_length]

            data_tensor[index] = index_lst

        return data_tensor


    def get_seq_length(self):
        
        return self.documents_max_words


    def get_vocabulary_size(self):
        
        return len(self.map)


    def get_reverse_map(self):
        
        return self.revmap
