# Operator Pack Desk

Sell surface for Operator Pages. This repo does not reimplement QuantumGuard.

**Product truth**

- QuantumGuard v1 is a classical Ed25519 offline verifier. Verdicts are only PASS, FAIL, or INDETERMINATE. CLI and HTTP share one function. PQC is reserved, not shipped.
- This desk is not that verifier. `desk.py` builds a design-partner packet (SHA-256 manifest + cover). Sealing still happens in the public QuantumGuard CLI.
- This QuantumGuard is not OpenMatter, not the Senate Quantum-GUARD Act (S.5313), not H.R.9129, and not @QuantumGuard17.

**List price (from MARKETING.md)**

- Operator Pack, single site: $490 one-time or $1,490/year
- Design-partner packet: free, one per prospect, used to close the pack
- Contact: danpennic@gmail.com

## Run

```bash
python3 desk.py packet --buyer "Acme OT" --site "Plant 1" --out ./out
python3 -m http.server 8080
# open http://127.0.0.1:8080/storefront/
```

Stripe is not live in this repo. Set `STRIPE_PAYMENT_LINK` in `storefront/config.js` after you create a Payment Link for the $490 SKU. Do not invent a live checkout URL.

## What a buyer gets

1. Collaborator invite to the private Operator Pack repo, or a signed tarball plus LICENSE.json.
2. Air-gap runbook and the frozen CONTRACT-v1 pointer: https://github.com/danpennic-sys/quantumguard
3. Optional design-partner packet generated here, then sealed with QuantumGuard outside this desk.

## Do not sell from this desk

LedgerLite, snoop-blocker, PQC, freshness, a second verifier, or photonic hardware.
