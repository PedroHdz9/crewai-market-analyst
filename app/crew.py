from crewai import Crew

from app.agents.scout import scout
from app.agents.critic import critic
from app.agents.writer import writer
from app.agents.fact_checker import fact_checker

from app.tasks.research_task import create_research_task
from app.tasks.analysis_task import create_analysis_task
from app.tasks.report_task import create_report_task
from app.tasks.fact_check_task import create_fact_check_task


def run_crew(topic):

    research = create_research_task(
        scout,
        topic
    )

    fact_check = create_fact_check_task(
        fact_checker
    )

    analysis = create_analysis_task(
        critic
    )

    report = create_report_task(
        writer
    )

    crew = Crew(
        agents=[
            scout,
            fact_checker,
            critic,
            writer
        ],
        tasks=[
            research,
            fact_check,
            analysis,
            report
        ],
        verbose=True
    )

    result = crew.kickoff()

    return result