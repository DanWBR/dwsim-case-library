# Benzene-toluene column in dynamics: level and pressure control riding a feed step

**Category:** separation-processes
**Status:** community
**DWSIM version:** 10.2.9
**Language:** English
**Contributor:** Daniel Medeiros (built with the DWSIM fluent API, script in the DWSIM repository)

## Summary

A 16-stage benzene-toluene column is run in dynamic mode with tray hydraulics from the column
internals rating, a level controller on the reflux drum acting on the distillate valve, a level
controller on the sump acting on the bottoms valve, and a pressure controller acting on the
condenser duty. The feed is stepped up by 10 % at 10 min and back at 40 min. The run shows how
the tray levels, the column pressure drop, the temperature profile and the product purities move
and how the three controllers bring the levels and the pressure back. The flowsheet opens with the
schedule configured: press play on "Feed step run".

## Process description

The feed, 100 mol/s of an equimolar benzene-toluene mixture at 95 °C and 1.5 bar, enters stage 8
of a 16-stage column (condenser stage 1, reboiler stage 16). The steady state is solved with a
reflux ratio of 2.5 and a bottoms rate of 50 mol/s, top pressure 1.2 bar and 10 kPa of column
pressure drop, which gives about 98 % benzene in the distillate and 98 % toluene in the bottoms.

For the dynamic run the column carries the hydraulics of sieve trays sized by the column internals
tool at 75 % of flood: 2.58 m diameter, 0.5 m tray spacing, 12 % downcomers (weir 1.88 m), 50 mm
weirs and 10 % hole area. The condenser stage doubles as the reflux drum (2 m of vessel) and its
liquid leaves through a short reflux line rather than a weir (a 1 m dead height plus a 0.05 m
outlet), which holds about 0.75 m of liquid at the design reflux and makes the reflux a gentle
function of the drum level. The reboiler stage doubles as the sump (2 m of vessel below the last tray) and starts half full (1 m). The dry tray coefficients are calibrated at initialisation so the steady-state
vapour rate crosses each tray at the steady-state pressure drop.

Products leave through valves in Kv mode (Kv 150, about a third open at the design rate) into 0.9 bar
boundaries. Three PID controllers close the loops:

| Controller | Measures | Moves | Tuning (Kp, Ki) |
|---|---|---|---|
| LC-01 | reflux drum level (stage 1) | distillate valve LV-01 | 1.5, 0.01 |
| LC-02 | sump level | bottoms valve LV-02 | 2.0, 0.02 |
| PC-01 | top pressure (stage 1) | condenser duty | 2.0, 0.02 |

The reboiler duty is held at its steady-state value. A chart object on the PFD shows the variables
monitored by the integrator, a second one the column temperature profile, and a property table
and a master table list the column and stream results.

## Feed and operating conditions

| Item | Value | Unit | Notes |
|---|---|---|---|
| Feed flow | 100 | mol/s | 8.51 kg/s, stepped to 9.36 kg/s at 600 s and back at 2400 s |
| Feed composition | 50 / 50 | mol % | benzene / toluene |
| Feed temperature | 95 | °C | sub-cooled liquid at 1.5 bar |
| Top pressure | 120 | kPa | 10 kPa column pressure drop |
| Reflux ratio | 2.5 | | steady-state specification |
| Bottoms rate | 50 | mol/s | steady-state specification |
| Condenser / reboiler duty | 5285 / 5428 | kW | steady state |
| Integration | 2 s steps, 2 sub-steps | | 1 h of simulated time in about 17 min |

## Thermodynamics

- **Property package:** Peng-Robinson
- **Why this package:** two non-polar aromatics near atmospheric pressure; a cubic equation of
  state reproduces the vapour-liquid equilibrium well and its flashes are fast, which matters in a
  run with tens of thousands of stage flashes.
- **Interaction parameters / assays:** the built-in binary.

## Tuning and convergence notes

- The dynamic column runs with the quasi-steady vapour option: each tray keeps only the vapour
  its free volume holds and passes the rest up within the step; the stage pressures follow the
  tray hydraulics from the drum downward; the drum pressure is the bubble pressure of its liquid.
  Without it (the pressure-driven vapour holdup on every tray) the vapour balance has a time
  constant of milliseconds and no practical step is stable.
- Initialisation matters: the trays start at the level that passes the steady-state liquid rate
  over the weir, the sump half full, and the tray coefficients calibrated to the steady-state
  pressure profile (column dynamic properties "Calibrate Tray Coefficients" and "Quasi-Steady
  Vapor", both on in the file).
- The pressure controller is the sensitive loop: the drum answers the condenser duty within
  seconds, so a gain of 20 on the normalised error drove the duty between its limits; 2 holds
  the pressure within a few kilopascals through the feed step, outside the burst episode.
- The reflux is not controlled: it is what the drum outlet passes at the drum level, so the reflux
  rises with the drum level and the distillate valve takes the balance. With a full-width weir on
  the drum the reflux was a cliff function of the level and a 2 % level dip stopped it. Product purities drift
  with the feed rate because nothing controls composition.
- Sub-steps of 1 s are enough once the vapour is quasi-steady; the liquid time constant of a
  tray is about 8 s.

## Results

The run integrates one hour in about seventeen minutes of wall time (2 s steps, 1 s sub-steps, 17
stage holdups flashed per sub-step). The first two minutes are the settling of the seeded initial
state (the pressure rises to 131 kPa before the pressure controller catches it). From then on:

| Quantity | DWSIM | Notes |
|---|---|---|
| Top pressure, whole hour after the first 2 min | 108.5 to 125.0 kPa | setpoint 120.0 kPa; the excursions are one episode of vapour bursts between 8 and 12 min around the feed step, 118 to 123 kPa otherwise |
| Column pressure drop | 3.0 to 19.1 kPa in that episode, 10 kPa otherwise | 10 kPa at steady state |
| Sump level during the step | 0.998 to 1.046 m | setpoint 1.000 m |
| Bottoms valve during the step | 31 to 39 % | 32 % at design (against a 0.9 bar boundary) |
| Bottoms flow, peak during the step | 5.39 kg/s | 4.59 kg/s at design |
| Reflux drum level | 0.728 to 0.755 m | setpoint 0.755 m |
| Condenser duty | 4096 to 5478 kW | 5285 kW at design |
| Feed tray temperature | 99.9 to 104.8 °C | 100.3 °C at design |
| Toluene in bottoms, lowest | 0.9730 at 40 min | 0.9794 at design; no composition control |
| Benzene in distillate, highest | 0.9780 | 0.9793 at design |
| End of the hour: sump level, top pressure, bottoms flow | 1.000 m, 120.0 kPa, 4.43 kg/s | levels and pressure back on setpoint |

What to look at: the sump level and the bottoms valve carry the feed step (a 10 % feed increase with the
reboiler duty fixed leaves the column as extra bottoms), the pressure controller holds the top within a
few kilopascals by trimming the condenser duty, the temperature profile slides a few degrees while the
extra liquid runs through, and the bottoms toluene purity falls by half a point because nothing controls
composition; it recovers once the feed returns. The vapour to the condenser comes in bursts for a few
minutes around the feed step (the quasi-steady vapour at a pressure transient), which is what the pressure
excursion is; it dies out on its own. No comparison against plant or another simulator: the case is a
model exercise, and the point is the behaviour of the loops, not the numbers.

![Response to the feed step](feed-step-response.png)

## Files

- `benzene-toluene-column-dynamics.dwxmz` - the flowsheet, steady state solved, dynamics schedule
  "Feed step run" configured with the integrator, the event set and the monitored variables.
- `benzene-toluene-column-dynamics.png` - the PFD.
- `feed-step-response.png` - the monitored variables over the hour.
- `feed-step-run.csv` - the monitored variables, one row per integration step.

## Confidentiality

Nothing to anonymise: an academic mixture and made-up operating conditions.

## References

- Skogestad, S., "Dynamics and control of distillation columns: a tutorial introduction",
  Trans IChemE 75A (1997) 539-562, for the quasi-steady vapour and the level/pressure loop
  structure.
- Kister, H. Z., Distillation Design, McGraw-Hill (1992), for the tray hydraulics.
