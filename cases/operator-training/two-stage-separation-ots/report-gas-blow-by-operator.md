# Operator training exercise report

- Scenario: 3. Gas blow-by
- Flowsheet: OTS two-stage separation
- Date: 2026-09-19 18:35
- Simulated duration: 00:40:00 (480 steps)
- Score: **70 / 70** (100%)

## Objectives

| Objective | What | Result | Points | Detail |
|---|---|---|---:|---|
| No HH pressure in V-200 | avoid PIT-200 HH alarm | Passed | 25 / 25 | never happened |
| No low level trip | avoid interlock 'V-100 low level trip' tripped | Passed | 15 / 15 | never happened |
| Take LIC-100 to manual | operator does 'LIC-100 mode -> MANUAL' within 420 s | Passed | 10 / 10 | 'LIC-100 mode -> MANUAL' at 00:04:00 |
| Hold the HP level | keep LIT-100.Monitored Value in [0.7, 1.8] for 70% of the time | Passed | 20 / 20 | 100% of the time inside the range (required 70%) |

## Counts

- Operator actions: 3
- Alarms raised: 2
- Interlock trips: 0
- Malfunctions injected: 1
- Steps that failed to solve: 0

## Timeline

| Sim. time | Category | Event |
|---|---|---|
| 00:00:00 | Instructor | Scenario '3. Gas blow-by' loaded (1 scheduled faults) |
| 00:00:00 | Session | Pressure-flow network: 0 junction(s) to solve, 0 valve(s) attached |
| 00:00:00 | Session | Session started with scenario '3. Gas blow-by', speed 20x |
| 00:01:30 | Malfunction | ACTIVATED Sensor failure (FullScale) on LT-100 (severity 1) |
| 00:01:30 | Alarm | LT-100 H alarm ACTIVE (value 3 m) |
| 00:01:30 | Alarm | LT-100 HH alarm ACTIVE (value 3 m) |
| 00:04:00 | Operator | LIC-100 mode -> MANUAL |
| 00:04:00 | Operator | LIC-100 manual output -> 20  |
| 00:04:05 | Session | Objective 'Take LIC-100 to manual' PASSED: 'LIC-100 mode -> MANUAL' at 00:04:00 |
| 00:10:00 | Operator | LIC-100 manual output -> 50  |
| 00:40:00 | Instructor | Frozen at 00:40:00 |
| 00:40:00 | Session | Objective 'No HH pressure in V-200' PASSED: never happened |
| 00:40:00 | Session | Objective 'No low level trip' PASSED: never happened |
| 00:40:00 | Session | Objective 'Hold the HP level' PASSED: 100% of the time inside the range (required 70%) |
| 00:40:00 | Session | Exercise ended: score 70 of 70 |
