# Race Weekend Workspace Templates

This directory provides standardized templates for analyzing a Formula 1 Grand Prix weekend.

---

## 🚀 How to Start a New Grand Prix Analysis

1. **Create the Race Directory**:
   Follow the naming convention `YYYY_RXX_GrandPrixName_GP`:
   ```bash
   mkdir -p 2026_R12_Dutch_GP/{data,notebooks,plots,reports}
   ```

2. **Copy the Notebook Templates**:
   ```bash
   cp templates/*.ipynb 2026_R12_Dutch_GP/notebooks/
   ```

3. **Copy the Report Template**:
   ```bash
   cp templates/report_template.md 2026_R12_Dutch_GP/reports/Master_Report.md
   ```

4. **Run the Notebooks in Sequence**:
   - `01_results_and_laps.ipynb`:
     - Loads Qualifying & Race results.
     - Saves clean CSVs to `data/`.
     - Automatically runs `find_top_battles()` and saves detected contenders to `data/battles.json`.
     - Saves race progression plots to `plots/`.
   - `02_telemetry_analysis.ipynb`:
     - Reads `data/battles.json`.
     - Generates distance vs Speed, Brake, Throttle, Gear, and RPM plots.
     - Saves comparison charts directly into `plots/`.
   - `03_tyre_and_stint_analysis.ipynb`:
     - Calculates grid-wide stint counts and pit stops (`data/Race_Stint_Summary.csv`).
     - Evaluates compound breakdown and tyre degradation slopes.
     - Saves tyre degradation plots to `plots/`.

5. **Finalize the Master Report**:
   - Open `reports/Master_Report.md`.
   - Embed the generated tables from `data/` and plots from `plots/`.
   - Write your strategic race conclusions and insights!
