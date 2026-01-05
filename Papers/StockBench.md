# STOCKBENCH: CAN LLM AGENTS TRADE STOCKS PROFITABLY IN REAL-WORLD MARKETS?


All tested LLM agents failed to outperform the passive baseline strategy during the downturn period. In contrast, during the upturn period, most LLM agents surpassed the baseline.
This is the conclusion of the StockBench research paper.
StockBench is a benchmark framework designed to evaluate LLM agents in realistic, multi-month stock trading environments.


Paper link: https://arxiv.org/pdf/2510.02209


## 👉 StockBench has 3 key principles: :

### 1- Realistic Market Interaction:
This is where the back-trading environment plays a role that mimic real-world trading scenarios by:
Using a selected number of stocks (manual pick): 20 stocks from Dow Jones Industrial Average (DJIA), with the highest weights. Why? because they are “representative of the global stock market, and are less prone to short-term irrational sentiment driven events”.
Their related data such as prices and fundamentals are transparent and easy to collect.
News corpus that can be timely constrained (last 48h)

### 2- Continuous Decision Making:
In this workflow, the agent starts with 
a portfolio overview, 
then performs an in-depth analysis of individual stocks when needed, 
and finally produces daily trading decisions based on this analysis: buy, sell, or hold.
These steps mirror the ongoing decision-making process of retail investors and allow the agent to adapt its strategy over time as market conditions change.

### 3- Data Contamination Free. 
The authors ensure the agent has no prior exposure to the test data during its training.


## 👉 Agentic workflow:
### 1- Portfolio overview: 
The agent scans the market and reviews key info for each stock (recent news, current holdings, past actions, opening price).


### 2- In-depth analysis: 
The agent selects specific stocks for deeper analysis and examines extra fundamentals (e.g., market cap, P/E, dividend yield).


### 3- Decision generation: 
For each stock, the agent decides to increase, decrease, or hold the position.


### 4- Execution and validation: 
The system converts dollar targets into shares, checks liquidity constraints, forces revisions if needed, then updates portfolio weights and moves to the next day.



## 👉 Key results
### 1-Average Return : 
As stated at the beginning:

All tested LLM agents underperform during downturn (page 8 and 9)
Downturn period is from January to April 2025. While the Upturn period is from May to August).

However, they also ran experiments during a period of time combining downturn and upturn (from March 3 to June 30, 2025), they found that most of the tested LLM agents surpassed the baseline, up to 2.5% on return vs 0.4% for the baseline. (page 6).

So depending on the timeline, you have different results…

### 2- Basket size:
Increasing the size of the basket from 5 to 30 leads to a declining mean return (two LLMs were compared, Kimi-K2 and GPT-OSS-120B).

### 3- Reasoning vs non-reasoning:
It’s not because you are using a reasoning model that you’ll expect a better performance: 
In the large period from March 3 to June 30, 2025, Instruct LLMs outperformed their reasoning versions.


## 👉 Links
Paper https://arxiv.org/pdf/2510.02209

Code: https://github.com/ChenYXxxx/stockbench/

Project: https://stockbench.github.io

GitHub: https://github.com/ChenYXxxx/stockbench
