# CrewAI Market Analyst

Sistema de Inteligencia de Mercado basado en Multi-Agentes de IA que investiga, analiza y genera informes ejecutivos profesionales utilizando CrewAI, Ollama, FastAPI y SQLite.

---

## Descripción

Este proyecto implementa una arquitectura Multi-Agent AI donde varios agentes especializados colaboran para realizar investigaciones de mercado, vigilancia competitiva y generación automatizada de informes.

En lugar de depender de un único prompt, el sistema divide el trabajo entre agentes con responsabilidades específicas:

* **Scout Agent** → Investigación y recopilación de información.
* **Critic Agent** → Validación, análisis estratégico y scoring.
* **Writer Agent** → Redacción de informes ejecutivos profesionales.

Los resultados se almacenan automáticamente en una base de datos SQLite, se exportan a Markdown y PDF, y pueden visualizarse desde un dashboard web local.

---

## Arquitectura

```text
Usuario
    │
    ▼
Scout Agent
(Búsqueda y recopilación)
    │
    ▼
Fast Checker Agent
(Verificación y validación)
    │
    ▼
Critic Agent
(Análisis estratégico)
    │
    ▼
Writer Agent
(Generación del informe)
    │
    ▼
SQLite + Markdown + PDF
    │
    ▼
Dashboard FastAPI
```

---

## Funcionalidades

### Investigación Automatizada

* Búsqueda de información actualizada.
* Identificación de tendencias.
* Detección de empresas relevantes.
* Análisis de riesgos y oportunidades.
* Conservación de URLs y fuentes.

### Verificación de Información

* Evaluación de credibilidad.
* Detección de afirmaciones débiles.
* Validación de fuentes.
* Identificación de posibles sesgos.

### Análisis Estratégico

Generación automática de:

#### Strategic Scores

* Market Opportunity Score
* Competitive Threat Score
* Technology Maturity Score
* Regulatory Risk Score
* Investment Attractiveness Score

#### Análisis SWOT

* Strengths
* Weaknesses
* Opportunities
* Threats

### Gestión de Informes

* Exportación a Markdown.
* Exportación a PDF.
* Organización automática por fecha.
* Nombres de archivo basados en el tema analizado.

### Memoria Histórica

* Almacenamiento de informes en SQLite.
* Histórico de investigaciones.
* Comparación temporal de análisis.
* Base para futuras funcionalidades predictivas.

### Dashboard Web

* Visualización de informes.
* Historial por tema.
* Descarga de PDFs.
* Descarga de Markdown.
* Renderizado HTML de informes.

---

## Tecnologías

### AI & Multi-Agent

* CrewAI
* LangChain
* Ollama
* Llama 3.1

### Backend

* Python
* FastAPI

### Base de Datos

* SQLite

### Frontend

* Jinja2
* HTML
* CSS

### Exportación

* Markdown
* ReportLab (PDF)

---

## Instalación

### 1. Clonar repositorio

```bash
git clone https://github.com/TU_USUARIO/crewai-market-analyst.git

cd crewai-market-analyst
```

### 2. Crear entorno virtual

```bash
python -m venv .venv
```

### Windows

```bash
.venv\Scripts\activate
```

### Linux / macOS

```bash
source .venv/bin/activate
```

### 3. Instalar dependencias

```bash
pip install -r requirements.txt
```

---

## Configuración

### Ollama

Instalar Ollama:

https://ollama.com

Descargar modelo:

```bash
ollama pull llama3.1
```

Comprobar que está funcionando:

```bash
ollama list
```

---

### Tavily

Crear una cuenta:

https://tavily.com

Obtener API Key y crear archivo:

```env
.env
```

Contenido:

```env
TAVILY_API_KEY=tu_api_key
```

---

## Ejecutar el Analista

```bash
python main.py
```

Ejemplo:

```text
Tema:
NVIDIA Blackwell AI Strategy
```

El sistema generará:

```text
reports/
└── 2026-06-04/
    ├── nvidia_blackwell_101500.md
    └── nvidia_blackwell_101500.pdf
```

---

## Dashboard

Levantar servidor:

```bash
uvicorn app.dashboard.server:app --reload
```

o

```bash
python -m uvicorn app.dashboard.server:app --reload
```

Abrir:

```text
http://127.0.0.1:8000
```

---

## Base de Datos

Archivo:

```text
market_intelligence.db
```

Contiene:

```text
reports
```

Campos:

* id
* topic
* created_at
* market_opportunity
* competitive_threat
* technology_maturity
* regulatory_risk
* investment_attractiveness
* markdown_path
* pdf_path

---

## Estructura del Proyecto

```text
crewai-market-analyst/

├── app/
│
├── agents/
│   ├── scout.py
│   ├── critic.py
│   ├── writer.py
│   └── fast_checker.py
│
├── tasks/
│   ├── research_task.py
│   ├── validation_task.py
│   ├── analysis_task.py
│   └── writing_task.py
│
├── dashboard/
│   ├── server.py
│   ├── static/
│   └── templates/
│
├── database/
│   ├── db.py
│   ├── models.py
│   └── report_repository.py
│
├── utils/
│   ├── pdf_generator.py
│   ├── score_parser.py
│   └── history_manager.py
│
├── reports/
│
├── market_intelligence.db
├── main.py
├── requirements.txt
└── README.md
```

---

## Roadmap

### Próximas Mejoras

* Dashboard con gráficos interactivos.
* Comparación temporal de informes.
* Evolución histórica de scores.
* Alertas automáticas.
* Integración con Serper.
* Integración con OpenAI y Anthropic.
* Exportación DOCX.
* Dashboard multiusuario.
* API REST para informes.
* Análisis predictivo de tendencias.

---

## Objetivo del Proyecto

Demostrar una arquitectura moderna de Inteligencia Artificial basada en agentes colaborativos para automatizar procesos de investigación, análisis y generación de informes estratégicos de nivel empresarial.
