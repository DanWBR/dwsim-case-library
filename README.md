# DWSIM Case Library

A community collection of real industrial process cases modeled in [DWSIM](https://dwsim.org): crude distillation, hydrotreating, gas processing, separation and reaction systems, and more. Each case documents the process, the thermodynamic choices, the tuning and convergence tips, and, where allowed, a comparison against plant or commercial-software data and the DWSIM flowsheet file itself.

The goal is simple: shorten the learning curve for new users and show what DWSIM can do on industrial problems, using examples contributed by engineers who actually run these processes.

## What belongs here

- Process cases with enough context that another engineer can reproduce them.
- Thermodynamic package choices and the reasoning behind them.
- Practical tuning and convergence notes (initial estimates, solver settings, what to watch out for).
- Optional: the DWSIM flowsheet file (`.dwxmz`).
- Optional: a comparison of DWSIM results against plant data or another simulator, **only when you are allowed to publish that comparison** (see [Confidentiality and licensing](#confidentiality-and-licensing)).

## What does not belong here

- Confidential or proprietary plant data you do not have the right to publish.
- Benchmark comparisons that a commercial tool's license forbids you from publishing.
- Personal data of any kind.
- Support questions. Use the [DWSIM forums](https://sourceforge.net/p/dwsim/discussion/) or [Discussions](https://github.com/DanWBR/dwsim10/discussions) for those.

## Browse the cases

| Category | Folder | Examples |
|---|---|---|
| Crude and vacuum distillation | [`cases/crude-distillation`](cases/crude-distillation) | atmospheric crude unit, vacuum tower |
| Hydrotreating and hydrocracking | [`cases/hydrotreating`](cases/hydrotreating) | diesel HDS, naphtha hydrotreater |
| Gas processing | [`cases/gas-processing`](cases/gas-processing) | dehydration, amine sweetening, NGL recovery |
| Separation processes | [`cases/separation-processes`](cases/separation-processes) | distillation, absorption, extraction |
| Reaction systems | [`cases/reaction-systems`](cases/reaction-systems) | reactors, kinetics, equilibrium |
| Heat integration and utilities | [`cases/heat-integration-utilities`](cases/heat-integration-utilities) | heat exchanger networks, steam systems |
| Other processes | [`cases/other`](cases/other) | anything that does not fit above |

Each case is a folder with a `README.md` built from the [case template](templates/CASE_TEMPLATE.md), plus any files it needs.

## Contribute a case

Two ways, pick whichever you are comfortable with:

1. **Web form (no git required).** Open a [Case submission](../../issues/new?template=case-submission.yml) issue and fill in the fields. A maintainer turns it into a case folder.
2. **Pull request.** Copy [`templates/CASE_TEMPLATE.md`](templates/CASE_TEMPLATE.md) into the right category folder, fill it in, add your files, and open a PR.

Read [CONTRIBUTING.md](CONTRIBUTING.md) first. It covers the confidentiality checklist, the template fields, naming, and how cases get reviewed.

## Verified vs community cases

- **Community** cases are published as submitted. They are useful but have not been independently checked.
- **Verified** cases have been reproduced by a maintainer or a second contributor: the flowsheet opens, solves, and matches the reported results. Verified cases carry a badge and are listed first in each category.

Verification criteria are in [VERIFICATION.md](VERIFICATION.md).

## Confidentiality and licensing

This matters, please read it before submitting.

- **Only publish what you are allowed to publish.** Real plant data is usually confidential. If you cannot share absolute values, share the shape of the problem: normalized flows, relative errors, trends. Anonymize stream names, site names, and any identifying detail.
- **Commercial-software comparisons.** Some simulator licenses restrict publishing benchmark comparisons. Check your license before posting Aspen, HYSYS, PRO/II, or similar comparison numbers. When in doubt, describe the agreement qualitatively rather than posting the competitor's raw output.
- **License of what you submit.** Case write-ups (the text and figures) are published under [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/). DWSIM flowsheet files you attach are shared for others to open and learn from. By submitting, you confirm you have the right to publish the material and agree to these terms. See [LICENSE.md](LICENSE.md).

## Relationship to FOSSEE

The [FOSSEE DWSIM flowsheeting project](https://dwsim.fossee.in/) already hosts a large set of user-contributed DWSIM flowsheets with reports, and is a great place to look and to contribute. This library is complementary: it focuses on industrial cases with tuning notes and, where possible, comparisons against real or commercial data. If your case fits FOSSEE better, contribute it there too.

## Disclaimer

The cases here are provided as-is by their contributors, for education and reference. They are not validated engineering deliverables. Do not use them for design, safety, or operational decisions without independent verification.
