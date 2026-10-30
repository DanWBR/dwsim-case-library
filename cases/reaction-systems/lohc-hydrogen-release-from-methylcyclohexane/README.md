# Hydrogen released from a liquid organic carrier: methylcyclohexane dehydrogenated in a catalytic reactor heated by engine exhaust, against Usman and Cresswell's reactor model

**Category:** reaction-systems
**Status:** community
**DWSIM version:** 10.2.12
**Language:** English
**Contributor:** Prof. Nicolas Spogis, Ph.D. (@Spogis), AI4Tech · nicolas.spogis@ai4tech.ai · www.ai4tech.ai

## Summary

- **What it is:** hydrogen carried as a liquid. Methylcyclohexane (MCH), a liquid organic hydrogen carrier, is dehydrogenated over 1 wt% Pt/γ-Al2O3 to toluene and three molecules of hydrogen. The reaction takes 205 kJ/mol of MCH, and the engine's exhaust supplies it. The reactor is the one Usman & Cresswell (2015) designed for a car: 12 catalyst tubes inside shroud tubes, with the exhaust flowing outside them. The case builds their base design in DWSIM on their own kinetics, with the plant around it. The MCH is pumped and vaporised by the exhaust leaving the reactor, the products are cooled, the hydrogen is flashed off for the engine and the toluene goes back to its tank.
- **Headline:** their rate law gives their rate at the reactor inlet to 0.6 %. Against their two-dimensional model run co-current:
  - the exhaust leaves the reactor within 1.6 K of theirs, so the heat it gives is the same;
  - 0.953 of the MCH is converted, against their 0.922;
  - the bed leaves 23 K hotter than theirs, the price of a one-dimensional bed.

  The engine gets 0.722 kg/h of hydrogen at 98.95 mol %.
- **What DWSIM needed** - five things the case documents, each measured on 10.2.12:
  - **Co-current flow.** The PFR does not solve counter-current: past its first pass the volume step it restarts from is zero. The paper's base case is counter-current, and the paper also gives the co-current case at the same conditions, which is the one modelled here.
  - **A volume step that lands on the reactor's volume.** With dV = 0.001 the last slice is 4e-15 of the volume, and the solve stops on "Array dimensions exceeded supported range".
  - **Every division in the rate written with a decimal.** DWSIM divides integers as integers, so `1/650` is 0.
  - **R-1 set aside in the balance.** The PFR needs an energy stream even when a utility stream heats it, and it writes the heat into that stream as well.
  - **The tube diameter given beforehand.** On its first calculation the PFR heats its first slice through 0.1 m tubes, its default, and computes the real diameter only after that slice.

## Process description

One process line, as the flowsheet draws it.

**The MCH.** The pump P-1 takes 0.03493 mol/s of MCH (12.35 kg/h) from its tank at 25 °C to 9 bar. E-1 vaporises it and heats it to 380 °C, which is Usman & Cresswell's reactor inlet. The heat comes from the exhaust after it has left the reactor.

**R-1, the reactor-heat exchanger.**
- 12 tubes of 16.561 mm inside diameter hold 0.500 m of catalyst, 0.9232 kg of 1.2 mm Pt/γ-Al2O3 spheres.
- MCH → toluene + 3 H2 runs on Usman & Cresswell's Langmuir-Hinshelwood rate.
- The engine's exhaust, 2.5339 mol/s at 638.02 °C and 5 bar, flows co-current outside the tubes. In DWSIM it is the PFR's utility stream, through its ports 2 (in) and 1 (out). It then goes on to E-1 and the tailpipe.
- The exhaust leaving R-1 heats the MCH entering it, so the loop is torn on the exhaust by a Recycle (REC-1). E-1 is specified by the MCH's outlet temperature.

**E-2 and V-1.** The products are cooled to 40 °C. V-1 flashes the hydrogen off at 9 bar for the engine. The toluene, with the MCH left, returns to its tank, ready to be hydrogenated again.

The engine, the hydrogenation that refills the MCH, and the start-up are outside the case. Hamayun et al. (2019, 2020) simulate a stationary release plant on the same kinetics at 360 °C and 1.8 bar, but publish no flows; Usman & Cresswell give every dimension.

## Feed and operating conditions

| Item | Value | Unit | Notes |
|---|---|---|---|
| MCH | 0.03493 | mol/s | Usman & Cresswell (2015), Table 1; pure, from a tank at 25 °C (the case's) |
| Reactor inlet | 380 °C, 9 bar | | Table 1 |
| Tubes | 12; 16.561 mm inside; 0.500 m | | Table 1 |
| Catalyst | 0.9232 kg of 1 wt% Pt/γ-Al2O3, 1.2 mm spheres | | Table 1; bed voidage 0.4058 from Dixon (1988), as the paper computes it |
| Rate | LHHW, their Eqs. 31-34 | mol/(s g cat) | Usman, Cresswell & Garforth (2012); the activity term at td = 0.063, as the paper uses it |
| Exhaust | 2.5339 mol/s at 638.02 °C, 5 bar | | Table 1: CO2 9.24, H2O 14.05, O2 3.26, N2 73.45 mol % |
| Flow direction | co-current | | the paper's Section 5.3; its base case is counter-current |
| Overall heat transfer coefficient | 176.4 | W/m2.K | from the paper's Table 3, below |
| Products | cooled to 40 °C, flashed at 9 bar | | the case's |

## Thermodynamics

- **Property package:** Peng-Robinson.
- **Why this package:** MCH, toluene and hydrogen as gases at 9 bar and 380-480 °C, the exhaust at 5 bar, the condensate at 40 °C. Hydrocarbons and light gases are the ground a cubic equation of state was made for.
- **Interaction parameters:** DWSIM's. Its review notes 13 pairs with a non-hydrocarbon and no kij, among them hydrogen with MCH and toluene. They set how much toluene and MCH the hydrogen carries out of V-1 (1 mol %), not the reaction.
- **Heats of formation:** DWSIM's, checked first, as the skill asks of any reacting case.
  - At 25 °C, MCH -154.80 and toluene +50.17 kJ/mol, ideal gas, against NIST's -154.8 ± 1.0 and +50.1 ± 1.1.
  - The reaction takes 204.97 kJ/mol against NIST's 204.9.
  - At 650 K it takes 216.3 kJ/mol, from the slope of DWSIM's own ln K. The paper's equilibrium constant implies 217.65.
- **Equilibrium:** DWSIM's constant, from its Gibbs energies, is 0.62 of the paper's at 650 K (2215 against 3600 bar³).
  - The rate keeps the paper's K, as published.
  - At 9 bar the reaction stays far from either. The quotient Q never passes 1.0 % of DWSIM's K along the tubes, so the rate's equilibrium term stays above 0.99.

## Tuning and convergence notes

- **Why co-current.** DWSIM 10.2.12's PFR does not solve counter-current heat exchange.
  - Its counter-current mode integrates the tube, recomputes the coolant's profile backwards, and integrates again until the profile settles.
  - The second integration restarts from the last volume step of the first. That step is the remainder of the volume, zero when the steps land on it.
  - On integrator 0 the solve stopped on "tf = t0" in 2.6 s. On integrator 4 it never finished, and was stopped after more than 9 minutes.
  - Co-current needs one pass and solves.
- **The volume step.** The PFR walks its volume in slices of dV and cuts the last one to what is left. Its co-current pass sizes the exhaust's temperature profile from that last slice.
  - With dV = 0.001 on these tubes (1.29245e-3 m3) the last slice is 4e-15 of the volume, and the solve stopped on "Array dimensions exceeded supported range".
  - The case takes dV = 2^-9 (512 slices), which lands exactly, found by `dwsim_api.pfr_dv`.
  - The build also checks, with a constant-rate probe (`dwsim_api.pfr_slice_check`), that each slice is integrated whole. On integrator 4 the same slices integrate 0.990 of themselves; on integrator 0, the default, all of them.
- **The tube diameter.** On its first calculation, DWSIM's PFR gives its first slice the area of its default 0.1 m tubes, six times these tubes' area, and computes the real diameter only after that slice.
  - Solved once, the reactor alone heated its gas 13 K in the first millimetre, where it heats it 0.5 K, and converted 0.9553 instead of 0.9533.
  - The case's flowsheet solves R-1 several times through the Recycle, which hides the error.
  - The build gives the diameter (`Diameter`) before the first solve.
- **Integer division.** The paper's K is `3600*exp(-217650/8.314*(1/T-1/650))`. Written so, DWSIM's expression evaluator made `1/650` zero and K about 1e-14 bar³. The reaction then ran backwards from the first slice, and 0.03 % of the MCH was converted. It is written `1/650.0`.
- **One U from a two-dimensional bed.** The paper's model is two-dimensional. Its Ui (Table 3, 183 to 302 W/m2.K along the tube) runs from the exhaust to the bed at the tube wall, and its kr is the bed's radial conductivity.
  - A one-dimensional bed has one temperature across the tube, the mean. Between the wall and the mean, a parabolic radial profile adds R/(4 kr).
  - So each point of Table 3 gives U = 1/(1/Ui + R/(4 kr)), 102 to 206 W/m2.K. Averaged along the bed it is 176.4 W/m2.K (the card).
  - With Ui's own average, 270 W/m2.K, the bed takes too much heat: 0.993 converted and the bed out at 521 °C.
  - With 140 W/m2.K, the bed leaves at the paper's temperature (456.6 °C), but only 0.904 is converted.
  - No single U reproduces all three of the paper's numbers. The one-dimensional bed misses the hot wall layer where the two-dimensional one converts most.
- **The utility stream.** The PFR reads the utility's flow and heat capacity from the stream connected to its port 2. It does not read its inlet temperature: that is given again (`CoolantInletTemperature`). The heat capacity is the inlet's, held constant along the tubes.
- **R-1 duty and the balance.** The PFR refuses to solve without an energy stream: "No energy stream associated with the reactor". It writes its duty into that stream (8.41 kW) although the exhaust already gives the heat. The exhaust's enthalpy falls by 8.241 kW and the reacting gas takes 8.327 kW, heats of formation included. The finish and the check set R-1 aside by name for this; everything else closes to 1e-10.
- **Pressure drop.** The PFR applies Ergun's equation with the bed's voidage and particle size: 3.2 kPa over the bed. The paper's counter-current profile loses 5 kPa (Table 3).
- **Solve:** the whole flowsheet, the Recycle included, solves in about 7 s.

## Results

- **The kinetics.** At the inlet, 380 °C and 9 bar of MCH, the rate DWSIM integrates over the first slice is 5.633e-5 kmol/(s kg). The paper's Table 3 gives 5.60e-5.
- **The reactor, co-current, against the paper's two-dimensional model (its Section 5.3):**
  - the exhaust leaves at 544.9 °C against 546.5 °C, so the heat is the same within 2 %;
  - 0.953 of the MCH is converted against 0.922;
  - the bed leaves at 482.0 °C against 459.2 °C.

  The two-dimensional bed is hot at the wall and cold at the axis (the paper's Fig. 5), and its mean temperature is lower for the same heat. The one-dimensional bed runs at the mean.
- **The exhaust it needs.** For 90 % conversion, DWSIM's reactor needs the exhaust at 603 °C, against the paper's 622.3 °C (the second figure).
- **For the engine:** 0.722 kg/h of hydrogen at 98.95 mol %, the rest toluene and MCH vapour at 40 °C. 11.27 kg/h of toluene, with the MCH left, goes back to its tank.
- **The exhaust's heat:** 8.24 kW to R-1 and 3.84 kW to vaporise the MCH (E-1). It reaches the tailpipe at 500.7 °C.

| Quantity | DWSIM | Reference | Reference source | Rel. error |
|---|---|---|---|---|
| Catalyst in the 12 tubes, kg | 0.9232 | 0.9232 | Usman & Cresswell (2015), Table 1 | 0.00 % |
| Rate at the reactor inlet, 1e-5 kmol/(s.kg cat) | 5.633 | 5.600 | Usman & Cresswell (2015), Table 3 | +0.58 % |
| MCH conversion, co-current | 0.9533 | 0.9220 | Usman & Cresswell (2015), Section 5.3 | +3.40 % |
| Exhaust leaving R-1, C | 544.9 | 546.5 | Usman & Cresswell (2015), Section 5.3 | −0.20 % |
| Bed leaving R-1, C | 482.0 | 459.2 | Usman & Cresswell (2015), Section 5.3 | +3.11 % |
| Heat the exhaust gives R-1, kW | 8.241 | — | its enthalpy; R-1 duty repeats it (skill F93) | — |
| Heat the reacting gas takes, kW | 8.327 | — | heats of formation included | — |
| Hydrogen to the engine, kg/h | 0.7224 | — | — | — |
| Hydrogen purity to the engine, mol % | 98.95 | — | toluene and MCH vapour at 40 C, 9 bar | — |
| E-1, MCH vaporised by the exhaust, kW | 3.844 | — | — | — |
| Exhaust to the tailpipe, C | 500.7 | — | — | — |
| Heat of reaction at 650 K, kJ/mol | 216.3 | 217.7 | Usman & Cresswell (2015), Eq. 32 | −0.61 % |
| Equilibrium constant at 650 K, bar3 | 2 215 | 3 600 | Usman & Cresswell (2015), Eq. 32 | −38.47 % |
| Largest Q/K along R-1 | 0.0102 | — | DWSIM's K | — |

## Files

- `lohc-hydrogen-release-from-methylcyclohexane.dwxmz` - the DWSIM flowsheet, with AI4Tech's title block.
- `lohc-hydrogen-release-from-methylcyclohexane.png` - the flowsheet as DWSIM draws it, with the three figures and the results panel.

## Confidentiality

Every number comes from public sources: the published literature cited below and the NIST Chemistry WebBook. No plant or client data were used, and no client is named. The contributor's contact details are in the flowsheet's title block with the maintainer's agreement. I have the right to publish this case.

## References

- Usman, M. R., Cresswell, D. L. (2015). Prototype reactor simulation for on-board use of hydrogen in a hybrid MTH (methylcyclohexane-toluene-hydrogen)-gasoline system and a simplified dynamic modeling for the startup. *Chemical Engineering Research and Design* 104, 125-138. https://doi.org/10.1016/j.cherd.2015.07.026
- Usman, M. R., Cresswell, D. L., Garforth, A. A. (2012). Detailed reaction kinetics for the dehydrogenation of methylcyclohexane over Pt catalyst. *Industrial & Engineering Chemistry Research* 51, 158-170.
- Dixon, A. G. (1988). Correlations for wall and particle shape effects on fixed bed bulk voidage. *Canadian Journal of Chemical Engineering* 66, 705-708.
- Hamayun, M. H., Hussain, M., Maafa, I. M., Aslam, R. (2019). Integration of hydrogenation and dehydrogenation system for hydrogen storage and electricity generation - simulation study. *International Journal of Hydrogen Energy* 44, 20213-20222. https://doi.org/10.1016/j.ijhydene.2019.06.053
- Hamayun, M. H., Maafa, I. M., Hussain, M., Aslam, R. (2020). Simulation study to investigate the effects of operational conditions on methylcyclohexane dehydrogenation for hydrogen production. *Energies* 13, 206. https://doi.org/10.3390/en13010206
- NIST Chemistry WebBook, SRD 69, https://webbook.nist.gov: gas-phase heats of formation of methylcyclohexane (Prosen, Johnson et al. 1946) and toluene (Roux, Temprado et al. 2008).
