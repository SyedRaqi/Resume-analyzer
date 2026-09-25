from openai import OpenAI

from ..database import settings

FALLBACKS = {
    "resume": "Start with a role-specific summary, then show evidence: projects, measurable outcomes, and the tools you used. Keep bullets concise and use action verbs.",
    "interview": "Prepare three stories using Situation, Task, Action, Result. Rehearse your introduction, core projects, and a few thoughtful questions for the interviewer.",
    "python": "Build a path through Python fundamentals, data structures, testing, SQL, one web or data framework, and two portfolio projects that solve real problems.",
    "sql": "SQL lets you query structured data. Learn SELECT and filtering first, then joins, grouping, subqueries, indexes, and transactions by practicing on a small database.",
}


def fallback_reply(message: str) -> str:
    lower = message.lower()
    for keyword, reply in FALLBACKS.items():
        if keyword in lower:
            return reply
    return "A useful next step is to turn your goal into a small weekly plan. Tell me the role you are targeting, your current skills, and where you feel stuck, and I can make the plan more specific."


def answer(message: str, history: list[dict[str, str]]) -> str:
    if not settings.openai_api_key:
        return fallback_reply(message)
    client = OpenAI(api_key=settings.openai_api_key)
    response = client.chat.completions.create(model=settings.openai_model, temperature=0.4, messages=[{"role": "system", "content": "You are SmartHire Assistant, a clear and honest career mentor for students. Give practical steps, explain technical concepts simply, and never invent user qualifications or guarantee jobs."}, *history[-10:], {"role": "user", "content": message}])
    return response.choices[0].message.content or fallback_reply(message)
