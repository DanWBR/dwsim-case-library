# Gas-liquid separator: the training plant of the OTS course

**Category:** operator-training
**Status:** community
**DWSIM version:** 10.2.9
**Language:** English
**Contributor:** Daniel Medeiros

> **Requirement.** The training features (Instructor Station, scenarios, interlocks, operator screens) belong to the Operator Training Simulator extender of DWSIM Patreon level 3, Classic interface on Windows. The flowsheet itself, with its dynamics schedule, controllers and gauges, opens and runs in any DWSIM 10.2.9 or later; the scenarios, interlocks and screens travel inside the file and are simply ignored where the extender is not present. The course that goes with these plants is at [dwsim.org/tutorials](https://dwsim.org/tutorials), section Operator Training.

## Summary

A one-cubic-metre gas-liquid separator with a pressure loop and a level loop, in dynamic mode, carrying the
first training exercise of the Operator Training Simulator course: a feed valve that fails open at one minute,
scored on four objectives, with a high-pressure trip and two operator screens. It is the plant the course builds
page by page (pages 1 to 12), saved at the end of page 8. The pressure controller copes with the failed valve on
its own (70 of 80 points with nobody at the panel); the file is there to learn the mechanics of scenarios,
scoring, alarms, trips and screens on a plant small enough to read at a glance. Closing the vent by hand shows the
other side: H at 02:25, HH at 02:45, trip at 02:50.

## Process description

A two-phase feed (air, carbon dioxide, water and methanol at about 274 K) comes from a 5 bar header through the
feed valve **FV-001** into the separator **SG-01** (1 m³, 2 m tall). The gas leaves through **PV-001** and the
liquid through **LV-001**, both to atmospheric headers. **PID-012** holds the separator at 2 bar on PV-001 and
**PID-013** holds the level at 0.3 m on LV-001; both are reverse acting (an outlet valve opens when its variable
is above the set point). The transmitter **XT-001** duplicates the pressure measurement for the sensor-failure
lessons.

![The separator in dynamic mode](gas-liquid-separator-ots.png)

| Tag | Object | Role |
|---|---|---|
| 1 | Material stream | Feed header at 5 bar, pressure-specified |
| FV-001 | Valve, Kv (general) | Feed valve, Kv 2.7, 50 % open; about 0.08 kg/s |
| SG-01 | Gas-liquid separator | 1 m³, 2 m tall |
| PV-001, LV-001 | Valves, Kv (gas, liquid) | Gas and liquid outlets to 1 atm |
| PID-012 | PID controller | Pressure, set point 2 bar, on PV-001 |
| PID-013 | PID controller | Level, set point 0.3 m, on LV-001 |
| PIT-001 | Analog gauge | Pressure in kPa; alarms LL 100, L 150, H 400, HH 450 |
| LIT-001 | Level gauge | Level in m; alarms LL 0.15, L 0.25, H 0.4, HH 0.5 |
| XT-001 | Transmitter | Pressure, for the sensor-failure lessons |
| FI-001, FI-002, FI-003 | Digital gauges | Feed, gas and liquid flows in kg/h |

Dynamics: schedule `schedule1`, integrator `1`, 5 s step, initial state `a` (the plant settled at 2 bar and
0.3 m), historian on.

## Feed and operating conditions

| Item | Value | Unit | Notes |
|---|---|---|---|
| Feed header pressure | 5 | bar | pressure-specified stream; the flow follows FV-001 |
| Feed flow at 50 % | about 0.08 | kg/s | air, CO2, water, methanol, two-phase at about 274 K |
| Separator pressure | 2 | bar | PID-012 set point |
| Liquid level | 0.3 | m | PID-013 set point |
| Vessel | 1 m³, 2 m | | |

## Training content

**Scenario "Feed valve fails open"** (speed 10x, initial state `a`, schedule `schedule1`): `ValveFailOpen` on
FV-001, severity 1, ramp 20 s, at 60 s. The trainee is told "shift handover: FV-001 positioner reported erratic;
keep the separator inside limits".

| Objective | Kind | Condition | Deadline | Points |
|---|---|---|---|---|
| Hold the pressure | KeepInRange | PIT-001 in 150 to 400 kPa for 90 % of the time | | 30 (0.1 per second outside) |
| No HH pressure | Avoid | PIT-001 HH alarm | | 20 |
| Take PID-012 to manual | OperatorAction | journal line "PID-012 mode -> MANUAL" | 240 s | 10 |
| Pressure back to 2 bar | Reach | PIT-001 below 250 kPa for 30 s | 600 s | 20 |

**Interlock "High pressure trip"**: PIT-001 HH for 5 s closes FV-001 (stem locked until reset) and hands
PID-012 to manual at 100 % (vent open).

**Screens**: "Overview" (symbols, pipes coloured by phase, ISA bubbles, trend) and "Separator detail".

## Thermodynamics

- **Property package:** Raoult's law
- **Why this package:** a made-up mixture at 2 bar chosen for the dynamics, where the point is the pressure and
  level response and the flash has to be fast; nothing in the exercise depends on the vapour-liquid equilibrium
  being accurate.

## Tuning and convergence notes

- The feed is pressure-specified so that a valve fault changes the flow; a flow-specified feed makes a failed-open
  feed valve invisible.
- Both controllers are reverse acting. The direct-acting original (vent closing as the pressure rose) ran away in
  the first minute.
- The stored state `a` is the plant settled under the controllers; `UseCurrentStateAsInitial` is off on the
  schedule, otherwise the restore is skipped and every run starts where the last one ended.
- Kv sizing: the steady state does not size the valves; the Kv values were set so each valve sits near 50 %
  open at the design flow.

## Results

Measured by running the scenario headlessly, 15 minutes of simulated time, three ways:

| Operator | What happens | Score |
|---|---|---|
| Nobody | FV-001 fails open from 01:00; PID-012 opens PV-001 and holds 2 bar; no alarm at all | 70 / 80 (only "Take PID-012 to manual" is missed) |
| Manual at 01:30, vent to 100 % | pressure falls to the L alarm (122 kPa) and stays there; level H at 13:35 | 50 / 80 |
| Manual at 01:30, vent to 0 % (the page 7 experiment) | H at 02:25, HH at 02:45, trip at 02:50 (FV-001 closed, PID-012 handed back at 100 %); then pressure L, level L at 04:00 and LL at 06:35 | 30 / 80 |

The lesson the course draws from it: the plant is safe in automatic, the interlock does its job when the
operator makes it worse, and every one of those lines is in the journal and the report. The two-stage plant is
where the faults need an operator.

## Files

- `gas-liquid-separator-ots.dwxmz` - the flowsheet with the schedule, the stored state, the scenario, the
  interlock and the two screens.
- `gas-liquid-separator-ots.png` - the flowsheet in dynamic mode.

## Confidentiality

Nothing to anonymise: a made-up plant.

## References

- DWSIM tutorials, Operator Training section, pages 1 to 12 (the course that builds this file).
- ISA-18.2, Management of Alarm Systems for the Process Industries, for the alarm lifecycle the OTS follows.
