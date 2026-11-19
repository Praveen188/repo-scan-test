"""Add taxes to fare lines. Pure computation: no network, no file writes."""

import json
import sys

import yaml  # noqa: F401  (tax table loader in a later version)

TAX = {"FR": 0.10, "DE": 0.07, "GB": 0.0}


def total(lines: list[dict]) -> dict:
    subtotal = sum(float(l["fare_eur"]) for l in lines)
    taxes = sum(float(l["fare_eur"]) * TAX.get(l["country"], 0.0) for l in lines)
    return {"subtotal_eur": round(subtotal, 2), "taxes_eur": round(taxes, 2), "total_eur": round(subtotal + taxes, 2)}


if __name__ == "__main__":
    print(json.dumps(total(json.load(sys.stdin))))
