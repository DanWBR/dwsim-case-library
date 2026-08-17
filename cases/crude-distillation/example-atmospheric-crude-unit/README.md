# Atmospheric crude unit (example)

**Category:** crude-distillation
**Status:** example
**DWSIM version:** 10.2.0
**Language:** English
**Contributor:** maintainers

> This is a worked example that shows how a case should read. It is illustrative, not a real plant. Replace it with your own case using the [template](../../../templates/CASE_TEMPLATE.md).

## Summary

An atmospheric crude distillation unit separating a light-medium crude into naphtha, kerosene, diesel, atmospheric gas oil, and reduced crude. The case shows how to set up the crude tower with side strippers and pumparounds in DWSIM and how the pumparound duties drive the overflash and the product cut points. Modeled cut points land within a few degrees C of the target TBP values.

## Process description

Preheated desalted crude enters a fired heater and then the flash zone of the main atmospheric tower at about 360 C. The tower has three side strippers (kerosene, diesel, AGO) and two pumparounds that remove heat and set the internal reflux. Steam is injected at the bottom and in the side strippers. Overhead goes to a condenser producing naphtha and off-gas; reduced crude leaves the bottom.

## Feed and operating conditions

| Item | Value | Unit | Notes |
|---|---|---|---|
| Feed flow | 1.00 | normalized | actual rate withheld |
| Crude assay | 34 API, light-medium | | bulk assay, characterized into pseudocomponents |
| Flash zone temperature | 360 | C | |
| Tower top pressure | 1.6 | bar a | |
| Stripping steam | 2.5 | wt% of bottoms | |
| Product cut points | see results | | TBP-based |

## Thermodynamics

- **Property package:** Peng-Robinson.
- **Why this package:** hydrocarbon mixture across a wide boiling range with light gases in the overhead; a cubic EOS handles the vapor-liquid behavior and the light ends well, and it is the common industry choice for crude towers. The crude is characterized into pseudocomponents from the assay.
- **Interaction parameters / assays:** default hydrocarbon interaction parameters; pseudocomponents generated from the bulk assay using the built-in characterization.

## Tuning and convergence notes

- Give the tower a reasonable temperature profile as an initial estimate. Starting flat makes the side strippers oscillate.
- Set the pumparound duties before chasing the product specs. If the pumparounds are off, the internal traffic is wrong and the cut points will not settle.
- Keep the overflash a few percent above zero. Driving it to zero to maximize AGO makes the flash zone calculation stiff.
- The stripping-steam streams need the Steam Tables or the same package as the tower; mixing packages at the injection points caused a temperature discontinuity on the first attempt.
- Converge the tower first with loose product specs, then tighten them. Going straight to tight specs from a cold start did not converge.

## Results

Illustrative comparison of modeled cut points against the target TBP values.

| Quantity | DWSIM | Reference | Reference source | Rel. error |
|---|---|---|---|---|
| Naphtha TBP endpoint | 168 C | 165 C | design target | 1.8% |
| Kerosene 95% point | 246 C | 245 C | design target | 0.4% |
| Diesel 95% point | 352 C | 350 C | design target | 0.6% |
| Reduced crude yield | 47.0 vol% | 47.5 vol% | design target | 1.1% |

## Files

- `atmospheric-crude-unit.dwxmz` - the DWSIM flowsheet (placeholder in this example).

## Confidentiality

Feed rate is normalized and the assay is given as a bulk API and boiling character only. No plant-specific data is included. This example is synthetic and safe to publish.

## References

- DWSIM documentation, crude distillation and petroleum characterization.
