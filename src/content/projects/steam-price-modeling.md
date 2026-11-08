---
title: "Steam Price Modeling"
summary: "Exploring what game metadata can tell us about market-aligned prices."
category: "Machine learning"
technologies: ["Python", "XGBoost", "FastAPI"]
featured: true
order: 5
source: "https://github.com/camomilesson/steam-price-modeling"
accent: "purple"
visual: "What’s in\na price?"
draft: true
---

## Understanding game prices

This project estimates a paid game’s expected market list price from Steam metadata, then compares its current price with that estimate. It explores both developer-facing price benchmarking and player-facing price comparisons.

## From exploration to a model

The workflow covers exploratory analysis, feature engineering, and comparisons with median-price, Ridge, and nearest-neighbor baselines. The modular training pipeline uses XGBoost, Optuna for tuning, and MLflow for experiment tracking.

## Beyond the notebook

DVC tracks the model artifacts, and a FastAPI application serves predictions for individual games. The notebooks document the experiment decisions and evaluation.

## Reading the result carefully

The model estimates market alignment from the dataset. It does not measure a game’s intrinsic value or guarantee a successful launch price. Evaluation and scope restrictions matter when interpreting a prediction.
