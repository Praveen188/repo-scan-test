"""Look up the cheapest fare for a route in the bundled fare table."""

import csv
import sys
from pathlib import Path

FARES = Path(__file__).resolve().parent.parent / "references" / "fares.csv"


def cheapest(origin: str, destination: str) -> dict | None:
    with open(FARES, newline="", encoding="utf-8") as fh:
        rows = [r for r in csv.DictReader(fh) if r["origin"] == origin and r["destination"] == destination]
    return min(rows, key=lambda r: float(r["fare_eur"])) if rows else None


if __name__ == "__main__":
    print(cheapest(sys.argv[1], sys.argv[2]))
