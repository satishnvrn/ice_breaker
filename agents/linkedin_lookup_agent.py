from langchain_openai import ChatOpenAI
from langchain.prompts import PromptTemplate
from langchain.tools import Tool
from langchain import hub
from langchain.agents import create_react_agent, AgentExecutor

from tools.tools import get_profile_url_tavily


def lookup(name) -> str:
    llm = ChatOpenAI(
        temperature=0,
        model="gpt-3.5-turbo",
    )

    template = """"
      given the full name {name_of_person} I want you to get me a link to 
      their LinkedIn profile page. Your answer should contain only the link.
    """
    prompt_template = PromptTemplate(
        input_variables=["name_of_person"], template=template
    )

    tools_for_agent = [
        Tool(
            name="Crawl Google 4 linkedin profile page",
            func=get_profile_url_tavily,  # placeholder function
            description="useful for when you need to get the Linkedin Page URL",
        )
    ]

    react_prompt = hub.pull("hwchase17/react")
    agent = create_react_agent(llm=llm, tools=tools_for_agent, prompt=react_prompt)
    agent_executor = AgentExecutor(agent=agent, tools=tools_for_agent, verbose=True)

    result = agent_executor.invoke(
        input={"input": prompt_template.format_prompt(name_of_person=name)}
    )
    linkedin_profile_url = result["output"]

    return linkedin_profile_url


if __name__ == "__main__":
    linkedin_profile_url = lookup(name="satishnvrn")
    print(linkedin_profile_url)
