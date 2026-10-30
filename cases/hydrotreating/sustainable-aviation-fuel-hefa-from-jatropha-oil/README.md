# Sustainable aviation fuel from jatropha oil by HEFA: hydrotreating, hydrocracking and fractionation on NREL's design basis, the kerosene checked against ASTM D7566

**Category:** hydrotreating
**Status:** community
**DWSIM version:** 10.2.12
**Language:** English
**Contributor:** Prof. Nicolas Spogis, Ph.D. (@Spogis), AI4Tech · nicolas.spogis@ai4tech.ai · www.ai4tech.ai

## Summary

- **What it is:** a HEFA plant (hydroprocessed esters and fatty acids) that turns 788 dry US tons a day of jatropha oil into sustainable aviation fuel. The design basis is NREL's (Tao et al. 2017): the oil is hydrotreated at 400 C and 9.2 MPa, hydrocracked and isomerised at 355 C and 600 psig, and fractionated into LPG, naphtha and a synthetic paraffinic kerosene (HEFA-SPK, ASTM D7566 Annex A2) that blends into jet fuel.
- **Headline:** 175 US gallons of SPK per dry ton of oil, against NREL's 170. Hydrogen 2.07 % of the oil, exactly what the reactions take by hand. The SPK meets every Annex A2 limit DWSIM can calculate: density 747 kg/m3, D86 10 % at 167 C, end point 240 C, flash point 44 C, and freezing point -44 C by an API correlation.
- **What DWSIM needed** - three things the case documents, each measured:
  - DWSIM's triglycerides are formed with 171 to 209 kJ/mol less heat than NIST's measurements. Left so, the hydrotreater would release 31 % more heat than it does. The case gives the oil NIST's heats of formation.
  - DWSIM's 2-methyl C11-C14 come from ChEDL Thermo with a heat of formation of exactly 0.0 (no datum). Left so, the hydrocracker would take in 3 MW where it gives out 1.4. They get their n-isomer's value plus the branching increment of DWSIM's own lighter pairs.
  - DWSIM 10.2.12's rigorous distillation column does not answer with hydrogen in its feed. V-3 flashes the dissolved gas off at the stabiliser's pressure, and both columns then solve in seconds.

## Process description

Three sections, as the flowsheet draws them.

**1 - Hydrotreating.** The oil is pumped from the tank to 9.2 MPa (P-1), joined by hydrogen (M-1) and heated to 400 C (H-1). In R-1 every triglyceride is saturated, its glycerol backbone is cleaved off as propane, and its three fatty acids are decarboxylated to n-alkanes one carbon shorter. NREL chose decarboxylation over hydrodeoxygenation, and so does the case. The free fatty acids are saturated and decarboxylated the same way. The palmitic chains become n-pentadecane, and the stearic, oleic and linoleic chains become n-heptadecane. The effluent is cooled to 50 C (E-1), and the high-pressure separator V-1 takes off the CO2, the propane and the hydrogen left. Part of the CO2 stays dissolved in the paraffins at 9.2 MPa and leaves downstream.

**2 - Hydrocracking and isomerisation.** The paraffins are let down to 600 psig (VLV-1), joined by fresh hydrogen at 50 standard cubic feet a gallon (M-3) and heated to 355 C (H-2). NREL models R-2 as cracking every C15 to C23 alkane completely. Here each C15 and C17 is cut once, at any carbon-carbon bond that leaves two fragments of at least three carbons, every such split equally likely. This is ideal hydrocracking (Weitkamp 2012): primary cracking only, so no methane or ethane. Then 80 % of each n-alkane from C4 to C14 goes to its 2-methyl isomer, an iso/normal ratio of 4, inside the 3 to 6 that UOP's pilot plant gave (US patent 9,039,790). The effluent is cooled to 40 C (E-2), and V-2 takes off the light gases.

**3 - Fractionation.** The liquid is let down to 1.0 MPa (VLV-2), and V-3 flashes off most of the hydrogen still dissolved in it, from 4.4 % to 0.7 % of the liquid by mole, with part of the CO2. The stabiliser T-1 sends C4 and lighter overhead as vapour, to LPG recovery. The splitter T-2 cuts the naphtha, C5 to C8, from the SPK, C9 to C14. The cut sits between n-octane (126 C) and 2-methyloctane (143 C), next to the 132 C at which UOP's patent cuts naphtha from jet. Both columns are rigorous, in theoretical stages. The SPK is cooled to 40 C (E-3).

The hydrogen is once through: there is no recycle compressor, amine wash or PSA. The off-gases carry the hydrogen not taken, and what the plant consumes is what the reactions take.

## Feed and operating conditions

| Item | Value | Unit | Notes |
|---|---|---|---|
| Feed flow | 29,786 | kg/h | 788 dry US tons a day, Tao et al. (2017) |
| Feed composition | 85 glycerides, 15 free fatty acids | wt % | Tao et al.'s jatropha oil: 80.4 % tri-, 2.1 % di- and 2.5 % monoglycerides, taken here as triglycerides, and 15.0 % free acids |
| Fatty acids | palmitic 12.41, stearic 7.96, oleic 45.44, linoleic 34.18 | wt % | Campuzano-Duque & Cardeño-López (2020): 12.41, 7.43, 44.62, 33.95, with the minor acids joined to their kind (saturated to stearic, monounsaturated to oleic, polyunsaturated to linoleic) for the hydrogen they take. C16 12.4 % and C18 87.6 %, as Tao et al.'s Fig. 4 shows jatropha |
| Triglycerides | tripalmitin, tristearin, triolein, trilinolein | | each carrying one fatty acid, their masses in the acids' proportions |
| R-1 | 400 °C, 9.2 MPa | | Tao et al.; isothermal, its duty the heat to remove |
| Hydrogen to R-1 | 614 | kg/h | 1.5 times the 409 kg/h the reactions take |
| V-1 | 50 °C, 9.2 MPa | | |
| R-2 | 355 °C, 4.24 MPa (600 psig) | | Tao et al.; isothermal |
| Hydrogen to R-2 | 998 | kg/h | 50 scf a US gallon of the paraffins at 60 F (Tao et al.); the cracking takes 208 kg/h |
| V-2 | 40 °C, 4.24 MPa | | |
| V-3 | 1.0 MPa, adiabatic | | the dissolved gas flashed off before T-1 |
| T-1 | 20 stages, feed on the 9th; 1.0 MPa | | the condenser and the reboiler included, counted from the top; overhead as vapour (full reflux), reflux ratio 1.0; bottoms 99.8 % of the C5 and heavier it is fed |
| T-2 | 40 stages, feed on the 20th; 150 kPa | | total condenser, reflux ratio 2.5; bottoms its feed less the C4 to C8 in it |
| Product specification | ASTM D7566 Annex A2, HEFA-SPK | | density at 15 °C 730 to 772 kg/m3, D86 10 % at most 205 °C, final boiling point at most 300 °C, T90 - T10 at least 22 K, flash point at least 38 °C, freezing point at most -40 °C |

## Thermodynamics

- **Property package:** Peng-Robinson.
- **Why this package:** hydrogen, CO2 and paraffins from C3 to C17 at up to 9.2 MPa, the classic ground of a cubic equation of state. The oxygenates are only the feed, a liquid that is pumped and heated, and they are gone after R-1.
- **Interaction parameters:** DWSIM's. Its review notes 282 pairs with no kij, mostly hydrogen and CO2 with the paraffins. These set how much CO2 and propane V-1, V-2 and V-3 leave dissolved (part of the CO2 reaches the LPG), not the paraffins' fractionation.
- **Heats of formation corrected** (the results panel's card):
  - **The oil.** In DWSIM, ChemSep's triglycerides, as liquids at 25 °C on Peng-Robinson, are formed with 171 to 209 kJ/mol less heat than NIST's data. Triolein: -2023.1 against -2193.7 kJ/mol. Trilinolein: -1671.0 against -1880.1 kJ/mol.
    - These two come from their measured heats of combustion (Freedman, Bagby et al. 1989).
    - NIST's solid tristearin and tripalmitin, with their heats of fusion, are not consistent with the liquids: tristearin would be formed with less heat than triolein. So tristearin is triolein plus three hydrogenations of oleic to stearic acid, and tripalmitin is tristearin less six CH2, both from NIST's acids. NIST's acids are used directly.
    - `dwsim_api.set_formation_enthalpy` turns each liquid value into the ideal-gas number DWSIM keeps, through the package's own liquid enthalpy, and gives it before the reactions are defined. DWSIM's conversion reactor uses each reaction's heat as it was computed when the reaction was defined.
    - With DWSIM's own data, R-1 would release 1.5 MW more, 6.3 MW where it releases 4.8.
  - **2-methyl C11 to C14.** These are ChEDL Thermo entries, and their heats and Gibbs energies of formation are 0.0. They are given their n-isomer's value plus the 2-methyl increment of DWSIM's own C5 to C10 pairs, -6.9 kJ/mol (Benson's group additivity).
    - Without that, the 52 kmol/h of them that R-2 makes would carry 4.4 MW of formation heat that DWSIM does not see, and R-2 would take in 3.0 MW where it gives out 1.4.
    - Their constants, heat capacities, vapour pressures and densities are present and consistent with the n-isomers'.
- **Water** plays no part: decarboxylation forms none.

## Tuning and convergence notes

- **Why V-3.** DWSIM 10.2.12's rigorous column does not answer with hydrogen in its feed.
  - Fed V-2's liquid let down to 1.0 MPa, with 4.4 % hydrogen and 6.4 % CO2 by mole, the stabiliser ran past every time limit, or stopped on "Failed to fulfill mass balance for Hydrogen". That held on Wang-Henke and Naphtali-Sandholm, and on Peng-Robinson, Grayson-Streed, Chao-Seader and Raoult's law.
  - The oil's compounds made it worse, even at zero flow: without them in the flowsheet, the same column on the same feed solved, in 27 s.
  - A plain paraffin stabiliser with 5 % of hydrogen gave no answer in 300 s, and it solves in under a second without the hydrogen.
  - V-3 flashes the gas off at the column's pressure first. 0.7 % of hydrogen is left, and T-1 solves in 3 s and T-2 in 10 s, with the oil's compounds present. A real stabiliser is fed a degassed liquid too.
- **The columns' specifications** are reflux ratio and the bottoms flow, the pair DWSIM's bubble-point method (Wang-Henke) solves. Each bottoms flow is read off the flowsheet solved up to that column: T-1's bottoms flow is 99.8 % of the C5 and heavier it is fed, and T-2's is its feed less the C4 to C8 in it. So the build solves to V-3, adds T-1 and solves, then adds T-2 and solves.
- **T-1's overhead leaves as vapour** (a full-reflux condenser). The hydrogen and CO2 left cannot condense, and on a total condenser the column runs out the clock.
- **The conversion reactor has two outlets**, vapour and liquid, and both must be connected. The case joins them in a mixer before each cooler. At 400 °C and 9.2 MPa, R-1's effluent is half vapour, half liquid by mass; R-2's is all vapour.
- **The reactions of R-2 run in two ranks:** the cracking (rank 0), then the isomerisation of what it makes (rank 1). Within a rank, DWSIM's conversion reactor meets all the conversions at once with no flow negative. R-2 needs its own hydrogen: in a first try fed only R-1's excess, the cracking ran short of hydrogen and stopped at 98 %.
- **Hydrogen:** R-1's takes 3 per triglyceride to cleave the propane and 3 per double bond; R-2's takes one per molecule cracked. The flowsheet's consumption, fed less what leaves, equals that by hand to the last digit.
- **The SPK's front end** is set by the splitter. T-2 sends 99.9 % of the C4 to C8 it is fed overhead and keeps 99.9 % of the C9 and heavier: 0.07 % of C8 by mass is left in the SPK, whose D86 5 % is 147 °C.
- **Solve:** the flowsheet has no recycle. Up to V-3 it solves in under a second; T-1 adds 3 s and T-2 10 s.

## Results

- **Product yields.** The comparison is against NREL's own model. A gallon here is the product's standard liquid volume at 60 F, from DWSIM's specific gravities of its compounds.
  - The SPK is 2.8 % above NREL's.
  - The propane is 55 % above, and the naphtha 20 % below. These two come from the cracking rule.
    - In NREL's model the cracked C15 goes to "CH4 to C14", and its propane, 18.3 gal/ton, is about the glycerol's alone.
    - Ideal hydrocracking makes no methane or ethane. Its short fragments are C3 and C4, and the propane they make (777 kg/h) joins the glycerol's (1,278 kg/h).
  - By mass: LPG and gas 7.3 %, naphtha 21.1 % and SPK 54.4 % of the oil. The three off-gases carry 22.5 %, most of it CO2. NREL's Fig. 5 gives 4 % propane, 28 % naphtha and 66 % jet of its products.
- **Hydrogen** is checked against the reactions' stoichiometry by hand: 409.4 kg/h in R-1 and 207.7 in R-2.
- **The SPK against ASTM D7566 Annex A2** (limits as Table A2.1 of D7566-24d gives them, reproduced on a producer's public certificate of analysis):
  - The density at 15 °C and the distillation come from DWSIM's Distillation Curves calculation (`dwsim_api.distillation_curves`). The TBP is from the compounds' boiling points and standard volumes; the D86 is from API procedure 3A1.1, with the end point extrapolated.
  - The flash point (API 2B7.1, from the D86 10 %) and the freezing point (API 2B11.1, from gravity and mean boiling point) are correlations for petroleum fractions. Treat them as estimates: the freezing point of a synthetic paraffin depends on its branching, which they do not see.
  - That certificate's commercial HEFA-SPK gives a D86 10 % of 168 °C, a flash point of 41.3 °C and a freezing point of -40.6 °C. Its end point is 291 °C, against this case's 240: here every C15 and C17 is cracked, as NREL assumes, so nothing above C14 reaches the SPK.

| Quantity | DWSIM | Reference | Reference source | Rel. error |
|---|---|---|---|---|
| Jatropha oil, t/h | 29.786 | 29.786 | Tao et al. (2017): 788 dry US t/d | 0.00 % |
| Hydrogen the reactions take, % of the oil | 2.0716 | 2.0716 | stoichiometry, by hand | 0.00 % |
| Propane, gal/dry ton of oil | 28.4 | 18.3 | Tao et al. (2017), NREL, Table 3 | +54.97 % |
| Naphtha, C5-C8, gal/dry ton of oil | 75.3 | 94.2 | Tao et al. (2017), NREL, Table 3 | −20.06 % |
| Jet, the SPK, gal/dry ton of oil | 174.7 | 170.0 | Tao et al. (2017), NREL, Table 3 | +2.76 % |
| SPK density at 15 C, kg/m3 | 746.8 | — | ASTM D7566 A2: 730 to 772 | — |
| SPK D86 10 %, C | 166.7 | — | ASTM D7566 A2: at most 205 C | — |
| SPK D86 final boiling point, C | 239.8 | — | at most 300 C | — |
| SPK D86 90 % less 10 %, K | 66.5 | — | at least 22 K | — |
| SPK flash point, closed cup (API 2B7.1), C | 43.9 | — | at least 38 C | — |
| SPK freezing point (API 2B11.1), C | -44.3 | — | at most -40 C | — |
| R-1, hydrotreating: heat released, MW | 4.832 | — | NIST's heats of formation for the oil | — |
| R-2, hydrocracking and isomerisation: heat released, MW | 1.393 | — | 2-methyl C11-C14 given a heat of formation | — |

## Files

- `sustainable-aviation-fuel-hefa-from-jatropha-oil.dwxmz` - the DWSIM flowsheet, with AI4Tech's title block.
- `sustainable-aviation-fuel-hefa-from-jatropha-oil.png` - the flowsheet as DWSIM draws it, with the three figures and the results panel.

## Confidentiality

Every number comes from public sources:
- an open-access NREL paper (CC BY 4.0);
- an open-access journal;
- a US patent;
- the NIST Chemistry WebBook;
- a public certificate of analysis.

No plant or client data were used, and no client is named. The contributor's contact details are in the flowsheet's title block with the maintainer's agreement. I have the right to publish this case.

## References

- Tao, L., Milbrandt, A., Zhang, Y., Wang, W.-C. (2017). Techno-economic and resource analysis of hydroprocessed renewable jet fuel. *Biotechnology for Biofuels* 10, 261. https://doi.org/10.1186/s13068-017-0945-3 (CC BY 4.0)
- Campuzano-Duque, L. F., Cardeño-López, F. (2020). Fatty acids composition of genotypes of *Jatropha curcas* L., in Colombia. *Agronomía Mesoamericana* 31(1), 95-104. https://doi.org/10.15517/am.v31i1.37574
- Kalnes, T. N. (2015). Hydroprocessing of fats, oils, and waxes to produce low carbon footprint distillate fuels. US Patent 9,039,790.
- Weitkamp, J. (2012). Catalytic hydrocracking - mechanisms and versatility of the process. *ChemCatChem* 4, 292-306.
- NIST Chemistry WebBook, SRD 69, https://webbook.nist.gov:
  - heats of combustion of triolein and trilinolein (Freedman, Bagby et al. 1989);
  - heats of formation of oleic and linoleic acid (Rogers et al. 1978), palmitic acid (Lebedeva 1964, Cox & Pilcher 1970) and stearic acid (Lebedeva 1964);
  - heats of fusion of tristearin and tripalmitin (Domalski & Hearing 1996).
- ASTM D7566-24d, Annex A2, Table A2.1, as reproduced in a HEFA-SPK certificate of analysis, Montana Renewables, 23 September 2024, filed with the Montana Department of Environmental Quality: https://deq.mt.gov/files/Energy/Documents/Public_Comment/MRL/02172025_Submittal/SPK_HEFA_COA_9_23_2024.pdf
- API Technical Data Book, procedures 2B7.1 (flash point), 2B11.1 (freezing point) and 3A1.1 (TBP to ASTM D86), as implemented in DWSIM.
