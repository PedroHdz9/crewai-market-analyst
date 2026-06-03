from crewai import Task

def create_research_task(
    agent,
    topic,
    historical_context=""
):

    return Task(
    description=f"""
    Investiga el siguiente tema:

    {topic}

    CONTEXTO HISTÓRICO DISPONIBLE:

    {historical_context}

    Si existe contexto histórico:

    - Utilízalo únicamente como referencia.
    - Identifica cambios respecto a informes anteriores.
    - Detecta nuevas tendencias o acontecimientos.
    - Señala si algún riesgo u oportunidad ha aumentado o disminuido.
    - No copies literalmente los informes anteriores.
    - Prioriza siempre la información más reciente encontrada mediante búsqueda.

    Debes utilizar la herramienta Tavily para obtener información actualizada.

    Objetivos de la investigación:

    - Encontrar noticias recientes.
    - Identificar tendencias del mercado.
    - Detectar empresas relevantes.
    - Analizar riesgos y oportunidades.
    - Identificar tecnologías emergentes.

    IMPORTANTE:

    - Utiliza varias búsquedas cortas.
    - Nunca superes los 100 caracteres por consulta.
    - No combines múltiples preguntas en una sola búsqueda.
    - Realiza búsquedas específicas y concretas.
    - Si necesitas más información, realiza otra búsqueda independiente.
    - Conserva todas las URLs encontradas.
    - No elimines ninguna fuente.
    - Asocia cada hallazgo con su URL correspondiente.

    Devuelve la información en este formato:

    Hallazgo:
    ...

    Fuente:
    https://...

    Ejemplos válidos:

    ✓ baterías estado sólido fabricantes
    ✓ Toyota solid state battery
    ✓ solid state battery market forecast

    Ejemplos no válidos:

    ✗ Un único texto largo que contenga varias preguntas o instrucciones.

    Entrega un resumen estructurado de los hallazgos.
    """,
    expected_output="""
    Informe con:

    - Hallazgos clave
    - Tendencias detectadas
    - Empresas relevantes
    - Riesgos
    - Oportunidades
    - Fuentes consultadas
    """,
    agent=agent
)