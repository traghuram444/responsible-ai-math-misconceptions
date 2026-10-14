# E012 complete numerical results

Equal-fold means and sample SD are descriptive only. No inferential evidence or deployment claim.

## Primary comparisons

| Comparator | MAP@3 delta mean | SD | Positive folds | Criterion |
|---|---:|---:|---:|---|
| frequency | -0.001987 | 0.003825 | 2/5 | False |
| e011_full_context | 0.025341 | 0.057834 | 3/5 | False |

Overall primary criterion met: **False**.

## Aggregate exact labels and Category

| Arm | MAP@3 | Accuracy | ECE | Corrected Brier | Category accuracy | Category macro-F1 (six) |
|---|---:|---:|---:|---:|---:|---:|
| frequency | 0.539215 | 0.402009 | 0.056271 | 0.795057 | 0.402009 | 0.095344 |
| full_context | 0.537228 | 0.402374 | 0.377470 | 0.985662 | 0.258167 | 0.068232 |

## All primary fold deltas

| Comparator | Fold 0 | Fold 1 | Fold 2 | Fold 3 | Fold 4 |
|---|---:|---:|---:|---:|---:|
| frequency | 0.000542 | 0.001258 | -0.002069 | -0.001269 | -0.008395 |
| e011_full_context | 0.038967 | 0.115501 | -0.021648 | -0.027993 | 0.021877 |

## Prespecified secondary paired differences

| Comparator | Metric | Mean | SD | Fold values |
|---|---|---:|---:|---|
| frequency | map_at_3 | -0.001987 | 0.003825 | 0.000542, 0.001258, -0.002069, -0.001269, -0.008395 |
| frequency | top1_accuracy | 0.000364 | 0.000744 | 0.000130, 0.000000, 0.000000, 0.001692, 0.000000 |
| frequency | ece | 0.321199 | 0.034060 | 0.347654, 0.277471, 0.324510, 0.297198, 0.359162 |
| frequency | brier | 0.190605 | 0.024906 | 0.221213, 0.162606, 0.194452, 0.168340, 0.206413 |
| e011_full_context | map_at_3 | 0.025341 | 0.057834 | 0.038967, 0.115501, -0.021648, -0.027993, 0.021877 |
| e011_full_context | top1_accuracy | 0.033816 | 0.080124 | 0.046578, 0.152357, -0.021092, -0.056974, 0.048211 |
| e011_full_context | ece | 0.227844 | 0.169691 | 0.377585, -0.038644, 0.285543, 0.166075, 0.348662 |
| e011_full_context | brier | 0.147578 | 0.122646 | 0.227119, -0.060658, 0.234307, 0.136340, 0.200783 |

## All fold and question support groups

| Arm | Fold | Question (all=pooled) | Stratum | n | Accuracy | MAP@3 | Macro-F1 union | ECE | Brier | Calibration exclusions |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---|
| frequency | 0 | all | all | 7686 | 0.485818 | 0.591812 | 0.040871 | 0.112647 | 0.755854 | eligible |
| frequency | 0 | all | unsupported | 407 | 0.000000 | 0.000000 | 0.000000 | null | null | correct_below_20 |
| frequency | 0 | all | rare | 0 | null | null | null | null | null | n_below_200, correct_below_20, incorrect_below_20 |
| frequency | 0 | all | frequent | 7279 | 0.512983 | 0.624903 | 0.113018 | 0.139811 | 0.730497 | eligible |
| frequency | 0 | all | well_supported | 7025 | 0.531530 | 0.647497 | 0.138823 | 0.158359 | 0.713308 | eligible |
| frequency | 0 | 31772 | all | 4857 | 0.353922 | 0.485862 | 0.065351 | 0.019249 | 0.831751 | eligible |
| frequency | 0 | 31772 | unsupported | 16 | 0.000000 | 0.000000 | 0.000000 | null | null | n_below_200, correct_below_20, incorrect_below_20 |
| frequency | 0 | 31772 | rare | 0 | null | null | null | null | null | n_below_200, correct_below_20, incorrect_below_20 |
| frequency | 0 | 31772 | frequent | 4841 | 0.355092 | 0.487468 | 0.087348 | 0.018080 | 0.830503 | eligible |
| frequency | 0 | 31772 | well_supported | 4587 | 0.374755 | 0.514461 | 0.109039 | 0.001583 | 0.809714 | eligible |
| frequency | 0 | 32829 | all | 2156 | 0.732839 | 0.790816 | 0.105728 | 0.359667 | 0.613243 | eligible |
| frequency | 0 | 32829 | unsupported | 272 | 0.000000 | 0.000000 | 0.000000 | null | null | correct_below_20 |
| frequency | 0 | 32829 | rare | 0 | null | null | null | null | null | n_below_200, correct_below_20, incorrect_below_20 |
| frequency | 0 | 32829 | frequent | 1884 | 0.838641 | 0.904989 | 0.228060 | 0.465470 | 0.527182 | eligible |
| frequency | 0 | 32829 | well_supported | 1884 | 0.838641 | 0.904989 | 0.228060 | 0.465470 | 0.527182 | eligible |
| frequency | 0 | 104665 | all | 673 | 0.646360 | 0.718920 | 0.098150 | 0.273188 | 0.664976 | eligible |
| frequency | 0 | 104665 | unsupported | 119 | 0.000000 | 0.000000 | 0.000000 | null | null | n_below_200, correct_below_20 |
| frequency | 0 | 104665 | rare | 0 | null | null | null | null | null | n_below_200, correct_below_20, incorrect_below_20 |
| frequency | 0 | 104665 | frequent | 554 | 0.785199 | 0.873345 | 0.219919 | 0.412027 | 0.548044 | eligible |
| frequency | 0 | 104665 | well_supported | 554 | 0.785199 | 0.873345 | 0.219919 | 0.412027 | 0.548044 | eligible |
| full_context | 0 | all | all | 7686 | 0.485948 | 0.592354 | 0.040993 | 0.460301 | 0.977067 | eligible |
| full_context | 0 | all | unsupported | 407 | 0.000000 | 0.000000 | 0.000000 | null | null | correct_below_20 |
| full_context | 0 | all | rare | 0 | null | null | null | null | null | n_below_200, correct_below_20, incorrect_below_20 |
| full_context | 0 | all | frequent | 7279 | 0.513120 | 0.625475 | 0.113343 | 0.487472 | 0.974351 | eligible |
| full_context | 0 | all | well_supported | 7025 | 0.531673 | 0.648090 | 0.139215 | 0.506025 | 0.974351 | eligible |
| full_context | 0 | 31772 | all | 4857 | 0.353922 | 0.486068 | 0.065351 | 0.328275 | 0.974522 | eligible |
| full_context | 0 | 31772 | unsupported | 16 | 0.000000 | 0.000000 | 0.000000 | null | null | n_below_200, correct_below_20, incorrect_below_20 |
| full_context | 0 | 31772 | rare | 0 | null | null | null | null | null | n_below_200, correct_below_20, incorrect_below_20 |
| full_context | 0 | 31772 | frequent | 4841 | 0.355092 | 0.487675 | 0.087348 | 0.329445 | 0.974353 | eligible |
| full_context | 0 | 31772 | well_supported | 4587 | 0.374755 | 0.514679 | 0.109039 | 0.349107 | 0.974353 | eligible |
| full_context | 0 | 32829 | all | 2156 | 0.733302 | 0.792285 | 0.107328 | 0.707654 | 0.980817 | eligible |
| full_context | 0 | 32829 | unsupported | 272 | 0.000000 | 0.000000 | 0.000000 | null | null | correct_below_20 |
| full_context | 0 | 32829 | rare | 0 | null | null | null | null | null | n_below_200, correct_below_20, incorrect_below_20 |
| full_context | 0 | 32829 | frequent | 1884 | 0.839172 | 0.906670 | 0.231278 | 0.813524 | 0.974346 | eligible |
| full_context | 0 | 32829 | well_supported | 1884 | 0.839172 | 0.906670 | 0.231278 | 0.813524 | 0.974346 | eligible |
| full_context | 0 | 104665 | all | 673 | 0.646360 | 0.718920 | 0.098150 | 0.620714 | 0.983420 | eligible |
| full_context | 0 | 104665 | unsupported | 119 | 0.000000 | 0.000000 | 0.000000 | null | null | n_below_200, correct_below_20 |
| full_context | 0 | 104665 | rare | 0 | null | null | null | null | null | n_below_200, correct_below_20, incorrect_below_20 |
| full_context | 0 | 104665 | frequent | 554 | 0.785199 | 0.873345 | 0.219919 | 0.759553 | 0.974351 | eligible |
| full_context | 0 | 104665 | well_supported | 554 | 0.785199 | 0.873345 | 0.219919 | 0.759553 | 0.974351 | eligible |
| frequency | 1 | all | all | 7023 | 0.358963 | 0.501804 | 0.029349 | 0.055844 | 0.823525 | eligible |
| frequency | 1 | all | unsupported | 1613 | 0.000000 | 0.000000 | 0.000000 | null | null | correct_below_20 |
| frequency | 1 | all | rare | 0 | null | null | null | null | null | n_below_200, correct_below_20, incorrect_below_20 |
| frequency | 1 | all | frequent | 5410 | 0.465989 | 0.651417 | 0.105956 | 0.051181 | 0.700869 | eligible |
| frequency | 1 | all | well_supported | 5005 | 0.503696 | 0.704129 | 0.167486 | 0.088889 | 0.658084 | eligible |
| frequency | 1 | 31778 | all | 3640 | 0.313187 | 0.435989 | 0.052999 | 0.101621 | 0.877694 | eligible |
| frequency | 1 | 31778 | unsupported | 1017 | 0.000000 | 0.000000 | 0.000000 | null | null | correct_below_20 |
| frequency | 1 | 31778 | rare | 0 | null | null | null | null | null | n_below_200, correct_below_20, incorrect_below_20 |
| frequency | 1 | 31778 | frequent | 2623 | 0.434617 | 0.605032 | 0.100983 | 0.019809 | 0.739192 | eligible |
| frequency | 1 | 31778 | well_supported | 2218 | 0.513977 | 0.715509 | 0.169744 | 0.099169 | 0.649644 | eligible |
| frequency | 1 | 32835 | all | 2332 | 0.409091 | 0.565466 | 0.052786 | 0.005717 | 0.769317 | eligible |
| frequency | 1 | 32835 | unsupported | 399 | 0.000000 | 0.000000 | 0.000000 | null | null | correct_below_20 |
| frequency | 1 | 32835 | rare | 0 | null | null | null | null | null | n_below_200, correct_below_20, incorrect_below_20 |
| frequency | 1 | 32835 | frequent | 1933 | 0.493533 | 0.682187 | 0.165223 | 0.078726 | 0.673211 | eligible |
| frequency | 1 | 32835 | well_supported | 1933 | 0.493533 | 0.682187 | 0.165223 | 0.078726 | 0.673211 | eligible |
| frequency | 1 | 109465 | all | 1051 | 0.406280 | 0.588487 | 0.096301 | 0.008528 | 0.756196 | eligible |
| frequency | 1 | 109465 | unsupported | 197 | 0.000000 | 0.000000 | 0.000000 | null | null | n_below_200, correct_below_20 |
| frequency | 1 | 109465 | rare | 0 | null | null | null | null | null | n_below_200, correct_below_20, incorrect_below_20 |
| frequency | 1 | 109465 | frequent | 854 | 0.500000 | 0.724239 | 0.166667 | 0.085192 | 0.645766 | eligible |
| frequency | 1 | 109465 | well_supported | 854 | 0.500000 | 0.724239 | 0.166667 | 0.085192 | 0.645766 | eligible |
| full_context | 1 | all | all | 7023 | 0.358963 | 0.503061 | 0.029742 | 0.333316 | 0.986131 | eligible |
| full_context | 1 | all | unsupported | 1613 | 0.000000 | 0.000000 | 0.000000 | null | null | correct_below_20 |
| full_context | 1 | all | rare | 0 | null | null | null | null | null | n_below_200, correct_below_20, incorrect_below_20 |
| full_context | 1 | all | frequent | 5410 | 0.465989 | 0.653050 | 0.107133 | 0.440341 | 0.974351 | eligible |
| full_context | 1 | all | well_supported | 5005 | 0.503696 | 0.705894 | 0.169267 | 0.478049 | 0.974350 | eligible |
| full_context | 1 | 31778 | all | 3640 | 0.313187 | 0.438324 | 0.052999 | 0.287536 | 0.988679 | eligible |
| full_context | 1 | 31778 | unsupported | 1017 | 0.000000 | 0.000000 | 0.000000 | null | null | correct_below_20 |
| full_context | 1 | 31778 | rare | 0 | null | null | null | null | null | n_below_200, correct_below_20, incorrect_below_20 |
| full_context | 1 | 31778 | frequent | 2623 | 0.434617 | 0.608273 | 0.100983 | 0.408966 | 0.974348 | eligible |
| full_context | 1 | 31778 | well_supported | 2218 | 0.513977 | 0.719342 | 0.169744 | 0.488326 | 0.974346 | eligible |
| full_context | 1 | 32835 | all | 2332 | 0.409091 | 0.565609 | 0.052802 | 0.383446 | 0.983128 | eligible |
| full_context | 1 | 32835 | unsupported | 399 | 0.000000 | 0.000000 | 0.000000 | null | null | correct_below_20 |
| full_context | 1 | 32835 | rare | 0 | null | null | null | null | null | n_below_200, correct_below_20, incorrect_below_20 |
| full_context | 1 | 32835 | frequent | 1933 | 0.493533 | 0.682359 | 0.165281 | 0.467888 | 0.974353 | eligible |
| full_context | 1 | 32835 | well_supported | 1933 | 0.493533 | 0.682359 | 0.165281 | 0.467888 | 0.974353 | eligible |
| full_context | 1 | 109465 | all | 1051 | 0.406280 | 0.588487 | 0.100624 | 0.380637 | 0.983969 | eligible |
| full_context | 1 | 109465 | unsupported | 197 | 0.000000 | 0.000000 | 0.000000 | null | null | n_below_200, correct_below_20 |
| full_context | 1 | 109465 | rare | 0 | null | null | null | null | null | n_below_200, correct_below_20, incorrect_below_20 |
| full_context | 1 | 109465 | frequent | 854 | 0.500000 | 0.724239 | 0.173098 | 0.474357 | 0.974356 | eligible |
| full_context | 1 | 109465 | well_supported | 854 | 0.500000 | 0.724239 | 0.173098 | 0.474357 | 0.974356 | eligible |
| frequency | 2 | all | all | 7491 | 0.395408 | 0.538824 | 0.031485 | 0.045889 | 0.793789 | eligible |
| frequency | 2 | all | unsupported | 1985 | 0.000000 | 0.000000 | 0.000000 | null | null | correct_below_20 |
| frequency | 2 | all | rare | 0 | null | null | null | null | null | n_below_200, correct_below_20, incorrect_below_20 |
| frequency | 2 | all | frequent | 5506 | 0.537959 | 0.733079 | 0.174894 | 0.096662 | 0.628435 | eligible |
| frequency | 2 | all | well_supported | 5506 | 0.537959 | 0.733079 | 0.174894 | 0.096662 | 0.628435 | eligible |
| frequency | 2 | 31774 | all | 3115 | 0.451043 | 0.593847 | 0.062168 | 0.009746 | 0.744183 | eligible |
| frequency | 2 | 31774 | unsupported | 637 | 0.000000 | 0.000000 | 0.000000 | null | null | correct_below_20 |
| frequency | 2 | 31774 | rare | 0 | null | null | null | null | null | n_below_200, correct_below_20, incorrect_below_20 |
| frequency | 2 | 31774 | frequent | 2478 | 0.566990 | 0.746503 | 0.180917 | 0.125693 | 0.613528 | eligible |
| frequency | 2 | 31774 | well_supported | 2478 | 0.566990 | 0.746503 | 0.180917 | 0.125693 | 0.613528 | eligible |
| frequency | 2 | 33474 | all | 1766 | 0.182899 | 0.368913 | 0.038655 | 0.258398 | 0.950089 | eligible |
| frequency | 2 | 33474 | unsupported | 683 | 0.000000 | 0.000000 | 0.000000 | null | null | correct_below_20 |
| frequency | 2 | 33474 | rare | 0 | null | null | null | null | null | n_below_200, correct_below_20, incorrect_below_20 |
| frequency | 2 | 33474 | frequent | 1083 | 0.298246 | 0.601570 | 0.114865 | 0.143051 | 0.759404 | eligible |
| frequency | 2 | 33474 | well_supported | 1083 | 0.298246 | 0.601570 | 0.114865 | 0.143051 | 0.759404 | eligible |
| frequency | 2 | 91695 | all | 2610 | 0.472797 | 0.588123 | 0.080255 | 0.031500 | 0.747236 | eligible |
| frequency | 2 | 91695 | unsupported | 665 | 0.000000 | 0.000000 | 0.000000 | null | null | correct_below_20 |
| frequency | 2 | 91695 | rare | 0 | null | null | null | null | null | n_below_200, correct_below_20, incorrect_below_20 |
| frequency | 2 | 91695 | frequent | 1945 | 0.634447 | 0.789203 | 0.194086 | 0.193150 | 0.574502 | eligible |
| frequency | 2 | 91695 | well_supported | 1945 | 0.634447 | 0.789203 | 0.194086 | 0.193150 | 0.574502 | eligible |
| full_context | 2 | all | all | 7491 | 0.395408 | 0.536755 | 0.031485 | 0.370399 | 0.988241 | eligible |
| full_context | 2 | all | unsupported | 1985 | 0.000000 | 0.000000 | 0.000000 | null | null | correct_below_20 |
| full_context | 2 | all | rare | 0 | null | null | null | null | null | n_below_200, correct_below_20, incorrect_below_20 |
| full_context | 2 | all | frequent | 5506 | 0.537959 | 0.730264 | 0.174894 | 0.512950 | 0.974988 | eligible |
| full_context | 2 | all | well_supported | 5506 | 0.537959 | 0.730264 | 0.174894 | 0.512950 | 0.974988 | eligible |
| full_context | 2 | 31774 | all | 3115 | 0.451043 | 0.596415 | 0.062168 | 0.426033 | 0.985214 | eligible |
| full_context | 2 | 31774 | unsupported | 637 | 0.000000 | 0.000000 | 0.000000 | null | null | correct_below_20 |
| full_context | 2 | 31774 | rare | 0 | null | null | null | null | null | n_below_200, correct_below_20, incorrect_below_20 |
| full_context | 2 | 31774 | frequent | 2478 | 0.566990 | 0.749731 | 0.180917 | 0.541979 | 0.974986 | eligible |
| full_context | 2 | 31774 | well_supported | 2478 | 0.566990 | 0.749731 | 0.180917 | 0.541979 | 0.974986 | eligible |
| full_context | 2 | 33474 | all | 1766 | 0.182899 | 0.354473 | 0.038655 | 0.157889 | 0.994331 | eligible |
| full_context | 2 | 33474 | unsupported | 683 | 0.000000 | 0.000000 | 0.000000 | null | null | correct_below_20 |
| full_context | 2 | 33474 | rare | 0 | null | null | null | null | null | n_below_200, correct_below_20, incorrect_below_20 |
| full_context | 2 | 33474 | frequent | 1083 | 0.298246 | 0.578024 | 0.114865 | 0.273236 | 0.974990 | eligible |
| full_context | 2 | 33474 | well_supported | 1083 | 0.298246 | 0.578024 | 0.114865 | 0.273236 | 0.974990 | eligible |
| full_context | 2 | 91695 | all | 2610 | 0.472797 | 0.588889 | 0.080255 | 0.447791 | 0.987733 | eligible |
| full_context | 2 | 91695 | unsupported | 665 | 0.000000 | 0.000000 | 0.000000 | null | null | correct_below_20 |
| full_context | 2 | 91695 | rare | 0 | null | null | null | null | null | n_below_200, correct_below_20, incorrect_below_20 |
| full_context | 2 | 91695 | frequent | 1945 | 0.634447 | 0.790231 | 0.194086 | 0.609441 | 0.974991 | eligible |
| full_context | 2 | 91695 | well_supported | 1945 | 0.634447 | 0.790231 | 0.194086 | 0.609441 | 0.974991 | eligible |
| frequency | 3 | all | all | 7091 | 0.368777 | 0.501222 | 0.028360 | 0.048873 | 0.822135 | eligible |
| frequency | 3 | all | unsupported | 2162 | 0.000000 | 0.000000 | 0.000000 | null | null | correct_below_20 |
| frequency | 3 | all | rare | 0 | null | null | null | null | null | n_below_200, correct_below_20, incorrect_below_20 |
| frequency | 3 | all | frequent | 4929 | 0.530534 | 0.721073 | 0.173317 | 0.112883 | 0.641079 | eligible |
| frequency | 3 | all | well_supported | 4929 | 0.530534 | 0.721073 | 0.173317 | 0.112883 | 0.641079 | eligible |
| frequency | 3 | 32833 | all | 3105 | 0.397746 | 0.497370 | 0.063236 | 0.019905 | 0.824189 | eligible |
| frequency | 3 | 32833 | unsupported | 1124 | 0.000000 | 0.000000 | 0.000000 | null | null | correct_below_20 |
| frequency | 3 | 32833 | rare | 0 | null | null | null | null | null | n_below_200, correct_below_20, incorrect_below_20 |
| frequency | 3 | 32833 | frequent | 1981 | 0.623423 | 0.779573 | 0.192009 | 0.205772 | 0.591150 | eligible |
| frequency | 3 | 32833 | well_supported | 1981 | 0.623423 | 0.779573 | 0.192009 | 0.205772 | 0.591150 | eligible |
| frequency | 3 | 33472 | all | 2800 | 0.362143 | 0.518750 | 0.053173 | 0.055508 | 0.806528 | eligible |
| frequency | 3 | 33472 | unsupported | 652 | 0.000000 | 0.000000 | 0.000000 | null | null | correct_below_20 |
| frequency | 3 | 33472 | rare | 0 | null | null | null | null | null | n_below_200, correct_below_20, incorrect_below_20 |
| frequency | 3 | 33472 | frequent | 2148 | 0.472067 | 0.676210 | 0.160342 | 0.054416 | 0.676497 | eligible |
| frequency | 3 | 33472 | well_supported | 2148 | 0.472067 | 0.676210 | 0.160342 | 0.054416 | 0.676497 | eligible |
| frequency | 3 | 76870 | all | 1186 | 0.308600 | 0.469927 | 0.058956 | 0.109050 | 0.853601 | eligible |
| frequency | 3 | 76870 | unsupported | 386 | 0.000000 | 0.000000 | 0.000000 | null | null | correct_below_20 |
| frequency | 3 | 76870 | rare | 0 | null | null | null | null | null | n_below_200, correct_below_20, incorrect_below_20 |
| frequency | 3 | 76870 | frequent | 800 | 0.457500 | 0.696667 | 0.156947 | 0.039849 | 0.669619 | eligible |
| frequency | 3 | 76870 | well_supported | 800 | 0.457500 | 0.696667 | 0.156947 | 0.039849 | 0.669619 | eligible |
| full_context | 3 | all | all | 7091 | 0.370470 | 0.499953 | 0.029504 | 0.346071 | 0.990475 | eligible |
| full_context | 3 | all | unsupported | 2162 | 0.000000 | 0.000000 | 0.000000 | null | null | correct_below_20 |
| full_context | 3 | all | rare | 0 | null | null | null | null | null | n_below_200, correct_below_20, incorrect_below_20 |
| full_context | 3 | all | frequent | 4929 | 0.532968 | 0.719247 | 0.178870 | 0.508570 | 0.975598 | eligible |
| full_context | 3 | all | well_supported | 4929 | 0.532968 | 0.719247 | 0.178870 | 0.508570 | 0.975598 | eligible |
| full_context | 3 | 32833 | all | 3105 | 0.397746 | 0.492646 | 0.063236 | 0.373346 | 0.993259 | eligible |
| full_context | 3 | 32833 | unsupported | 1124 | 0.000000 | 0.000000 | 0.000000 | null | null | correct_below_20 |
| full_context | 3 | 32833 | rare | 0 | null | null | null | null | null | n_below_200, correct_below_20, incorrect_below_20 |
| full_context | 3 | 32833 | frequent | 1981 | 0.623423 | 0.772169 | 0.192009 | 0.599023 | 0.975596 | eligible |
| full_context | 3 | 32833 | well_supported | 1981 | 0.623423 | 0.772169 | 0.192009 | 0.599023 | 0.975596 | eligible |
| full_context | 3 | 33472 | all | 2800 | 0.366429 | 0.520893 | 0.058461 | 0.342030 | 0.986960 | eligible |
| full_context | 3 | 33472 | unsupported | 652 | 0.000000 | 0.000000 | 0.000000 | null | null | correct_below_20 |
| full_context | 3 | 33472 | rare | 0 | null | null | null | null | null | n_below_200, correct_below_20, incorrect_below_20 |
| full_context | 3 | 33472 | frequent | 2148 | 0.477654 | 0.679004 | 0.173769 | 0.453255 | 0.975599 | eligible |
| full_context | 3 | 33472 | well_supported | 2148 | 0.477654 | 0.679004 | 0.173769 | 0.453255 | 0.975599 | eligible |
| full_context | 3 | 76870 | all | 1186 | 0.308600 | 0.469646 | 0.058956 | 0.284205 | 0.991482 | eligible |
| full_context | 3 | 76870 | unsupported | 386 | 0.000000 | 0.000000 | 0.000000 | null | null | correct_below_20 |
| full_context | 3 | 76870 | rare | 0 | null | null | null | null | null | n_below_200, correct_below_20, incorrect_below_20 |
| full_context | 3 | 76870 | frequent | 800 | 0.457500 | 0.696250 | 0.156947 | 0.433105 | 0.975603 | eligible |
| full_context | 3 | 76870 | well_supported | 800 | 0.457500 | 0.696250 | 0.156947 | 0.433105 | 0.975603 | eligible |
| frequency | 4 | all | all | 7405 | 0.401080 | 0.562413 | 0.047711 | 0.018103 | 0.779983 | eligible |
| frequency | 4 | all | unsupported | 1588 | 0.000000 | 0.000000 | 0.000000 | null | null | correct_below_20 |
| frequency | 4 | all | rare | 0 | null | null | null | null | null | n_below_200, correct_below_20, incorrect_below_20 |
| frequency | 4 | all | frequent | 5817 | 0.510572 | 0.715948 | 0.135200 | 0.091389 | 0.657173 | eligible |
| frequency | 4 | all | well_supported | 5722 | 0.519049 | 0.727834 | 0.170847 | 0.099866 | 0.649938 | eligible |
| frequency | 4 | 31777 | all | 2809 | 0.579566 | 0.704047 | 0.104833 | 0.160382 | 0.656059 | eligible |
| frequency | 4 | 31777 | unsupported | 314 | 0.000000 | 0.000000 | 0.000000 | null | null | correct_below_20 |
| frequency | 4 | 31777 | rare | 0 | null | null | null | null | null | n_below_200, correct_below_20, incorrect_below_20 |
| frequency | 4 | 31777 | frequent | 2495 | 0.652505 | 0.792652 | 0.157943 | 0.233322 | 0.583847 | eligible |
| frequency | 4 | 31777 | well_supported | 2419 | 0.673005 | 0.817555 | 0.201137 | 0.253822 | 0.567852 | eligible |
| frequency | 4 | 33471 | all | 1542 | 0.454604 | 0.562365 | 0.089294 | 0.035421 | 0.770777 | eligible |
| frequency | 4 | 33471 | unsupported | 418 | 0.000000 | 0.000000 | 0.000000 | null | null | correct_below_20 |
| frequency | 4 | 33471 | rare | 0 | null | null | null | null | null | n_below_200, correct_below_20, incorrect_below_20 |
| frequency | 4 | 33471 | frequent | 1124 | 0.623665 | 0.771501 | 0.153644 | 0.204482 | 0.600056 | eligible |
| frequency | 4 | 33471 | well_supported | 1105 | 0.634389 | 0.784766 | 0.194075 | 0.215206 | 0.591581 | eligible |
| frequency | 4 | 89443 | all | 3054 | 0.209889 | 0.432165 | 0.043369 | 0.209295 | 0.898613 | eligible |
| frequency | 4 | 89443 | unsupported | 856 | 0.000000 | 0.000000 | 0.000000 | null | null | correct_below_20 |
| frequency | 4 | 89443 | rare | 0 | null | null | null | null | null | n_below_200, correct_below_20, incorrect_below_20 |
| frequency | 4 | 89443 | frequent | 2198 | 0.291629 | 0.600470 | 0.112892 | 0.127554 | 0.769616 | eligible |
| frequency | 4 | 89443 | well_supported | 2198 | 0.291629 | 0.600470 | 0.112892 | 0.127554 | 0.769616 | eligible |
| full_context | 4 | all | all | 7405 | 0.401080 | 0.554018 | 0.047711 | 0.377265 | 0.986396 | eligible |
| full_context | 4 | all | unsupported | 1588 | 0.000000 | 0.000000 | 0.000000 | null | null | correct_below_20 |
| full_context | 4 | all | rare | 0 | null | null | null | null | null | n_below_200, correct_below_20, incorrect_below_20 |
| full_context | 4 | all | frequent | 5817 | 0.510572 | 0.705260 | 0.135200 | 0.486757 | 0.976183 | eligible |
| full_context | 4 | all | well_supported | 5722 | 0.519049 | 0.713067 | 0.170847 | 0.495234 | 0.976183 | eligible |
| full_context | 4 | 31777 | all | 2809 | 0.579566 | 0.700961 | 0.104833 | 0.555750 | 0.981504 | eligible |
| full_context | 4 | 31777 | unsupported | 314 | 0.000000 | 0.000000 | 0.000000 | null | null | correct_below_20 |
| full_context | 4 | 31777 | rare | 0 | null | null | null | null | null | n_below_200, correct_below_20, incorrect_below_20 |
| full_context | 4 | 31777 | frequent | 2495 | 0.652505 | 0.789178 | 0.157943 | 0.628689 | 0.976180 | eligible |
| full_context | 4 | 31777 | well_supported | 2419 | 0.673005 | 0.804740 | 0.201137 | 0.649189 | 0.976180 | eligible |
| full_context | 4 | 33471 | all | 1542 | 0.454604 | 0.560852 | 0.089294 | 0.430790 | 0.989093 | eligible |
| full_context | 4 | 33471 | unsupported | 418 | 0.000000 | 0.000000 | 0.000000 | null | null | correct_below_20 |
| full_context | 4 | 33471 | rare | 0 | null | null | null | null | null | n_below_200, correct_below_20, incorrect_below_20 |
| full_context | 4 | 33471 | frequent | 1124 | 0.623665 | 0.769425 | 0.153644 | 0.599851 | 0.976183 | eligible |
| full_context | 4 | 33471 | well_supported | 1105 | 0.634389 | 0.782655 | 0.194075 | 0.610575 | 0.976183 | eligible |
| full_context | 4 | 89443 | all | 3054 | 0.209889 | 0.415411 | 0.043369 | 0.186074 | 0.989534 | eligible |
| full_context | 4 | 89443 | unsupported | 856 | 0.000000 | 0.000000 | 0.000000 | null | null | correct_below_20 |
| full_context | 4 | 89443 | rare | 0 | null | null | null | null | null | n_below_200, correct_below_20, incorrect_below_20 |
| full_context | 4 | 89443 | frequent | 2198 | 0.291629 | 0.577191 | 0.112892 | 0.267814 | 0.976185 | eligible |
| full_context | 4 | 89443 | well_supported | 2198 | 0.291629 | 0.577191 | 0.112892 | 0.267814 | 0.976185 | eligible |

## All fold and question Category results

| Arm | Fold | Question | n | Accuracy | Macro-F1 six |
|---|---:|---|---:|---:|---:|
| frequency | 0 | all | 7686 | 0.485818 | 0.108990 |
| frequency | 0 | 31772 | 4857 | 0.353922 | 0.087135 |
| frequency | 0 | 32829 | 2156 | 0.732839 | 0.140971 |
| frequency | 0 | 104665 | 673 | 0.646360 | 0.130866 |
| full_context | 0 | all | 7686 | 0.259042 | 0.068582 |
| full_context | 0 | 31772 | 4857 | 0.330451 | 0.082792 |
| full_context | 0 | 32829 | 2156 | 0.125696 | 0.037220 |
| full_context | 0 | 104665 | 673 | 0.170877 | 0.048646 |
| frequency | 1 | all | 7023 | 0.358963 | 0.088048 |
| frequency | 1 | 31778 | 3640 | 0.313187 | 0.079498 |
| frequency | 1 | 32835 | 2332 | 0.409091 | 0.096774 |
| frequency | 1 | 109465 | 1051 | 0.406280 | 0.096301 |
| full_context | 1 | all | 7023 | 0.266695 | 0.070181 |
| full_context | 1 | 31778 | 3640 | 0.356044 | 0.087520 |
| full_context | 1 | 32835 | 2332 | 0.162950 | 0.046706 |
| full_context | 1 | 109465 | 1051 | 0.187441 | 0.052618 |
| frequency | 2 | all | 7491 | 0.395408 | 0.094455 |
| frequency | 2 | 31774 | 3115 | 0.451043 | 0.103614 |
| frequency | 2 | 33474 | 1766 | 0.182899 | 0.051540 |
| frequency | 2 | 91695 | 2610 | 0.472797 | 0.107007 |
| full_context | 2 | all | 7491 | 0.258844 | 0.068540 |
| full_context | 2 | 31774 | 3115 | 0.198074 | 0.055109 |
| full_context | 2 | 33474 | 1766 | 0.382786 | 0.092274 |
| full_context | 2 | 91695 | 2610 | 0.247510 | 0.066134 |
| frequency | 3 | all | 7091 | 0.368777 | 0.089807 |
| frequency | 3 | 32833 | 3105 | 0.397746 | 0.094854 |
| frequency | 3 | 33472 | 2800 | 0.362143 | 0.088621 |
| frequency | 3 | 76870 | 1186 | 0.308600 | 0.078608 |
| full_context | 3 | all | 7091 | 0.301932 | 0.077304 |
| full_context | 3 | 32833 | 3105 | 0.358454 | 0.087956 |
| full_context | 3 | 33472 | 2800 | 0.230357 | 0.062409 |
| full_context | 3 | 76870 | 1186 | 0.322934 | 0.081368 |
| frequency | 4 | all | 7405 | 0.401080 | 0.095422 |
| frequency | 4 | 31777 | 2809 | 0.579566 | 0.122305 |
| frequency | 4 | 33471 | 1542 | 0.454604 | 0.104176 |
| frequency | 4 | 89443 | 3054 | 0.209889 | 0.057826 |
| full_context | 4 | all | 7405 | 0.204321 | 0.056552 |
| full_context | 4 | 31777 | 2809 | 0.138839 | 0.040638 |
| full_context | 4 | 33471 | 1542 | 0.279507 | 0.072816 |
| full_context | 4 | 89443 | 3054 | 0.226588 | 0.061577 |

## Every fixed review budget and fold

| Arm | Fold | Review % | Retained n | Risk | MAP@3 | ECE | Brier |
|---|---:|---:|---:|---:|---:|---:|---:|
| frequency | 0 | 0 | 7686 | 0.514182 | 0.591812 | 0.112647 | 0.755854 |
| frequency | 0 | 10 | 6918 | 0.513877 | 0.593380 | 0.112952 | 0.754674 |
| frequency | 0 | 20 | 6149 | 0.515043 | 0.592942 | 0.111785 | 0.755079 |
| frequency | 0 | 30 | 5381 | 0.512730 | 0.595986 | 0.114098 | 0.752794 |
| frequency | 0 | 40 | 4612 | 0.510191 | 0.598620 | 0.116638 | 0.750879 |
| frequency | 0 | 50 | 3843 | 0.513401 | 0.596192 | 0.113427 | 0.752719 |
| full_context | 0 | 0 | 7686 | 0.514052 | 0.592354 | 0.460301 | 0.977067 |
| full_context | 0 | 10 | 6918 | 0.516334 | 0.588441 | 0.458018 | 0.976434 |
| full_context | 0 | 20 | 6149 | 0.485120 | 0.618718 | 0.489233 | 0.976327 |
| full_context | 0 | 30 | 5381 | 0.444155 | 0.655392 | 0.530197 | 0.976399 |
| full_context | 0 | 40 | 4612 | 0.398092 | 0.693192 | 0.576260 | 0.976440 |
| full_context | 0 | 50 | 3843 | 0.353630 | 0.730636 | 0.620722 | 0.976470 |
| frequency | 1 | 0 | 7023 | 0.641037 | 0.501804 | 0.055844 | 0.823525 |
| frequency | 1 | 10 | 6321 | 0.642778 | 0.500026 | 0.057586 | 0.824955 |
| frequency | 1 | 20 | 5619 | 0.640861 | 0.501987 | 0.055669 | 0.823350 |
| frequency | 1 | 30 | 4917 | 0.643075 | 0.499695 | 0.057883 | 0.825261 |
| frequency | 1 | 40 | 4214 | 0.645230 | 0.499011 | 0.060038 | 0.825864 |
| frequency | 1 | 50 | 3512 | 0.645501 | 0.499525 | 0.060309 | 0.825560 |
| full_context | 1 | 0 | 7023 | 0.641037 | 0.503061 | 0.333316 | 0.986131 |
| full_context | 1 | 10 | 6321 | 0.646575 | 0.491721 | 0.327777 | 0.986579 |
| full_context | 1 | 20 | 5619 | 0.654031 | 0.481729 | 0.320320 | 0.986901 |
| full_context | 1 | 30 | 4917 | 0.661176 | 0.471832 | 0.313175 | 0.987305 |
| full_context | 1 | 40 | 4214 | 0.669435 | 0.459658 | 0.304915 | 0.987786 |
| full_context | 1 | 50 | 3512 | 0.673121 | 0.441676 | 0.301228 | 0.988880 |
| frequency | 2 | 0 | 7491 | 0.604592 | 0.538824 | 0.045889 | 0.793789 |
| frequency | 2 | 10 | 6742 | 0.602937 | 0.540146 | 0.044234 | 0.792633 |
| frequency | 2 | 20 | 5993 | 0.601201 | 0.541354 | 0.042498 | 0.791444 |
| frequency | 2 | 30 | 5244 | 0.601831 | 0.540427 | 0.043128 | 0.792258 |
| frequency | 2 | 40 | 4495 | 0.601780 | 0.540860 | 0.043077 | 0.791877 |
| frequency | 2 | 50 | 3746 | 0.606781 | 0.535549 | 0.048078 | 0.796601 |
| full_context | 2 | 0 | 7491 | 0.604592 | 0.536755 | 0.370399 | 0.988241 |
| full_context | 2 | 10 | 6742 | 0.611540 | 0.529393 | 0.363451 | 0.988600 |
| full_context | 2 | 20 | 5993 | 0.618555 | 0.526225 | 0.356435 | 0.988473 |
| full_context | 2 | 30 | 5244 | 0.623188 | 0.523074 | 0.351801 | 0.988454 |
| full_context | 2 | 40 | 4495 | 0.641602 | 0.506007 | 0.333388 | 0.989229 |
| full_context | 2 | 50 | 3746 | 0.621997 | 0.511746 | 0.352992 | 0.990059 |
| frequency | 3 | 0 | 7091 | 0.631223 | 0.501222 | 0.048873 | 0.822135 |
| frequency | 3 | 10 | 6382 | 0.631934 | 0.500392 | 0.049584 | 0.822824 |
| frequency | 3 | 20 | 5673 | 0.633175 | 0.499412 | 0.050825 | 0.823753 |
| frequency | 3 | 30 | 4964 | 0.631144 | 0.500168 | 0.048795 | 0.822993 |
| frequency | 3 | 40 | 4255 | 0.630552 | 0.500627 | 0.048203 | 0.822585 |
| frequency | 3 | 50 | 3546 | 0.631698 | 0.500611 | 0.049348 | 0.822761 |
| full_context | 3 | 0 | 7091 | 0.629530 | 0.499953 | 0.346071 | 0.990475 |
| full_context | 3 | 10 | 6382 | 0.611877 | 0.511804 | 0.363724 | 0.990139 |
| full_context | 3 | 20 | 5673 | 0.596862 | 0.517598 | 0.378738 | 0.990313 |
| full_context | 3 | 30 | 4964 | 0.579573 | 0.524409 | 0.396027 | 0.990626 |
| full_context | 3 | 40 | 4255 | 0.560752 | 0.535018 | 0.414848 | 0.990675 |
| full_context | 3 | 50 | 3546 | 0.542583 | 0.544651 | 0.433016 | 0.990855 |
| frequency | 4 | 0 | 7405 | 0.598920 | 0.562413 | 0.018103 | 0.779983 |
| frequency | 4 | 10 | 6665 | 0.598050 | 0.562891 | 0.017233 | 0.779532 |
| frequency | 4 | 20 | 5924 | 0.597063 | 0.563611 | 0.016246 | 0.778807 |
| frequency | 4 | 30 | 5184 | 0.595486 | 0.564525 | 0.014669 | 0.777913 |
| frequency | 4 | 40 | 4443 | 0.595994 | 0.562158 | 0.015177 | 0.779515 |
| frequency | 4 | 50 | 3703 | 0.594113 | 0.561797 | 0.013296 | 0.779434 |
| full_context | 4 | 0 | 7405 | 0.598920 | 0.554018 | 0.377265 | 0.986396 |
| full_context | 4 | 10 | 6665 | 0.585296 | 0.561565 | 0.390888 | 0.986465 |
| full_context | 4 | 20 | 5924 | 0.568028 | 0.574330 | 0.408156 | 0.986264 |
| full_context | 4 | 30 | 5184 | 0.552469 | 0.585680 | 0.423715 | 0.986058 |
| full_context | 4 | 40 | 4443 | 0.534324 | 0.595806 | 0.441860 | 0.986161 |
| full_context | 4 | 50 | 3703 | 0.505806 | 0.613016 | 0.470378 | 0.985982 |

## Aggregate input diagnostics

| Question | n | Blank selected answer | Zero word tokens in selected answer |
|---|---:|---:|---:|
| all | 36696 | 0 | 9502 |
| 31772 | 4857 | 0 | 0 |
| 31774 | 3115 | 0 | 659 |
| 31777 | 2809 | 0 | 0 |
| 31778 | 3640 | 0 | 3640 |
| 32829 | 2156 | 0 | 248 |
| 32833 | 3105 | 0 | 0 |
| 32835 | 2332 | 0 | 2152 |
| 33471 | 1542 | 0 | 668 |
| 33472 | 2800 | 0 | 0 |
| 33474 | 1766 | 0 | 0 |
| 76870 | 1186 | 0 | 275 |
| 89443 | 3054 | 0 | 1860 |
| 91695 | 2610 | 0 | 0 |
| 104665 | 673 | 0 | 0 |
| 109465 | 1051 | 0 | 0 |

## Provenance

```json
{
  "git_revision": "99ff908b8489c15701d71915e731a5f990b9e45f",
  "docker_image_id": "sha256:464fc81faf49a6355e4bd0f55956243cc0fee586f657937f495975c2268e6fe0",
  "lock_sha256": "05a203f9fe979213820ceed3a1e9723bf98cc159c74d8d21a6c9f0656235c094",
  "data_sha256": "0a5e4523ec9b1656b979002a58e7cb743d02c9ac2697cc154008f971d413686c",
  "manifest_sha256": "93a25f33389b68487c09c5e9b34cfd10ca0d03b9b6438a53e2c385b2e87a7b94",
  "assignments_sha256": "b0211bafc055aedcd334877782d8db818a7c0a05873f1826ad32f0c17a61c9dd",
  "e011_sha256": "98d48fb1b9143d3f9a9c461d7b28eb89b8a9d873722b0cd622b1cf18ddb20c87",
  "started_utc": "2026-10-14T01:38:06.352267+00:00",
  "finished_utc": "2026-10-14T01:45:02.014665+00:00",
  "wall_seconds": 415.69920248771086,
  "uid": 10001,
  "gid": 10001,
  "seed": 20260831,
  "model_fits": 95,
  "fit_warnings": 0,
  "preserved_files": 163,
  "preservation_verified": true,
  "global_freeze_verified": true,
  "reproduction_checks": 15,
  "frozen_development_sha256": "a7aa03771f2807732a95297ff0d27a4ef70ccfcc0e9831b9edfda9c4dd5b82f0",
  "row_level_outputs": false
}
```

The accompanying aggregate JSON includes full five-value summary statistics, selection scores, temperatures, counts and eligibility. No row-level prediction, response, selected-answer text or fitted parameter is published.
