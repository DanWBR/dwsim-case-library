# Raw sugar mill: extraction, five-effect evaporator, three-boiling pan house, dryer and bagasse boiler

**Category:** other
**Status:** community
**DWSIM version:** 10.2.17 or later
**DWSIM edition:** Patreon Edition (Sugar Solutions property package)
**Language:** English
**Contributor:** Daniel Wagner Oliveira de Medeiros (@DanWBR)

> **Requirement.** The Sugar Solutions (S-UNIFAC) property package belongs to DWSIM Patreon. The file opens anywhere, but it only solves where the package is licensed.

## Summary

A raw sugar mill crushing 100 t/h of cane, from the diffuser to the dried sugar and the bagasse boiler. The juice is extracted, heated, clarified and concentrated to a syrup at Bx 65 in a five-effect evaporator; a three-boiling pan house (A, B and C massecuites, with the B and C sugars returned as seed) crystallizes the sucrose, and the A sugar is dried with hot air. All the bagasse burns in the boiler, which raises 21 bar steam for a back-pressure turbine. The mill makes 12.2 t/h of raw sugar at 99.1 % sucrose, recovers 89.6 % of the sucrose in the cane, and the turbine delivers 5.3 MW. The whole flowsheet, with its two recycles, solves in about 40 s.

## Process description

**Extraction:** the diffuser D-100 (a component separator) extracts 96.5 % of the dissolved solids of the cane with 30 t/h of imbibition water at 70 °C. The bagasse leaves with all the fibre, 10 % of the mud solids and 50 % moisture.

**Juice heating and clarification:** the mixed juice is pumped to 3.5 bar (P-101), heated to 103 °C (E-101) and flashed to 1 atm (V-101, V-102), as in the heaters and flash tank of a mill. The clarifier C-101 settles the mud solids with 10 % of the juice; the mud filter F-101 returns 85 % of that juice, and the filter cake leaves the process.

**Evaporation:** five effects at 1.70, 1.25, 0.85, 0.50 and 0.16 bar, forward feed, heated by exhaust steam at 2.2 bar. In each effect the heating vapour condenses to saturated liquid in CD-n, and its latent heat goes through an energy stream to EV-n, where the juice enters at the pressure of the effect and boils. The separator VS-n splits the vapour, which heats the next effect, from the concentrated juice. The vapour of the last effect goes to the condenser.

**Pan house:** three vacuum pans at 0.16 bar, each a mixer, a heater at the boiling temperature and a separator for the pan vapour:
- the A pan (62 °C) boils the syrup with the B sugar as seed; the A sugar is the product;
- the B pan (68 °C) boils the A molasses with the C sugar as seed; the B sugar returns to the A pan (REC-B);
- the C pan (75 °C) boils the B molasses; the C massecuite is cooled to 45 °C in CR-C, and the C sugar returns to the B pan (REC-C); the C molasses is the final molasses.

The centrifugals CF-A, CF-B and CF-C (solids separators) keep 5, 7 and 10 % of the mother liquor on the sugar. The pan house stays at the pan pressure throughout, which does not change the liquid and the crystals; PM-A takes the A sugar to 1 atm.

**Drying:** 15 t/h of air at 30 °C and 55 % relative humidity is heated to 90 °C (E-AIR) and mixed with the A sugar; DRYER-SEP splits the exhaust air from the raw sugar.

**Boiler and turbine:** the bagasse burns with 30 % excess air in FURNACE, an adiabatic conversion reactor: the fibre (C6H8.94O4.32) and the sugars left in the bagasse burn to CO2 and water, and the ash, the organic non-sugars and the mud solids leave unburnt. The flue gas raises steam at 21 bar and 320 °C in BOILER and leaves at about 180 °C; the back-pressure turbine TURBINE expands the steam to 2.2 bar with an adiabatic efficiency of 65 %.

![The flowsheet, as DWSIM draws it](raw-sugar-mill.png)

## Feed and operating conditions

| Item | Value | Unit | Notes |
|---|---|---|---|
| Cane | 100 | t/h | 30 °C |
| Cane composition | fibre 13, sucrose 13.5, glucose 0.35, fructose 0.35, ash 0.5, organic non-sugars 0.8, mud 0.5, water 71 | % | purity of the juice 87.1 |
| Imbibition water | 30 | t/h | 70 °C, 30 % on cane |
| Juice heater | 103 | °C | at 3 bar, then flashed to 1 atm |
| Evaporator effects | 1.70 / 1.25 / 0.85 / 0.50 / 0.16 | bar | forward feed |
| Exhaust steam to the evaporator | 16.08 | t/h | 2.2 bar; gives the syrup at Bx 65 |
| Pans A / B / C | 62 / 68 / 75 | °C | at 0.16 bar |
| C massecuite cooling | 45 | °C | |
| Centrifugals A / B / C | 95 / 93 / 90 | % | mother liquor separated from the sugar |
| Dryer air | 15 | t/h | dry basis, heated to 90 °C |
| Combustion air | 30 | % excess | on the fibre and the sugars of the bagasse |
| Boiler feed water | 63.09 | t/h | 105 °C, 21 bar; gives a stack at 180 °C |
| Live steam | 21 bar, 320 °C | | |
| Turbine | 2.2 bar outlet, 65 % | | adiabatic efficiency |

## Thermodynamics

- **Property package:** Sugar Solutions (S-UNIFAC), DWSIM Patreon, for the cane, the juices, the massecuites and the gases; Steam Tables (IAPWS-IF97) for the boiler feed water, the live steam and the turbine.
- **Why this package:** sucrose, glucose and fructose solutions are far from ideal, and the boiling point elevation, the solubility of sucrose and the crystallization in the pans all come from the activity coefficients. The package uses S-UNIFAC (Spiliotis and Tassios, 2000) with terms fitted to the solubility of sucrose, to the boiling point elevation of cane syrups and to the saturation coefficient of impure solutions. Sucrose crystallizes as a solid; glucose and fructose stay dissolved.
- **Pseudo-compounds:** sugarcane fibre, cane ash, cane organic non-sugars and cane mud solids come with DWSIM. Fibre and mud are always solid; ash and organic non-sugars are dissolved solids.
- **Gases:** nitrogen, oxygen and carbon dioxide take an activity coefficient of 1 and sit in the vapour.

## Tuning and convergence notes

- **Start both recycles near the answer.** The B and C sugar returns carry crystals and a molasses film. Starting them at 4.2 and 0.9 t/h with the composition of a converged run, REC-B converges in 2 iterations and REC-C in 1.
- **Recycle tolerance:** the default mass flow tolerance of a new recycle (0.01 % of the flow) is below the noise of the solid-liquid flashes in the sugar returns (about 2e-4 kg/s). At that tolerance REC-B cycles until it runs out of iterations; the case uses 0.1 % and Wegstein acceleration.
- **C pan temperature:** at 80 °C the C pan sits near the saturation of the B molasses, and the two recycles alternate between two states without converging. At 75 °C they converge in two iterations.
- **Evaporator effects:** in a forward-feed train the vapour and the juice leave each effect at the same temperature. A heat exchanger that picks its hot side by comparing inlet temperatures can swap the sides on that tie. A cooler and a heater joined by an energy stream avoid the comparison and each needs a single flash.
- **Fixed steam flows:** the exhaust steam (16.08 t/h) and the boiler feed water (63.09 t/h) were set with Adjusts on the syrup Brix and the stack temperature, and then fixed: each Adjust iteration re-solves the pan house and its recycles.
- **Steam circuit:** the feed water, the live steam and the turbine use the steam tables, so the turbine works with the IAPWS-IF97 entropy.
- **Solve time:** about 40 s for the whole flowsheet, and about 15 s when re-solved from the saved file.

## Results

| Quantity | DWSIM | Notes |
|---|---|---|
| Recycles | converged | REC-B 2 iterations, REC-C 1 |
| Mixed juice | 102.8 t/h, Bx 14.6 | |
| Clear juice | 100.3 t/h, Bx 14.7, 100.2 °C | after the flash tank |
| Syrup | 22.7 t/h, Bx 65.0, 58.4 °C | |
| Evaporation | 77.7 t/h | 4.8 kg of water per kg of exhaust steam |
| Calandria duties, effects 1 to 5 | 9.86 / 8.18 / 9.05 / 9.89 / 10.69 | MW |
| A massecuite | 22.3 t/h, dry substance 89.6 %, 53 % crystals | |
| A molasses | purity 74.8 | |
| B massecuite | dry substance 93.6 %, 53 % crystals | |
| B molasses | purity 43.1 | |
| C massecuite | dry substance 90.7 % at 75 °C | 5 % crystals before cooling |
| Final molasses | 2.86 t/h, Bx 88.7, purity 29.0 | |
| B / C sugar returned | 5.25 / 1.01 t/h | |
| Raw sugar | 12.21 t/h, 99.1 % sucrose, 0.056 % moisture | |
| Sucrose recovery | 89.6 % | of the sucrose in the cane |
| Juice heater / pans A, B, C / dryer air | 6.90 / 3.66, 1.05, 0.14 / 0.26 | MW |
| Flame / stack | 1158 / 180 | °C |
| Live steam | 63.1 t/h | 2.3 t per t of bagasse |
| Turbine power | 5.30 | MW |
| Mass balance | closes to 3e-4 t/h | on 259.8 t/h in |

**Steam balance:** the turbine exhaust (63.1 t/h at 2.2 bar) is more than the process needs. If the evaporator (16.1 t/h) and the juice heater, the pans and the dryer (12.0 MW, about 19 t/h of exhaust steam) all took exhaust steam, the demand would be about 35 t/h, 35 % on cane. The case burns all the bagasse and doesn't take any loss in the boiler other than the stack, so the surplus is the bagasse a mill could sell or burn for condensing power.

**Equilibrium pan house:** pans, cooler and centrifugals are equilibrium stages. The mother liquor leaves each pan saturated, while in a real pan it leaves supersaturated, so the molasses purities here are the lower bound of what a pan house reaches.

## Files

- `raw-sugar-mill.dwxmz`: the DWSIM flowsheet.
- `raw-sugar-mill.png`: the flowsheet.
- The flowsheet is built by `RawSugarMillTest.cs` in the DWSIM FluentAPI tests, which also checks the mass balance and the syrup Brix.

## Confidentiality

The cane composition and the operating conditions are typical values for a raw sugar mill, chosen for this case. No plant data were used.

## References

- E. Hugot, *Handbook of Cane Sugar Engineering*, 3rd ed., Elsevier, 1986.
- P. Rein, *Cane Sugar Engineering*, Bartens, 2007.
- N. Spiliotis, D. Tassios, "A UNIFAC model for phase equilibrium calculations in aqueous and nonaqueous sugar solutions", *Fluid Phase Equilibria* 173 (2000) 39-55.
