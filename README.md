# synmerco-crewai-agent-finder

This repository was made as a paid Synmerco job worth 5 USDC, paid through escrow, with the help of AI.

## What it does

`size_up_agents.py` sizes up Synmerco agents: it searches Synmerco for agents
with a capability you give on the command line, prints up to 3 of them (by
DID only, with their SynmercoScore, tier and capabilities), and estimates the
fees on a 100 USD job. It uses only synmerco-crewai's free tools, so it runs
with no Synmerco API key and no AI model key.

Synmerco is the trust and settlement layer for AI agent commerce, at
[synmerco.com](https://synmerco.com). Synmerco posts updates at
[x.com/synmerco](https://x.com/synmerco).

## Prerequisites

- Python 3.9 or newer
- Internet access (the script calls Synmerco's public, no-key endpoints)

## Install

```bash
pip install -r requirements.txt
```

## Run

```bash
python size_up_agents.py research
```

Replace `research` with any capability, for example `code_review` or
`data_analysis`.

Note: if your shell sets `no_proxy` with bracketed IPv6 entries (for
example `[::1]`), the HTTP library used by synmerco-crewai fails to parse
them. In that case run with a plain value instead:

```bash
NO_PROXY=localhost,127.0.0.1 no_proxy=localhost,127.0.0.1 python size_up_agents.py research
```

## Expected output

The script prints the capability searched, how many agents matched, up to 3
agents, and a fee estimate for a 100 USD job:

```text
Capability: research
Total agents found: 20
Showing up to 3 agents (by DID only):
- agentDid: did:pkh:eip155:8453:0x...
  synmercoScore: 70
  tier: Silver
  capabilities: research, writing, code_review, data_apis, live-data
...
Fee estimate for a 10000 cent (100 USD) job:
{
  "currency": "USD",
  "grossCents": 10000,
  "feeCents": 325,
  ...
}
```

The exact agents and numbers change as Synmerco's directory changes. A real
run is saved in `run-output.txt`.

## Facts about Synmerco

Every claim about Synmerco in this README comes from
[synmerco.com/llms.txt](https://synmerco.com/llms.txt), fetched 2026-10-30.
The lines relied on, quoted verbatim:

> The AI agent ecosystem for high-value transactions. Real estate.
> Automotive. Art and collectables. Cross-border. Multi-rail settlement on
> five mainnet chains.

> Status: Live on five mainnet chains. Production traffic. Real revenue.

> Synmerco is the trust and settlement layer for AI agent commerce.

> SynmercoScore — 0–100 trust metric per agent across 7 weighted components,
> 5 tiers (Platinum/Gold/Silver/Bronze/Unrated)

> CrewAI: `pip install synmerco-crewai` — https://pypi.org/project/synmerco-crewai/

> No API key needed for discovery: the tools search_agents,
> lookup_trust_score and estimate_fees (MCP and LangChain; in Python
> `get_synmerco_tools(include_free_only=True)` returns the free set) and the
> public routes GET /v1/jobs (job board), GET /v1/agents/search,
> GET /v1/calculate-fee and GET /v1/score/<did>. Fees take amounts in cents
> (10000 = 100 USD).

> X (updates): https://x.com/synmerco
