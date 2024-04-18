from crewai import Agent, Task, Crew, Process
import os
from langchain_google_genai import GoogleGenerativeAI

os.environ["GOOGLE_API_KEY"] = your_api_key

go_llm = GoogleGenerativeAI(model="gemini-pro")

researcher = Agent(
    role="Researcher",
    goal="Research new AI insights",
    backstory="You are an AI research assistant",
    verbose=True,
    allow_delegation=False,
    llm=go_llm
)

writer = Agent(
    role="Writer",
    goal="Write an engaging blog post about AI trends and insights",
    backstory="You are an AI blog post writer who specializes in writing about AI topics",
    verbose=False,
    allow_delegation=False,
    llm=go_llm
)

task1 = Task(
    description="Investigate the latest AI trend",
    agent=researcher,
    expected_output="Findings and insights from the investigation"
)

task2 = Task(
    description="Write a blog post about the latest AI trend",
    agent=writer,
    expected_output="Engaging blog post about the latest AI trend"
)

crew = Crew(
    agents=[researcher, writer],
    tasks=[task1, task2],
    verbose=False,
    process=Process.sequential
)

result = crew.kickoff()

print ("kanna result: ", result)