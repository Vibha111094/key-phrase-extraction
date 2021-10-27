import os
import pandas as pd
from bs4 import BeautifulSoup
import RAKE
import operator
import streamlit as st
from config import stop_dir, data_directory
from utils import Sort_Tuple


from sklearn.feature_extraction.text import CountVectorizer
from utils import mmr

from sentence_transformers import SentenceTransformer

from sklearn.metrics.pairwise import cosine_similarity

from utils import max_sum_sim


#method-1
@st.cache(suppress_st_warning=True)
def method_stat():
    #st.write("Cache ran")
    rake_object = RAKE.Rake(stop_dir)
    i = 0
    #Create a dataframe containing doc_id and corresponding key phrases using RAKE algorithm
    df = pd.DataFrame(columns=["doc_id", "phrases"], dtype=object)

    for filename in os.listdir(data_directory):
        fn = data_directory + "/" + filename
        base = os.path.basename(filename)
        docid = os.path.splitext(base)[0]
        string_list = []
        infile = open(fn, "r")
        contents = infile.read()
        soup = BeautifulSoup(contents, "xml")
        abstracts = soup.find_all("abstract")
        if len(abstracts) != 0:
            for abstract in abstracts:
                string_list.append(abstract.get_text().strip())
        else:
            continue
        final_sting = (" ").join(string_list)
        doc = final_sting.replace("\n", "")
        keywords = Sort_Tuple(rake_object.run(doc))[-30:]
        kw = []
        for j in keywords:
            kw.append(j[0])
        df.loc[i] = [docid, kw]
        i = i + 1
    return df

@st.cache(suppress_st_warning=True)
def method_bert(input_fn):
    model = SentenceTransformer("distilbert-base-nli-mean-tokens")
    
    fn = data_directory + "/" +input_fn+ ".xml"
    string_list = []
    infile = open(fn, "r")
    contents = infile.read()
    soup = BeautifulSoup(contents, "xml")
    abstracts = soup.find_all("abstract")
    if len(abstracts) != 0:
        for abstract in abstracts:
            string_list.append(abstract.get_text().strip())
    else:
        return None
    final_sting = (" ").join(string_list)
    doc = final_sting.replace("\n", "")
    n_gram_range = (1, 4)
    stop_words = "english"
    count = CountVectorizer(ngram_range=n_gram_range, stop_words=stop_words).fit([doc])
    candidates = count.get_feature_names()
    doc_embedding = model.encode([doc])
    candidate_embeddings = model.encode(candidates)
    keywords = mmr(doc_embedding, candidate_embeddings, candidates, top_n=30, diversity=0.7)
    return keywords

    




#Create load page
st.title("Key-Phrase Extraction")
input_fn = st.text_input("Enter file name", "AT258697B")
st.title("Method-1")

#Get output of the two methods
df_method1=method_stat()
method2_keywords=method_bert(input_fn)

#Get output of method-1
df2 = df_method1[df_method1.doc_id == input_fn]
if(len(df2)>0):
    st.dataframe(df2)
else:
    st.text("No Abstract")

#Get output of method-2
st.title("Method-2")
if(len(method2_keywords)>0):
    st.text(method2_keywords)
else:
    st.text("No Abstract")
