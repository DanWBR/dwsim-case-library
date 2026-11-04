# UHT milk by direct steam injection: preheating, steam injector, holding tube, vacuum flash cooling and aseptic homogenization, with the lethality F0, B* and C* integrated along the holding tube

**Category:** other
**Status:** community
**DWSIM version:** 10.2.13
**DWSIM edition:** open source
**Language:** English
**Contributor:** Prof. Nicolas Spogis, Ph.D. (@Spogis), AI4Tech · nicolas.spogis@ai4tech.ai · www.ai4tech.ai

## Summary

A direct UHT line for milk, as the Tetra Pak *Dairy Processing Handbook* describes it. 10,000 L/h of raw milk are preheated to 80 °C and brought in an instant to the UHT temperature by culinary steam injected into them. They are held in a holding tube, then flash cooled in a vacuum vessel that takes back exactly the water the steam brought. Last, the milk is homogenized aseptically and cooled to 20 °C against the incoming milk.

The case also computes what a process simulator does not compute by itself: the sterilizing effect. In the holding tube, DWSIM's own kinetics integrate three lethality meters (F0, Kessler's B* and C*) and two spore populations: the thermophilic spores of B* and *Clostridium botulinum*. DWSIM's spreadsheet reads them live, before the injection and at every quarter of the tube, and compares them with the z-value model by formula.

The steam is controlled on the lethality itself. An Adjust sets its flow for F0 = 5.0 min at the fastest particle, which holds the milk at 139.85 °C for 4.0 s. The fastest particle then sees 10.3 decimal reductions of thermophilic spores (the Handbook: 10-15 in UHT plants) and 20.0 of *C. botulinum* (the botulinum cook is 12).

## Process description

**Preheating and regeneration (section 1).**
- P-101 pumps the raw milk from the balance tank at 4 °C.
- E-101A, the regenerative section, heats it with the outgoing UHT milk until that milk leaves at 20 °C.
- E-102, the heating section, takes it to 80 °C with hot water, and P-102 raises it to 6.5 bar.
- E-101A and E-101B are the regenerative section's two sides. SPEC-101 hands E-101A's duty to E-101B: drawn as one exchanger, the section would close a loop around the whole line.

**UHT heating, holding and flash cooling (section 2).**
- The culinary steam is dry saturated at 10 bar(a). It is let down to the milk's pressure by its control valve, V-102, and injected into the milk by INJ-101.
- The holding tube, H-101A to H-101D, is four straight lengths of a 50 mm-bore hygienic tube (EN 10357 series A, formerly DIN 11850 series 2, DN 50: 53 × 1.5 mm). It is 7.96 m long in all: 4.0 s for the fastest particle.
- The back-pressure valve V-101 lets the milk down into the vacuum vessel VV-101, where it boils back to 83.6 °C.
- E-103 condenses the flash vapour on cooling water, and P-104 pumps the condensate out.

**Aseptic homogenization (section 3).**
- P-103 feeds the two-stage homogenizer: HOM-101 to 200 bar, then HV-101 to 40 bar and HV-102 to 3 bar.
- The homogenized milk goes back to E-101B and leaves as UHT milk at 20 °C, for the aseptic tank or the filler.

**The plant's two controllers.**
- ADJ-101 sets the steam flow for the lethality, F0 = 5.0 min at the fastest particle.
- ADJ-102 sets the back-pressure valve, and so the vacuum, so that the milk leaves the vessel with the raw milk's 87.1 % of water. The vapour flashed off then equals the steam injected, which is how the Handbook describes the control.

## The lethality, and how to check it in DWSIM

Two kinds of compound react in the holding tube's four lengths, and only there. Both are DWSIM kinetic reactions whose rate is a kinetic expression in T (UserDefined): the z-value model exactly, not an Arrhenius fit of it, which drifts 5 % within 10 K.

- **Three lethality meters, zero order**, made at 10^((T - Tref)/z) / D mol/(m³ s). Their concentration in mol/m³ at any point of the tube *is* the lethality accumulated up to that point.
  - F0: 121.1 °C, z 10 K, D 60 s. One minute at 121.1 °C is F0 = 1.
  - Kessler's B*: 135 °C, z 10.5 K, 10.1 s.
  - Kessler's C*: 135 °C, z 31.4 K, 30.5 s.
- **Two spore populations, first order**, dying at ln 10 / D(T), with D(T) = Dref × 10^((Tref - T)/z). Their survivors give the decimal reductions log N0/N, the Handbook's measure of a sterilizing effect.
  - **Thermophilic spores.** They are the natural thermophilic spore population of Kessler's B*: 9 decimal reductions at B* = 1, 135 °C for 10.1 s, so D135 = 1.12 s. Their z is 10.5 K, the Handbook's z for *Bacillus stearothermophilus* (now *Geobacillus*), the test organism of UHT plants.
  - ***Clostridium botulinum*.** The most heat-resistant pathogenic spore: D121.1 = 0.25 min, z 10 K, as the Handbook gives them. One F0 minute is 4 decimal reductions, and F0 = 3 is the 12D botulinum cook.

The meters are formed from the milk's water. Each is a thousandth of a water molecule: a thousandth of its molar mass, the same heat capacity and heat of formation per kg. Forming them moves no energy, and the 7.5 mol/m³ of meters at the tube's end take 0.13 g of water per m³. The spores, 1 mol/m³ in the raw milk, are a tracer: log N0/N does not depend on N0.

DWSIM's plug flow is the mean particle's. The fastest particle, in turbulent flow, moves at the mean velocity / 0.85 (the Handbook: 0.85-1.00; 0.5, laminar, in the US). In an isothermal tube it collects 0.85 of the lethality.

**Checking it in DWSIM.**
- **The lethality table on the drawing** is a range of DWSIM's own spreadsheet (Spreadsheet tab), so every number in it is a formula that DWSIM recomputes on every solve.
  - For the spores: log N/N0 before the injection and at the end of the holding, the decimal reductions for the mean and the fastest particle, and the z-value model computed by formula from the tube's temperature and residence time.
  - For F0, B* and C*, the same.
  - Along the tube, the same numbers after each of its four lengths.
  - Change the milk flow, the tube, the steam or ADJ-101's target, solve, and the table follows.
- **The profile of any length of the tube** (H-101A to H-101D, Results) lists every compound's concentration along it. The meters' columns are F0, B* and C* in their own units.
- The figure *The lethality, metre by metre* draws those profiles; *The UHT window* puts the line on Kessler's diagram.

## Feed and operating conditions

| Item | Value | Unit | Notes |
|---|---|---|---|
| Raw milk | 10,000 | L/h | at 4 °C and 1.2 bar(a), from the balance tank; 10,288 kg/h by DWSIM's own density |
| Raw milk, by mass | fat 3.9, protein 3.4, lactose 4.8, minerals 0.8, water 87.1 | % | the Handbook's mean composition (ch. 2, Table 2.3), water by difference |
| Preheat | 80 | °C | the Handbook; regeneration, then hot water |
| Product | 20 | °C | the Handbook; the regeneration is sized for it |
| Culinary steam | 10 | bar(a) | dry saturated, at IAPWS's enthalpy |
| Product in the holding tube | 6.5 | bar(a) | 140 °C boils at 3.6 bar |
| Lethality | F0 = 5.0 | min | at the fastest particle - ADJ-101's target; the Handbook: 5-6 for good-quality milk |
| Holding | 4.0 | s | for the fastest particle: the tube's length |
| Homogenization | 200 and 40 | bar | two stages |
| Pressure drop per heat exchanger side | 0.5 | bar | |

## Thermodynamics

- **Property package:** Raoult's law, on ExpData enthalpies.
- **Why this package:**
  - Milk is water with non-volatile solutes, an ideal solution at these mole fractions (water 0.994).
  - ExpData builds the liquid's enthalpy from the compounds' own heat capacities, and a mixture's heat capacity by mass. Its density is additive in volume. That is Choi and Okos's mixing.
- **The milk's solids** are four pseudo-compounds (JSON compounds of DWSIM's, built from its own Lactose.json): fat, protein, lactose and minerals.
  - Each carries Choi and Okos's (1986) heat capacity and density as functions of temperature, as ASHRAE gives them. Castell-Perez (2020, Table 2) prints the heat capacities. CoolProp's INCOMP::Food* fluids reproduce both to the last digit, and they settle the fat's coefficient, which Castell-Perez misprints as 4.8088e-6 for 4.8008e-6.
  - The molar masses only set Raoult's mole fractions: a triglyceride (807 g/mol), a casein (25 kg/mol), lactose (342.3), and 100 for the salts.
  - They are non-volatile: 10^-6 Pa at 140 °C.
- **The steam.** The vapour of Raoult's law is an ideal gas, and DWSIM's dry saturated steam at 10 bar came out 58 kJ/kg richer than IAPWS-95's. That would have made the flash vessel's rise over the preheat 40 % too large.
  - The steam is specified instead by its pressure and IAPWS's enthalpy, anchored on DWSIM's own liquid water at 25 °C. DWSIM shows it as 97 % quality.
  - Below 100 °C, at the flash, the ideal-gas vapour is within 5 kJ/kg of IAPWS's. The liquid water is within 1.2 kJ/kg up to 180 °C.

## Tuning and convergence notes

- **The two Adjusts are in DWSIM's simultaneous solver.**
  - ADJ-101 holds the F0 meter's mole fraction in the held milk. It is intensive, so it holds whatever the flow. The build sets it to the value that is F0 = 5.0 min at the fastest particle: 1.13 × 10^-4.
  - ADJ-102 holds the flash-cooled milk's water fraction at the raw milk's 0.871.
  - The saved file solves in about 2 s.
- **The tube's step, dV 0.025 on integrator 0: 40 slices to a length.** Two of DWSIM's PFR habits decide it, and the build checks both before it keeps a step.
  - DWSIM integrates each slice of dV × its volume to the last point its integrator reports. A floating-point accident of the slice's length can leave that point a hundredth of the slice short, and every meter then reads 1 % low: on these lengths dV 0.02 did, and every power-of-two step tried. The build checks the F0 meter against the z-value model on DWSIM's own profile.
  - A first-order death of more than about one decade in a slice comes out exactly zero. 21.6 decimal reductions of *C. botulinum* in one tube gave 0.0 at 2.2 decades a slice and the right number at 0.43. Here each slice holds 0.15 decade, a third of the 0.43 seen to integrate. The build checks the survivors too.
- **Every compound's order in a kinetic reaction.** DWSIM wants an order for every compound of a reaction, in both directions: here all zero, the spores' own one.
- **The spreadsheet's argument separator is ';'.** DWSIM keeps its spreadsheet on the invariant separator, whatever Windows' culture; with ',' a formula fails with "expect )". GETPROPVAL with no unit returns SI.
- **The steam's pressure and enthalpy go together.** A new steam pressure needs IAPWS's enthalpy at it: the stream is specified by both.

## Results

The case's heat and mass balances follow IAPWS-95 and Choi and Okos's properties within 0.1 %. Its lethality follows the z-value model integrated apart on DWSIM's own temperature profile within 0.01 %. Its flash vessel is 0.07 K cooler than the IAPWS balance, because DWSIM's vapour at 84 °C carries 5 kJ/kg more than IAPWS's.

| Quantity | DWSIM | Reference | Reference source | Rel. error |
|---|---|---|---|---|
| Raw milk, L/h | 10 000 | 10 000 | Dairy Processing Handbook, ch. 10 | 0.00 % |
| Raw milk density at 4 C, kg/m3 | 1 028.8 | 1 028.6 | Choi & Okos with IAPWS water, by hand | +0.02 % |
| Holding temperature, after the injector, C | 139.85 | 139.85 | z-value model for F0 = 5.0 min, by hand | 0.00 % |
| Culinary steam, 10 bar(a), kg/h | 1 106.7 | 1 105.8 | IAPWS-95 and Choi & Okos, by hand | +0.08 % |
| Steam per kg of raw milk, kg/kg | 0.1076 | 0.1075 | IAPWS-95 and Choi & Okos, by hand | +0.08 % |
| Holding tube length, m | 7.96 | — | 4.0 s for the fastest particle, DN 50 (50 mm inside), in four lengths | — |
| Mean velocity in the tube, m/s | 1.692 | — | — | — |
| Reynolds number in the tube, thousand | 398 | — | turbulent; DWSIM's milk has water's viscosity | — |
| Mean residence time in the tube, s | 4.706 | — | — | — |
| Fastest particle's residence time, s | 4.000 | 4.000 | Dairy Processing Handbook, ch. 10 | −0.01 % |
| Pressure drop in the tube, bar | 0.0434 | 0.0436 | Darcy-Weisbach and Churchill, by hand | −0.46 % |
| Thermophilic spores, decimal reductions, mean particle | 12.15 | 12.15 | z-value model on DWSIM's T profile | 0.00 % |
| Thermophilic spores, decimal reductions, fastest particle | 10.33 | 10.33 | z-value model on DWSIM's T profile | 0.00 % |
| C. botulinum spores, decimal reductions, mean particle | 23.53 | 23.53 | z-value model on DWSIM's T profile | 0.00 % |
| C. botulinum spores, decimal reductions, fastest particle | 20.00 | 20.00 | z-value model on DWSIM's T profile | 0.00 % |
| F0 at the tube's end, mean particle, min | 5.882 | 5.882 | z-value model on DWSIM's T profile | 0.00 % |
| F0 at the tube's end, fastest particle, min | 5.000 | 5.000 | z-value model on DWSIM's T profile | 0.00 % |
| B* at the tube's end, mean particle | 1.3498 | 1.3498 | z-value model on DWSIM's T profile | 0.00 % |
| B* at the tube's end, fastest particle | 1.1474 | 1.1474 | z-value model on DWSIM's T profile | 0.00 % |
| C* at the tube's end, mean particle | 0.2202 | 0.2202 | z-value model on DWSIM's T profile | 0.00 % |
| C* at the tube's end, fastest particle | 0.1872 | 0.1872 | z-value model on DWSIM's T profile | 0.00 % |
| Length where the fastest particle reaches B* = 1, m | 6.939 | 6.939 | z-value model on DWSIM's T profile | 0.00 % |
| Length where the fastest particle reaches F0 = 3 min, m | 4.777 | 4.777 | z-value model on DWSIM's T profile | +0.01 % |
| Flash vessel temperature, C | 83.57 | 83.64 | IAPWS-95 and Choi & Okos, by hand | −0.02 % |
| Flash vessel above the preheat, K | 3.57 | 3.64 | IAPWS-95 and Choi & Okos, by hand | −1.85 % |
| Flash vessel pressure, bar | 0.5440 | 0.5439 | Raoult's law on IAPWS's vapour pressure | +0.02 % |
| Flash vapour, kg/h | 1 106.7 | 1 106.7 | the steam injected | 0.00 % |
| Water in the UHT milk, % | 87.100 | 87.100 | the raw milk | 0.00 % |
| Rise through the homogenizer, K | 5.06 | 5.06 | first law, (200 - 3) bar / (rho cp) | −0.05 % |
| Raw milk after regeneration, C | 72.79 | — | the UHT milk leaves at 20 C | — |
| Regeneration, of the heating to the holding temperature, % | 50.6 | — | — | — |
| Hot water, E-102, kW | 80.2 | — | — | — |
| Cooling water, vapour condenser E-103, kW | 719.1 | — | — | — |
| Homogenizer power, kW | 56.2 | — | — | — |

## Files

- `uht-milk-direct-steam-injection.dwxmz` - the DWSIM flowsheet, with AI4Tech's title block and the live lethality table.
- `uht-milk-direct-steam-injection.png` - the flowsheet as DWSIM draws it.

## Confidentiality

Everything in the case is public: the Handbook's process, composition and lethality definitions, Choi and Okos's properties, the IAPWS steam tables. No client and no plant data are in it. The contributor's contact is in the flowsheet's title block with the maintainer's agreement.

## References

- Tetra Pak (2015 and online). *Dairy Processing Handbook*. Chapter 10, Long life dairy products: the direct UHT plant, the holding, the sterilizing effect (log N0/N), B. stearothermophilus and C. botulinum, B*, C*, F0 and their targets, the fastest-particle coefficient. Chapter 2, The chemistry of milk: Table 2.3, the composition of milk. https://dairyprocessinghandbook.tetrapak.com
- Kessler, H. G. (1981). *Food Engineering and Dairy Technology*. Verlag A. Kessler, Freising - the B* and C* definitions, as the Handbook gives them.
- Choi, Y., Okos, M. R. (1986). Effects of temperature and composition on the thermal properties of foods. In M. Le Maguer, P. Jelen (eds.), *Food Engineering and Process Applications*, vol. 1, 93-101. Elsevier.
- Castell-Perez, M. E. (2020). Freezing of food. In N. M. Holden et al. (eds.), *Introduction to Biosystems Engineering*. ASABE and Virginia Tech Publishing, CC BY 4.0, Table 2 - Choi and Okos's heat capacities. https://doi.org/10.21061/IntroBiosystemsEngineering/Freezing_Food
- Bell, I. H., Wronski, J., Quoilin, S., Lemort, V. (2014). Pure and pseudo-pure fluid thermophysical property evaluation and the open-source thermophysical property library CoolProp. *Industrial & Engineering Chemistry Research* 53(6), 2498-2508 - IAPWS-95 and the food components (INCOMP::Food*).
- Wagner, W., Pruss, A. (2002). The IAPWS formulation 1995 for the thermodynamic properties of ordinary water substance for general and scientific use. *Journal of Physical and Chemical Reference Data* 31(2), 387-535.
- Churchill, S. W. (1977). Friction-factor equation spans all fluid-flow regimes. *Chemical Engineering* 84(24), 91-92.
- EN 10357 (2013), series A (formerly DIN 11850 series 2) - DN 50 hygienic tube, 53 × 1.5 mm.
