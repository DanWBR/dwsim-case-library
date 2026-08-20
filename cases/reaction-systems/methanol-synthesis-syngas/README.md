# Methanol synthesis from syngas

**Category:** reaction-systems
**Status:** community
**DWSIM version:** 10.2.0
**Language:** English
**Contributor:** Daniel Wagner Oliveira de Medeiros (@DanWBR)

## Summary

A single-pass methanol synthesis train with product purification: syngas (CO/CO2/H2) is compressed to 50 bar, reacted to equilibrium in a Gibbs reactor at 523 K (69 % CO conversion), condensed and flashed, degassed, and distilled to a 99.8 mol% methanol distillate with a water-rich bottoms.

## Process description

55 mol/s of syngas (10 CO / 5 CO2 / 40 H2) is compressed adiabatically from 10 to 50 bar, heated to 523 K and fed to an isothermal Gibbs reactor minimizing free energy over CO/CO2/H2/MeOH/H2O — this captures both methanol synthesis reactions and the water-gas shift at once. The effluent is cooled to 313 K and flashed: the unconverted gas leaves overhead (a real plant recycles it) and the crude methanol is let down to 1 atm. A warm degasser (330 K + drum) vents the CO2 and H2 that stayed dissolved at 50 bar, and a 20-stage column with reflux ratio 2 splits the crude into methanol distillate and water bottoms.

![PFD](methanol-synthesis-syngas.png)

## Feed and operating conditions

| Item | Value | Unit | Notes |
|---|---|---|---|
| Syngas | 55 | mol/s | CO 10 / CO2 5 / H2 40, 300 K / 10 bar |
| Reactor | 523 K, 50 bar | | isothermal Gibbs |
| Flash separator | 313 K, 50 bar | | |
| Degasser | 330 K, 1 atm | | vents dissolved CO2/H2 |
| Column | 20 stages, RR = 2, 1 atm | | feed on stage 10 |

## Thermodynamics

- **Property package:** Peng-Robinson
- **Why this package:** high-pressure syngas dominates the flowsheet; PR handles the reactor and flash sections well. The MeOH/water column at 1 atm is a mildly non-ideal pair PR represents acceptably for this purpose; swap NRTL in if column accuracy matters more than train consistency.

## Tuning and convergence notes

- The Gibbs reactor's element matrix must be created **after** connecting the feed (`ComponentIDs` + `CreateElementMatrix()`), and both product ports must be connected.
- The column would not converge fed directly with the let-down crude: the CO2/H2 dissolved at 50 bar are non-condensables that a total condenser cannot pass. Warming the crude to 330 K and flashing before the column removes them and the column then converges without touching solver settings.
- The bottoms flow specification is sized from the water that actually reaches the column (bottoms ≈ feed water / 0.75) rather than guessed: a flow spec converges where a reboiler temperature spec hunted.

## Results

| Quantity | DWSIM | Notes |
|---|---|---|
| CO conversion | 69.2 % | equilibrium at 523 K / 50 bar |
| Carbon atom balance (reactor) | 15.000 in / 15.000 out | mol/s, < 0.01 % |
| Methanol distillate purity | 99.8 mol% | |
| Bottoms water | 75.0 mol% | remainder mostly methanol |
| Syngas compressor | 349.8 kW | |

## Files

- `methanol-synthesis-syngas.dwxmz` — the DWSIM flowsheet.
- `methanol-synthesis-syngas.png` — PFD screenshot.

This case is generated and verified by an automated test in the DWSIM repository (`tests/DWSIM.FluentAPI.Tests/Samples/MethanolSynthesisSample.cs`): built through the fluent API, solved, checked for the results above, saved, then reloaded and re-solved from the saved file.

## Confidentiality

All conditions are literature-typical values; no plant data was used.

## References

- Moulijn, Makkee, van Diepen, *Chemical Process Technology* — methanol synthesis.
