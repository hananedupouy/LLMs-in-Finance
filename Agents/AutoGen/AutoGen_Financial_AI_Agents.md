# Learn How to Configure an AutoGen Financial AI Agent!

👉 In this notebook, you'll learn step-by-step how to create your own financial AI agent using AutoGen, with clear and practical examples to guide you through the entire process.


## 👉 Setup and Instructions:
🔹 Agent Setup: 
I created two key agents: AssistantAgent and UserProxyAgent (more on that below).

🔹 Fetch and Analyze Data: 
We start by fetching NVIDIA's historical stock prices, then plot them for visual analysis.

🔹 Develop a Momentum Trading Strategy: 
The agents generate a momentum trading strategy, implement it in Python, compute it using NVIDIA's historical data, and then save the results as both a plot and a CSV file.

Here's a quick overview of the workflow:

```
1- Propose a Python code implementation of a momentum trading strategy.
2- Save the code in 'https://lnkd.in/eqfvDHVP'.
3- Apply the strategy to NVIDIA's historical prices.
4- Save the results as 'nvidia_trading_strategy.csv'.
5- Plot and save the strategy in 'nvidia_trading_strategy.png'.
```


## 👉 Meet the Agents:

🔹 AssistantAgent 
Acts like a typical AI assistant powered by a large language model (LLM). It can generate and refine Python code or summarize texts without needing human input or code execution.

🔹 UserProxyAgent
This agent is more advanced. It can:
- Interact with human inputs,
- Execute code directly,
- Call functions or tools, 
- And either rely on LLMs for answers or execute code, depending on the task.

More explanation in the notebook.


## 👉Key Takeaways:

1. Easy to Implement: The setup process is straightforward and user-friendly.

2. Simpler and More Powerful: In my experience, this approach is even easier and more effective than using the standard OpenAI Assistant AI.

3. Automatic and Local File Generation: Files are generated automatically and saved locally for future use, unlike OpenAI Assistant AI where I had to include multiple checks to confirm file creation and re-request if necessary.

4. Highly Customizable: You can create multiple agents and integrate them into a GroupChat manager (which I’ll cover in future notebooks), offering a high degree of customization and flexibility.