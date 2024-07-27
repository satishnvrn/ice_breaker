from langchain.prompts.prompt import PromptTemplate
from langchain_openai import ChatOpenAI

information = """"
As a Lead Engineer at Carrier, I design and develop scalable and responsive web and mobile applications using React, React Native, Svelte, Node, and Serverless technologies. I also leverage my AWS Solutions Architect certification to build secure and efficient cloud infrastructure and deployment pipelines using AWS services such as SAM, S3, Cloudfront, and Cloudformation.

With over 10 years of experience in full-stack development, I have helped various startups and established companies create and release applications from scratch in production. I have also contributed to multiple open-source projects. I am passionate about learning new technologies and frameworks and sharing my knowledge and skills with others.
"""

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

    llm = ChatOpenAI(
        temperature=0,
        model="gpt-3.5-turbo",
    )

    chain = summary_prompt_template | llm

    res = chain.invoke(input={"information": information})

    print(res)
