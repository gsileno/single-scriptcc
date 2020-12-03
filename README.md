# singleCC 

A single-threaded version of AgentScriptCC agents in python.

The AgentScriptCC DSL is a language inspired by the BDI agent programming language AgentSpeak(L), further extended in Jason, and also used in more recent platforms as LightJason, ASTRA and pyson. 

The CC stands for cross-compiler: given an agent script, the output is a python program to control an agent in performing deliberations and then actions, depending on percepts, in an environment.

A single-threaded version can be used for:
- integrate intentional agents in a discrete-event simulator
- having individual intentional agents running as web services or independent processes.

The agent (mind) needs to interact with a body (part of the environment) to perform actions.  
  
**Example of usage**
```
$ scriptcc examples/robot/robot.ascript
```
At the moment, the script returns a Python program defining the behavioural component of the agent (see `examples/robot/robot_agent_script.py`).

To see how a running agent script will look like, looks at `examples/robot/robot_manual_script.py` 

**Requirements**

antlr4 for the parser.
if you use anaconda, do, e.g. ```conda install -c conda-forge antlr-python-runtime```
 
 
### Agent execution cycle

An agent program runs the deliberation of a "mind".
It is associated to a *belief base*, and maintain an *intentional stack*.
Because we are constrained to a single thread, the program deals only with one intentional stack.
However, in order to maintain reactivity to external events, we consider kernel and user modes of execution (cf. operating systems).

At each execution step:
- kernel mode: 
    - check whether rules with priority highest than the current thread are applicable,
    - if yes, reset the intentional stack and append a new thread in it;
- user mode:
    - if there is a thread and it is unlocked
        - run the thread, performing the internal deliberation up to deciding an action, and lock the thread before initiating the action with the body,   
        - if the thread ends with no further action, restarts kernel mode.

   
    


 



