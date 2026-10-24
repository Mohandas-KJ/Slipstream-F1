<div align="center">

```
 ███████╗██╗     ██╗██████╗ ███████╗████████╗██████╗ ███████╗ █████╗ ███╗   ███╗
 ██╔════╝██║     ██║██╔══██╗██╔════╝╚══██╔══╝██╔══██╗██╔════╝██╔══██╗████╗ ████║
 ███████╗██║     ██║██████╔╝███████╗   ██║   ██████╔╝█████╗  ███████║██╔████╔██║
 ╚════██║██║     ██║██╔═══╝ ╚════██║   ██║   ██╔══██╗██╔══╝  ██╔══██║██║╚██╔╝██║
 ███████║███████╗██║██║     ███████║   ██║   ██║  ██║███████╗██║  ██║██║ ╚═╝ ██║
 ╚══════╝╚══════╝╚═╝╚═╝     ╚══════╝   ╚═╝   ╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝╚═╝     ╚═╝
```

### F1 Data Analytics & Race Intelligence Lab

*"Don't just watch the race. Understand it through data."*

![Python](https://img.shields.io/badge/Python-3.11+-00d4ff?style=for-the-badge&logo=python&logoColor=white)
![FastF1](https://img.shields.io/badge/FastF1-Telemetry-f472b6?style=for-the-badge&logo=formula1&logoColor=white)
![Pandas](https://img.shields.io/badge/Pandas-Data_Analysis-a855f7?style=for-the-badge&logo=pandas&logoColor=white)
![Matplotlib](https://img.shields.io/badge/Matplotlib-Visualization-fbbf24?style=for-the-badge&logo=plotly&logoColor=black)
![Status](https://img.shields.io/badge/Status-Active_%26_Evolving-00ff88?style=for-the-badge)

</div>

---

## `$ cat about.md`

**Slipstream F1** is a long-term Formula 1 data analytics and race intelligence project built using **Python** and **FastF1**.

The project was created to learn and apply real-world data analysis, statistics, visualization, and engineering concepts through one of the most data-rich sports in the world: Formula 1.

Unlike traditional tutorial-based learning, Slipstream F1 follows a **hands-on approach**. Every Grand Prix becomes a mini data science project — historical race data, telemetry, qualifying results, race pace, tire strategies, weather conditions, and driver performance are analyzed to uncover insights and improve understanding of race engineering.

The project is structured around individual Formula 1 race weekends. Each Grand Prix has its own workspace containing notebooks, visualizations, reports, and analyses. Historical race data is used to understand track characteristics, team strengths, tire behavior, and driver performance patterns.

The long-term goal is to evolve beyond descriptive analysis and move toward **predictive analytics** — generating data-driven predictions for upcoming races, including qualifying performance, race pace, strategy choices, podium contenders, and race outcomes.

---

## `$ cat goals.txt`

This project exists to:

- 🐍 Learn practical data analysis using real-world datasets
- 📊 Develop proficiency in **Python**, **Pandas**, **Matplotlib**, and **FastF1**
- 🏎️ Understand Formula 1 telemetry, strategy, and race engineering concepts
- 💼 Build a public portfolio demonstrating analytical and technical skills
- 🔮 Explore predictive modeling using historical motorsport data
- 📅 Document and analyze an entire Formula 1 season through data

---

## `$ ./race_weekend_workflow.sh`

Each race weekend follows a structured, repeatable workflow:

| Step | Stage | What happens |
|---|---|---|
| 01 | **Historical Analysis** | Analyze previous editions of the same Grand Prix; study team performance trends and track characteristics |
| 02 | **Session Analysis** | Examine qualifying and race results; investigate lap times, sector performance, and consistency |
| 03 | **Telemetry Analysis** | Compare drivers using speed, throttle, brake, gear, and DRS data; identify where lap time is gained or lost |
| 04 | **Strategy Analysis** | Evaluate tire choices, degradation, pit stops, and race strategy |
| 05 | **Visualization & Reporting** | Transform raw data into meaningful charts and reports |
| 06 | **Prediction & Evaluation** | Generate race predictions using historical insights; compare against actual outcomes and refine future models |

---

## `$ ls -la`

Each Grand Prix has its own dedicated workspace with data, notebooks, plots, and reports:

```
slipstream-f1/
├── Sliplib/                          # Reusable analytics, algorithms & visualization library
│   ├── slipload.py                   # Session loader & robust cache management
│   ├── selection.py                  # Lap, driver & telemetry extraction
│   ├── battle_finder.py              # Automated weighted battle detection algorithm
│   ├── Gotyres.py                    # Tyre stint analysis
│   ├── GridSum.py                    # Grid position gain & stint summaries
│   ├── plotting.py                   # Matplotlib chart helpers (auto-save enabled)
│   └── dashboard.py                  # F1 dark-theme telemetry dashboard
├── templates/                        # Master templates for new race weekends
│   ├── 01_results_and_laps.ipynb
│   ├── 02_telemetry_analysis.ipynb
│   ├── 03_tyre_and_stint_analysis.ipynb
│   ├── report_template.md
│   └── README.md
├── 2026_R8_Austria_GP/               # Example Race Weekend Workspace
│   ├── data/                         # Exported CSVs & local battles.json
│   ├── notebooks/                    # Sequential analysis notebooks
│   ├── plots/                        # Generated PNG charts
│   └── reports/                      # Master_Report.md
└── README.md
```

### 📂 Race weekends

| Grand Prix | Status | Workspace |
|---|---|---|
| 🇪🇸 Spanish GP (Barcelona) | ✅ Analyzed | [`2026_R8_Barcelona_GP/`](./2026_R8_Barcelona_GP) |
| 🇦🇹 Austrian GP (Spielberg) | ✅ Master Report | [`2026_R8_Austria_GP/`](./2026_R8_Austria_GP) |
| 🇬🇧 British GP (Silverstone) | 🚧 In progress | [`2026_R9_British_GP/`](./2026_R9_British_GP) |
| 🇧🇪 Belgian GP (Spa) | 🚧 In progress | [`2026_R10_Belgian_GP/`](./2026_R10_Belgian_GP) |
| 🇭🇺 Hungarian GP (Hungaroring) | ✅ Analyzed | [`2026_R11_Hungary_GP/`](./2026_R11_Hungary_GP) |

---

## `$ cat philosophy.md`

> Slipstream F1 is **not** a collection of notebooks or tutorials.
>
> It is a continuously evolving Formula 1 analytics laboratory — where every race weekend becomes an opportunity to ask questions, investigate data, test hypotheses, and improve analytical thinking.

---

<div align="center">

```
~/slipstream-f1 $ █
```

**Don't just watch the race. Understand it through data.**

</div>
