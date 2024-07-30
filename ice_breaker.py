import os
from langchain.prompts.prompt import PromptTemplate

# from langchain_openai import ChatOpenAI
from langchain_ollama import ChatOllama
from langchain_core.output_parsers import StrOutputParser

from third_parties.linkedin import scrape_linkedin_profile


if __name__ == "__main__":
    print("Hello LangChain!")

    summary_template = """
        given the information {information} about a person 
        from I want you to create:
        1. a short summary of the person
        2. two interesting facts about the person
    """

    summary_prompt_template = PromptTemplate(
        input_variables=["information"], template=summary_template
    )

    # llm = ChatOpenAI(
    #     temperature=0,
    #     model="gpt-3.5-turbo",
    # )
    llm = ChatOllama(
        temperature=0,
        model="mistral",
    )

    chain = summary_prompt_template | llm | StrOutputParser()

    linkedin_data = scrape_linkedin_profile(
        linkedin_profile_url=os.environ["LINKEDIN_PROFILE_URL"]
    )

    res = chain.invoke(input={"information": linkedin_data})

    print(res)
