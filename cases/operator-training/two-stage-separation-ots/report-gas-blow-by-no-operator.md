# Operator training exercise report

- Scenario: 3. Gas blow-by
- Flowsheet: OTS two-stage separation
- Date: 2026-09-19 18:33
- Simulated duration: 00:40:00 (480 steps)
- Score: **25 / 70** (36%)

## Objectives

| Objective | What | Result | Points | Detail |
|---|---|---|---:|---|
| No HH pressure in V-200 | avoid PIT-200 HH alarm | Passed | 25 / 25 | never happened |
| No low level trip | avoid interlock 'V-100 low level trip' tripped | Failed | 0 / 15 | interlock 'V-100 low level trip' tripped happened at 00:06:30 |
| Take LIC-100 to manual | operator does 'LIC-100 mode -> MANUAL' within 420 s | Failed | 0 / 10 | no matching action before 00:07:00 |
| Hold the HP level | keep LIT-100.Monitored Value in [0.7, 1.8] for 70% of the time | Failed | 0 / 20 | 27.1% of the time inside the range (required 70%), 20 points lost |

## Counts

- Operator actions: 0
- Alarms raised: 7
- Interlock trips: 1
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
| 00:04:40 | Alarm | LIT-100 L alarm ACTIVE (value 0.69028 m) |
| 00:06:25 | Alarm | LIT-100 LL alarm ACTIVE (value 0.3925 m) |
| 00:06:30 | Trip | INTERLOCK 'V-100 low level trip' TRIPPED, first out: LIT-100 LL alarm; CloseValve LV-100, LIC-100 to MANUAL, output 0 |
| 00:06:30 | Session | Objective 'No low level trip' FAILED: interlock 'V-100 low level trip' tripped happened at 00:06:30 |
| 00:07:00 | Alarm | LIT-100 LL alarm cleared (value 0.41176 m) |
| 00:07:05 | Session | Objective 'Take LIC-100 to manual' FAILED: no matching action before 00:07:00 |
| 00:08:40 | Alarm | LIT-100 L alarm cleared (value 0.70999 m) |
| 00:14:55 | Alarm | LIT-100 H alarm ACTIVE (value 1.8149 m) |
| 00:17:05 | Alarm | LIT-100 HH alarm ACTIVE (value 2.2043 m) |
| 00:27:05 | Alarm | PIT-100 H alarm ACTIVE (value 36.686 bar) |
| 00:27:10 | Alarm | PIT-100 H alarm cleared (value 33.534 bar) |
| 00:40:00 | Instructor | Frozen at 00:40:00 |
| 00:40:00 | Session | Objective 'No HH pressure in V-200' PASSED: never happened |
| 00:40:00 | Session | Objective 'Hold the HP level' FAILED: 27.1% of the time inside the range (required 70%), 20 points lost |
| 00:40:00 | Session | Exercise ended: score 25 of 70 |
