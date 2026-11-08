---
title: "Steam Price Modeling"
summary: "Estimating market-aligned game prices from Steam metadata, from messy data to a served ML model."
category: "Machine learning"
technologies: ["Python", "scikit-learn", "XGBoost", "Optuna", "MLflow", "FastAPI", "DVC"]
featured: true
order: 5
source: "https://github.com/camomilesson/steam-price-modeling"
accent: "purple"
visual: "What’s in\na price?"
role: "Solo developer"
context: "Machine Learning course"
image: "/images/steam/model-comparison.svg"
imageAlt: "Selected-scope notebook comparison: dollar MAE is 6.329 for the median baseline, 4.911 for Ridge, 4.813 for KNN, and 4.587 for XGBoost. Lower is better."
imageKind: "screenshot"
screenshots:
  - src: "/images/steam/data-selection.svg"
    alt: "Data selection: 122,611 raw games, 96,062 valid paid price targets, and 49,139 selected games with at least ten reviews."
    title: "Deciding what belongs in the dataset"
    caption: "Target cleaning and market selection answer different questions. The review threshold retains about half the valid paid dataset and limits which market the results describe."
    width: 1800
    height: 1080
  - src: "/images/steam/model-comparison.svg"
    alt: "Four notebook benchmarks evaluated on the same 9,828-game selected-scope test split: median 6.329, Ridge 4.911, KNN 4.813, and XGBoost 4.587 dollars MAE."
    title: "Make complexity earn its place"
    caption: "The notebook compares a constant median, sparse linear regression, nearest-neighbor pricing, and boosting on the same selected split. These are notebook benchmarks, separate from the tuned serving model."
    width: 1800
    height: 1080
  - src: "/images/steam/price-band-error.svg"
    alt: "In the earlier full-valid-price baseline experiment, dollar errors rise sharply for higher price bands. The most expensive band has only 127 test games."
    title: "Look beyond the average error"
    caption: "An earlier broad-market experiment shows how baseline errors vary by price band. It uses a different scope from the selected-scope comparison above and does not show tuned XGBoost results."
    width: 1800
    height: 1080
draft: false
---

## The question

A solo Machine Learning course project exploring a practical indie-dev question: what should your game cost? I’ve since used it to check newly released games and projects acquaintances are working on.

## Making the data usable

The hardest part was deciding what the model should learn from. I repaired a malformed CSV header, reconstructed list prices from discounts, and excluded free games, invalid discounts, and prices above $100.

The selected market contains **49,139 games with at least ten reviews**—about half the valid paid dataset. Review count selects this reference group; it isn’t a launch-price predictor.

## Features and models

Genres, tags, categories, platforms, and other pre-release metadata become a sparse feature matrix. Models learn log-transformed prices, with errors reported in dollars. Reviews and player activity are kept out of the developer-facing predictors.

On the same **9,828-game test split**, the notebook compares median pricing, Ridge, KNN, and XGBoost. Mean absolute error improves from **$6.329** for the median baseline to **$4.587** for XGBoost.

## Beyond the notebook

The modular Python pipeline uses **Optuna** for tuning, **MLflow** for experiment tracking, and **DVC** for model artifacts. **FastAPI** serves price estimates and alignment labels.

The separate tuned model records **$4.554 test MAE**, with **42.2%** of predictions within 50% of the target price.

## Reading the result

The model estimates listed prices, not profitability or an optimal launch price. Discount reconstruction and review-based selection limit what the results represent. Random test splits don’t establish performance on future releases; my later checks were exploratory, not a new validation study.
