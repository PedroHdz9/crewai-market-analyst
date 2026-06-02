from crewai import Agent
from app.tools.search_tool import search_tool

critic = Agent(
    role="Business Analyst",
    goal="Analizar información",
    backstory="Consultor estratégico",
    llm="ollama/llama3.1",
    verbose=True
)