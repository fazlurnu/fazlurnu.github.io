# TODO — CO2 Calculation (3 methods)

Goal: estimate flight CO2 emissions using three independent methods, then
compare them (likely as an interactive blog post / widget).

## Flight app integration
- [ ] Replace the current trajectory-only Flask app (`flight-app/`) with a
      CO2 emission calculator: takes the same CSV input, runs LightGBM model
      + OpenAP, plots trajectory coloured by emission rate and shows total CO2.
      See `flight-app/my-first-cloud-app.md` for full deployment instructions.

## Method 1 — LightGBM model (own)
Source: https://github.com/PRC-Data-Challenge-2025/resourceful-quiver/tree/main/models

- [ ] Identify the trained model artifact(s) in the repo and their format
      (e.g. `.txt` / `.pkl` / booster dump).
- [ ] Document required input features and their units / preprocessing.
- [ ] Decide how to run inference in the browser vs. precompute
      (Pyodide + lightgbm? export to a lighter format? server-side?).
- [ ] Define the prediction target (CO2 per flight? per km? fuel burn → CO2?).

## Method 2 — OpenAP
Source: https://github.com/junzis/openap

- [ ] Confirm OpenAP install path (pip package, runs under Pyodide?).
- [ ] Map inputs: aircraft type, distance/trajectory, mass assumptions.
- [ ] Compute fuel burn → CO2 (fuel × 3.16 kg CO2/kg fuel).
- [ ] Note coverage limits (which aircraft types are supported).

## Method 3 — myclimate flight emission calculator
Source: https://www.myclimate.org/en/information/about-myclimate/downloads/flight-emission-calculator/

- [ ] Download the calculator spreadsheet / methodology PDF.
- [ ] Extract the formula and coefficients (distance bands, cabin class,
      RFI / radiative forcing factor, detour & holding constants).
- [ ] Reimplement the formula (likely a closed-form equation of distance).

## Cross-cutting
- [ ] Agree on a common input interface (origin/dest or distance, aircraft, etc.).
- [ ] Agree on common output units (kg CO2 total / per passenger).
- [ ] Build comparison view (table + chart of the three estimates).
- [ ] Decide delivery: interactive widget (Pyodide) vs. precomputed results.
- [ ] Write up assumptions and caveats for the blog post.

## Open questions (discuss)
- Per-flight or per-passenger basis?
- Single example route or user-adjustable inputs?
- Where does method 1's feature set come from at inference time?
