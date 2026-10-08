# VCT Agent Strengths for Coaches

**Correlation One capstone project**

Project code is released under the MIT License. The Kaggle dataset is separate and remains subject to its own license and terms; see the source listing before downloading or redistributing it.

A coach-facing exploration of Valorant Champions Tour agent picks across maps and years. The notebooks and trend script use pick patterns and observed team/map outcomes to present possible discussion points about agent selection and composition.

Here, "strength" means an observed pattern in the available tournament data, not an inherent character quality or a proven causal effect. This is an exploratory demonstration, not a validated ranking or prediction system.

## Project contents

- `agent_pick_rate_trends.py` - plots agent and role pick-rate trends by map and year.
- `Download_VCT_Data.ipynb` - downloads the latest public source data and copies it into the expected local folder.
- `vct-2024-agent-composition-analysis.ipynb` and `vct-2024-agent-composition-analysis2.ipynb` - exploratory summaries and visualizations of agent picks and team/map outcomes.
- `Clean_Agent_Composition_With_Summary.ipynb` and `Clean_Agent_Composition_By_Year(1).ipynb` - notebooks for preparing yearly data and producing summaries.
- `cleaned_data/` - prepared yearly and combined CSV files.

## Data and limitations

The source is the public [Valorant Champions Tour 2021-2023 dataset on Kaggle](https://www.kaggle.com/datasets/ryanluong1/valorant-champion-tour-2021-2023-data). Run `Download_VCT_Data.ipynb` to fetch its latest version with KaggleHub and copy it to `kaggle/input/valorant-champion-tour-2021-2023-data/`, the location used by the analysis notebooks. Raw Kaggle files stay local and are excluded from Git uploads by `.gitignore`; they are not deleted. KaggleHub may require authentication depending on your environment. Keep credentials outside this repository. The MIT License applies to this project code only, not to Kaggle's dataset. The existing local source folder contains year folders through 2025, despite its 2021-2023 name; available years depend on the downloaded dataset version.

The notebooks use relative paths, so launch them with this project folder as the working directory. Pick and outcome rates depend on the dataset's coverage and aggregation; treat them as descriptive signals for discussion, not standalone coaching recommendations.

## Run locally

From the project directory, install the listed packages with `pip install -r requirements.txt`, then run all cells in `Download_VCT_Data.ipynb` before opening the analysis notebooks. The downloader and analysis notebooks expect the project directory to be the working directory.