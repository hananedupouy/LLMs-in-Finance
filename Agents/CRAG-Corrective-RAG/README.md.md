# How Can Corrective RAG Enhance Financial Analysis?

CRAG is a technique developed to enhance the reliability of text generation by addressing the shortcomings of large language models (LLMs) and retrieval-augmented generation (RAG) systems.

By integrating corrective mechanisms with advanced retrieval and refinement strategies, CRAG significantly improves the accuracy and dependability of generated text.


# CRAG: Corrective RAG Package
## LlamaIndex has developed a CRAG package.
!pip install llama-index llama-index-tools-tavily-research -q
!llamaindex-cli download-llamapack CorrectiveRAGPack --download-dir ./corrective_rag_pack

## Steps
👉 It combines standard retrieval strategies, with the corrective component:
▪ For each document, the relevance of the user query to this document is evaluated, using an LLM, to provide a binary score ('yes' or 'no')
▪ The user query is refined to improve its search perfomance when it comes to call external search API.
▪ If there is only one 'no' score in the retrieved documents, the external search API is triggered, and all the information is sent back to an LLM to provide the final answer to the query.


## 👉 Key Takeaways:

1- The quality of your query is crucial here. Since CRAG will refine your question into a better prompt to enhance its search performance, you need to include all the important keywords:

For example: 
*  You are attempted to ask this following question because you are chating with your LLM:
**"What was the net income in 2019?"**

So the transformed query by the CRAG will be: 
**"2019 net income"**
==> This, when sent to Tavily search, it will results in a poor-quality answers!!

*  However, if you ask: 
**"What was the net income in 2019 of JPMorgan Chase bank?"**
The refined question will be: **"JPMorgan Chase bank 2019 net income"**
=> This will result in a good answer.

2- One a question at a time


## 👉Notes:

1- I didn't use gpt-4o when using LlamaParse, because I wanted to evaluate the quality of the CRAG over the quality of the parsing (coming soon).
2- I made small modification to the CorrectiveRAGPack (to visualize some intermediate results). 