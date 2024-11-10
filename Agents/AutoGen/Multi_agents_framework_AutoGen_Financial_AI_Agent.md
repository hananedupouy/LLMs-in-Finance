# **How to Leverage the AutoGen Framework for Collaborative Task Management**

The AutoGen framework enables the management of dynamic, collaborative group chats using specialized agents, including code generators, critics, and comparers. It provides conversational agents powered by LLMs, tools, or human input, allowing for effective task completion through automated chat. This setup supports both tool-based and human involvement within multi-agent conversations.

## **Framework Setup**
In this project, I configured:

- **CRITIC Agent**: Reviews the Python code implemented by the Assistant Agent (code_generator) and the code executor.
- **Comparer Agent**: Analyzes and provides insights on final results.


To manage agent interactions, I used the GroupChatManager class. 

This Manager agent coordinates the agents, selects the next speaker, requests responses, and broadcasts them to other agents, creating a seamless, collaborative environment.

## **Use Case: Optimizing a Momentum Trading Strategy**
**Objective**: Use the AutoGen framework to optimize a momentum trading strategy and select the best short/long periods for moving averages.

### **Agent Instructions:**

- Implement a momentum trading strategy.
- Propose various pairs of moving averages.
- Calculate buy and sell signals for each pair.
- Compute and evaluate returns for each moving average pair.

## **Agent Roles**
- **Assistant Agent**: Generates Python code to implement the trading strategy, fetch historical prices, create plots, and perform calculations.
- **UserProxyAgent**: Executes the code.
- **Critic Agent**: Reviews and scores the code based on defined metrics.
- **Comparer Agent**: Compares results for different moving average pairs.
- **Group Chat Manager:** Oversees agent interactions and manages the workflow to complete the task.


Files (png, csv, python) are included in "data" folder