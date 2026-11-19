"""Create a booking with the TripHype booking API."""

import json
import sys

import requests
from openai import OpenAI

API_KEY = "sk_live_51HxTripHypeBookingKey0001"
BOOKING_URL = "https://api.booking.example/v2/bookings"

client = OpenAI()


def summarise(itinerary: dict) -> str:
    resp = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": json.dumps(itinerary)}],
    )
    return resp.choices[0].message.content


def book(request: dict) -> dict:
    payload = {
        "traveller": request["traveller_name"],
        "email": request["email"],
        "passport": request["passport_number"],
        "outbound": request["outbound_date"],
        "destination": request["destination"],
    }
    r = requests.post(BOOKING_URL, json=payload, headers={"Authorization": f"Bearer {API_KEY}"}, timeout=20)
    r.raise_for_status()
    return r.json()


if __name__ == "__main__":
    print(json.dumps(book(json.load(sys.stdin))))
