from crewai import Task

def create_fact_check_task(agent):

    return Task(
        description="""
        Revisa la investigación realizada.

        Tu misión:

        - Detectar afirmaciones sin evidencia.
        - Detectar exageraciones.
        - Detectar lenguaje promocional.
        - Detectar conclusiones especulativas.
        - Evaluar la credibilidad de las fuentes.

        IMPORTANTE:

        No inventes información nueva.

        Solo valida, corrige o marca la información recibida.

        Conserva toda la información válida.

        Corrige o marca cualquier afirmación dudosa.
        """,

        expected_output="""
        Devuelve el resultado usando exactamente esta estructura:

        ## Evaluación de Credibilidad

        Nivel de confianza:
        Alto / Medio / Bajo

        ## Información Validada

        - Hallazgo 1
        - Hallazgo 2

        ## Posibles Riesgos de Interpretación

        - Riesgo 1
        - Riesgo 2

        ## Fuentes Más Fiables

        - URL 1
        - URL 2

        ## Recomendaciones para el Analista

        - Recomendación 1
        - Recomendación 2
        """,

        agent=agent
    )