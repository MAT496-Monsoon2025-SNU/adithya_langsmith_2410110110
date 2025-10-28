# ADITHYA CHIGULLAPALLY 2410110110  
## LANG GRANPH  

---

### vid1:motivation
**learnt:** i learnt what is lang graph, basically it is used for control flow of the llm model to process. lang graph helps it run smoothly and makes sure everything is working safely.  
**code:** no source code.  

---

### vid2:simple graph
**learnt:** i learnt how to build the graph through coding and what basic components are needed for it.  
**changes:** i added a new node 4 with a state similar to the other nodes, and it decides which path to take. earlier it started from node 1, but now it can choose between node 1 and node 4, where node 4 directly leads to the end.  
**source code:** https://github.com/langchain-ai/langchain-academy/blob/main/module-1/simple-graph.ipynb  
**teaked code:** http://github.com/MAT496-Monsoon2025-SNU/adithya_langsmith_2410110110/blob/main/lang_graph/simple-graph.ipynb  

---

### vid3:langgraphh studio
**learnt:** after running my studio, it directly opened in my browser in langsmith and showed me the graph of vid2. for input, i wrote "hi this is adithya".  
**code:** no code to modify.  

<img width="1604" height="727" alt="image" src="https://github.com/user-attachments/assets/3978c2dd-2b4d-4633-8a4e-916673c1a12a" />

---

### vid4:chain
**learnt:** i learnt how to build a simple chain in langgraph that uses chat messages, chat models, binds tools to the llm, and executes tool calls in the graph.  
**changes:** eplaced the default tool-calling cell with a custom web_search tool that uses serper and tavily apis to search the web, and tested it by searching “ajitkumar shiv nadar university  
**source code:** https://github.com/langchain-ai/langchain-academy/blob/main/module-1/chain.ipynb  
**tweaked code:** https://github.com/MAT496-Monsoon2025-SNU/adithya_langsmith_2410110110/blob/main/lang_graph/chain.ipynb  

---

### vid5:router
**learnt:** i learnt how a chat model decides its route based on our input.  
**changes:** added a new tool called xor, which contains multiply, and added a new route about shopping that tells us the prices of our desired product and cretaed cell for each path so we can compare the ouput.  
**source code:** https://github.com/langchain-ai/langchain-academy/blob/main/module-1/router.ipynb  
**tweaked code:** https://github.com/MAT496-Monsoon2025-SNU/adithya_langsmith_2410110110/blob/main/lang_graph/router.ipynb  

**IMAGE IN LANGSMIT(ran through studio)H**  
<img width="1153" height="664" alt="image" src="https://github.com/user-attachments/assets/b93fc0eb-698d-469f-a74e-c0130821780d" />

---

### vid6:agent
**learnt:** i learnt how the output is affected when we feed the output of the tool to it again, and how it can be used in other calling.  
**changes:** added a new node "temp" which calculates the temperature from celsius to fahrenheit. this node calls the tool, and again the tool calls itself to calculate the temperature and create 2 cells to compare the output.  
**source code:** https://github.com/langchain-ai/langchain-academy/blob/main/module-1/agent.ipynb  
**tweaked code:** https://github.com/MAT496-Monsoon2025-SNU/adithya_langsmith_2410110110/blob/main/lang_graph/agent.ipynb  

**IMAGE IN LANGSMITH(ran through studio)**  
<img width="1228" height="907" alt="image" src="https://github.com/user-attachments/assets/61a09557-31ee-40f2-abfb-2031724951d1" />

---

### vid7: agent-memory
**learnt:** i learned that an agent normally does not remember the functions it executes. to make it remember, we add a checkpoint and use memory, so it can recall the function and run it. this makes it easier because we don’t have to repeat the task every time we need a change.  
**changes:** added a new tool called xor, then added new cells at the end where it calls the tools and updates the output, which is stored in memory, and performed a new arithmetic operation on a number to test whether it would get confused with the old value or operate only on the most recent one. the test was successful.(i thought it ould get confused quiet impressive)  
**source code:** https://github.com/langchain-ai/langchain-academy/blob/main/module-1/agent-memory.ipynb  
**tweaked code:** https://github.com/MAT496-Monsoon2025-SNU/adithya_langsmith_2410110110/blob/main/lang_graph/agent-memory.ipynb  

---

### vid8:deployment
**learnt:** i learned how to get output of the our input message dirrecty from grpah present at our local host.  
**changes:** i could not deploy d=because deployment can be done when we are a part of paid plan but i tried it.  
**source code:** https://github.com/langchain-ai/langchain-academy/blob/main/module-1/deployment.ipynb  
**tweaked code:** https://github.com/MAT496-Monsoon2025-SNU/adithya_langsmith_2410110110/blob/main/lang_graph/deployment.ipynb  

---

## MODULE 2  

---

### vid1:state-schema 
**learnt:** learned about typeddict dataclass and pydantic for defining and validating structured data in python  
**changes:** added another node called comeback and made the occurrence of each variable equal probability  
**source code:** https://github.com/langchain-ai/langchain-academy/blob/main/module-2/state-schema.ipynb  
**tweaked code:** https://github.com/MAT496-Monsoon2025-SNU/adithya_langsmith_2410110110/blob/main/lang_graph/module2/state-schema.ipynb  

---

### vid2: state-reducers**
**learnt:** learned about parallel execution of nodes and how to add, overwrite, or delete annotated keys in langgraph  
**changes:** added 3 new nodes in reducers to test if the same node can work on 2 different levels and how it stores values like node 5, also added a tag describing the output.  
**source code:** https://github.com/langchain-ai/langchain-academy/blob/main/module-2/state-reducers.ipynb  
**tweaked code:** https://github.com/MAT496-Monsoon2025-SNU/adithya_langsmith_2410110110/blob/main/lang_graph/module2/state-reducers.ipynb  

---

### vid3:multiple schemas
**learnt:** learned how to use different input and output schemas for different nodes in langgraph and how internal state merges automatically  
**changes:** added hint node with a separate schema to modify notes and combined multiple node schemas to create a structured final output  
**source code:** https://github.com/langchain-ai/langchain-academy/blob/main/module-2/multiple-schemas.ipynb  
**tweaked code:** https://github.com/MAT496-Monsoon2025-SNU/adithya_langsmith_2410110110/blob/main/lang_graph/module2/multiple-schemas.ipynb  

---

### vid4:trim-filtering-messages
**learnt:** learned how to make multiple messages pass through the model, add new messages, filter them, and reduce user input so that it becomes token-efficient.  
**changes:** added another node called chat_model1 to run two chat models in parallel, created a new cell to test filtering by removing the filtering node to observe if only the latest messages are processed, and added a new message with id 5 to check if the model executes only messages with ids 4 and 5.  
**source code:** https://github.com/langchain-ai/langchain-academy/blob/main/module-2/trim-filter-messages.ipynb  
**teaked code:** https://github.com/MAT496-Monsoon2025-SNU/adithya_langsmith_2410110110/blob/main/lang_graph/module2/trim-filter-messages.ipynb  

---

### vid5:chat summarization
**Learned:** Learned how trimming and filtering messages can help generate a summary of our conversation, allowing us to continue later and pick up exactly where we left off.  
**Changes:** Modified the State schema by changing summary from str to int, and implemented arithmetic conversation logic instead of normal chat.(I observed that when I removed the previous input (which was a normal conversation), the AI correctly added the arithmetic messages. However, the summary still remembered the old default conversation from the source code. Even after removing the old messages and adding new ones, the summary retained the old conversation while also including the new arithmetic inputs)  
**source code:** https://github.com/langchain-ai/langchain-academy/blob/main/module-2/chatbot-summarization.ipynb  
**tweaked code:** https://github.com/MAT496-Monsoon2025-SNU/adithya_langsmith_2410110110/blob/main/lang_graph/module2/chatbot-summarization.ipynb 

---

### vid6:chat-external-memo
**Learned:** Learned how database-backed memory helps retain summaries and conversation context across sessions for better summarization. Without it, all conversation history is lost once the session ends.  
**Changes:** replaced filtering with trimming to test efficiency and see the difference from filtering, and updated threshold logic to use token counts for summarization.  
**source code:** https://github.com/langchain-ai/langchain-academy/blob/main/module-2/chatbot-external-memory.ipynb  
**tweaked code:** https://github.com/MAT496-Monsoon2025-SNU/adithya_langsmith_2410110110/blob/main/lang_graph/module2/chatbot-external-memory.ipynb  

---

## MODULE 3  

---

### vid1:streaming
**learned:** i learned what streaming is how it works and the different methods like streaming updates and values i also learned how to stream input from a graph in langsmith  

**changes:** i added a new input for both updates and values to see how the output changes i also added a cell after the first execution of values it kept its previous output and then gave a new output which i did not expect i thought it would combine the three inputs but it did not.pic of that particular cell(i felt interesting)  

<img width="1307" height="809" alt="image" src="https://github.com/user-attachments/assets/e226a085-b4f4-40bc-b509-2fd26d471d85" />

in streaming from a graph i changed the graph by adding a node called temperature which calculates temperature or simply works as a calculator  
**tweakedcode:** https://github.com/MAT496-Monsoon2025-SNU/adithya_langsmith_2410110110/blob/main/lang_graph/module3/vid1/streaming-interruption.ipynb  
**source code:** https://github.com/langchain-ai/langchain-academy/blob/main/module-3/streaming-interruption.ipynb  
**new graph created by me in studio**  

<img width="1515" height="1004" alt="image" src="https://github.com/user-attachments/assets/a59d0f22-bb39-43ab-9159-11a6a51481ea" />

---

### video 2: breaking point
**learnt:** i learnt how a breaking point works and how we can use it. i also learnt how to add a new tool, how to add the breaking point to it, and how to use the breaking point from the studio manually using the code.  
**changes made:** i added new logical tools which show true or false. i shifted the breaking point to these new tools named logical tools. i added a new cell in the middle to show that the arithmetic tools run but the logical ones do not run until we manually make them run. i also added a cell at the end and in the studio part i ran the temperature one and asked the question to the llm, one directly to the assistant tool and one to the temperature tool.he follwing pic of the studio is below  

<img width="1507" height="978" alt="image" src="https://github.com/user-attachments/assets/b349500c-6a40-46ec-bf6a-c6c370d45273" />

**source code:** https://github.com/langchain-ai/langchain-academy/blob/main/module-3/breakpoints.ipynb  
**tweaked code:** https://github.com/MAT496-Monsoon2025-SNU/adithya_langsmith_2410110110/blob/main/lang_graph/module3/vid2/breakpoints.ipynb  

---

### vid3: edit-state-human-feedback
**learnt:** i learnt that interrupt_before basically lets us rewrite or change the input before a node runs, so we can control the flow and modify what the agent will see. i also learnt how to give human feedback after a breakpoint, and how the checkpointer is used to save and restore graph state.  
**changes:** i added an interrupt_before in front of the tools node to observe what happens. i created a graph that includes interrupt_after for tools and executed it to compare behavior. i also added a new cell that runs the modified graph and explained what the cell does. i included the graph adn the cell image so it is to revie it ;).out of curiosity, in the studio, i created the temperature graph and added an interrupt_before to the assistant node and interrupt_after to both the tools and temperature nodes. i also added interrupt_before to the tools and temperature nodes to check all possible combinations and observe their behavior.  

<img width="340" height="350" alt="image" src="https://github.com/user-attachments/assets/d515aa3e-fe2b-4fe1-a924-c33e4beed305" />

heres the pic of studio graph i added interrupts ith output.  
<img width="1479" height="978" alt="image" src="https://github.com/user-attachments/assets/5c9edc3a-4724-424d-bef0-142e59fe3445" />

**source code:** https://github.com/langchain-ai/langchain-academy/blob/main/module-3/edit-state-human-feedback.ipynb  
**tweaked code:** https://github.com/MAT496-Monsoon2025-SNU/adithya_langsmith_2410110110/blob/main/lang_graph/module3/edit-state-human-feedback.ipynb  

---

### **vid4: dynamic breaking point**
**learnt:** i learnt that this breaking point is not like interrupt before or interrupt after. it works more like a limit when something crosses that limit it stops the process. this is useful for saving tokens and controlling execution in our code. also to use this in the studio we need to update the studio code itself while interrupt before or after can be directly changed in langsith.  
**changes:** i added one more interruption in node 1 to check if the input is greater than 7. i also changed the length check in node 2 to 4. then i added a new cell because if we are interrupting twice we need to change our input twice when it crosses both thresholds 4 and 7. i even applied the same change to the studio code of the breaking point and deployed it in langsith to check if it is working.  

**source code:** https://github.com/langchain-ai/langchain-academy/blob/main/module-3/dynamic-breakpoints.ipynb  
**teaked code:** https://github.com/MAT496-Monsoon2025-SNU/adithya_langsmith_2410110110/blob/main/lang_graph/module3/dynamic-breakpoints.ipynb  

<img width="1511" height="789" alt="image" src="https://github.com/user-attachments/assets/ee4d3f76-a880-46a9-88f5-75d9de7e1ffb" />

---

### vid5:time travel
**learnt:**  
i learnt how to debug by forking through code. before i was doing it in studio, but now i learned to do it through hardcoding. i also learnt how to replay and how to check all the states in the graph.  

**changes:**  
i updated the graph and made my own graph where we calculate the temperature. then i made a new thread so it doesn’t get mixed up. then i updated the cell where we can see all the states. for example, there were 5 states present initially giving us output, showing what each state is doing. after forking, there were 13 states, and i made it print all 13 states. in studio, i passed the updated graph with me and did the same thing, passing the updated graph from studio.  

**source code:** https://github.com/langchain-ai/langchain-academy/blob/main/module-3/time-travel.ipynb  
**teaked code:** https://github.com/MAT496-Monsoon2025-SNU/adithya_langsmith_2410110110/blob/main/lang_graph/module3/time-travel.ipynb  

**studio graph**  
he was using the same graph through out the module so i used my graph  
<img width="844" height="644" alt="image" src="https://github.com/user-attachments/assets/1be0fe79-d61a-4369-b750-45a3badb9560" />

---
## MODULE 4
### **vid1 : parallelization:**
**learnt**:i learnt that hat is parallelization and how it works and how does it gets tarnsversal if there are nodes that are pointing to other nodes or have sub nodes.
**changes**i created two cyclic graphs one where only a single node output was executed and another where the outputs of multiple nodes were stored i wanted to observe how long the execution would continue and whether it would run endlessly i also modified a node to point to another node to see which node path would reach the end for each change i added a new cell in the studio i asked for the price of an object and tested whether it could remember my previous input since no memory component was included it did not remember my code and here is the picture of the studio with my inputs.
**studio graph**
<img width="1414" height="1037" alt="image" src="https://github.com/user-attachments/assets/ffebfda1-6780-40e3-9506-fcedec6513ba" />
**source code:** https://github.com/langchain-ai/langchain-academy/blob/main/module-4/parallelization.ipynb
**teaked code:** https://github.com/MAT496-Monsoon2025-SNU/adithya_langsmith_2410110110/blob/main/lang_graph/module4/parallelization.ipynb
