# LlamaParse_GPT_4o_mode_10K_report

## How to Perform Advanced Parsing using LlamaParse with gpt-4o for a 10k Financial Report?

I parsed Amazon 10k Financial Report using LlamaIndex:

▪ LlamaParse with GPT-4o mode to improve the parsing quality, particularly when financial charts are included in the report

▪ SimpleDirectoryParser: a standard way of parsing.

I used HuggingFace local embedding (from LlamaIndex), to store data in a VectoreStore

I created a query engine using different LLMs and compare their results: gpt-3.5-turbo, GPT-4o, and Claude Sonnet 3.5.


## 👉 Key takeaways:
1- In terms of parsing, since the 10k report includes only tables, using LlamaParse with markdown is sufficient (and also visually clear). There's no need for GPT-4o mode. However, as you don't know if there are charts in the PDFs, using GPT-4o mode could be beneficial. 

In a previous post, I found that Claude 3.5 Sonnet was better than GPT-4o on parsing charts as images.
It could be great to have Claude 3.5 Sonnet mode on LlamaParse. It can also be more expensive.

The simple parsing (SimpleDirectoryReader), was good too for these kind of simple questions.

2- In the chat comparison, Claude 3.5 Sonnet was slightly better than GPT-4o. It provides accurate answers and offers valuable details on how some calculations are performed, as well as justifications for certain losses. However, GPT-3.5-Turbo lags significantly behind.