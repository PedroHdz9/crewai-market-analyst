from crewai import Task

def create_analysis_task(agent):

    return Task(
        description="""
        Analiza la investigación validada recibida.

        Realiza:

        1. Análisis FODA.
        2. Evaluación estratégica.
        3. Identificación de riesgos.
        4. Identificación de oportunidades.

        Además, asigna puntuaciones del 1 al 10 para:

        - Market Opportunity Score
        - Competitive Threat Score
        - Technology Maturity Score
        - Regulatory Risk Score
        - Investment Attractiveness Score

        IMPORTANTE:

        Si la investigación contiene información histórica:

        - Identifica cambios respecto a informes anteriores.
        - Detecta tendencias emergentes.
        - Evalúa si los riesgos aumentan o disminuyen.
        - Evalúa si las oportunidades aumentan o disminuyen.
        - Analiza la evolución competitiva del mercado.

        No inventes datos.

        Si no existe contexto histórico suficiente,
        indica que no se puede realizar comparación temporal.

        Justifica brevemente cada puntuación.

        Utiliza únicamente la información disponible.
        No inventes datos.
        """,


        expected_output="""
        Devuelve el análisis usando esta estructura:

        ## Strategic Scores

        Market Opportunity Score: X/10
        Justificación: ...

        Competitive Threat Score: X/10
        Justificación: ...

        Technology Maturity Score: X/10
        Justificación: ...

        Regulatory Risk Score: X/10
        Justificación: ...

        Investment Attractiveness Score: X/10
        Justificación: ...

        # Historical Evolution

        Cambios detectados:

        - Cambio 1
        - Cambio 2

        Nuevos riesgos:

        - Riesgo 1
        - Riesgo 2

        Nuevas oportunidades:

        - Oportunidad 1
        - Oportunidad 2

        Nuevos competidores detectados:

        - Competidor 1
        - Competidor 2

        ## SWOT Analysis

        ### Strengths

        ...

        ### Weaknesses

        ...

        ### Opportunities

        ...

        ### Threats

        ...
        """,
        agent=agent
    )