# Contributing a case

Thank you for sharing your work. A good case here can save another engineer days. This guide keeps submissions consistent and, just as important, safe to publish.

## Before you start: the confidentiality checklist

Go through this before writing anything down. If you cannot tick every box, either anonymize the case or do not submit it.

- [ ] I have the right to publish this process description and data.
- [ ] No confidential plant data is included, or it has been normalized/anonymized so nothing proprietary is exposed.
- [ ] Any comparison against a commercial simulator is allowed by that simulator's license.
- [ ] Site names, company names, and personal data have been removed.
- [ ] I am the author of the DWSIM flowsheet I am attaching, or I have permission to share it.

When in doubt, share the shape of the problem instead of raw numbers: normalized flows, relative errors, and trends still make a case useful without exposing anything.

## What makes a good case

- A clear process description that another engineer can follow.
- The thermodynamic package and the reasoning for it (not just "I used Peng-Robinson").
- Enough operating conditions to reproduce the result.
- Honest tuning and convergence notes, including what did not work.
- Optional but valuable: the `.dwxmz` file, and a comparison against plant or commercial data.

A short, well-documented case beats a large, unexplained one.

## Two ways to submit

### Web form (no git)

Open a **Case submission** issue from the [issue templates](../../issues/new/choose) and fill in the fields. A maintainer will turn it into a case folder and credit you. This is the easiest path if you do not use git.

### Pull request

1. Copy `templates/CASE_TEMPLATE.md` into the right category under `cases/`.
2. Rename the folder using the convention below.
3. Fill in the template. Delete the guidance comments.
4. Add any files (flowsheet, figures) into the same folder.
5. Open a pull request.

## Folder and file naming

- One folder per case, inside the matching category: `cases/<category>/<case-name>/`.
- Case folder name: lowercase, words separated by hyphens, descriptive. Example: `atmospheric-crude-unit-40kbpd`.
- The write-up is always `README.md` inside that folder.
- Flowsheet file: `<case-name>.dwxmz`.
- Figures: put them in the case folder and reference them with relative links. Keep images reasonably sized.

```
cases/
  crude-distillation/
    atmospheric-crude-unit-40kbpd/
      README.md
      atmospheric-crude-unit-40kbpd.dwxmz
      column-profile.png
```

## Categories

Pick the closest fit. If nothing fits, use `other` and suggest a new category in your submission.

- `crude-distillation` - atmospheric and vacuum distillation of crude oil.
- `hydrotreating` - hydrotreating and hydrocracking.
- `gas-processing` - dehydration, sweetening, NGL recovery, LNG.
- `separation-processes` - distillation, absorption, extraction, flash, membranes.
- `reaction-systems` - reactors, kinetics, equilibrium, conversion.
- `heat-integration-utilities` - heat exchanger networks, steam and utility systems.
- `other` - anything else.

## Licensing and consent

By submitting, you agree that:

- Your case write-up (text and figures) is published under [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/), so others can reuse it with attribution.
- Any DWSIM flowsheet file you attach may be downloaded and opened by others for learning.
- You have the right to publish everything in the submission.

See [LICENSE.md](LICENSE.md) for the full statement.

## Review and verification

1. A maintainer checks the submission for completeness and for the confidentiality checklist.
2. It is published as a **community** case.
3. If a maintainer or a second contributor reproduces it (the flowsheet opens, solves, and matches the reported results), it is promoted to **verified** and gets the badge.

You can help by verifying someone else's case: open the flowsheet, run it, and comment on the case's issue or PR with what you found.

## Style

- Write in English so the library stays usable worldwide. A second language version of a case is welcome as an extra file.
- Use SI units, and state the unit system if you deviate.
- Prefer plain, specific language. "The reboiler duty had to be raised about 8% over the design value to hit the bottoms spec" is more useful than "it was hard to converge".
