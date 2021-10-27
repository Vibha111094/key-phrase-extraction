## Key Phrase Extraction

#### Method-1 : Using statistical properties of text

How RAKE algorithm works?

- First convert all text to lower case

- Then split into array of words (tokens) by the specified word delimiters (space, comma, dot etc.)

- This array is then split into sequences of contiguous words by phrase delimiters and stop word positions.

- Words within a sequence are assigned the same position in the text and together are considered a candidate keyword.

- Calculating keyword score by taking ratio of degree to frequency of words.

  

*Reference*:

https://thinkinfi.com/automatic-keyword-extraction-using-rake-in-python/

  

#### Method-2 : Using BERT (a bi-directional transformer model that allows us to transform phrases and documents to vectors that capture their meaning.)

  

- We start by creating a list of candidate keywords or keyphrases from a document.

- Next, we convert both the document as well as the candidate keywords/keyphrases to numerical data(Embeddings)

- We assume that the most similar candidates to the document are good keywords/keyphrases for representing the document.

- To calculate the similarity between candidates and the document, we will be using the cosine similarity.

- We then apply Maximal Marginal Relevance. MMR tries to minimize redundancy and maximize the diversity of results in text summarization tasks.

- We start by selecting the keyword/keyphrase that is the most similar to the document. Then, we iteratively select new candidates that are both similar to the document and not similar to the already selected keywords/keyphrases.