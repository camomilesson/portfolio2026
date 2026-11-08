# Steam Price Modeling — case-study evidence

Status: developed case study and three reproducible charts integrated locally,
2026-11-08. Source notebooks and model artifacts were read, not executed or changed.

## User context

Solo Machine Learning course project. Interest in indie game development motivated
a pricing-reference experiment. Andrei later checked newly released games and
projects acquaintances were developing or considering. No developer identity,
private project details, or commercial validation claims are published.

## Figure provenance

Recorded values are in `docs/dev/chart-data/steam-notebook-results.json`.
`scripts/render-steam-charts.py` renders standalone SVG and PNG outputs using
Matplotlib. No training, inference, or network calls are needed to render them.

- Model comparison: `03_modeling.ipynb`, cells 31 and 40. Same selected-scope
  random split, 9,828 test games. Median 6.329, Ridge 4.911, KNN k=25 4.813,
  XGBoost 4.587 dollars MAE. Do not substitute full-valid or tuned-run results.
- Data selection: `01_eda.ipynb` cell 27; `02_feature_eng.ipynb` cells 6–7;
  `03_modeling.ipynb` cell 27. Raw 122,611; exclude 26,206 free, 2 invalid
  fully discounted, 341 above $100 => 96,062 valid. Select 49,139 with 10+ reviews.
  These are nested cohort counts, not measured model accuracy improvements.
- Price bands: `03_modeling.ipynb` cell 24. Earlier full-valid scope, 19,213
  test games, three baseline models. Not the selected scope or tuned XGBoost.
  Highest price band has 127 test examples. The chart explicitly states this.

Separate tuned pipeline: local `models/metrics.json` and `models/metadata.json`
record MAE 4.553957, median AE 2.813379, and within-50% 42.175417%.
Training/validation/test counts are 31,940 / 7,371 / 9,828. Values are reported
as a separate run; the comparison plot uses the original notebook benchmarks.

Review count selects the market cohort but is excluded from pre-release model
predictors. That distinction does not eliminate selection bias. Random splits
are not proof of temporal generalization. Listing-price prediction is not revenue
optimization or a causal valuation model. No current Steam release-rate claim
is used in the copy.

Website content: `src/content/projects/steam-price-modeling.md`.
