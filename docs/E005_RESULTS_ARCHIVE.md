# E005 historical aggregate results archive

Archive prepared on 2026-09-13 from the preserved completed result artifact. This is a retrospective publication of existing results, not a prospectively preregistered Git record. No models, bootstrap resamples, or permutations were run to produce this archive. E001-E005 source artifacts remain unchanged.

Source artifact SHA-256: `b69cda4fd8ce9d412da443d5d5728b16542fd3758ba195b34305b0e3069663e9`.
Source data SHA-256: `0a5e4523ec9b1656b979002a58e7cb743d02c9ac2697cc154008f971d413686c`.

**Metric status:** every Brier value below is **LEGACY**, retained verbatim or summarized from the historical implementation. It must not be interpreted as a validated corrected Brier score; see [metric erratum](METRIC_ERRATUM_2026_09.md).

Numerical summaries use equal-weight fold means and sample standard deviation (denominator k - 1), formatted to six decimal places. Counts are summed across the five disjoint evaluation folds. Paired differences use learned minus frequency within each fold. The five folds have overlapping training sets; their variation and any archived intervals are descriptive, not formal inferential evidence.

Frozen split-manifest SHA-256: `93a25f33389b68487c09c5e9b34cfd10ca0d03b9b6438a53e2c385b2e87a7b94`.

Support definitions are unchanged: unsupported = zero training examples; rare = 1-19; frequent = at least 20; well-supported = at least 20 across at least two training questions. Well-supported is nested inside frequent and must not be added to the three mutually exclusive count strata.

Random and grouped support subsets are defined from their respective fold-local training roles and can contain different examples. Their score difference is a comparison of those subsets, not a matched-row causal decomposition. Category probabilities were formed by summing exact-label probabilities in the original run.

**Calibration eligibility:** the source execution applied the rule separately within each fold (at least 200 examples, 20 correct, and 20 incorrect), although the protocol described pooled eligibility. This archive preserves the executed foldwise results and flags the discrepancy; it does not claim pooled calibration or silently repair the implementation. In stratum tables, ECE/Brier are averaged only across the source's eligible folds; eligibility counts are shown. Unsupported exact labels cannot yield correct closed-set predictions and are ineligible.

## explanation_only

### Question-held-out: all-row exact-label performance

| Model | Evaluation n | Accuracy | Macro-F1 | MAP@3 | ECE | Brier (LEGACY) |
| --- | --- | --- | --- | --- | --- | --- |
| Frequency | 36696 | 0.402009 +/- 0.050064 | 0.035555 +/- 0.008409 | 0.539215 +/- 0.039204 | 0.056271 +/- 0.034633 | 0.581666 +/- 0.074249 |
| TF-IDF | 36696 | 0.353703 +/- 0.052241 | 0.048780 +/- 0.012241 | 0.496853 +/- 0.033889 | 0.119816 +/- 0.086872 | 0.619925 +/- 0.131160 |

### All-row fold values

| Fold | Model | n | Accuracy | Macro-F1 | MAP@3 | ECE | Brier (LEGACY) | MAP@3 delta |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 0 | Frequency | 7686 | 0.485818 | 0.040871 | 0.591812 | 0.112647 | 0.702901 | 0.000000 |
| 0 | TF-IDF | 7686 | 0.332162 | 0.044237 | 0.475193 | 0.191684 | 0.823163 | -0.116619 |
| 1 | Frequency | 7023 | 0.358963 | 0.029349 | 0.501804 | 0.055844 | 0.593851 | 0.000000 |
| 1 | TF-IDF | 7023 | 0.281931 | 0.040878 | 0.453320 | 0.234320 | 0.673575 | -0.048484 |
| 2 | Frequency | 7491 | 0.395408 | 0.031485 | 0.538824 | 0.045889 | 0.528804 | 0.000000 |
| 2 | TF-IDF | 7491 | 0.344814 | 0.042688 | 0.499333 | 0.049250 | 0.539191 | -0.039492 |
| 3 | Frequency | 7091 | 0.368777 | 0.028360 | 0.501222 | 0.048873 | 0.517241 | 0.000000 |
| 3 | TF-IDF | 7091 | 0.404879 | 0.045653 | 0.516876 | 0.051279 | 0.495832 | 0.015654 |
| 4 | Frequency | 7405 | 0.401080 | 0.047711 | 0.562413 | 0.018103 | 0.565533 | 0.000000 |
| 4 | TF-IDF | 7405 | 0.404727 | 0.070446 | 0.539545 | 0.072548 | 0.567864 | -0.022867 |

### Exact-label support strata

| Stratum | Model | n | Nonempty folds | Accuracy | Macro-F1 | MAP@3 | Eligible calibration folds | Eligible calibration n | ECE | Brier (LEGACY) |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| unsupported | Frequency | 7755 | 5 | 0.000000 +/- 0.000000 | 0.000000 +/- 0.000000 | 0.000000 +/- 0.000000 | 0 | 0 | Not estimable | Not estimable |
| unsupported | TF-IDF | 7755 | 5 | 0.000000 +/- 0.000000 | 0.000000 +/- 0.000000 | 0.000000 +/- 0.000000 | 0 | 0 | Not estimable | Not estimable |
| rare | Frequency | 0 | 0 | Not estimable | Not estimable | Not estimable | 0 | 0 | Not estimable | Not estimable |
| rare | TF-IDF | 0 | 0 | Not estimable | Not estimable | Not estimable | 0 | 0 | Not estimable | Not estimable |
| frequent | Frequency | 28941 | 5 | 0.511607 +/- 0.028003 | 0.140477 +/- 0.032544 | 0.689284 +/- 0.048006 | 5 | 28941 | 0.098385 +/- 0.032428 | 0.671611 +/- 0.042803 |
| frequent | TF-IDF | 28941 | 5 | 0.456707 +/- 0.098557 | 0.111902 +/- 0.024621 | 0.640004 +/- 0.095181 | 5 | 28941 | 0.131950 +/- 0.058868 | 0.702685 +/- 0.102444 |
| well_supported | Frequency | 28187 | 5 | 0.524554 +/- 0.013504 | 0.165073 +/- 0.014938 | 0.706722 +/- 0.034859 | 5 | 28187 | 0.111332 +/- 0.027678 | 0.658169 +/- 0.032727 |
| well_supported | TF-IDF | 28187 | 5 | 0.466877 +/- 0.089983 | 0.121468 +/- 0.023823 | 0.655384 +/- 0.085042 | 5 | 28187 | 0.124401 +/- 0.054195 | 0.687112 +/- 0.091576 |

### Support-stratum fold values

| Fold | Stratum | Model | n | Accuracy | Macro-F1 | MAP@3 | ECE | Brier (LEGACY) |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 0 | unsupported | Frequency | 407 | 0.000000 | 0.000000 | 0.000000 | Not estimable | Not estimable |
| 1 | unsupported | Frequency | 1613 | 0.000000 | 0.000000 | 0.000000 | Not estimable | Not estimable |
| 2 | unsupported | Frequency | 1985 | 0.000000 | 0.000000 | 0.000000 | Not estimable | Not estimable |
| 3 | unsupported | Frequency | 2162 | 0.000000 | 0.000000 | 0.000000 | Not estimable | Not estimable |
| 4 | unsupported | Frequency | 1588 | 0.000000 | 0.000000 | 0.000000 | Not estimable | Not estimable |
| 0 | unsupported | TF-IDF | 407 | 0.000000 | 0.000000 | 0.000000 | Not estimable | Not estimable |
| 1 | unsupported | TF-IDF | 1613 | 0.000000 | 0.000000 | 0.000000 | Not estimable | Not estimable |
| 2 | unsupported | TF-IDF | 1985 | 0.000000 | 0.000000 | 0.000000 | Not estimable | Not estimable |
| 3 | unsupported | TF-IDF | 2162 | 0.000000 | 0.000000 | 0.000000 | Not estimable | Not estimable |
| 4 | unsupported | TF-IDF | 1588 | 0.000000 | 0.000000 | 0.000000 | Not estimable | Not estimable |
| 0 | rare | Frequency | 0 | Not estimable | Not estimable | Not estimable | Not estimable | Not estimable |
| 1 | rare | Frequency | 0 | Not estimable | Not estimable | Not estimable | Not estimable | Not estimable |
| 2 | rare | Frequency | 0 | Not estimable | Not estimable | Not estimable | Not estimable | Not estimable |
| 3 | rare | Frequency | 0 | Not estimable | Not estimable | Not estimable | Not estimable | Not estimable |
| 4 | rare | Frequency | 0 | Not estimable | Not estimable | Not estimable | Not estimable | Not estimable |
| 0 | rare | TF-IDF | 0 | Not estimable | Not estimable | Not estimable | Not estimable | Not estimable |
| 1 | rare | TF-IDF | 0 | Not estimable | Not estimable | Not estimable | Not estimable | Not estimable |
| 2 | rare | TF-IDF | 0 | Not estimable | Not estimable | Not estimable | Not estimable | Not estimable |
| 3 | rare | TF-IDF | 0 | Not estimable | Not estimable | Not estimable | Not estimable | Not estimable |
| 4 | rare | TF-IDF | 0 | Not estimable | Not estimable | Not estimable | Not estimable | Not estimable |
| 0 | frequent | Frequency | 7279 | 0.512983 | 0.113018 | 0.624903 | 0.139811 | 0.730497 |
| 1 | frequent | Frequency | 5410 | 0.465989 | 0.105956 | 0.651417 | 0.051181 | 0.700869 |
| 2 | frequent | Frequency | 5506 | 0.537959 | 0.174894 | 0.733079 | 0.096662 | 0.628435 |
| 3 | frequent | Frequency | 4929 | 0.530534 | 0.173317 | 0.721073 | 0.112883 | 0.641079 |
| 4 | frequent | Frequency | 5817 | 0.510572 | 0.135200 | 0.715948 | 0.091389 | 0.657173 |
| 0 | frequent | TF-IDF | 7279 | 0.350735 | 0.080547 | 0.501763 | 0.172510 | 0.847073 |
| 1 | frequent | TF-IDF | 5410 | 0.365989 | 0.093666 | 0.588478 | 0.160235 | 0.771810 |
| 2 | frequent | TF-IDF | 5506 | 0.469125 | 0.114570 | 0.679350 | 0.072918 | 0.655950 |
| 3 | frequent | TF-IDF | 4929 | 0.582471 | 0.134590 | 0.743592 | 0.189827 | 0.607871 |
| 4 | frequent | TF-IDF | 5817 | 0.515214 | 0.136133 | 0.686837 | 0.064259 | 0.630720 |
| 0 | well_supported | Frequency | 7025 | 0.531530 | 0.138823 | 0.647497 | 0.158359 | 0.713308 |
| 1 | well_supported | Frequency | 5005 | 0.503696 | 0.167486 | 0.704129 | 0.088889 | 0.658084 |
| 2 | well_supported | Frequency | 5506 | 0.537959 | 0.174894 | 0.733079 | 0.096662 | 0.628435 |
| 3 | well_supported | Frequency | 4929 | 0.530534 | 0.173317 | 0.721073 | 0.112883 | 0.641079 |
| 4 | well_supported | Frequency | 5722 | 0.519049 | 0.170847 | 0.727834 | 0.099866 | 0.649938 |
| 0 | well_supported | TF-IDF | 7025 | 0.363416 | 0.088872 | 0.519905 | 0.159113 | 0.827587 |
| 1 | well_supported | TF-IDF | 5005 | 0.395604 | 0.116763 | 0.635831 | 0.134921 | 0.727343 |
| 2 | well_supported | TF-IDF | 5506 | 0.469125 | 0.114570 | 0.679350 | 0.072918 | 0.655950 |
| 3 | well_supported | TF-IDF | 4929 | 0.582471 | 0.134590 | 0.743592 | 0.189827 | 0.607871 |
| 4 | well_supported | TF-IDF | 5722 | 0.523768 | 0.152544 | 0.698241 | 0.065225 | 0.616811 |

### Six-way Category: aggregate and fold values

| Model | n | Accuracy | Macro-F1 | ECE | Brier (LEGACY) |
| --- | --- | --- | --- | --- | --- |
| Frequency | 36696 | 0.402009 +/- 0.050064 | 0.095344 +/- 0.008229 | 0.056271 +/- 0.034633 | 0.724024 +/- 0.023487 |
| TF-IDF | 36696 | 0.360008 +/- 0.053663 | 0.207540 +/- 0.031552 | 0.131710 +/- 0.074530 | 0.768897 +/- 0.065520 |

| Fold | Model | n | Accuracy | Macro-F1 | ECE | Brier (LEGACY) |
| --- | --- | --- | --- | --- | --- | --- |
| 0 | Frequency | 7686 | 0.485818 | 0.108990 | 0.112647 | 0.684595 |
| 0 | TF-IDF | 7686 | 0.337237 | 0.178608 | 0.192505 | 0.828712 |
| 1 | Frequency | 7023 | 0.358963 | 0.088048 | 0.055844 | 0.745868 |
| 1 | TF-IDF | 7023 | 0.296170 | 0.182224 | 0.222772 | 0.841464 |
| 2 | Frequency | 7491 | 0.395408 | 0.094455 | 0.045889 | 0.723593 |
| 2 | TF-IDF | 7491 | 0.344280 | 0.207703 | 0.076845 | 0.734044 |
| 3 | Frequency | 7091 | 0.368777 | 0.089807 | 0.048873 | 0.730550 |
| 3 | TF-IDF | 7091 | 0.438020 | 0.257403 | 0.047741 | 0.685802 |
| 4 | Frequency | 7405 | 0.401080 | 0.095422 | 0.018103 | 0.735514 |
| 4 | TF-IDF | 7405 | 0.384335 | 0.211761 | 0.118689 | 0.754461 |

### Random: all-row exact-label performance

| Model | Evaluation n | Accuracy | Macro-F1 | MAP@3 | ECE | Brier (LEGACY) |
| --- | --- | --- | --- | --- | --- | --- |
| Frequency | 36696 | 0.403368 +/- 0.000063 | 0.010771 +/- 0.000272 | 0.540331 +/- 0.000095 | 0.000056 +/- 0.000026 | 0.780231 +/- 0.000096 |
| TF-IDF | 36696 | 0.644321 +/- 0.002202 | 0.306357 +/- 0.004599 | 0.763807 +/- 0.002354 | 0.022682 +/- 0.005347 | 0.480070 +/- 0.004194 |

### All-row fold values

| Fold | Model | n | Accuracy | Macro-F1 | MAP@3 | ECE | Brier (LEGACY) | MAP@3 delta |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 0 | Frequency | 7340 | 0.403406 | 0.010646 | 0.540395 | 0.000068 | 0.780241 | 0.000000 |
| 0 | TF-IDF | 7340 | 0.643460 | 0.307294 | 0.762035 | 0.022751 | 0.483048 | 0.221639 |
| 1 | Frequency | 7339 | 0.403461 | 0.011057 | 0.540469 | 0.000097 | 0.780290 | 0.000000 |
| 1 | TF-IDF | 7339 | 0.642731 | 0.312242 | 0.762752 | 0.029708 | 0.482911 | 0.222283 |
| 2 | Frequency | 7339 | 0.403325 | 0.011054 | 0.540264 | 0.000039 | 0.780274 | 0.000000 |
| 2 | TF-IDF | 7339 | 0.643276 | 0.305993 | 0.762524 | 0.020834 | 0.482277 | 0.222260 |
| 3 | Frequency | 7339 | 0.403325 | 0.010645 | 0.540264 | 0.000039 | 0.780063 | 0.000000 |
| 3 | TF-IDF | 7339 | 0.643957 | 0.306879 | 0.763887 | 0.024948 | 0.478912 | 0.223623 |
| 4 | Frequency | 7339 | 0.403325 | 0.010451 | 0.540264 | 0.000039 | 0.780287 | 0.000000 |
| 4 | TF-IDF | 7339 | 0.648181 | 0.299378 | 0.767838 | 0.015170 | 0.473199 | 0.227574 |

### Exact-label support strata

| Stratum | Model | n | Nonempty folds | Accuracy | Macro-F1 | MAP@3 | Eligible calibration folds | Eligible calibration n | ECE | Brier (LEGACY) |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| unsupported | Frequency | 9 | 4 | 0.000000 +/- 0.000000 | 0.000000 +/- 0.000000 | 0.000000 +/- 0.000000 | 0 | 0 | Not estimable | Not estimable |
| unsupported | TF-IDF | 9 | 4 | 0.000000 +/- 0.000000 | 0.000000 +/- 0.000000 | 0.000000 +/- 0.000000 | 0 | 0 | Not estimable | Not estimable |
| rare | Frequency | 231 | 5 | 0.000000 +/- 0.000000 | 0.000000 +/- 0.000000 | 0.000000 +/- 0.000000 | 0 | 0 | Not estimable | Not estimable |
| rare | TF-IDF | 231 | 5 | 0.012608 +/- 0.011639 | 0.011181 +/- 0.010716 | 0.025000 +/- 0.008070 | 0 | 0 | Not estimable | Not estimable |
| frequent | Frequency | 36456 | 5 | 0.406024 +/- 0.000288 | 0.017399 +/- 0.000233 | 0.543889 +/- 0.000389 | 5 | 36456 | 0.002665 +/- 0.000295 | 0.777590 +/- 0.000373 |
| frequent | TF-IDF | 36456 | 5 | 0.648481 +/- 0.002328 | 0.485157 +/- 0.013594 | 0.768676 +/- 0.002454 | 5 | 36456 | 0.019373 +/- 0.005176 | 0.474256 +/- 0.004373 |
| well_supported | Frequency | 29667 | 5 | 0.498945 +/- 0.002028 | 0.083216 +/- 0.000226 | 0.668361 +/- 0.002719 | 5 | 29667 | 0.095586 +/- 0.002025 | 0.682216 +/- 0.001957 |
| well_supported | TF-IDF | 29667 | 5 | 0.675564 +/- 0.003336 | 0.157508 +/- 0.011653 | 0.799113 +/- 0.002715 | 5 | 29667 | 0.018009 +/- 0.006210 | 0.442156 +/- 0.005014 |

### Support-stratum fold values

| Fold | Stratum | Model | n | Accuracy | Macro-F1 | MAP@3 | ECE | Brier (LEGACY) |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 0 | unsupported | Frequency | 1 | 0.000000 | 0.000000 | 0.000000 | Not estimable | Not estimable |
| 1 | unsupported | Frequency | 1 | 0.000000 | 0.000000 | 0.000000 | Not estimable | Not estimable |
| 2 | unsupported | Frequency | 3 | 0.000000 | 0.000000 | 0.000000 | Not estimable | Not estimable |
| 3 | unsupported | Frequency | 4 | 0.000000 | 0.000000 | 0.000000 | Not estimable | Not estimable |
| 4 | unsupported | Frequency | 0 | Not estimable | Not estimable | Not estimable | Not estimable | Not estimable |
| 0 | unsupported | TF-IDF | 1 | 0.000000 | 0.000000 | 0.000000 | Not estimable | Not estimable |
| 1 | unsupported | TF-IDF | 1 | 0.000000 | 0.000000 | 0.000000 | Not estimable | Not estimable |
| 2 | unsupported | TF-IDF | 3 | 0.000000 | 0.000000 | 0.000000 | Not estimable | Not estimable |
| 3 | unsupported | TF-IDF | 4 | 0.000000 | 0.000000 | 0.000000 | Not estimable | Not estimable |
| 4 | unsupported | TF-IDF | 0 | Not estimable | Not estimable | Not estimable | Not estimable | Not estimable |
| 0 | rare | Frequency | 52 | 0.000000 | 0.000000 | 0.000000 | Not estimable | Not estimable |
| 1 | rare | Frequency | 42 | 0.000000 | 0.000000 | 0.000000 | Not estimable | Not estimable |
| 2 | rare | Frequency | 40 | 0.000000 | 0.000000 | 0.000000 | Not estimable | Not estimable |
| 3 | rare | Frequency | 50 | 0.000000 | 0.000000 | 0.000000 | Not estimable | Not estimable |
| 4 | rare | Frequency | 47 | 0.000000 | 0.000000 | 0.000000 | Not estimable | Not estimable |
| 0 | rare | TF-IDF | 52 | 0.019231 | 0.013333 | 0.038462 | Not estimable | Not estimable |
| 1 | rare | TF-IDF | 42 | 0.023810 | 0.021739 | 0.023810 | Not estimable | Not estimable |
| 2 | rare | TF-IDF | 40 | 0.000000 | 0.000000 | 0.025000 | Not estimable | Not estimable |
| 3 | rare | TF-IDF | 50 | 0.020000 | 0.020833 | 0.020000 | Not estimable | Not estimable |
| 4 | rare | TF-IDF | 47 | 0.000000 | 0.000000 | 0.017730 | Not estimable | Not estimable |
| 0 | frequent | Frequency | 7287 | 0.406340 | 0.017511 | 0.544326 | 0.003002 | 0.777187 |
| 1 | frequent | Frequency | 7296 | 0.405839 | 0.016981 | 0.543654 | 0.002475 | 0.777842 |
| 2 | frequent | Frequency | 7296 | 0.405702 | 0.017492 | 0.543448 | 0.002338 | 0.778100 |
| 3 | frequent | Frequency | 7285 | 0.406314 | 0.017510 | 0.544269 | 0.002950 | 0.777359 |
| 4 | frequent | Frequency | 7292 | 0.405924 | 0.017498 | 0.543747 | 0.002560 | 0.777461 |
| 0 | frequent | TF-IDF | 7287 | 0.648003 | 0.491706 | 0.767303 | 0.018855 | 0.476471 |
| 1 | frequent | TF-IDF | 7296 | 0.646382 | 0.463507 | 0.767110 | 0.026739 | 0.477748 |
| 2 | frequent | TF-IDF | 7296 | 0.647067 | 0.482825 | 0.766881 | 0.017561 | 0.477219 |
| 3 | frequent | TF-IDF | 7285 | 0.648593 | 0.487946 | 0.769412 | 0.021138 | 0.472476 |
| 4 | frequent | TF-IDF | 7292 | 0.652359 | 0.499800 | 0.772673 | 0.012574 | 0.467368 |
| 0 | well_supported | Frequency | 5947 | 0.497898 | 0.083099 | 0.666975 | 0.094560 | 0.683289 |
| 1 | well_supported | Frequency | 5912 | 0.500846 | 0.083427 | 0.670924 | 0.097482 | 0.680317 |
| 2 | well_supported | Frequency | 5918 | 0.500169 | 0.083352 | 0.669990 | 0.096805 | 0.681032 |
| 3 | well_supported | Frequency | 5921 | 0.499916 | 0.083324 | 0.669650 | 0.096552 | 0.681331 |
| 4 | well_supported | Frequency | 5969 | 0.495895 | 0.082876 | 0.664265 | 0.092532 | 0.685110 |
| 0 | well_supported | TF-IDF | 5947 | 0.670422 | 0.157461 | 0.794939 | 0.019549 | 0.448861 |
| 1 | well_supported | TF-IDF | 5912 | 0.674729 | 0.147391 | 0.798489 | 0.028269 | 0.444331 |
| 2 | well_supported | TF-IDF | 5918 | 0.676073 | 0.167624 | 0.799623 | 0.014025 | 0.442210 |
| 3 | well_supported | TF-IDF | 5921 | 0.677250 | 0.170541 | 0.800203 | 0.014420 | 0.440032 |
| 4 | well_supported | TF-IDF | 5969 | 0.679343 | 0.144522 | 0.802312 | 0.013782 | 0.435348 |

### Six-way Category: aggregate and fold values

| Model | n | Accuracy | Macro-F1 | ECE | Brier (LEGACY) |
| --- | --- | --- | --- | --- | --- |
| Frequency | 36696 | 0.403368 +/- 0.000063 | 0.095810 +/- 0.000011 | 0.000056 +/- 0.000026 | 0.718352 +/- 0.000055 |
| TF-IDF | 36696 | 0.660508 +/- 0.002461 | 0.424248 +/- 0.010764 | 0.021853 +/- 0.005061 | 0.457651 +/- 0.003787 |

| Fold | Model | n | Accuracy | Macro-F1 | ECE | Brier (LEGACY) |
| --- | --- | --- | --- | --- | --- | --- |
| 0 | Frequency | 7340 | 0.403406 | 0.095816 | 0.000068 | 0.718347 |
| 0 | TF-IDF | 7340 | 0.661172 | 0.412232 | 0.021212 | 0.459683 |
| 1 | Frequency | 7339 | 0.403461 | 0.095825 | 0.000097 | 0.718272 |
| 1 | TF-IDF | 7339 | 0.657719 | 0.412773 | 0.028650 | 0.460804 |
| 2 | Frequency | 7339 | 0.403325 | 0.095802 | 0.000039 | 0.718358 |
| 2 | TF-IDF | 7339 | 0.658809 | 0.430788 | 0.021462 | 0.460223 |
| 3 | Frequency | 7339 | 0.403325 | 0.095802 | 0.000039 | 0.718358 |
| 3 | TF-IDF | 7339 | 0.660717 | 0.432060 | 0.023392 | 0.455589 |
| 4 | Frequency | 7339 | 0.403325 | 0.095802 | 0.000039 | 0.718426 |
| 4 | TF-IDF | 7339 | 0.664123 | 0.433389 | 0.014550 | 0.451957 |

### Random minus grouped MAP@3: all rows and well-supported subset

| Subset | Model | Random n | Grouped n | Random MAP@3 | Grouped MAP@3 | Random - grouped |
| --- | --- | --- | --- | --- | --- | --- |
| all | Frequency | 36696 | 36696 | 0.540331 +/- 0.000095 | 0.539215 +/- 0.039204 | 0.001116 |
| all | TF-IDF | 36696 | 36696 | 0.763807 +/- 0.002354 | 0.496853 +/- 0.033889 | 0.266954 |
| well_supported | Frequency | 29667 | 28187 | 0.668361 +/- 0.002719 | 0.706722 +/- 0.034859 | -0.038362 |
| well_supported | TF-IDF | 29667 | 28187 | 0.799113 +/- 0.002715 | 0.655384 +/- 0.085042 | 0.143729 |

### All 15 held-out questions: stored support and performance

| QuestionId | Fold | n | Supported share | Well-supported share | Frequency MAP@3 | TF-IDF MAP@3 |
| --- | --- | --- | --- | --- | --- | --- |
| 31772 | 0 | 4857 | 0.996706 | 0.944410 | 0.485862 | 0.473475 |
| 31774 | 2 | 3115 | 0.795506 | 0.795506 | 0.593847 | 0.571536 |
| 31777 | 4 | 2809 | 0.888216 | 0.861161 | 0.704047 | 0.685475 |
| 31778 | 1 | 3640 | 0.720604 | 0.609341 | 0.435989 | 0.438782 |
| 32829 | 0 | 2156 | 0.873840 | 0.873840 | 0.790816 | 0.526438 |
| 32833 | 3 | 3105 | 0.638003 | 0.638003 | 0.497370 | 0.467633 |
| 32835 | 1 | 2332 | 0.828902 | 0.828902 | 0.565466 | 0.458333 |
| 33471 | 4 | 1542 | 0.728923 | 0.716602 | 0.562365 | 0.425422 |
| 33472 | 3 | 2800 | 0.767143 | 0.767143 | 0.518750 | 0.571310 |
| 33474 | 2 | 1766 | 0.613250 | 0.613250 | 0.368913 | 0.399018 |
| 76870 | 3 | 1186 | 0.674536 | 0.674536 | 0.469927 | 0.517285 |
| 89443 | 4 | 3054 | 0.719712 | 0.719712 | 0.432165 | 0.462945 |
| 91695 | 2 | 2610 | 0.745211 | 0.745211 | 0.588123 | 0.481034 |
| 104665 | 0 | 673 | 0.823180 | 0.823180 | 0.718920 | 0.323427 |
| 109465 | 1 | 1051 | 0.812559 | 0.812559 | 0.588487 | 0.492547 |

## question_plus_explanation

### Question-held-out: all-row exact-label performance

| Model | Evaluation n | Accuracy | Macro-F1 | MAP@3 | ECE | Brier (LEGACY) |
| --- | --- | --- | --- | --- | --- | --- |
| Frequency | 36696 | 0.402009 +/- 0.050064 | 0.035555 +/- 0.008409 | 0.539215 +/- 0.039204 | 0.056271 +/- 0.034633 | 0.581666 +/- 0.074249 |
| TF-IDF | 36696 | 0.376306 +/- 0.052036 | 0.055077 +/- 0.015987 | 0.519971 +/- 0.037799 | 0.108524 +/- 0.081762 | 0.592337 +/- 0.121297 |

### All-row fold values

| Fold | Model | n | Accuracy | Macro-F1 | MAP@3 | ECE | Brier (LEGACY) | MAP@3 delta |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 0 | Frequency | 7686 | 0.485818 | 0.040871 | 0.591812 | 0.112647 | 0.702901 | 0.000000 |
| 0 | TF-IDF | 7686 | 0.392142 | 0.037931 | 0.521598 | 0.232242 | 0.793236 | -0.070214 |
| 1 | Frequency | 7023 | 0.358963 | 0.029349 | 0.501804 | 0.055844 | 0.593851 | 0.000000 |
| 1 | TF-IDF | 7023 | 0.300299 | 0.054689 | 0.471356 | 0.149953 | 0.619092 | -0.030448 |
| 2 | Frequency | 7491 | 0.395408 | 0.031485 | 0.538824 | 0.045889 | 0.528804 | 0.000000 |
| 2 | TF-IDF | 7491 | 0.350154 | 0.050678 | 0.508121 | 0.042552 | 0.525748 | -0.030704 |
| 3 | Frequency | 7091 | 0.368777 | 0.028360 | 0.501222 | 0.048873 | 0.517241 | 0.000000 |
| 3 | TF-IDF | 7091 | 0.405444 | 0.050740 | 0.522211 | 0.073886 | 0.498197 | 0.020989 |
| 4 | Frequency | 7405 | 0.401080 | 0.047711 | 0.562413 | 0.018103 | 0.565533 | 0.000000 |
| 4 | TF-IDF | 7405 | 0.433491 | 0.081346 | 0.576570 | 0.043984 | 0.525411 | 0.014157 |

### Exact-label support strata

| Stratum | Model | n | Nonempty folds | Accuracy | Macro-F1 | MAP@3 | Eligible calibration folds | Eligible calibration n | ECE | Brier (LEGACY) |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| unsupported | Frequency | 7755 | 5 | 0.000000 +/- 0.000000 | 0.000000 +/- 0.000000 | 0.000000 +/- 0.000000 | 0 | 0 | Not estimable | Not estimable |
| unsupported | TF-IDF | 7755 | 5 | 0.000000 +/- 0.000000 | 0.000000 +/- 0.000000 | 0.000000 +/- 0.000000 | 0 | 0 | Not estimable | Not estimable |
| rare | Frequency | 0 | 0 | Not estimable | Not estimable | Not estimable | 0 | 0 | Not estimable | Not estimable |
| rare | TF-IDF | 0 | 0 | Not estimable | Not estimable | Not estimable | 0 | 0 | Not estimable | Not estimable |
| frequent | Frequency | 28941 | 5 | 0.511607 +/- 0.028003 | 0.140477 +/- 0.032544 | 0.689284 +/- 0.048006 | 5 | 28941 | 0.098385 +/- 0.032428 | 0.671611 +/- 0.042803 |
| frequent | TF-IDF | 28941 | 5 | 0.483081 +/- 0.084068 | 0.172121 +/- 0.051167 | 0.667840 +/- 0.084737 | 5 | 28941 | 0.117973 +/- 0.060652 | 0.666724 +/- 0.102107 |
| well_supported | Frequency | 28187 | 5 | 0.524554 +/- 0.013504 | 0.165073 +/- 0.014938 | 0.706722 +/- 0.034859 | 5 | 28187 | 0.111332 +/- 0.027678 | 0.658169 +/- 0.032727 |
| well_supported | TF-IDF | 28187 | 5 | 0.494216 +/- 0.074604 | 0.202125 +/- 0.072460 | 0.684162 +/- 0.073814 | 5 | 28187 | 0.111126 +/- 0.059887 | 0.649470 +/- 0.090403 |

### Support-stratum fold values

| Fold | Stratum | Model | n | Accuracy | Macro-F1 | MAP@3 | ECE | Brier (LEGACY) |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 0 | unsupported | Frequency | 407 | 0.000000 | 0.000000 | 0.000000 | Not estimable | Not estimable |
| 1 | unsupported | Frequency | 1613 | 0.000000 | 0.000000 | 0.000000 | Not estimable | Not estimable |
| 2 | unsupported | Frequency | 1985 | 0.000000 | 0.000000 | 0.000000 | Not estimable | Not estimable |
| 3 | unsupported | Frequency | 2162 | 0.000000 | 0.000000 | 0.000000 | Not estimable | Not estimable |
| 4 | unsupported | Frequency | 1588 | 0.000000 | 0.000000 | 0.000000 | Not estimable | Not estimable |
| 0 | unsupported | TF-IDF | 407 | 0.000000 | 0.000000 | 0.000000 | Not estimable | Not estimable |
| 1 | unsupported | TF-IDF | 1613 | 0.000000 | 0.000000 | 0.000000 | Not estimable | Not estimable |
| 2 | unsupported | TF-IDF | 1985 | 0.000000 | 0.000000 | 0.000000 | Not estimable | Not estimable |
| 3 | unsupported | TF-IDF | 2162 | 0.000000 | 0.000000 | 0.000000 | Not estimable | Not estimable |
| 4 | unsupported | TF-IDF | 1588 | 0.000000 | 0.000000 | 0.000000 | Not estimable | Not estimable |
| 0 | rare | Frequency | 0 | Not estimable | Not estimable | Not estimable | Not estimable | Not estimable |
| 1 | rare | Frequency | 0 | Not estimable | Not estimable | Not estimable | Not estimable | Not estimable |
| 2 | rare | Frequency | 0 | Not estimable | Not estimable | Not estimable | Not estimable | Not estimable |
| 3 | rare | Frequency | 0 | Not estimable | Not estimable | Not estimable | Not estimable | Not estimable |
| 4 | rare | Frequency | 0 | Not estimable | Not estimable | Not estimable | Not estimable | Not estimable |
| 0 | rare | TF-IDF | 0 | Not estimable | Not estimable | Not estimable | Not estimable | Not estimable |
| 1 | rare | TF-IDF | 0 | Not estimable | Not estimable | Not estimable | Not estimable | Not estimable |
| 2 | rare | TF-IDF | 0 | Not estimable | Not estimable | Not estimable | Not estimable | Not estimable |
| 3 | rare | TF-IDF | 0 | Not estimable | Not estimable | Not estimable | Not estimable | Not estimable |
| 4 | rare | TF-IDF | 0 | Not estimable | Not estimable | Not estimable | Not estimable | Not estimable |
| 0 | frequent | Frequency | 7279 | 0.512983 | 0.113018 | 0.624903 | 0.139811 | 0.730497 |
| 1 | frequent | Frequency | 5410 | 0.465989 | 0.105956 | 0.651417 | 0.051181 | 0.700869 |
| 2 | frequent | Frequency | 5506 | 0.537959 | 0.174894 | 0.733079 | 0.096662 | 0.628435 |
| 3 | frequent | Frequency | 4929 | 0.530534 | 0.173317 | 0.721073 | 0.112883 | 0.641079 |
| 4 | frequent | Frequency | 5817 | 0.510572 | 0.135200 | 0.715948 | 0.091389 | 0.657173 |
| 0 | frequent | TF-IDF | 7279 | 0.414068 | 0.082153 | 0.550762 | 0.218276 | 0.817271 |
| 1 | frequent | TF-IDF | 5410 | 0.389834 | 0.189044 | 0.611892 | 0.072222 | 0.720640 |
| 2 | frequent | TF-IDF | 5506 | 0.476389 | 0.209989 | 0.691306 | 0.075631 | 0.636827 |
| 3 | frequent | TF-IDF | 4929 | 0.583283 | 0.194121 | 0.751268 | 0.130490 | 0.578636 |
| 4 | frequent | TF-IDF | 5817 | 0.551831 | 0.185300 | 0.733969 | 0.093247 | 0.580244 |
| 0 | well_supported | Frequency | 7025 | 0.531530 | 0.138823 | 0.647497 | 0.158359 | 0.713308 |
| 1 | well_supported | Frequency | 5005 | 0.503696 | 0.167486 | 0.704129 | 0.088889 | 0.658084 |
| 2 | well_supported | Frequency | 5506 | 0.537959 | 0.174894 | 0.733079 | 0.096662 | 0.628435 |
| 3 | well_supported | Frequency | 4929 | 0.530534 | 0.173317 | 0.721073 | 0.112883 | 0.641079 |
| 4 | well_supported | Frequency | 5722 | 0.519049 | 0.170847 | 0.727834 | 0.099866 | 0.649938 |
| 0 | well_supported | TF-IDF | 7025 | 0.429039 | 0.093006 | 0.570676 | 0.201531 | 0.791972 |
| 1 | well_supported | TF-IDF | 5005 | 0.421379 | 0.295486 | 0.661405 | 0.044158 | 0.672229 |
| 2 | well_supported | TF-IDF | 5506 | 0.476389 | 0.209989 | 0.691306 | 0.075631 | 0.636827 |
| 3 | well_supported | TF-IDF | 4929 | 0.583283 | 0.194121 | 0.751268 | 0.130490 | 0.578636 |
| 4 | well_supported | TF-IDF | 5722 | 0.560993 | 0.218021 | 0.746155 | 0.103820 | 0.567683 |

### Six-way Category: aggregate and fold values

| Model | n | Accuracy | Macro-F1 | ECE | Brier (LEGACY) |
| --- | --- | --- | --- | --- | --- |
| Frequency | 36696 | 0.402009 +/- 0.050064 | 0.095344 +/- 0.008229 | 0.056271 +/- 0.034633 | 0.724024 +/- 0.023487 |
| TF-IDF | 36696 | 0.379677 +/- 0.053686 | 0.185476 +/- 0.030303 | 0.112997 +/- 0.079498 | 0.751929 +/- 0.049023 |

| Fold | Model | n | Accuracy | Macro-F1 | ECE | Brier (LEGACY) |
| --- | --- | --- | --- | --- | --- | --- |
| 0 | Frequency | 7686 | 0.485818 | 0.108990 | 0.112647 | 0.684595 |
| 0 | TF-IDF | 7686 | 0.396695 | 0.142960 | 0.234835 | 0.816398 |
| 1 | Frequency | 7023 | 0.358963 | 0.088048 | 0.055844 | 0.745868 |
| 1 | TF-IDF | 7023 | 0.300014 | 0.166912 | 0.150891 | 0.792305 |
| 2 | Frequency | 7491 | 0.395408 | 0.094455 | 0.045889 | 0.723593 |
| 2 | TF-IDF | 7491 | 0.351755 | 0.201777 | 0.060202 | 0.724517 |
| 3 | Frequency | 7091 | 0.368777 | 0.089807 | 0.048873 | 0.730550 |
| 3 | TF-IDF | 7091 | 0.422507 | 0.219103 | 0.075250 | 0.719433 |
| 4 | Frequency | 7405 | 0.401080 | 0.095422 | 0.018103 | 0.735514 |
| 4 | TF-IDF | 7405 | 0.427414 | 0.196628 | 0.043806 | 0.706994 |

### Random: all-row exact-label performance

| Model | Evaluation n | Accuracy | Macro-F1 | MAP@3 | ECE | Brier (LEGACY) |
| --- | --- | --- | --- | --- | --- | --- |
| Frequency | 36696 | 0.403368 +/- 0.000063 | 0.010771 +/- 0.000272 | 0.540331 +/- 0.000095 | 0.000056 +/- 0.000026 | 0.780231 +/- 0.000096 |
| TF-IDF | 36696 | 0.668193 +/- 0.005254 | 0.329654 +/- 0.006149 | 0.785363 +/- 0.004098 | 0.015499 +/- 0.002977 | 0.453075 +/- 0.004928 |

### All-row fold values

| Fold | Model | n | Accuracy | Macro-F1 | MAP@3 | ECE | Brier (LEGACY) | MAP@3 delta |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 0 | Frequency | 7340 | 0.403406 | 0.010646 | 0.540395 | 0.000068 | 0.780241 | 0.000000 |
| 0 | TF-IDF | 7340 | 0.664305 | 0.323906 | 0.781926 | 0.014184 | 0.456000 | 0.241530 |
| 1 | Frequency | 7339 | 0.403461 | 0.011057 | 0.540469 | 0.000097 | 0.780290 | 0.000000 |
| 1 | TF-IDF | 7339 | 0.668075 | 0.339121 | 0.784962 | 0.015116 | 0.455906 | 0.244493 |
| 2 | Frequency | 7339 | 0.403325 | 0.011054 | 0.540264 | 0.000039 | 0.780274 | 0.000000 |
| 2 | TF-IDF | 7339 | 0.662488 | 0.330375 | 0.781396 | 0.012435 | 0.456858 | 0.241132 |
| 3 | Frequency | 7339 | 0.403325 | 0.010645 | 0.540264 | 0.000039 | 0.780063 | 0.000000 |
| 3 | TF-IDF | 7339 | 0.670255 | 0.324417 | 0.787142 | 0.015344 | 0.451528 | 0.246877 |
| 4 | Frequency | 7339 | 0.403325 | 0.010451 | 0.540264 | 0.000039 | 0.780287 | 0.000000 |
| 4 | TF-IDF | 7339 | 0.675841 | 0.330452 | 0.791388 | 0.020414 | 0.445083 | 0.251124 |

### Exact-label support strata

| Stratum | Model | n | Nonempty folds | Accuracy | Macro-F1 | MAP@3 | Eligible calibration folds | Eligible calibration n | ECE | Brier (LEGACY) |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| unsupported | Frequency | 9 | 4 | 0.000000 +/- 0.000000 | 0.000000 +/- 0.000000 | 0.000000 +/- 0.000000 | 0 | 0 | Not estimable | Not estimable |
| unsupported | TF-IDF | 9 | 4 | 0.000000 +/- 0.000000 | 0.000000 +/- 0.000000 | 0.000000 +/- 0.000000 | 0 | 0 | Not estimable | Not estimable |
| rare | Frequency | 231 | 5 | 0.000000 +/- 0.000000 | 0.000000 +/- 0.000000 | 0.000000 +/- 0.000000 | 0 | 0 | Not estimable | Not estimable |
| rare | TF-IDF | 231 | 5 | 0.000000 +/- 0.000000 | 0.000000 +/- 0.000000 | 0.011469 +/- 0.007153 | 0 | 0 | Not estimable | Not estimable |
| frequent | Frequency | 36456 | 5 | 0.406024 +/- 0.000288 | 0.017399 +/- 0.000233 | 0.543889 +/- 0.000389 | 5 | 36456 | 0.002665 +/- 0.000295 | 0.777590 +/- 0.000373 |
| frequent | TF-IDF | 36456 | 5 | 0.672592 +/- 0.005373 | 0.532236 +/- 0.013715 | 0.790460 +/- 0.004208 | 5 | 36456 | 0.016285 +/- 0.003356 | 0.447081 +/- 0.005068 |
| well_supported | Frequency | 29667 | 5 | 0.498945 +/- 0.002028 | 0.083216 +/- 0.000226 | 0.668361 +/- 0.002719 | 5 | 29667 | 0.095586 +/- 0.002025 | 0.682216 +/- 0.001957 |
| well_supported | TF-IDF | 29667 | 5 | 0.679135 +/- 0.005080 | 0.162738 +/- 0.010213 | 0.798213 +/- 0.003674 | 5 | 29667 | 0.019897 +/- 0.003159 | 0.440201 +/- 0.005389 |

### Support-stratum fold values

| Fold | Stratum | Model | n | Accuracy | Macro-F1 | MAP@3 | ECE | Brier (LEGACY) |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 0 | unsupported | Frequency | 1 | 0.000000 | 0.000000 | 0.000000 | Not estimable | Not estimable |
| 1 | unsupported | Frequency | 1 | 0.000000 | 0.000000 | 0.000000 | Not estimable | Not estimable |
| 2 | unsupported | Frequency | 3 | 0.000000 | 0.000000 | 0.000000 | Not estimable | Not estimable |
| 3 | unsupported | Frequency | 4 | 0.000000 | 0.000000 | 0.000000 | Not estimable | Not estimable |
| 4 | unsupported | Frequency | 0 | Not estimable | Not estimable | Not estimable | Not estimable | Not estimable |
| 0 | unsupported | TF-IDF | 1 | 0.000000 | 0.000000 | 0.000000 | Not estimable | Not estimable |
| 1 | unsupported | TF-IDF | 1 | 0.000000 | 0.000000 | 0.000000 | Not estimable | Not estimable |
| 2 | unsupported | TF-IDF | 3 | 0.000000 | 0.000000 | 0.000000 | Not estimable | Not estimable |
| 3 | unsupported | TF-IDF | 4 | 0.000000 | 0.000000 | 0.000000 | Not estimable | Not estimable |
| 4 | unsupported | TF-IDF | 0 | Not estimable | Not estimable | Not estimable | Not estimable | Not estimable |
| 0 | rare | Frequency | 52 | 0.000000 | 0.000000 | 0.000000 | Not estimable | Not estimable |
| 1 | rare | Frequency | 42 | 0.000000 | 0.000000 | 0.000000 | Not estimable | Not estimable |
| 2 | rare | Frequency | 40 | 0.000000 | 0.000000 | 0.000000 | Not estimable | Not estimable |
| 3 | rare | Frequency | 50 | 0.000000 | 0.000000 | 0.000000 | Not estimable | Not estimable |
| 4 | rare | Frequency | 47 | 0.000000 | 0.000000 | 0.000000 | Not estimable | Not estimable |
| 0 | rare | TF-IDF | 52 | 0.000000 | 0.000000 | 0.009615 | Not estimable | Not estimable |
| 1 | rare | TF-IDF | 42 | 0.000000 | 0.000000 | 0.000000 | Not estimable | Not estimable |
| 2 | rare | TF-IDF | 40 | 0.000000 | 0.000000 | 0.016667 | Not estimable | Not estimable |
| 3 | rare | TF-IDF | 50 | 0.000000 | 0.000000 | 0.013333 | Not estimable | Not estimable |
| 4 | rare | TF-IDF | 47 | 0.000000 | 0.000000 | 0.017730 | Not estimable | Not estimable |
| 0 | frequent | Frequency | 7287 | 0.406340 | 0.017511 | 0.544326 | 0.003002 | 0.777187 |
| 1 | frequent | Frequency | 7296 | 0.405839 | 0.016981 | 0.543654 | 0.002475 | 0.777842 |
| 2 | frequent | Frequency | 7296 | 0.405702 | 0.017492 | 0.543448 | 0.002338 | 0.778100 |
| 3 | frequent | Frequency | 7285 | 0.406314 | 0.017510 | 0.544269 | 0.002950 | 0.777359 |
| 4 | frequent | Frequency | 7292 | 0.405924 | 0.017498 | 0.543747 | 0.002560 | 0.777461 |
| 0 | frequent | TF-IDF | 7287 | 0.669137 | 0.532236 | 0.787544 | 0.013861 | 0.449287 |
| 1 | frequent | TF-IDF | 7296 | 0.672012 | 0.519935 | 0.789588 | 0.016331 | 0.450237 |
| 2 | frequent | TF-IDF | 7296 | 0.666393 | 0.521538 | 0.785910 | 0.013678 | 0.451649 |
| 3 | frequent | TF-IDF | 7285 | 0.675223 | 0.533194 | 0.792885 | 0.015616 | 0.445092 |
| 4 | frequent | TF-IDF | 7292 | 0.680197 | 0.554275 | 0.796375 | 0.021937 | 0.439139 |
| 0 | well_supported | Frequency | 5947 | 0.497898 | 0.083099 | 0.666975 | 0.094560 | 0.683289 |
| 1 | well_supported | Frequency | 5912 | 0.500846 | 0.083427 | 0.670924 | 0.097482 | 0.680317 |
| 2 | well_supported | Frequency | 5918 | 0.500169 | 0.083352 | 0.669990 | 0.096805 | 0.681032 |
| 3 | well_supported | Frequency | 5921 | 0.499916 | 0.083324 | 0.669650 | 0.096552 | 0.681331 |
| 4 | well_supported | Frequency | 5969 | 0.495895 | 0.082876 | 0.664265 | 0.092532 | 0.685110 |
| 0 | well_supported | TF-IDF | 5947 | 0.672944 | 0.151794 | 0.793341 | 0.020290 | 0.446876 |
| 1 | well_supported | TF-IDF | 5912 | 0.680480 | 0.153704 | 0.798658 | 0.020588 | 0.441053 |
| 2 | well_supported | TF-IDF | 5918 | 0.674721 | 0.166420 | 0.795849 | 0.015910 | 0.442392 |
| 3 | well_supported | TF-IDF | 5921 | 0.683162 | 0.176782 | 0.800766 | 0.024444 | 0.438416 |
| 4 | well_supported | TF-IDF | 5969 | 0.684369 | 0.164990 | 0.802452 | 0.018252 | 0.432270 |

### Six-way Category: aggregate and fold values

| Model | n | Accuracy | Macro-F1 | ECE | Brier (LEGACY) |
| --- | --- | --- | --- | --- | --- |
| Frequency | 36696 | 0.403368 +/- 0.000063 | 0.095810 +/- 0.000011 | 0.000056 +/- 0.000026 | 0.718352 +/- 0.000055 |
| TF-IDF | 36696 | 0.678466 +/- 0.004971 | 0.443702 +/- 0.010100 | 0.015568 +/- 0.003251 | 0.439337 +/- 0.004295 |

| Fold | Model | n | Accuracy | Macro-F1 | ECE | Brier (LEGACY) |
| --- | --- | --- | --- | --- | --- | --- |
| 0 | Frequency | 7340 | 0.403406 | 0.095816 | 0.000068 | 0.718347 |
| 0 | TF-IDF | 7340 | 0.677520 | 0.429049 | 0.010344 | 0.440541 |
| 1 | Frequency | 7339 | 0.403461 | 0.095825 | 0.000097 | 0.718272 |
| 1 | TF-IDF | 7339 | 0.677340 | 0.440990 | 0.015650 | 0.442007 |
| 2 | Frequency | 7339 | 0.403325 | 0.095802 | 0.000039 | 0.718358 |
| 2 | TF-IDF | 7339 | 0.671345 | 0.442586 | 0.018712 | 0.443932 |
| 3 | Frequency | 7339 | 0.403325 | 0.095802 | 0.000039 | 0.718358 |
| 3 | TF-IDF | 7339 | 0.681701 | 0.450299 | 0.015323 | 0.437136 |
| 4 | Frequency | 7339 | 0.403325 | 0.095802 | 0.000039 | 0.718426 |
| 4 | TF-IDF | 7339 | 0.684426 | 0.455585 | 0.017810 | 0.433071 |

### Random minus grouped MAP@3: all rows and well-supported subset

| Subset | Model | Random n | Grouped n | Random MAP@3 | Grouped MAP@3 | Random - grouped |
| --- | --- | --- | --- | --- | --- | --- |
| all | Frequency | 36696 | 36696 | 0.540331 +/- 0.000095 | 0.539215 +/- 0.039204 | 0.001116 |
| all | TF-IDF | 36696 | 36696 | 0.785363 +/- 0.004098 | 0.519971 +/- 0.037799 | 0.265392 |
| well_supported | Frequency | 29667 | 28187 | 0.668361 +/- 0.002719 | 0.706722 +/- 0.034859 | -0.038362 |
| well_supported | TF-IDF | 29667 | 28187 | 0.798213 +/- 0.003674 | 0.684162 +/- 0.073814 | 0.114051 |

### All 15 held-out questions: stored support and performance

| QuestionId | Fold | n | Supported share | Well-supported share | Frequency MAP@3 | TF-IDF MAP@3 |
| --- | --- | --- | --- | --- | --- | --- |
| 31772 | 0 | 4857 | 0.996706 | 0.944410 | 0.485862 | 0.486000 |
| 31774 | 2 | 3115 | 0.795506 | 0.795506 | 0.593847 | 0.566453 |
| 31777 | 4 | 2809 | 0.888216 | 0.861161 | 0.704047 | 0.708496 |
| 31778 | 1 | 3640 | 0.720604 | 0.609341 | 0.435989 | 0.453342 |
| 32829 | 0 | 2156 | 0.873840 | 0.873840 | 0.790816 | 0.676948 |
| 32833 | 3 | 3105 | 0.638003 | 0.638003 | 0.497370 | 0.493237 |
| 32835 | 1 | 2332 | 0.828902 | 0.828902 | 0.565466 | 0.444039 |
| 33471 | 4 | 1542 | 0.728923 | 0.716602 | 0.562365 | 0.519347 |
| 33472 | 3 | 2800 | 0.767143 | 0.767143 | 0.518750 | 0.570357 |
| 33474 | 2 | 1766 | 0.613250 | 0.613250 | 0.368913 | 0.388071 |
| 76870 | 3 | 1186 | 0.674536 | 0.674536 | 0.469927 | 0.484401 |
| 89443 | 4 | 3054 | 0.719712 | 0.719712 | 0.432165 | 0.484119 |
| 91695 | 2 | 2610 | 0.745211 | 0.745211 | 0.588123 | 0.519732 |
| 104665 | 0 | 673 | 0.823180 | 0.823180 | 0.718920 | 0.280832 |
| 109465 | 1 | 1051 | 0.812559 | 0.812559 | 0.588487 | 0.594355 |

## Existing descriptive uncertainty summaries

The intervals and permutation results below are copied from the finalized artifact, with no new random draws. Bootstrap intervals describe five-fold resampling only. Question associations use 15 questions and have low power; the stored two-sided permutation values are descriptive, not formal evidence.

Stored seed: `20260831`.

### explanation_only: TF-IDF minus frequency

| Split | Metric | Stored mean delta | Stored 95% descriptive interval | Resamples | Fold 0 delta | Fold 1 delta | Fold 2 delta | Fold 3 delta | Fold 4 delta |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Question-held-out | MAP@3 | -0.042362 | [-0.084242, -0.007459] | 100000 | -0.116619 | -0.048484 | -0.039492 | 0.015654 | -0.022867 |
| Question-held-out | ECE | 0.063545 | [0.013196, 0.123565] | 100000 | 0.079037 | 0.178475 | 0.003361 | 0.002405 | 0.054446 |
| Question-held-out | Brier (LEGACY) | 0.038259 | [-0.005554, 0.088568] | 100000 | 0.120263 | 0.079724 | 0.010387 | -0.021409 | 0.002331 |
| Random | MAP@3 | 0.223476 | [0.222016, 0.225597] | 100000 | 0.221639 | 0.222283 | 0.222260 | 0.223623 | 0.227574 |
| Random | ECE | 0.022626 | [0.018219, 0.026790] | 100000 | 0.022683 | 0.029611 | 0.020795 | 0.024909 | 0.015130 |
| Random | Brier (LEGACY) | -0.300161 | [-0.303921, -0.297428] | 100000 | -0.297192 | -0.297379 | -0.297997 | -0.301151 | -0.307088 |

| Model | Questions | Spearman rho | Stored two-sided permutation value | Permutations |
| --- | --- | --- | --- | --- |
| Frequency | 15 | 0.682143 | 0.005960 | 100000 |
| TF-IDF | 15 | 0.396429 | 0.144519 | 100000 |

### question_plus_explanation: TF-IDF minus frequency

| Split | Metric | Stored mean delta | Stored 95% descriptive interval | Resamples | Fold 0 delta | Fold 1 delta | Fold 2 delta | Fold 3 delta | Fold 4 delta |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Question-held-out | MAP@3 | -0.019244 | [-0.046457, 0.009284] | 100000 | -0.070214 | -0.030448 | -0.030704 | 0.020989 | 0.014157 |
| Question-held-out | ECE | 0.052252 | [0.013847, 0.095582] | 100000 | 0.119596 | 0.094109 | -0.003337 | 0.025013 | 0.025881 |
| Question-held-out | Brier (LEGACY) | 0.010671 | [-0.024278, 0.052978] | 100000 | 0.090335 | 0.025241 | -0.003057 | -0.019045 | -0.040122 |
| Random | MAP@3 | 0.245031 | [0.241963, 0.248356] | 100000 | 0.241530 | 0.244493 | 0.241132 | 0.246877 | 0.251124 |
| Random | ECE | 0.015442 | [0.013445, 0.018109] | 100000 | 0.014116 | 0.015019 | 0.012396 | 0.015305 | 0.020374 |
| Random | Brier (LEGACY) | -0.327156 | [-0.331512, -0.323940] | 100000 | -0.324241 | -0.324384 | -0.323416 | -0.328535 | -0.335203 |

| Model | Questions | Spearman rho | Stored two-sided permutation value | Permutations |
| --- | --- | --- | --- | --- |
| Frequency | 15 | 0.682143 | 0.005960 | 100000 |
| TF-IDF | 15 | 0.389286 | 0.150638 | 100000 |

The source serializes bootstrap intervals for all-row learned-minus-frequency MAP@3, ECE, and LEGACY Brier only. It contains no bootstrap intervals for stratum, Category, or random-minus-grouped comparisons; this archive does not create or imply those missing intervals.
