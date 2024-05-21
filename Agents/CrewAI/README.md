# Key Takeaway of CrewAI:

With CrewAI you can make several agents collaborate:


*   Each agent has a clear role, goal and a backstroy(description)
*   For each agent, you can specify a set of tools (crewAI tools, LangChain tools, or your own tools)
*   For each agent, you specify a task. It contains a description (instructions) and the expected ouputs. The task can also contains other parameters such as tools (overriding Agent tools), various outpout formats...
*   Then, you create the Crew, the manager, on which you specify your agents and their tasks (the order matter) and the process the agents need to follow to execute the tasks and provide the final answer. 
*   The process involves how the agents collaborate with each other. 
*   The one used is the Hierarchical process, in which the manager decices to which co-worker agent the next task will be delegated, and also handle the memory transition between the different agents. In this process, agents not only answer to the task but also refine the results of the other agents and ask for further improvements. Sequential process also exists.
*   Regardless of the choosen process, agents can also delegate tasks among themselves.

# Tools:
I used 2 examples of tools: one collectinh historical prices and the second one news article from Yhaoo Finance.
I used also 2 tools from CrewAI: Scrape and search tool.


# Use case:

I asked the CrewAI Agent to :
*   Provide insights from Apple' trend analysis, 
*   Extract sentiment analysis from news article, and 
*   Propose trading strategies based on these insights.


# Key Takeaway of Practicing with CrewAI:

*   What I find very interesting are the intermediary results of the agents, which are very insightful and provide much more important analysis than the final answer.

*   Some interesting analyses are highlighted from the news, which guided the agents to propose trading strategies accordingly, especially in light of recent developments and announcements regarding the integration of Microsoft Copilot AI in PCs.

*   Overall insights are correct, however the final result is generic, it can be applied to any instrument.

==> I enjoyed the process much more than the final result.

*   I reduced the number of iteration to 3 max. Even with this I had some interesting intermediate analysis.

*   Be specifc in the agent and task instructions/description. Example: In the same agent, I instruct to analyse historical data for trend analysis and news article for sentiment analysis, by providing 2 tools. It ended up doing one thing.

*   Be careful to specify the LLM you want CrewAI to use in the agents. If not, GPT-4 will be choosen by default (cf API documentation) and it's very expensive, especially when the default number of iteration is 25...(Hopefully I was monitoring costs in OpenAI in the sametime)