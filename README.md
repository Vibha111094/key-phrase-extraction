
## Key Phrase Extraction

Steps to run:(On VScode)
  - Step1 : Right Click on the dockerfile and choose build image
  - Step2 : docker run --rm -d  -p 8501:8501/tcp kpchallenge:latest
or right click on the latest image and choose Run

  -Note: Due to size and security reasons I have not uploaded the data.
Please upload the data and the corresponding path in the config file


#### Method-1 : Using statistical properties of text

How RAKE algorithm works?

- First convert all text to lower case

- Then split into array of words (tokens) by the specified word delimiters (space, comma, dot etc.)

- This array is then split into sequences of contiguous words by phrase delimiters and stop word positions.

- Words within a sequence are assigned the same position in the text and together are considered a candidate keyword.

- Calculating keyword score by taking ratio of degree to frequency of words.

-Arrange the phrases based on the keyword scores

  

#### Method-2 : Using BERT (a bi-directional transformer model that allows us to transform phrases and documents to vectors that capture their meaning.)

  

- We start by creating a list of candidate keywords or keyphrases from a document.

- Next, we convert both the document as well as the candidate keywords/keyphrases to numerical data(Embeddings)

- We assume that the most similar candidates to the document are good keywords/keyphrases for representing the document.

- To calculate the similarity between candidates and the document, we will be using the cosine similarity.

- We then apply Maximal Marginal Relevance. MMR tries to minimize redundancy and maximize the diversity of results in text summarization tasks.

- We start by selecting the keyword/keyphrase that is the most similar to the document. Then, we iteratively select new candidates that are both similar to the document and not similar to the already selected keywords/keyphrases.

Design:
Have built a simple streamlit App, that takes in the FileName as in the image attached.
We run the algorithms on the entire data and store it in a dataframe which is then cached.
On a new request, we query the file name against the existing existing dataframe and fetch the corresponding keywords.




Scope for improvement:
----> use a database like mongodb
----> some patents have  numbers in them, looks like each of the numbers have a particular description associated with them. Substituting them in the patents would give better results.


![image](https://user-images.githubusercontent.com/16645902/139236472-f0d3bc87-e6e4-4d51-97b0-0c99734950be.png)

