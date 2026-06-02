from crewai import Task

def create_report_task(agent):

    return Task(
        description="""
        Genera un informe ejecutivo profesional en Markdown.
        
        Mantén todas las puntuaciones estratégicas
        generadas por el analista.

        Incluye una sección específica:

        ## Strategic Scores

        antes del análisis principal.

        El informe debe contener:

        # Resumen Ejecutivo

        # Hallazgos Clave

        # Análisis Estratégico

        # Conclusiones

        # Fuentes

        Incluye todas las URLs utilizadas durante la investigación.

        Las URLs deben aparecer en una sección final llamada:

        ## Fuentes
        """,
        expected_output="Informe Markdown",
        agent=agent
    )