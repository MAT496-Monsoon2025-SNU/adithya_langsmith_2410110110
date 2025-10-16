ADITHYA CHIGULLAPALLY 2410110110
LANG GRANPH

vid1:motivation
learnt:i learnt what is lang graph, basically it is used for control flow of the llm model to process. lang graph helps it run smoothly and makes sure everything is working safely.
code:no source code.

vid2:simple graph
learnt: i learnt how to build the graph through coding and what basic components are needed for it.
changes: i added a new node 4 with a state similar to the other nodes, and it decides which path to take. earlier it started from node 1, but now it can choose between node 1 and node 4, where node 4 directly leads to the end.
source code:https://github.com/langchain-ai/langchain-academy/blob/main/module-1/simple-graph.ipynb
teaked code:http://github.com/MAT496-Monsoon2025-SNU/adithya_langsmith_2410110110/blob/main/lang_graph/simple-graph.ipynb


vid3:langgraphh studio
learnt: after running my studio, it directly opened in my browser in langsmith and showed me the graph of vid2. for input, i wrote "hi this is adithya".
code:no code to modify.
<img width="1604" height="727" alt="image" src="https://github.com/user-attachments/assets/3978c2dd-2b4d-4633-8a4e-916673c1a12a" />



vid4:chain
learnt: i learnt how to build a simple chain in langgraph that uses chat messages, chat models, binds tools to the llm, and executes tool calls in the graph.
changes:eplaced the default tool-calling cell with a custom web_search tool that uses serper and tavily apis to search the web, and tested it by searching “ajitkumar shiv nadar university
source code:https://github.com/langchain-ai/langchain-academy/blob/main/module-1/chain.ipynb
tweaked code:https://github.com/MAT496-Monsoon2025-SNU/adithya_langsmith_2410110110/blob/main/lang_graph/chain.ipynb


vid5:router
learnt: i learnt how a chat model decides its route based on our input.
changes: added a new tool called xor, which contains multiply, and added a new route about shopping that tells us the prices of our desired product.
source code:https://github.com/langchain-ai/langchain-academy/blob/main/module-1/router.ipynb
tweaked code:https://github.com/MAT496-Monsoon2025-SNU/adithya_langsmith_2410110110/blob/main/lang_graph/router.ipynb
