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
changes: added a new tool called xor, which contains multiply, and added a new route about shopping that tells us the prices of our desired product and cretaed cell for each path so we can compare the ouput.
source code:https://github.com/langchain-ai/langchain-academy/blob/main/module-1/router.ipynb
tweaked code:https://github.com/MAT496-Monsoon2025-SNU/adithya_langsmith_2410110110/blob/main/lang_graph/router.ipynb
IMAGE IN LANGSMIT(ran through studio)H 
<img width="1153" height="664" alt="image" src="https://github.com/user-attachments/assets/b93fc0eb-698d-469f-a74e-c0130821780d" />


vid6:agent
learnt: i learnt how the output is affected when we feed the output of the tool to it again, and how it can be used in other calling.
changes: added a new node "temp" which calculates the temperature from celsius to fahrenheit. this node calls the tool, and again the tool calls itself to calculate the temperature and create 2 cells to compare the output.
source code:https://github.com/langchain-ai/langchain-academy/blob/main/module-1/agent.ipynb
tweaked code:https://github.com/MAT496-Monsoon2025-SNU/adithya_langsmith_2410110110/blob/main/lang_graph/agent.ipynb
IMAGE IN LANGSMITH(ran through studio)
<img width="1228" height="907" alt="image" src="https://github.com/user-attachments/assets/61a09557-31ee-40f2-abfb-2031724951d1" />

vid7: agent-memory
learnt: i learned that an agent normally does not remember the functions it executes. to make it remember, we add a checkpoint and use memory, so it can recall the function and run it. this makes it easier because we don’t have to repeat the task every time we need a change.
changes: added a new tool called xor, then added new cells at the end where it calls the tools and updates the output, which is stored in memory, and performed a new arithmetic operation on a number to test whether it would get confused with the old value or operate only on the most recent one. the test was successful.(i thought it ould get confused quiet impressive)
source code:https://github.com/langchain-ai/langchain-academy/blob/main/module-1/agent-memory.ipynb
tweaked code:https://github.com/MAT496-Monsoon2025-SNU/adithya_langsmith_2410110110/blob/main/lang_graph/agent-memory.ipynb


vid8:deployment
learnt:i learned how to get output of the our input message dirrecty from grpah present at our local host.
i could not deploy d=because deployment can be done when we are a part of paid plan but i tried it.
changes:could not make any chnages as i could not deploy.
source code:https://github.com/langchain-ai/langchain-academy/blob/main/module-1/deployment.ipynb
tweaked code:https://github.com/MAT496-Monsoon2025-SNU/adithya_langsmith_2410110110/blob/main/lang_graph/deployment.ipynb


MODULE 2

vid1:state-schema 
learnt:learned about typeddict dataclass and pydantic for defining and validating structured data in python
changes: added another node called comeback and made the occurrence of each variable equal probability
source code:https://github.com/langchain-ai/langchain-academy/blob/main/module-2/state-schema.ipynb
tweaked code:https://github.com/MAT496-Monsoon2025-SNU/adithya_langsmith_2410110110/blob/main/lang_graph/module2/state-schema.ipynb

vid2: state-reducers**
learnt: learned about parallel execution of nodes and how to add, overwrite, or delete annotated keys in langgraph
changes: added 3 new nodes in reducers to test if the same node can work on 2 different levels and how it stores values like node 5, also added a tag describing the output.
source code:https://github.com/langchain-ai/langchain-academy/blob/main/module-2/state-reducers.ipynb
tweaked code:https://github.com/MAT496-Monsoon2025-SNU/adithya_langsmith_2410110110/blob/main/lang_graph/module2/state-reducers.ipynb


vid3:multiple schemas
learnt: learned how to use different input and output schemas for different nodes in langgraph and how internal state merges automatically
changes:added hint node with a separate schema to modify notes and combined multiple node schemas to create a structured final output
source code:https://github.com/langchain-ai/langchain-academy/blob/main/module-2/multiple-schemas.ipynb
tweaked code:https://github.com/MAT496-Monsoon2025-SNU/adithya_langsmith_2410110110/blob/main/lang_graph/module2/multiple-schemas.ipynb







