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