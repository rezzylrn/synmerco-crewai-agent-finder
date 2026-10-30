#!/usr/bin/env python3
"""Size up Synmerco agents with synmerco-crewai's free tools.

Searches Synmerco for agents with a given capability and estimates the
fees on a 100 USD job. Runs with no Synmerco API key and no AI model key.

Usage:
    python size_up_agents.py <capability>

Example:
    python size_up_agents.py research
"""

import json
import sys

from synmerco_crewai import get_synmerco_tools

MAX_AGENTS = 3
JOB_AMOUNT_CENTS = 10000  # 100 USD, in cents


def parse_result(result):
    """The tools return a JSON string (or a dict); normalise to a dict."""
    if isinstance(result, str):
        return json.loads(result)
    return result


def main(argv):
    if len(argv) != 2:
        print("Usage: python size_up_agents.py <capability>", file=sys.stderr)
        print("Example: python size_up_agents.py research", file=sys.stderr)
        return 2
    capability = argv[1]

    tools = {t.name: t for t in get_synmerco_tools(include_free_only=True)}
    search_agents = tools["search_agents"]
    estimate_fees = tools["estimate_fees"]

    search = parse_result(search_agents.run(capability=capability))
    agents = search.get("agents", [])[:MAX_AGENTS]
    print(f"Capability: {capability}")
    print(f"Total agents found: {search.get('totalResults')}")
    print(f"Showing up to {MAX_AGENTS} agents (by DID only):")
    for agent in agents:
        print(f"- agentDid: {agent.get('agentDid')}")
        print(f"  synmercoScore: {agent.get('synmercoScore')}")
        print(f"  tier: {agent.get('tier')}")
        print(f"  capabilities: {', '.join(agent.get('capabilities', []))}")

    fees = parse_result(estimate_fees.run(amount=JOB_AMOUNT_CENTS))
    print()
    print(f"Fee estimate for a {JOB_AMOUNT_CENTS} cent (100 USD) job:")
    print(json.dumps(fees, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
