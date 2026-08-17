<!--
  Copy this file to cases/<category>/<case-name>/README.md and fill it in.
  Delete these comments as you go. Keep the section headers.
  Before submitting, run through the confidentiality checklist in CONTRIBUTING.md.
-->

# <Case title>

**Category:** <crude-distillation | refining-conversion | hydrotreating | gas-processing | carbon-capture | separation-processes | reaction-systems | bioprocesses | electrolytes-and-aqueous | clean-energy | fluid-flow-and-piping | heat-integration-utilities | other>
**Status:** community <!-- a maintainer changes this to "verified" after reproduction -->
**DWSIM version:** <e.g. 10.2.0>
**Contributor:** <name or handle, optional>

## Summary

One short paragraph: what the process is, what the case demonstrates, and the headline result.

## Process description

What the unit does, the feed, the main equipment, and the operating objective. A simple block diagram or a screenshot of the flowsheet helps a lot here.

## Feed and operating conditions

| Item | Value | Unit | Notes |
|---|---|---|---|
| Feed flow | | | normalized if the real value is confidential |
| Feed composition / assay | | | |
| Key temperature(s) | | | |
| Key pressure(s) | | | |
| Product specification(s) | | | |

## Thermodynamics

- **Property package:** <e.g. Peng-Robinson, NRTL, Steam Tables, CoolProp>
- **Why this package:** the reasoning (component types, pressure range, polar/electrolyte behavior, availability of parameters).
- **Interaction parameters / assays:** any regressed or custom data used.

## Tuning and convergence notes

The most valuable section. Be specific and honest.

- Initial estimates that mattered.
- Solver and column settings you changed from the defaults.
- What did not converge at first and how you fixed it.
- Anything a new user should watch out for.

## Results

Key results, and if you are allowed to publish it, a comparison against plant data or another simulator. Use relative errors when absolute values are confidential.

| Quantity | DWSIM | Reference | Reference source | Rel. error |
|---|---|---|---|---|
| | | | plant / Aspen / HYSYS / literature | |

## Files

- `` `<case-name>.dwxmz` `` - the DWSIM flowsheet (optional but encouraged).
- Figures referenced above.

## Confidentiality

State what was anonymized or normalized, and confirm you have the right to publish this case and any comparison it contains.

## References

Papers, standards, or datasets used.
