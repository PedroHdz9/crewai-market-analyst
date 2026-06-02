from crewai import Agent
from app.tools.search_tool import search_tool

writer = Agent(
    role="Executive Report Writer",
    goal="Redactar informes",
    backstory="Redactor corporativo",
    llm="ollama/llama3.1",
    verbose=True
)