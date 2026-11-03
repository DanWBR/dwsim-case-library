# Seawater desalination by multi-effect distillation: the 14-effect PSA pilot plant

**Category:** electrolytes-and-aqueous
**Status:** community
**DWSIM version:** 10.2.13
**Language:** English
**Contributor:** Prof. Nicolas Spogis, Ph.D. (@Spogis), AI4Tech · nicolas.spogis@ai4tech.ai · www.ai4tech.ai

## Summary

- **What it is:** seawater desalination by forward-feed multi-effect distillation (MED), the 14-effect pilot plant of the Plataforma Solar de Almería (CIEMAT), at an operating point the plant measured on 31 October 2023. Hot water, 161.9 kW, boils effect 1; each effect's vapour boils the next, one effect cooler and at a lower pressure; 13 preheaters warm the feed; an end condenser, cooled by seawater, takes the last vapour. It is the library's first desalination case, on DWSIM's Seawater IAPWS-08 package as 10.2.13 fixed it.
- **Headline:** DWSIM makes 2 891 kg/h of distillate, a performance ratio of 11.53, where the plant made 2 527 kg/h at 10.12 ± 0.55: 14 % more. The plant's own measured streams carry out only 80 % of the hot water's heat - the rest leaves through the shells and the vacuum system - and the model, which loses nothing, carries out all of it. Where those losses do not enter, the model meets the plant:
  - the brine leaves the last effect at 33.39 °C, against 33.21 °C measured;
  - the duties DWSIM computes give an evaporator coefficient of 2.31 kW/(m² K) on the plant's areas, against El-Dessouky & Ettouney's 2.37.
- **What DWSIM needed** - each measured on 10.2.13:
  - **DWSIM 10.2.13.** Up to 10.2.12 the Seawater package could not evaporate seawater (DanWBR/dwsim10#122).
  - **A Recycle on every effect's vapour line.** With no loop at all, DWSIM refused the flowsheet at its fifth effect with "Infinite loop detected": it orders a flowsheet by walking back along every path and stops at 10,000, and each effect doubles the paths.
  - **The tears given by pressure and enthalpy.** A Recycle copies what it reads into its tear and keeps the tear's specification; by vapour fraction, the package refuses pure vapour at 1.
  - **Each preheater as its two sides**, a heater and a cooler joined by a Spec block: as one exchanger, each closes a loop with its neighbours.
  - **The condenser held at its set point by the flow, set from its duty.** An Adjust does it too, but DWSIM solves the whole flowsheet at each of its steps, over 10 minutes.

## Process description

A forward-feed multi-effect distillation (MED) plant, as the Plataforma Solar de Almería (PSA, CIEMAT) built its pilot: 14 effects in a vertical stack, a preheater beside each of effects 1 to 13, and an end condenser. The drawing is a serpentine of two rows:
- effects 1 to 7 run left to right, as the brine and the vapour go;
- effects 8 to 14 come back right to left, under them;
- the feed climbs the preheaters along the bottom of the second row, up the right edge and along the top of the first.

The lines are coloured by phase: blue liquid, orange vapour, purple two-phase.

**The heat.** Hot water, 12.00 L/s from the PSA's solar field and storage, enters effect 1's tubes at 72.01 °C and leaves at 68.72 °C (E-0). Effect 1 is the only effect the plant heats from outside.

**The effects, EF-1 to EF-14.** Each is a vessel at the pressure measured in it, 250.8 mbar in the first to 49.9 mbar in the last. The brine boils there at the temperature IAPWS-08 gives it at that pressure and salinity. Its vapour goes on to the next effect, and the brine left is let down into the next effect by a valve (VB-2 to VB-14), where part of it flashes.

**The tubes, C-2 to C-14.** Each effect's vapour condenses inside the next effect's tubes. In DWSIM that is a cooler that takes the vapour to its saturated liquid at the pressure it was raised at; its duty, an energy stream, is the heat that boils the brine outside the tubes. The temperature the vapour condenses at sits below the brine it left by that brine's boiling point elevation, and above the brine it boils by the temperature difference the tubes need.

**The distillate.** Each effect's condensate is let down into the next effect's tubes (VD-3 to VD-14), where it flashes and joins that effect's vapour (MV-2 to MV-14), as the plant's distillate cascades from tube bundle to tube bundle. The end condenser collects it all.

**The preheaters, PH-1 to PH-13.** The feed, 8.00 m³/h, climbs from the end condenser through the preheaters, PH-13 first, each heated by part of its effect's vapour, and enters effect 1 at 62.14 °C. Each preheater is drawn as its two sides: a heater on the feed (PH-nc, to the temperature measured after it) and a cooler on the vapour (PH-nh), the duty handed from one to the other by a Spec block (S-1 to S-13).

**The end condenser, CC.** The last vapour and all the distillate condense at 47.0 mbar against seawater at 20.22 °C (E-C). The plant holds the seawater's outlet at a set point, 28 °C, by the flow it sends through; here it leaves at the 27.96 °C measured and the flow is what that takes. 8.00 m³/h of it is the feed (SP); the rest is rejected. Held at its set point, the feed's state does not depend on the rest of the plant, so the preheater train starts from it ("Feed to preheaters") and the condenser's water, "Feed (calc)", is brought to the same state - the build checks the two agree to 1e-3 K.

The plant's double-effect absorption heat pump, its vacuum system (two seawater hydro-ejectors) and its closed seawater loop (pools and a cooling tower) are outside the case.

## Feed and operating conditions

The operating point is a measured one: "72_28_12_8-20231031", a steady state of 440 s on 31 October 2023, from the PSA's 2022-2024 campaign data (J. M. Serrano, CIEMAT-PSA, SolarMED repository, Apache-2.0).

| Item | Value | Unit | Notes |
|---|---|---|---|
| Hot water to effect 1 | 12.00 | L/s | measured; 72.01 °C in, 68.72 °C out; 3 bar, 0.4 bar of drop (assumed) |
| Effect pressures, 1 to 14 | 250.78, 222.31, 196.33, 175.34, 154.02, 136.68, 119.79, 104.36, 93.45, 82.07, 73.46, 63.73, 55.55, 49.93 | mbar | measured in every effect |
| End condenser | 47.01 | mbar | measured |
| Feed | 8.00 | m³/h | measured; it enters the preheaters at 27.96 °C, the end condenser's outlet |
| Feed salinity | 35 | g/kg | assumed: the plant runs a closed seawater loop and publishes no salinity |
| Feed after each preheater, 1 to 13 | 62.14 (into effect 1), 60.09, 57.78, 55.47, 52.38, 50.39, 46.89, 45.69, 43.24, 41.03, 38.66, 35.95, 32.56 | °C | measured; preheater 3's sensor reads 55.05 °C, below preheater 4's, and is replaced by the mean of its neighbours |
| Cooling seawater | 20.22 in, 27.96 out | °C | measured; the flow is calculated (the plant sent 11.19 m³/h) |
| Heat-transfer areas | 24.26 (effect 1), 26.28 (effects 2-14) | m² | SolarMED, ptOp.m; used only to read the evaporators' coefficient off the duties |

## Thermodynamics

- **Property package:** Seawater IAPWS-08, with the compounds Water and Salt.
- **Why this package:** it is the IAPWS-08 Gibbs function of seawater - the brine's enthalpy, density and the chemical potential of its water, from which the boiling point elevation follows - with IAPWS-95 for the vapour and the distillate. The elevation is what separates each effect's brine from the vapour it condenses against; at 50 g/kg it is about half a kelvin of the 2 to 2.7 K each effect has.
- **The version matters.** Up to DWSIM 10.2.12 this package could not evaporate seawater: its P-H flash failed in the two-phase region, so neither a heated vessel nor a brine valve calculated, and its boiling point elevation was 10-14 % above IAPWS-08 (reported as DanWBR/dwsim10#122). 10.2.13 fixed it: its elevation is IAPWS-08's to 0.002 K. Open this case in 10.2.13 or later.
- **Its range:** brine up to 0.12 kg/kg, the formulation's limit, and seawater above 0 °C. Here the brine leaves at 54.1 g/kg and nothing is below 20 °C.

## Tuning and convergence notes

- **DWSIM 10.2.13 or later.** Up to 10.2.12 the Seawater IAPWS-08 package's P-H flash failed in every two-phase state, so no effect here would calculate (DanWBR/dwsim10#122).
- **An effect is a vessel heated by an energy stream.** The vessel runs at its feed's pressure, so a valve before each one sets the effect's pressure (VF-1, VB-2 to VB-14). The heat comes in at its Heat In port, from the cooler that condenses the previous effect's vapour to its saturated liquid (outlet vapour fraction 0). The vessel's P-H flash finds the brine's boiling temperature and how much water leaves it.
- **"Infinite loop detected", with no loop.** DWSIM orders a flowsheet by walking back from its ends along every path, repeats included, and stops at 10,000 steps. Every effect connects to the one before twice, by its brine and by its heat, and the distillate cascade adds a third route, so the paths double with each effect. DWSIM refused the flowsheet at its fifth effect.
  - A Recycle on each effect's vapour line (RV-1 to RV-13) stops the walk there and keeps the count linear.
  - There is no loop to converge, so each closes in a pass or two.
  - Under a time limit (the automation's `CalculateFlowsheet3`) DWSIM says nothing at all: nothing is solved and no message is given. The GUI and `CalculateFlowsheet4` give the reason.
- **The tears given by pressure and enthalpy.** A Recycle copies the stream it reads into its tear and keeps the tear's own specification. A tear given by vapour fraction takes the vapour's 1, and the package refuses pure water at a vapour fraction of 1 ("Vapor fraction higher than water mole fraction in the mixture"). Pressure and enthalpy take any state, two phases included - a tear here carries the vapour with the distillate let down into it.
- **Recycle tolerances.** They are closed to 1e-7 kg/s, 1e-4 K and 0.1 Pa, well inside DWSIM's defaults (0.01 kg/s, 0.1 K). Every block then balances to about 1e-6, and so does the boundary (1.9e-6 on energy).
- **Preheaters as two sides.** As one heat-exchanger block each preheater closes a loop with its neighbours (the feed from the next one, the vapour from an effect that the previous one feeds), and DWSIM could not order 13 of them. A heater on the feed, a cooler on the vapour, and a Spec block (`X`, before the target) carry the duty across, kW to kW.
- **The end condenser at its set point.** The feed is drawn from the condenser's outlet. With the plant's 11.19 m³/h, the lossless model's outlet would be warmer than the feed after preheater 13, which would then have cooled it.
  - The plant holds that outlet at 28 °C by the cooling flow. The build does the same: the flow is the condenser's duty over the seawater's enthalpy rise, one pass, and the file keeps it.
  - An Adjust on that flow works too, but DWSIM solves the whole flowsheet, its recycles included, at every step of the Adjust: the solve was stopped after 10 minutes.
- **Brine valves.** The steps between these effects, 2 to 3 K, solve. On a larger one, 10.2.13's P-H flash can search outside its range and stop with "Seawater vapor pressure did not converge at 252.6 K": three effects 16 K apart met it at a brine valve.
- **Saved for DWSIM's interface.** The file names its property package "IAPWS-08 Seawater", as the Windows interface registers it. A file saved from a script carries the automation's name, "Seawater IAPWS-08", and the interface then stops at "The Seawater IAPWS-08 Property Package library was not found" and calculates nothing. The automation reads either name.
- **Solve:** 3 s from the saved file, which holds the converged state; about a minute from the build's first guesses.

## Results

The reference is the plant itself, at the operating point the model takes its inputs from. The performance ratio is the PSA's: kg of distillate per 2326 kJ of the heat the hot water gives effect 1 (Chorak et al. 2017).

- **Distillate, 14 % above the plant's.** DWSIM makes 2 891 kg/h at a performance ratio of 11.53; the plant made 2 527 kg/h (2.536 m³/h at 27.6 °C) at 10.12 ± 0.55. The plant loses heat that the model does not.
  - The plant's own measured streams - the reject, the brine, the distillate, against the seawater it took in - carry out 80.0 % of the hot water's heat. The model's carry out all of it, 100.0 %.
  - The other 20 % leaves through the shells of the 14 effects, at 33 to 65 °C on a 19 °C day, and through the vacuum system, whose two seawater hydro-ejectors vent effects 2 and 7 and the end condenser. Neither is in the model.
  - So every kilowatt the model receives either boils water or reaches the condenser, which needs 13.45 m³/h of seawater to hold its outlet at 27.96 °C. The plant needed 11.19 m³/h.
- **Where the losses do not enter, the model meets the plant.**
  - **The last effect's brine:** 33.39 °C against 33.21 °C measured. The pressure is the measured one, so this tests the boiling point elevation, 0.538 K at 54.1 g/kg above water's saturation at 49.93 mbar.
  - **The evaporators' coefficient:** the duty DWSIM gives each effect, over the plant's 26.28 m² and the difference between the condensing vapour and the brine, averages 2.31 kW/(m² K) over effects 2 to 14. El-Dessouky & Ettouney's correlation, at those brine temperatures, gives 2.37.
- **Effect by effect** (the figure): each effect boils about 200 to 215 kg/h; the last boils more, 235 kg/h, from the flash of the brine and the distillate let down to it. The brine boils 0.43 to 0.54 K above water at its effect's pressure, and leaves at 54.1 g/kg from 35 g/kg fed.

| Quantity | DWSIM | Reference | Reference source | Rel. error |
|---|---|---|---|---|
| Distillate, kg/h | 2 891 | 2 527 | PSA, 31 Oct 2023 | +14.41 % |
| Performance ratio, kg of distillate per 2326 kJ of the hot water's heat | 11.53 | 10.12 | PSA, 31 Oct 2023, +/- 0.55 | +13.98 % |
| Hot water's heat the products carry out, over the seawater taken in, % | 100.0 | 80.0 | PSA, 31 Oct 2023, its measured streams | +25.01 % |
| Seawater the end condenser needs to leave at 27.96 C, m3/h | 13.45 | 11.19 | PSA, 31 Oct 2023 | +20.16 % |
| Brine leaving effect 14, °C | 33.39 | 33.21 | PSA, 31 Oct 2023 | +0.06 % |
| Brine salinity, g/kg | 54.1 | — | 35 g/kg fed (assumed) | — |
| Heat from the hot water, kW | 161.9 | — | 12.00 L/s, 72.01 to 68.72 C | — |
| Brine temperature in effect 1, °C | 65.47 | — | — | — |
| Vapour boiled in effect 1, kg/h | 202.5 | — | — | — |
| Boiling point elevation in effect 14, K | 0.538 | — | — | — |
| Heat rejected in the end condenser, kW | 118.5 | — | — | — |
| Evaporator coefficient implied on the plant's 26.28 m2, effects 2-14, mean, kW/(m2 K) | 2.31 | 2.37 | El-Dessouky & Ettouney (2002) | −2.52 % |

## Files

- `multi-effect-distillation-seawater-desalination.dwxmz` - the DWSIM flowsheet, with AI4Tech's title block.
- `multi-effect-distillation-seawater-desalination.png` - the flowsheet as DWSIM draws it, with the effect-by-effect figure and the results panel.

## Confidentiality

Every number comes from public sources: the PSA's operating data, published under the Apache-2.0 licence in the SolarMED repository, and the papers cited below. The plant is a public research facility of CIEMAT; no client data were used and no client is named. The contributor's contact details are in the flowsheet's title block with the maintainer's agreement. I have the right to publish this case.

## References

- Serrano, J. M. (CIEMAT-PSA). SolarMED: modelling and data of the PSA's solar MED plant. https://github.com/juan11iguel/SolarMED (Apache-2.0): `modeling/data/datasets/med_2022_2024_exp_campaign_operation_points.csv` (the operating point) and `modeling/auxiliar_material/med_model/matlab_code/ptOp.m` (the areas).
- de la Calle, A., Bonilla, J., Roca, L., Palenzuela, P. (2014). Dynamic modeling and performance of the first cell of a multi-effect distillation plant. *Applied Thermal Engineering* 70, 410-420. https://doi.org/10.1016/j.applthermaleng.2014.05.035
- Chorak, A., Palenzuela, P., Alarcón-Padilla, D.-C., Ben Abdellah, A. (2017). Experimental characterization of a multi-effect distillation system coupled to a flat plate solar collector field: Empirical correlations. *Applied Thermal Engineering* 120, 298-313. https://doi.org/10.1016/j.applthermaleng.2017.03.115
- Palenzuela, P., Alarcón-Padilla, D.-C., Ortega-Delgado, B., Zaragoza, G. (2023). Cogeneration of fresh water and electricity with high-temperature power cycles: comparative assessment of multi-effect distillation and reverse osmosis. *Processes* 11, 1181. https://doi.org/10.3390/pr11041181 - the evaporator coefficient of El-Dessouky & Ettouney, their Eq. 21.
- El-Dessouky, H. T., Ettouney, H. M. (2002). *Fundamentals of Salt Water Desalination*. Elsevier, Amsterdam.
- IAPWS R13-08 (2008). Release on the IAPWS Formulation 2008 for the Thermodynamic Properties of Seawater.
- DanWBR/dwsim10#122 (2026). Seawater IAPWS-08: no partial evaporation; salinity, boiling point elevation, vapour enthalpy and freezing point depart from IAPWS-08. https://github.com/DanWBR/dwsim10/issues/122
