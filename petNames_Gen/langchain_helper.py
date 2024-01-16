from dotenv import load_dotenv
from langchain_openai import OpenAI
from langchain.prompts import PromptTemplate
from langchain.agents import AgentType
from langchain.agents import initialize_agent
from langchain.agents import load_tools
from langchain.chains import LLMChain


load_dotenv()


def generate_petNames(petType, petColor, user_api_key):
    llm = OpenAI(temperature= 0.7, api_key=user_api_key)

    prompt_temp_name = PromptTemplate(
        input_variables= ["petType", 'petColor'],
        template= "I have a {petType} pet whose color is {petColor}. Suggest me 5 cool names for my pet."
    )
    
    chain = LLMChain(llm= llm, prompt=prompt_temp_name, verbose=True, output_key='pet_name')
    response = chain.invoke({'petType': petType, 'petColor': petColor})
    return response['pet_name']

def langchain_agent():
    llm = OpenAI(temperature= 0.7)
    llm_tools = load_tools(['wikipedia', 'llm-math'], llm=llm)
    initAgent = initialize_agent(tools=llm_tools, llm=llm, verbose=True, agent= AgentType.ZERO_SHOT_REACT_DESCRIPTION)
    result = initAgent.invoke({'What is the average age of a dog? Multiply the age with 3.'})
    return result

if __name__ == "__main__":
    print(generate_petNames('Cat','White'))
    # print(langchain_agent())