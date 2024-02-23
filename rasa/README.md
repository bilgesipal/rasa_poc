

# Initilize a blank  RASA Greeting BOT 

<br/>

```bash
# Install dependencies 
pip install -r requiremetns.tx
cd rasa

## initialize rasa
rasa init

# Answer the questions
Welcome to Rasa! 🤖

To get started quickly, an initial project will be created.
If you need some help, check out the documentation at https://rasa.com/docs/rasa.
Now let's start! 👇🏽

? Please enter a path where the project will be created [default: current directory]
? Directory '/Users/bilgesipal/PycharmProjects/pythonProject8' is not empty. Continue? Yes
Created project directory at '/Users/bilgesipal/PycharmProjects/pythonProject8'.
Finished creating project structure.
? ? Do you want to train an initial model? 💪🏽 Yes

```
<br/><br/>


The new model will be trained and you whether you want to start chatting. 
You can start immediately to chat with the model

```bash
2024-02-23 11:03:44 INFO     root  - Rasa server is up and running.
Bot loaded. Type a message and press enter (use '/stop' to exit): 
Your input ->                                                                                                                                                 
Great, carry on!
Your input ->  hello                                                                                                                                          
Hey! How are you?
Your input ->  great                                                                                                                                          
Great, carry on!
Your input ->  are you a bot                                                                                                                                  
I am a bot, powered by Rasa.
Your input ->          

```
<br/><br/>

This system only works if you do not have an action server. 
If you want to use RAS with ChatGPT you need to write an action 
code for it and re-arrange the yml files accordingly.

Natural Language Understanding yaml Files

![NLU](https://github.com/bilgesipal/rasa_poc/blob/master/rasa/github/nlu.png)


RULES yaml Files

![RULES](https://github.com/bilgesipal/rasa_poc/blob/master/rasa/github/rule.png)


Endpoints  yaml Files

![ENDPOINTS](https://github.com/bilgesipal/rasa_poc/blob/master/rasa/github/endpoints.png)

Credentials

![CREDENTIALS](https://github.com/bilgesipal/rasa_poc/blob/master/rasa/github/credentials.png)


<br/><br/>


Activate the NLU service and the action service seperately. 
Once you've trained an initial model, execute the following command: 

rasa run --enable-api --cors '*'  This will start a new RASA server at localhost. 
--enable-api and --cors '*' are required to let users make requests from outside the RASA ecosystem. --cors '*' gives access to everyone,
however it can be changed in the future to control who can access the server. 



```bash

# First start the action service. This will enable the actions to be run as a we api
rasa run actions   


# Then start the NLU service. This time we do not want to use the shell. 
 rasa run  -m models --enable-api --cors "*"

```
<br/><br/>

B.Ş. Sert