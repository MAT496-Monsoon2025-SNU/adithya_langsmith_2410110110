ADITHYA CHIGULLAPALLY
module1:

vid1: tracing basics 
1.i learnt that tracing is the practice of keeping logs of activities or operations performed by a program.
2.purpose:it stores the information ,operation and we can review it at any point of the time
changes:asked "what is meta data?explain with example" adn "define the term trace?explain in simple terms".
source code:https://github.com/MAT496-Monsoon2025-SNU/adithya_langsmith_2410110110/blob/main/module_1/module_1/tracing_basics.ipynb
tweaked code:https://github.com/MAT496-Monsoon2025-SNU/adithya_langsmith_2410110110/blob/main/module_1tweaked/tracing_basics.ipynb

vid2:types of runs
1.There are different types of code execution runs, such as streaming and normal (basic) calls,tool calling.
2.purpose: Different run types can be used for different operations depending on the context and requirement.
chhnages:askede"to name a new born baby"and tool calling made to perfrm xor operation.
sourcecode:
tweaked code:

vid3:alterantive ways to trace
1.There are alternative ways of tracing in LangSmith:Using @traceable decorator (default method),Wrapping a run tree Using trace() functionLearned when and how to apply each method effectively.
2. Purpose:To understand what type of trace is suitable for different scenarios.
chnages:asked "what does tracing with wraping explain?" and "what is run tree"
source code:
tweaked code:

vid4:threads
1. What I learned:Threads are a way to group multiple traces together.Useful when sending two (or more) related prompts so that the LLM understands the context between them.
2. Purpose:To maintain connected conversation context across multiple related operations.
chnages:"How can I add tags to a Trace?" and "How do I add metadata to a Trace?"
source code:
tweaked code:
