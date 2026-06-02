from crewai import Agent

fact_checker = Agent(
    role="Fact Checker",
    goal="""
    Verificar la calidad y credibilidad de la información
    obtenida durante la investigación.
    """,
    backstory="""
    Especialista en verificación de datos,
    detección de exageraciones y validación
    de afirmaciones empresariales.
    """,
    llm="ollama/llama3.1",
    verbose=True
)