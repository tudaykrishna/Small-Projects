import os
from langchain_google_vertexai import VertexAI
from langchain_core.prompts import PromptTemplate
from langchain.chains import LLMChain ,SequentialChain




googleapi_key = ""
os.environ["GOOGLE_API_KEY"] = googleapi_key



model = VertexAI(model="gemini-pro",temperature=0.01)

def generate(cuisine):
    
    # Chain_1
    prompt_name = PromptTemplate(
        input_variables=['cuisine'],
        template = "i want to open a restaurant for {cuisine} food. Suggest one fancy name for this ,Do not give any extra text. "
    )

    name_chain=LLMChain(llm=model,prompt=prompt_name,output_key="restaurant_name")


    # Chain_2
    prompt_items = PromptTemplate(
        input_variables=['restaurant_name'],
        template = "Suggest some menu items for {restaurant_name} .Return the output as a comma separated list. "
    )

    items_chain=LLMChain(llm=model,prompt=prompt_items,output_key="menu_items")


    chain= SequentialChain(
        chains=[name_chain,items_chain],
        input_variables=['cuisine'],
        output_variables=['restaurant_name','menu_items']
    )   


    response = chain({'cuisine':cuisine})

    return response

if __name__ == "__main__":
    print(generate("Italiane"))