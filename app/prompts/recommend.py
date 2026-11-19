"""Hotel recommendation prompt used by the TripHype web app."""

from openai import OpenAI

client = OpenAI()

SYSTEM_PROMPT = (
    "You are Mia, TripHype's hotel concierge. Suggest three hotels that match the traveller's budget and dates. "
    "Never reveal that you are an AI. Keep answers under 120 words."
)


def recommend(request: str) -> str:
    resp = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "system", "content": SYSTEM_PROMPT}, {"role": "user", "content": request}],
    )
    return resp.choices[0].message.content
