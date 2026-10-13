# E011 complete numerical results

Equal-fold means and sample SD are descriptive only. No inferential evidence or deployment claim.

## Primary comparisons

| Comparator | MAP@3 delta mean | SD | Positive folds | Criterion |
|---|---:|---:|---:|---|
| frequency | -0.027328 | 0.056586 | 2/5 | False |
| question_plus_explanation | -0.008084 | 0.055319 | 3/5 | False |

Overall primary criterion met: **False**.

## Aggregate exact labels and Category

| Arm | MAP@3 | Accuracy | ECE | Corrected Brier | Category accuracy | Category macro-F1 (six) |
|---|---:|---:|---:|---:|---:|---:|
| frequency | 0.539215 | 0.402009 | 0.056271 | 0.795057 | 0.402009 | 0.095344 |
| full_context | 0.511887 | 0.368558 | 0.149626 | 0.838084 | 0.369042 | 0.182615 |
| question_plus_answer | 0.433872 | 0.247739 | 0.122322 | 0.882256 | 0.276756 | 0.102283 |
| question_plus_explanation | 0.519971 | 0.376306 | 0.108524 | 0.805728 | 0.379677 | 0.185476 |

## All primary fold deltas

| Comparator | Fold 0 | Fold 1 | Fold 2 | Fold 3 | Fold 4 |
|---|---:|---:|---:|---:|---:|
| frequency | -0.038425 | -0.114244 | 0.019579 | 0.026724 | -0.030272 |
| question_plus_explanation | 0.031789 | -0.083796 | 0.050283 | 0.005735 | -0.044429 |

## Prespecified secondary paired differences

| Comparator | Metric | Mean | SD | Fold values |
|---|---|---:|---:|---|
| frequency | map_at_3 | -0.027328 | 0.056586 | -0.038425, -0.114244, 0.019579, 0.026724, -0.030272 |
| frequency | top1_accuracy | -0.033451 | 0.080601 | -0.046448, -0.152357, 0.021092, 0.058666, -0.048211 |
| frequency | ece | 0.093355 | 0.137905 | -0.029930, 0.316115, 0.038967, 0.131123, 0.010500 |
| frequency | brier | 0.043027 | 0.104007 | -0.005906, 0.223264, -0.039855, 0.032000, 0.005630 |
| question_plus_explanation | map_at_3 | -0.008084 | 0.055319 | 0.031789, -0.083796, 0.050283, 0.005735, -0.044429 |
| question_plus_explanation | top1_accuracy | -0.007748 | 0.074321 | 0.047229, -0.093692, 0.066346, 0.022000, -0.080621 |
| question_plus_explanation | ece | 0.041103 | 0.138278 | -0.149526, 0.222006, 0.042304, 0.106110, -0.015381 |
| question_plus_explanation | brier | 0.032356 | 0.111011 | -0.096242, 0.198024, -0.036798, 0.051044, 0.045752 |
| question_plus_answer | map_at_3 | 0.078015 | 0.118072 | 0.261601, -0.064977, 0.044387, 0.089668, 0.059397 |
| question_plus_answer | top1_accuracy | 0.120819 | 0.126516 | 0.297294, -0.053823, 0.081565, 0.147934, 0.131128 |
| question_plus_answer | ece | 0.027304 | 0.144651 | -0.001755, 0.281198, -0.017201, -0.071506, -0.054213 |
| question_plus_answer | brier | -0.044172 | 0.146692 | -0.169428, 0.204889, -0.038935, -0.108668, -0.108720 |

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
| question_plus_explanation | 0 | all | all | 7686 | 0.392142 | 0.521598 | 0.037931 | 0.232242 | 0.846189 | eligible |
| question_plus_explanation | 0 | all | unsupported | 407 | 0.000000 | 0.000000 | 0.000000 | null | null | correct_below_20 |
| question_plus_explanation | 0 | all | rare | 0 | null | null | null | null | null | n_below_200, correct_below_20, incorrect_below_20 |
| question_plus_explanation | 0 | all | frequent | 7279 | 0.414068 | 0.550762 | 0.082153 | 0.218276 | 0.817271 | eligible |
| question_plus_explanation | 0 | all | well_supported | 7025 | 0.429039 | 0.570676 | 0.093006 | 0.201531 | 0.791972 | eligible |
| question_plus_explanation | 0 | 31772 | all | 4857 | 0.356599 | 0.486000 | 0.070947 | 0.344631 | 0.923206 | eligible |
| question_plus_explanation | 0 | 31772 | unsupported | 16 | 0.000000 | 0.000000 | 0.000000 | null | null | n_below_200, correct_below_20, incorrect_below_20 |
| question_plus_explanation | 0 | 31772 | rare | 0 | null | null | null | null | null | n_below_200, correct_below_20, incorrect_below_20 |
| question_plus_explanation | 0 | 31772 | frequent | 4841 | 0.357777 | 0.487606 | 0.094811 | 0.343477 | 0.921171 | eligible |
| question_plus_explanation | 0 | 31772 | well_supported | 4587 | 0.377589 | 0.514606 | 0.118045 | 0.324461 | 0.888179 | eligible |
| question_plus_explanation | 0 | 32829 | all | 2156 | 0.556122 | 0.676948 | 0.089706 | 0.073297 | 0.624711 | eligible |
| question_plus_explanation | 0 | 32829 | unsupported | 272 | 0.000000 | 0.000000 | 0.000000 | null | null | correct_below_20 |
| question_plus_explanation | 0 | 32829 | rare | 0 | null | null | null | null | null | n_below_200, correct_below_20, incorrect_below_20 |
| question_plus_explanation | 0 | 32829 | frequent | 1884 | 0.636412 | 0.774682 | 0.154547 | 0.136238 | 0.516612 | eligible |
| question_plus_explanation | 0 | 32829 | well_supported | 1884 | 0.636412 | 0.774682 | 0.154547 | 0.136238 | 0.516612 | eligible |
| question_plus_explanation | 0 | 104665 | all | 673 | 0.123328 | 0.280832 | 0.040366 | 0.314817 | 0.999889 | eligible |
| question_plus_explanation | 0 | 104665 | unsupported | 119 | 0.000000 | 0.000000 | 0.000000 | null | null | n_below_200, correct_below_20 |
| question_plus_explanation | 0 | 104665 | rare | 0 | null | null | null | null | null | n_below_200, correct_below_20, incorrect_below_20 |
| question_plus_explanation | 0 | 104665 | frequent | 554 | 0.149819 | 0.341155 | 0.081511 | 0.277188 | 0.931820 | eligible |
| question_plus_explanation | 0 | 104665 | well_supported | 554 | 0.149819 | 0.341155 | 0.081511 | 0.277188 | 0.931820 | eligible |
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
| question_plus_explanation | 1 | all | all | 7023 | 0.300299 | 0.471356 | 0.054689 | 0.149953 | 0.848766 | eligible |
| question_plus_explanation | 1 | all | unsupported | 1613 | 0.000000 | 0.000000 | 0.000000 | null | null | correct_below_20 |
| question_plus_explanation | 1 | all | rare | 0 | null | null | null | null | null | n_below_200, correct_below_20, incorrect_below_20 |
| question_plus_explanation | 1 | all | frequent | 5410 | 0.389834 | 0.611892 | 0.189044 | 0.072222 | 0.720640 | eligible |
| question_plus_explanation | 1 | all | well_supported | 5005 | 0.421379 | 0.661405 | 0.295486 | 0.044158 | 0.672229 | eligible |
| question_plus_explanation | 1 | 31778 | all | 3640 | 0.336813 | 0.453342 | 0.125597 | 0.145104 | 0.851475 | eligible |
| question_plus_explanation | 1 | 31778 | unsupported | 1017 | 0.000000 | 0.000000 | 0.000000 | null | null | correct_below_20 |
| question_plus_explanation | 1 | 31778 | rare | 0 | null | null | null | null | null | n_below_200, correct_below_20, incorrect_below_20 |
| question_plus_explanation | 1 | 31778 | frequent | 2623 | 0.467404 | 0.629114 | 0.228057 | 0.041390 | 0.685085 | eligible |
| question_plus_explanation | 1 | 31778 | well_supported | 2218 | 0.552750 | 0.743989 | 0.373519 | 0.039840 | 0.569351 | eligible |
| question_plus_explanation | 1 | 32835 | all | 2332 | 0.188250 | 0.444039 | 0.055855 | 0.234500 | 0.893283 | eligible |
| question_plus_explanation | 1 | 32835 | unsupported | 399 | 0.000000 | 0.000000 | 0.000000 | null | null | correct_below_20 |
| question_plus_explanation | 1 | 32835 | rare | 0 | null | null | null | null | null | n_below_200, correct_below_20, incorrect_below_20 |
| question_plus_explanation | 1 | 32835 | frequent | 1933 | 0.227108 | 0.535696 | 0.166716 | 0.192237 | 0.812232 | eligible |
| question_plus_explanation | 1 | 32835 | well_supported | 1933 | 0.227108 | 0.535696 | 0.166716 | 0.192237 | 0.812232 | eligible |
| question_plus_explanation | 1 | 109465 | all | 1051 | 0.422455 | 0.594355 | 0.161624 | 0.041429 | 0.740605 | eligible |
| question_plus_explanation | 1 | 109465 | unsupported | 197 | 0.000000 | 0.000000 | 0.000000 | null | null | n_below_200, correct_below_20 |
| question_plus_explanation | 1 | 109465 | rare | 0 | null | null | null | null | null | n_below_200, correct_below_20, incorrect_below_20 |
| question_plus_explanation | 1 | 109465 | frequent | 854 | 0.519906 | 0.731460 | 0.271931 | 0.119275 | 0.622530 | eligible |
| question_plus_explanation | 1 | 109465 | well_supported | 854 | 0.519906 | 0.731460 | 0.271931 | 0.119275 | 0.622530 | eligible |
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
| question_plus_explanation | 2 | all | all | 7491 | 0.350154 | 0.508121 | 0.050678 | 0.042552 | 0.790732 | eligible |
| question_plus_explanation | 2 | all | unsupported | 1985 | 0.000000 | 0.000000 | 0.000000 | null | null | correct_below_20 |
| question_plus_explanation | 2 | all | rare | 0 | null | null | null | null | null | n_below_200, correct_below_20, incorrect_below_20 |
| question_plus_explanation | 2 | all | frequent | 5506 | 0.476389 | 0.691306 | 0.209989 | 0.075631 | 0.636827 | eligible |
| question_plus_explanation | 2 | all | well_supported | 5506 | 0.476389 | 0.691306 | 0.209989 | 0.075631 | 0.636827 | eligible |
| question_plus_explanation | 2 | 31774 | all | 3115 | 0.433708 | 0.566453 | 0.093236 | 0.028961 | 0.737247 | eligible |
| question_plus_explanation | 2 | 31774 | unsupported | 637 | 0.000000 | 0.000000 | 0.000000 | null | null | correct_below_20 |
| question_plus_explanation | 2 | 31774 | rare | 0 | null | null | null | null | null | n_below_200, correct_below_20, incorrect_below_20 |
| question_plus_explanation | 2 | 31774 | frequent | 2478 | 0.545198 | 0.712066 | 0.230336 | 0.098049 | 0.607754 | eligible |
| question_plus_explanation | 2 | 31774 | well_supported | 2478 | 0.545198 | 0.712066 | 0.230336 | 0.098049 | 0.607754 | eligible |
| question_plus_explanation | 2 | 33474 | all | 1766 | 0.227067 | 0.388071 | 0.102466 | 0.079700 | 0.886685 | eligible |
| question_plus_explanation | 2 | 33474 | unsupported | 683 | 0.000000 | 0.000000 | 0.000000 | null | null | correct_below_20 |
| question_plus_explanation | 2 | 33474 | rare | 0 | null | null | null | null | null | n_below_200, correct_below_20, incorrect_below_20 |
| question_plus_explanation | 2 | 33474 | frequent | 1083 | 0.370268 | 0.632810 | 0.273158 | 0.068588 | 0.702692 | eligible |
| question_plus_explanation | 2 | 33474 | well_supported | 1083 | 0.370268 | 0.632810 | 0.273158 | 0.068588 | 0.702692 | eligible |
| question_plus_explanation | 2 | 91695 | all | 2610 | 0.333716 | 0.519732 | 0.106989 | 0.061954 | 0.789642 | eligible |
| question_plus_explanation | 2 | 91695 | unsupported | 665 | 0.000000 | 0.000000 | 0.000000 | null | null | correct_below_20 |
| question_plus_explanation | 2 | 91695 | rare | 0 | null | null | null | null | null | n_below_200, correct_below_20, incorrect_below_20 |
| question_plus_explanation | 2 | 91695 | frequent | 1945 | 0.447815 | 0.697429 | 0.247196 | 0.054364 | 0.637193 | eligible |
| question_plus_explanation | 2 | 91695 | well_supported | 1945 | 0.447815 | 0.697429 | 0.247196 | 0.054364 | 0.637193 | eligible |
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
| question_plus_explanation | 3 | all | all | 7091 | 0.405444 | 0.522211 | 0.050740 | 0.073886 | 0.803090 | eligible |
| question_plus_explanation | 3 | all | unsupported | 2162 | 0.000000 | 0.000000 | 0.000000 | null | null | correct_below_20 |
| question_plus_explanation | 3 | all | rare | 0 | null | null | null | null | null | n_below_200, correct_below_20, incorrect_below_20 |
| question_plus_explanation | 3 | all | frequent | 4929 | 0.583283 | 0.751268 | 0.194121 | 0.130490 | 0.578636 | eligible |
| question_plus_explanation | 3 | all | well_supported | 4929 | 0.583283 | 0.751268 | 0.194121 | 0.130490 | 0.578636 | eligible |
| question_plus_explanation | 3 | 32833 | all | 3105 | 0.390338 | 0.493237 | 0.091650 | 0.191852 | 0.873683 | eligible |
| question_plus_explanation | 3 | 32833 | unsupported | 1124 | 0.000000 | 0.000000 | 0.000000 | null | null | correct_below_20 |
| question_plus_explanation | 3 | 32833 | rare | 0 | null | null | null | null | null | n_below_200, correct_below_20, incorrect_below_20 |
| question_plus_explanation | 3 | 32833 | frequent | 1981 | 0.611812 | 0.773094 | 0.249829 | 0.181021 | 0.576606 | eligible |
| question_plus_explanation | 3 | 32833 | well_supported | 1981 | 0.611812 | 0.773094 | 0.249829 | 0.181021 | 0.576606 | eligible |
| question_plus_explanation | 3 | 33472 | all | 2800 | 0.453929 | 0.570357 | 0.101467 | 0.037629 | 0.711243 | eligible |
| question_plus_explanation | 3 | 33472 | unsupported | 652 | 0.000000 | 0.000000 | 0.000000 | null | null | correct_below_20 |
| question_plus_explanation | 3 | 33472 | rare | 0 | null | null | null | null | null | n_below_200, correct_below_20, incorrect_below_20 |
| question_plus_explanation | 3 | 33472 | frequent | 2148 | 0.591713 | 0.743482 | 0.235593 | 0.110139 | 0.559460 | eligible |
| question_plus_explanation | 3 | 33472 | well_supported | 2148 | 0.591713 | 0.743482 | 0.235593 | 0.110139 | 0.559460 | eligible |
| question_plus_explanation | 3 | 76870 | all | 1186 | 0.330523 | 0.484401 | 0.109242 | 0.103636 | 0.835113 | eligible |
| question_plus_explanation | 3 | 76870 | unsupported | 386 | 0.000000 | 0.000000 | 0.000000 | null | null | correct_below_20 |
| question_plus_explanation | 3 | 76870 | rare | 0 | null | null | null | null | null | n_below_200, correct_below_20, incorrect_below_20 |
| question_plus_explanation | 3 | 76870 | frequent | 800 | 0.490000 | 0.718125 | 0.262431 | 0.070355 | 0.635151 | eligible |
| question_plus_explanation | 3 | 76870 | well_supported | 800 | 0.490000 | 0.718125 | 0.262431 | 0.070355 | 0.635151 | eligible |
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
| question_plus_explanation | 4 | all | all | 7405 | 0.433491 | 0.576570 | 0.081346 | 0.043984 | 0.739861 | eligible |
| question_plus_explanation | 4 | all | unsupported | 1588 | 0.000000 | 0.000000 | 0.000000 | null | null | correct_below_20 |
| question_plus_explanation | 4 | all | rare | 0 | null | null | null | null | null | n_below_200, correct_below_20, incorrect_below_20 |
| question_plus_explanation | 4 | all | frequent | 5817 | 0.551831 | 0.733969 | 0.185300 | 0.093247 | 0.580244 | eligible |
| question_plus_explanation | 4 | all | well_supported | 5722 | 0.560993 | 0.746155 | 0.218021 | 0.103820 | 0.567683 | eligible |
| question_plus_explanation | 4 | 31777 | all | 2809 | 0.588110 | 0.708496 | 0.176419 | 0.091337 | 0.592866 | eligible |
| question_plus_explanation | 4 | 31777 | unsupported | 314 | 0.000000 | 0.000000 | 0.000000 | null | null | correct_below_20 |
| question_plus_explanation | 4 | 31777 | rare | 0 | null | null | null | null | null | n_below_200, correct_below_20, incorrect_below_20 |
| question_plus_explanation | 4 | 31777 | frequent | 2495 | 0.662124 | 0.797662 | 0.262658 | 0.151534 | 0.495061 | eligible |
| question_plus_explanation | 4 | 31777 | well_supported | 2419 | 0.682927 | 0.822723 | 0.333193 | 0.172994 | 0.469095 | eligible |
| question_plus_explanation | 4 | 33471 | all | 1542 | 0.374838 | 0.519347 | 0.101753 | 0.171872 | 0.848885 | eligible |
| question_plus_explanation | 4 | 33471 | unsupported | 418 | 0.000000 | 0.000000 | 0.000000 | null | null | correct_below_20 |
| question_plus_explanation | 4 | 33471 | rare | 0 | null | null | null | null | null | n_below_200, correct_below_20, incorrect_below_20 |
| question_plus_explanation | 4 | 33471 | frequent | 1124 | 0.514235 | 0.712485 | 0.161268 | 0.095023 | 0.627894 | eligible |
| question_plus_explanation | 4 | 33471 | well_supported | 1105 | 0.523077 | 0.724736 | 0.195311 | 0.095064 | 0.614654 | eligible |
| question_plus_explanation | 4 | 89443 | all | 3054 | 0.320891 | 0.484119 | 0.109829 | 0.080255 | 0.820015 | eligible |
| question_plus_explanation | 4 | 89443 | unsupported | 856 | 0.000000 | 0.000000 | 0.000000 | null | null | correct_below_20 |
| question_plus_explanation | 4 | 89443 | rare | 0 | null | null | null | null | null | n_below_200, correct_below_20, incorrect_below_20 |
| question_plus_explanation | 4 | 89443 | frequent | 2198 | 0.445860 | 0.672657 | 0.238716 | 0.043593 | 0.652571 | eligible |
| question_plus_explanation | 4 | 89443 | well_supported | 2198 | 0.445860 | 0.672657 | 0.238716 | 0.043593 | 0.652571 | eligible |
| full_context | 0 | all | all | 7686 | 0.439370 | 0.553387 | 0.046598 | 0.082716 | 0.749948 | eligible |
| full_context | 0 | all | unsupported | 407 | 0.000000 | 0.000000 | 0.000000 | null | null | correct_below_20 |
| full_context | 0 | all | rare | 0 | null | null | null | null | null | n_below_200, correct_below_20, incorrect_below_20 |
| full_context | 0 | all | frequent | 7279 | 0.463937 | 0.584329 | 0.107044 | 0.085549 | 0.718406 | eligible |
| full_context | 0 | all | well_supported | 7025 | 0.480712 | 0.605457 | 0.122749 | 0.078633 | 0.698122 | eligible |
| full_context | 0 | 31772 | all | 4857 | 0.379246 | 0.498765 | 0.101683 | 0.123951 | 0.805976 | eligible |
| full_context | 0 | 31772 | unsupported | 16 | 0.000000 | 0.000000 | 0.000000 | null | null | n_below_200, correct_below_20, incorrect_below_20 |
| full_context | 0 | 31772 | rare | 0 | null | null | null | null | null | n_below_200, correct_below_20, incorrect_below_20 |
| full_context | 0 | 31772 | frequent | 4841 | 0.380500 | 0.500413 | 0.135835 | 0.123859 | 0.804287 | eligible |
| full_context | 0 | 31772 | well_supported | 4587 | 0.401570 | 0.528123 | 0.168421 | 0.115069 | 0.777977 | eligible |
| full_context | 0 | 32829 | all | 2156 | 0.686456 | 0.759972 | 0.121150 | 0.225021 | 0.560049 | eligible |
| full_context | 0 | 32829 | unsupported | 272 | 0.000000 | 0.000000 | 0.000000 | null | null | correct_below_20 |
| full_context | 0 | 32829 | rare | 0 | null | null | null | null | null | n_below_200, correct_below_20, incorrect_below_20 |
| full_context | 0 | 32829 | frequent | 1884 | 0.785563 | 0.869692 | 0.224132 | 0.313014 | 0.444865 | eligible |
| full_context | 0 | 32829 | well_supported | 1884 | 0.785563 | 0.869692 | 0.224132 | 0.313014 | 0.444865 | eligible |
| full_context | 0 | 104665 | all | 673 | 0.081724 | 0.285785 | 0.021764 | 0.274176 | 0.953946 | eligible |
| full_context | 0 | 104665 | unsupported | 119 | 0.000000 | 0.000000 | 0.000000 | null | null | n_below_200, correct_below_20 |
| full_context | 0 | 104665 | rare | 0 | null | null | null | null | null | n_below_200, correct_below_20, incorrect_below_20 |
| full_context | 0 | 104665 | frequent | 554 | 0.099278 | 0.347172 | 0.043272 | 0.260059 | 0.898195 | eligible |
| full_context | 0 | 104665 | well_supported | 554 | 0.099278 | 0.347172 | 0.043272 | 0.260059 | 0.898195 | eligible |
| full_context | 1 | all | all | 7023 | 0.206607 | 0.387560 | 0.030928 | 0.371960 | 1.046789 | eligible |
| full_context | 1 | all | unsupported | 1613 | 0.000000 | 0.000000 | 0.000000 | null | null | correct_below_20 |
| full_context | 1 | all | rare | 0 | null | null | null | null | null | n_below_200, correct_below_20, incorrect_below_20 |
| full_context | 1 | all | frequent | 5410 | 0.268207 | 0.503112 | 0.095468 | 0.309355 | 0.938945 | eligible |
| full_context | 1 | all | well_supported | 5005 | 0.289910 | 0.543823 | 0.138634 | 0.274168 | 0.885859 | eligible |
| full_context | 1 | 31778 | all | 3640 | 0.187912 | 0.309753 | 0.047079 | 0.511187 | 1.192753 | eligible |
| full_context | 1 | 31778 | unsupported | 1017 | 0.000000 | 0.000000 | 0.000000 | null | null | correct_below_20 |
| full_context | 1 | 31778 | rare | 0 | null | null | null | null | null | n_below_200, correct_below_20, incorrect_below_20 |
| full_context | 1 | 31778 | frequent | 2623 | 0.260770 | 0.429851 | 0.080497 | 0.460832 | 1.083233 | eligible |
| full_context | 1 | 31778 | well_supported | 2218 | 0.308386 | 0.508341 | 0.123950 | 0.413433 | 0.989789 | eligible |
| full_context | 1 | 32835 | all | 2332 | 0.132933 | 0.412521 | 0.032732 | 0.319364 | 0.958863 | eligible |
| full_context | 1 | 32835 | unsupported | 399 | 0.000000 | 0.000000 | 0.000000 | null | null | correct_below_20 |
| full_context | 1 | 32835 | rare | 0 | null | null | null | null | null | n_below_200, correct_below_20, incorrect_below_20 |
| full_context | 1 | 32835 | frequent | 1933 | 0.160372 | 0.497672 | 0.099326 | 0.285044 | 0.888448 | eligible |
| full_context | 1 | 32835 | well_supported | 1933 | 0.160372 | 0.497672 | 0.099326 | 0.285044 | 0.888448 | eligible |
| full_context | 1 | 109465 | all | 1051 | 0.434824 | 0.601649 | 0.151151 | 0.035263 | 0.736359 | eligible |
| full_context | 1 | 109465 | unsupported | 197 | 0.000000 | 0.000000 | 0.000000 | null | null | n_below_200, correct_below_20 |
| full_context | 1 | 109465 | rare | 0 | null | null | null | null | null | n_below_200, correct_below_20, incorrect_below_20 |
| full_context | 1 | 109465 | frequent | 854 | 0.535129 | 0.740437 | 0.253477 | 0.095770 | 0.610075 | eligible |
| full_context | 1 | 109465 | well_supported | 854 | 0.535129 | 0.740437 | 0.253477 | 0.095770 | 0.610075 | eligible |
| full_context | 2 | all | all | 7491 | 0.416500 | 0.558403 | 0.064706 | 0.084856 | 0.753934 | eligible |
| full_context | 2 | all | unsupported | 1985 | 0.000000 | 0.000000 | 0.000000 | null | null | correct_below_20 |
| full_context | 2 | all | rare | 0 | null | null | null | null | null | n_below_200, correct_below_20, incorrect_below_20 |
| full_context | 2 | all | frequent | 5506 | 0.566655 | 0.759717 | 0.345548 | 0.217751 | 0.611542 | eligible |
| full_context | 2 | all | well_supported | 5506 | 0.566655 | 0.759717 | 0.345548 | 0.217751 | 0.611542 | eligible |
| full_context | 2 | 31774 | all | 3115 | 0.498234 | 0.632798 | 0.124732 | 0.117331 | 0.671537 | eligible |
| full_context | 2 | 31774 | unsupported | 637 | 0.000000 | 0.000000 | 0.000000 | null | null | correct_below_20 |
| full_context | 2 | 31774 | rare | 0 | null | null | null | null | null | n_below_200, correct_below_20, incorrect_below_20 |
| full_context | 2 | 31774 | frequent | 2478 | 0.626312 | 0.795467 | 0.357446 | 0.194594 | 0.545716 | eligible |
| full_context | 2 | 31774 | well_supported | 2478 | 0.626312 | 0.795467 | 0.357446 | 0.194594 | 0.545716 | eligible |
| full_context | 2 | 33474 | all | 1766 | 0.309173 | 0.440732 | 0.138023 | 0.067367 | 0.863028 | eligible |
| full_context | 2 | 33474 | unsupported | 683 | 0.000000 | 0.000000 | 0.000000 | null | null | correct_below_20 |
| full_context | 2 | 33474 | rare | 0 | null | null | null | null | null | n_below_200, correct_below_20, incorrect_below_20 |
| full_context | 2 | 33474 | frequent | 1083 | 0.504155 | 0.718683 | 0.357169 | 0.253648 | 0.692074 | eligible |
| full_context | 2 | 33474 | well_supported | 1083 | 0.504155 | 0.718683 | 0.357169 | 0.253648 | 0.692074 | eligible |
| full_context | 2 | 91695 | all | 2610 | 0.391571 | 0.549234 | 0.120541 | 0.088929 | 0.778458 | eligible |
| full_context | 2 | 91695 | unsupported | 665 | 0.000000 | 0.000000 | 0.000000 | null | null | correct_below_20 |
| full_context | 2 | 91695 | rare | 0 | null | null | null | null | null | n_below_200, correct_below_20, incorrect_below_20 |
| full_context | 2 | 91695 | frequent | 1945 | 0.525450 | 0.737018 | 0.277564 | 0.229106 | 0.650567 | eligible |
| full_context | 2 | 91695 | well_supported | 1945 | 0.525450 | 0.737018 | 0.277564 | 0.229106 | 0.650567 | eligible |
| full_context | 3 | all | all | 7091 | 0.427443 | 0.527946 | 0.063551 | 0.179996 | 0.854134 | eligible |
| full_context | 3 | all | unsupported | 2162 | 0.000000 | 0.000000 | 0.000000 | null | null | correct_below_20 |
| full_context | 3 | all | rare | 0 | null | null | null | null | null | n_below_200, correct_below_20, incorrect_below_20 |
| full_context | 3 | all | frequent | 4929 | 0.614932 | 0.759518 | 0.385630 | 0.123364 | 0.570983 | eligible |
| full_context | 3 | all | well_supported | 4929 | 0.614932 | 0.759518 | 0.385630 | 0.123364 | 0.570983 | eligible |
| full_context | 3 | 32833 | all | 3105 | 0.399678 | 0.476651 | 0.109339 | 0.398513 | 0.998184 | eligible |
| full_context | 3 | 32833 | unsupported | 1124 | 0.000000 | 0.000000 | 0.000000 | null | null | correct_below_20 |
| full_context | 3 | 32833 | rare | 0 | null | null | null | null | null | n_below_200, correct_below_20, incorrect_below_20 |
| full_context | 3 | 32833 | frequent | 1981 | 0.626451 | 0.747097 | 0.302606 | 0.230690 | 0.632703 | eligible |
| full_context | 3 | 32833 | well_supported | 1981 | 0.626451 | 0.747097 | 0.302606 | 0.230690 | 0.632703 | eligible |
| full_context | 3 | 33472 | all | 2800 | 0.477143 | 0.592917 | 0.123608 | 0.097832 | 0.716028 | eligible |
| full_context | 3 | 33472 | unsupported | 652 | 0.000000 | 0.000000 | 0.000000 | null | null | correct_below_20 |
| full_context | 3 | 33472 | rare | 0 | null | null | null | null | null | n_below_200, correct_below_20, incorrect_below_20 |
| full_context | 3 | 33472 | frequent | 2148 | 0.621974 | 0.772890 | 0.407563 | 0.049563 | 0.512191 | eligible |
| full_context | 3 | 33472 | well_supported | 2148 | 0.621974 | 0.772890 | 0.407563 | 0.049563 | 0.512191 | eligible |
| full_context | 3 | 76870 | all | 1186 | 0.382799 | 0.508853 | 0.131782 | 0.072269 | 0.803060 | eligible |
| full_context | 3 | 76870 | unsupported | 386 | 0.000000 | 0.000000 | 0.000000 | null | null | correct_below_20 |
| full_context | 3 | 76870 | rare | 0 | null | null | null | null | null | n_below_200, correct_below_20, incorrect_below_20 |
| full_context | 3 | 76870 | frequent | 800 | 0.567500 | 0.754375 | 0.313261 | 0.143703 | 0.576003 | eligible |
| full_context | 3 | 76870 | well_supported | 800 | 0.567500 | 0.754375 | 0.313261 | 0.143703 | 0.576003 | eligible |
| full_context | 4 | all | all | 7405 | 0.352870 | 0.532140 | 0.067933 | 0.028603 | 0.785613 | eligible |
| full_context | 4 | all | unsupported | 1588 | 0.000000 | 0.000000 | 0.000000 | null | null | correct_below_20 |
| full_context | 4 | all | rare | 0 | null | null | null | null | null | n_below_200, correct_below_20, incorrect_below_20 |
| full_context | 4 | all | frequent | 5817 | 0.449201 | 0.677411 | 0.154992 | 0.121598 | 0.679454 | eligible |
| full_context | 4 | all | well_supported | 5722 | 0.456659 | 0.688367 | 0.182568 | 0.130013 | 0.671706 | eligible |
| full_context | 4 | 31777 | all | 2809 | 0.589178 | 0.710336 | 0.175355 | 0.231549 | 0.645083 | eligible |
| full_context | 4 | 31777 | unsupported | 314 | 0.000000 | 0.000000 | 0.000000 | null | null | correct_below_20 |
| full_context | 4 | 31777 | rare | 0 | null | null | null | null | null | n_below_200, correct_below_20, incorrect_below_20 |
| full_context | 4 | 31777 | frequent | 2495 | 0.663327 | 0.799733 | 0.261515 | 0.302656 | 0.577696 | eligible |
| full_context | 4 | 31777 | well_supported | 2419 | 0.684167 | 0.824170 | 0.331638 | 0.324374 | 0.559861 | eligible |
| full_context | 4 | 33471 | all | 1542 | 0.140078 | 0.380134 | 0.044079 | 0.202669 | 0.934733 | eligible |
| full_context | 4 | 33471 | unsupported | 418 | 0.000000 | 0.000000 | 0.000000 | null | null | correct_below_20 |
| full_context | 4 | 33471 | rare | 0 | null | null | null | null | null | n_below_200, correct_below_20, incorrect_below_20 |
| full_context | 4 | 33471 | frequent | 1124 | 0.192171 | 0.521501 | 0.070866 | 0.145550 | 0.831052 | eligible |
| full_context | 4 | 33471 | well_supported | 1105 | 0.195475 | 0.530468 | 0.085938 | 0.144763 | 0.825586 | eligible |
| full_context | 4 | 89443 | all | 3054 | 0.242960 | 0.444990 | 0.091238 | 0.044661 | 0.839577 | eligible |
| full_context | 4 | 89443 | unsupported | 856 | 0.000000 | 0.000000 | 0.000000 | null | null | correct_below_20 |
| full_context | 4 | 89443 | rare | 0 | null | null | null | null | null | n_below_200, correct_below_20, incorrect_below_20 |
| full_context | 4 | 89443 | frequent | 2198 | 0.337580 | 0.618289 | 0.196940 | 0.047746 | 0.717438 | eligible |
| full_context | 4 | 89443 | well_supported | 2198 | 0.337580 | 0.618289 | 0.196940 | 0.047746 | 0.717438 | eligible |
| question_plus_answer | 0 | all | all | 7686 | 0.142077 | 0.291786 | 0.015514 | 0.084472 | 0.919376 | eligible |
| question_plus_answer | 0 | all | unsupported | 407 | 0.000000 | 0.000000 | 0.000000 | null | null | correct_below_20 |
| question_plus_answer | 0 | all | rare | 0 | null | null | null | null | null | n_below_200, correct_below_20, incorrect_below_20 |
| question_plus_answer | 0 | all | frequent | 7279 | 0.150021 | 0.308101 | 0.039604 | 0.081269 | 0.908288 | eligible |
| question_plus_answer | 0 | all | well_supported | 7025 | 0.155445 | 0.319241 | 0.047744 | 0.085378 | 0.903294 | eligible |
| question_plus_answer | 0 | 31772 | all | 4857 | 0.179741 | 0.398772 | 0.038089 | 0.014654 | 0.875854 | eligible |
| question_plus_answer | 0 | 31772 | unsupported | 16 | 0.000000 | 0.000000 | 0.000000 | null | null | n_below_200, correct_below_20, incorrect_below_20 |
| question_plus_answer | 0 | 31772 | rare | 0 | null | null | null | null | null | n_below_200, correct_below_20, incorrect_below_20 |
| question_plus_answer | 0 | 31772 | frequent | 4841 | 0.180335 | 0.400090 | 0.050928 | 0.014060 | 0.875176 | eligible |
| question_plus_answer | 0 | 31772 | well_supported | 4587 | 0.190320 | 0.422244 | 0.063956 | 0.004074 | 0.865693 | eligible |
| question_plus_answer | 0 | 32829 | all | 2156 | 0.074212 | 0.105519 | 0.017271 | 0.195737 | 0.966242 | eligible |
| question_plus_answer | 0 | 32829 | unsupported | 272 | 0.000000 | 0.000000 | 0.000000 | null | null | correct_below_20 |
| question_plus_answer | 0 | 32829 | rare | 0 | null | null | null | null | null | n_below_200, correct_below_20, incorrect_below_20 |
| question_plus_answer | 0 | 32829 | frequent | 1884 | 0.084926 | 0.120754 | 0.039139 | 0.207324 | 0.942387 | eligible |
| question_plus_answer | 0 | 32829 | well_supported | 1884 | 0.084926 | 0.120754 | 0.039139 | 0.207324 | 0.942387 | eligible |
| question_plus_answer | 0 | 104665 | all | 673 | 0.087667 | 0.116394 | 0.055792 | 0.308501 | 1.083332 | eligible |
| question_plus_answer | 0 | 104665 | unsupported | 119 | 0.000000 | 0.000000 | 0.000000 | null | null | n_below_200, correct_below_20 |
| question_plus_answer | 0 | 104665 | rare | 0 | null | null | null | null | null | n_below_200, correct_below_20, incorrect_below_20 |
| question_plus_answer | 0 | 104665 | frequent | 554 | 0.106498 | 0.141396 | 0.196667 | 0.411310 | 1.081674 | eligible |
| question_plus_answer | 0 | 104665 | well_supported | 554 | 0.106498 | 0.141396 | 0.196667 | 0.411310 | 1.081674 | eligible |
| question_plus_answer | 1 | all | all | 7023 | 0.260430 | 0.452537 | 0.032563 | 0.090762 | 0.841900 | eligible |
| question_plus_answer | 1 | all | unsupported | 1613 | 0.000000 | 0.000000 | 0.000000 | null | null | correct_below_20 |
| question_plus_answer | 1 | all | rare | 0 | null | null | null | null | null | n_below_200, correct_below_20, incorrect_below_20 |
| question_plus_answer | 1 | all | frequent | 5410 | 0.338078 | 0.587461 | 0.115644 | 0.105941 | 0.730220 | eligible |
| question_plus_answer | 1 | all | well_supported | 5005 | 0.365435 | 0.634998 | 0.182924 | 0.146109 | 0.689952 | eligible |
| question_plus_answer | 1 | 31778 | all | 3640 | 0.313187 | 0.435989 | 0.052999 | 0.077269 | 0.885291 | eligible |
| question_plus_answer | 1 | 31778 | unsupported | 1017 | 0.000000 | 0.000000 | 0.000000 | null | null | correct_below_20 |
| question_plus_answer | 1 | 31778 | rare | 0 | null | null | null | null | null | n_below_200, correct_below_20, incorrect_below_20 |
| question_plus_answer | 1 | 31778 | frequent | 2623 | 0.434617 | 0.605032 | 0.100983 | 0.044161 | 0.750001 | eligible |
| question_plus_answer | 1 | 31778 | well_supported | 2218 | 0.513977 | 0.715509 | 0.169744 | 0.123521 | 0.662747 | eligible |
| question_plus_answer | 1 | 32835 | all | 2332 | 0.112350 | 0.417095 | 0.018364 | 0.185873 | 0.815753 | eligible |
| question_plus_answer | 1 | 32835 | unsupported | 399 | 0.000000 | 0.000000 | 0.000000 | null | null | correct_below_20 |
| question_plus_answer | 1 | 32835 | rare | 0 | null | null | null | null | null | n_below_200, correct_below_20, incorrect_below_20 |
| question_plus_answer | 1 | 32835 | frequent | 1933 | 0.135541 | 0.503190 | 0.059681 | 0.162682 | 0.741096 | eligible |
| question_plus_answer | 1 | 32835 | well_supported | 1933 | 0.135541 | 0.503190 | 0.059681 | 0.162682 | 0.741096 | eligible |
| question_plus_answer | 1 | 109465 | all | 1051 | 0.406280 | 0.588487 | 0.096301 | 0.073542 | 0.749638 | eligible |
| question_plus_answer | 1 | 109465 | unsupported | 197 | 0.000000 | 0.000000 | 0.000000 | null | null | n_below_200, correct_below_20 |
| question_plus_answer | 1 | 109465 | rare | 0 | null | null | null | null | null | n_below_200, correct_below_20, incorrect_below_20 |
| question_plus_answer | 1 | 109465 | frequent | 854 | 0.500000 | 0.724239 | 0.166667 | 0.167262 | 0.644847 | eligible |
| question_plus_answer | 1 | 109465 | well_supported | 854 | 0.500000 | 0.724239 | 0.166667 | 0.167262 | 0.644847 | eligible |
| question_plus_answer | 2 | all | all | 7491 | 0.334935 | 0.514017 | 0.045289 | 0.102058 | 0.792869 | eligible |
| question_plus_answer | 2 | all | unsupported | 1985 | 0.000000 | 0.000000 | 0.000000 | null | null | correct_below_20 |
| question_plus_answer | 2 | all | rare | 0 | null | null | null | null | null | n_below_200, correct_below_20, incorrect_below_20 |
| question_plus_answer | 2 | all | frequent | 5506 | 0.455685 | 0.699328 | 0.244829 | 0.198812 | 0.674428 | eligible |
| question_plus_answer | 2 | all | well_supported | 5506 | 0.455685 | 0.699328 | 0.244829 | 0.198812 | 0.674428 | eligible |
| question_plus_answer | 2 | 31774 | all | 3115 | 0.451043 | 0.590209 | 0.062168 | 0.215745 | 0.654310 | eligible |
| question_plus_answer | 2 | 31774 | unsupported | 637 | 0.000000 | 0.000000 | 0.000000 | null | null | correct_below_20 |
| question_plus_answer | 2 | 31774 | rare | 0 | null | null | null | null | null | n_below_200, correct_below_20, incorrect_below_20 |
| question_plus_answer | 2 | 31774 | frequent | 2478 | 0.566990 | 0.741929 | 0.180917 | 0.204660 | 0.528752 | eligible |
| question_plus_answer | 2 | 31774 | well_supported | 2478 | 0.566990 | 0.741929 | 0.180917 | 0.204660 | 0.528752 | eligible |
| question_plus_answer | 2 | 33474 | all | 1766 | 0.395243 | 0.503398 | 0.138243 | 0.169108 | 0.854157 | eligible |
| question_plus_answer | 2 | 33474 | unsupported | 683 | 0.000000 | 0.000000 | 0.000000 | null | null | correct_below_20 |
| question_plus_answer | 2 | 33474 | rare | 0 | null | null | null | null | null | n_below_200, correct_below_20, incorrect_below_20 |
| question_plus_answer | 2 | 33474 | frequent | 1083 | 0.644506 | 0.820868 | 0.381886 | 0.410424 | 0.695121 | eligible |
| question_plus_answer | 2 | 33474 | well_supported | 1083 | 0.644506 | 0.820868 | 0.381886 | 0.410424 | 0.695121 | eligible |
| question_plus_answer | 2 | 91695 | all | 2610 | 0.155556 | 0.430268 | 0.033654 | 0.149852 | 0.916769 | eligible |
| question_plus_answer | 2 | 91695 | unsupported | 665 | 0.000000 | 0.000000 | 0.000000 | null | null | correct_below_20 |
| question_plus_answer | 2 | 91695 | rare | 0 | null | null | null | null | null | n_below_200, correct_below_20, incorrect_below_20 |
| question_plus_answer | 2 | 91695 | frequent | 1945 | 0.208740 | 0.577378 | 0.086346 | 0.239465 | 0.848501 | eligible |
| question_plus_answer | 2 | 91695 | well_supported | 1945 | 0.208740 | 0.577378 | 0.086346 | 0.239465 | 0.848501 | eligible |
| question_plus_answer | 3 | all | all | 7091 | 0.279509 | 0.438279 | 0.038100 | 0.251503 | 0.962803 | eligible |
| question_plus_answer | 3 | all | unsupported | 2162 | 0.000000 | 0.000000 | 0.000000 | null | null | correct_below_20 |
| question_plus_answer | 3 | all | rare | 0 | null | null | null | null | null | n_below_200, correct_below_20, incorrect_below_20 |
| question_plus_answer | 3 | all | frequent | 4929 | 0.402110 | 0.630520 | 0.225967 | 0.129083 | 0.753298 | eligible |
| question_plus_answer | 3 | all | well_supported | 4929 | 0.402110 | 0.630520 | 0.225967 | 0.129083 | 0.753298 | eligible |
| question_plus_answer | 3 | 32833 | all | 3105 | 0.397746 | 0.455556 | 0.063236 | 0.399434 | 0.962463 | eligible |
| question_plus_answer | 3 | 32833 | unsupported | 1124 | 0.000000 | 0.000000 | 0.000000 | null | null | correct_below_20 |
| question_plus_answer | 3 | 32833 | rare | 0 | null | null | null | null | null | n_below_200, correct_below_20, incorrect_below_20 |
| question_plus_answer | 3 | 32833 | frequent | 1981 | 0.623423 | 0.714033 | 0.192009 | 0.289910 | 0.655754 | eligible |
| question_plus_answer | 3 | 32833 | well_supported | 1981 | 0.623423 | 0.714033 | 0.192009 | 0.289910 | 0.655754 | eligible |
| question_plus_answer | 3 | 33472 | all | 2800 | 0.163214 | 0.419286 | 0.028063 | 0.421978 | 1.010207 | eligible |
| question_plus_answer | 3 | 33472 | unsupported | 652 | 0.000000 | 0.000000 | 0.000000 | null | null | correct_below_20 |
| question_plus_answer | 3 | 33472 | rare | 0 | null | null | null | null | null | n_below_200, correct_below_20, incorrect_below_20 |
| question_plus_answer | 3 | 33472 | frequent | 2148 | 0.212756 | 0.546555 | 0.087716 | 0.357584 | 0.865357 | eligible |
| question_plus_answer | 3 | 33472 | well_supported | 2148 | 0.212756 | 0.546555 | 0.087716 | 0.357584 | 0.865357 | eligible |
| question_plus_answer | 3 | 76870 | all | 1186 | 0.244519 | 0.437886 | 0.049119 | 0.067617 | 0.851778 | eligible |
| question_plus_answer | 3 | 76870 | unsupported | 386 | 0.000000 | 0.000000 | 0.000000 | null | null | correct_below_20 |
| question_plus_answer | 3 | 76870 | rare | 0 | null | null | null | null | null | n_below_200, correct_below_20, incorrect_below_20 |
| question_plus_answer | 3 | 76870 | frequent | 800 | 0.362500 | 0.649167 | 0.133028 | 0.048121 | 0.693961 | eligible |
| question_plus_answer | 3 | 76870 | well_supported | 800 | 0.362500 | 0.649167 | 0.133028 | 0.048121 | 0.693961 | eligible |
| question_plus_answer | 4 | all | all | 7405 | 0.221742 | 0.472744 | 0.031201 | 0.082816 | 0.894333 | eligible |
| question_plus_answer | 4 | all | unsupported | 1588 | 0.000000 | 0.000000 | 0.000000 | null | null | correct_below_20 |
| question_plus_answer | 4 | all | rare | 0 | null | null | null | null | null | n_below_200, correct_below_20, incorrect_below_20 |
| question_plus_answer | 4 | all | frequent | 5817 | 0.282276 | 0.601799 | 0.088137 | 0.140778 | 0.852445 | eligible |
| question_plus_answer | 4 | all | well_supported | 5722 | 0.286963 | 0.611791 | 0.111594 | 0.145424 | 0.850070 | eligible |
| question_plus_answer | 4 | 31777 | all | 2809 | 0.162335 | 0.495431 | 0.043588 | 0.027072 | 0.866150 | eligible |
| question_plus_answer | 4 | 31777 | unsupported | 314 | 0.000000 | 0.000000 | 0.000000 | null | null | correct_below_20 |
| question_plus_answer | 4 | 31777 | rare | 0 | null | null | null | null | null | n_below_200, correct_below_20, incorrect_below_20 |
| question_plus_answer | 4 | 31777 | frequent | 2495 | 0.182766 | 0.557782 | 0.061957 | 0.045481 | 0.843136 | eligible |
| question_plus_answer | 4 | 31777 | well_supported | 2419 | 0.188508 | 0.575307 | 0.079498 | 0.051283 | 0.838350 | eligible |
| question_plus_answer | 4 | 33471 | all | 1542 | 0.143320 | 0.406723 | 0.035816 | 0.022861 | 0.953176 | eligible |
| question_plus_answer | 4 | 33471 | unsupported | 418 | 0.000000 | 0.000000 | 0.000000 | null | null | correct_below_20 |
| question_plus_answer | 4 | 33471 | rare | 0 | null | null | null | null | null | n_below_200, correct_below_20, incorrect_below_20 |
| question_plus_answer | 4 | 33471 | frequent | 1124 | 0.196619 | 0.557977 | 0.065725 | 0.020416 | 0.917851 | eligible |
| question_plus_answer | 4 | 33471 | well_supported | 1105 | 0.200000 | 0.567572 | 0.083333 | 0.023149 | 0.916517 | eligible |
| question_plus_answer | 4 | 89443 | all | 3054 | 0.315979 | 0.485211 | 0.060027 | 0.187445 | 0.890543 | eligible |
| question_plus_answer | 4 | 89443 | unsupported | 856 | 0.000000 | 0.000000 | 0.000000 | null | null | correct_below_20 |
| question_plus_answer | 4 | 89443 | rare | 0 | null | null | null | null | null | n_below_200, correct_below_20, incorrect_below_20 |
| question_plus_answer | 4 | 89443 | frequent | 2198 | 0.439035 | 0.674173 | 0.152545 | 0.310502 | 0.829565 | eligible |
| question_plus_answer | 4 | 89443 | well_supported | 2198 | 0.439035 | 0.674173 | 0.152545 | 0.310502 | 0.829565 | eligible |

## All fold and question Category results

| Arm | Fold | Question | n | Accuracy | Macro-F1 six |
|---|---:|---|---:|---:|---:|
| frequency | 0 | all | 7686 | 0.485818 | 0.108990 |
| frequency | 0 | 31772 | 4857 | 0.353922 | 0.087135 |
| frequency | 0 | 32829 | 2156 | 0.732839 | 0.140971 |
| frequency | 0 | 104665 | 673 | 0.646360 | 0.130866 |
| question_plus_explanation | 0 | all | 7686 | 0.396695 | 0.142960 |
| question_plus_explanation | 0 | 31772 | 4857 | 0.356599 | 0.094596 |
| question_plus_explanation | 0 | 32829 | 2156 | 0.575139 | 0.244062 |
| question_plus_explanation | 0 | 104665 | 673 | 0.114413 | 0.063076 |
| frequency | 1 | all | 7023 | 0.358963 | 0.088048 |
| frequency | 1 | 31778 | 3640 | 0.313187 | 0.079498 |
| frequency | 1 | 32835 | 2332 | 0.409091 | 0.096774 |
| frequency | 1 | 109465 | 1051 | 0.406280 | 0.096301 |
| question_plus_explanation | 1 | all | 7023 | 0.300014 | 0.166912 |
| question_plus_explanation | 1 | 31778 | 3640 | 0.340934 | 0.193025 |
| question_plus_explanation | 1 | 32835 | 2332 | 0.181389 | 0.099702 |
| question_plus_explanation | 1 | 109465 | 1051 | 0.421503 | 0.163151 |
| frequency | 2 | all | 7491 | 0.395408 | 0.094455 |
| frequency | 2 | 31774 | 3115 | 0.451043 | 0.103614 |
| frequency | 2 | 33474 | 1766 | 0.182899 | 0.051540 |
| frequency | 2 | 91695 | 2610 | 0.472797 | 0.107007 |
| question_plus_explanation | 2 | all | 7491 | 0.351755 | 0.201777 |
| question_plus_explanation | 2 | 31774 | 3115 | 0.406742 | 0.216936 |
| question_plus_explanation | 2 | 33474 | 1766 | 0.279162 | 0.181068 |
| question_plus_explanation | 2 | 91695 | 2610 | 0.335249 | 0.154810 |
| frequency | 3 | all | 7091 | 0.368777 | 0.089807 |
| frequency | 3 | 32833 | 3105 | 0.397746 | 0.094854 |
| frequency | 3 | 33472 | 2800 | 0.362143 | 0.088621 |
| frequency | 3 | 76870 | 1186 | 0.308600 | 0.078608 |
| question_plus_explanation | 3 | all | 7091 | 0.422507 | 0.219103 |
| question_plus_explanation | 3 | 32833 | 3105 | 0.368438 | 0.167559 |
| question_plus_explanation | 3 | 33472 | 2800 | 0.522143 | 0.285487 |
| question_plus_explanation | 3 | 76870 | 1186 | 0.328836 | 0.151414 |
| frequency | 4 | all | 7405 | 0.401080 | 0.095422 |
| frequency | 4 | 31777 | 2809 | 0.579566 | 0.122305 |
| frequency | 4 | 33471 | 1542 | 0.454604 | 0.104176 |
| frequency | 4 | 89443 | 3054 | 0.209889 | 0.057826 |
| question_plus_explanation | 4 | all | 7405 | 0.427414 | 0.196628 |
| question_plus_explanation | 4 | 31777 | 2809 | 0.588466 | 0.208856 |
| question_plus_explanation | 4 | 33471 | 1542 | 0.352789 | 0.134430 |
| question_plus_explanation | 4 | 89443 | 3054 | 0.316961 | 0.177551 |
| full_context | 0 | all | 7686 | 0.437679 | 0.164019 |
| full_context | 0 | 31772 | 4857 | 0.379246 | 0.135578 |
| full_context | 0 | 32829 | 2156 | 0.685993 | 0.281742 |
| full_context | 0 | 104665 | 673 | 0.063893 | 0.031475 |
| full_context | 1 | all | 7023 | 0.211163 | 0.106264 |
| full_context | 1 | 31778 | 3640 | 0.201374 | 0.091232 |
| full_context | 1 | 32835 | 2332 | 0.125643 | 0.057668 |
| full_context | 1 | 109465 | 1051 | 0.434824 | 0.151151 |
| full_context | 2 | all | 7491 | 0.439728 | 0.240584 |
| full_context | 2 | 31774 | 3115 | 0.563403 | 0.289939 |
| full_context | 2 | 33474 | 1766 | 0.426954 | 0.189148 |
| full_context | 2 | 91695 | 2610 | 0.300766 | 0.159185 |
| full_context | 3 | all | 7091 | 0.429700 | 0.218621 |
| full_context | 3 | 32833 | 3105 | 0.392271 | 0.161086 |
| full_context | 3 | 33472 | 2800 | 0.490714 | 0.249750 |
| full_context | 3 | 76870 | 1186 | 0.383642 | 0.182141 |
| full_context | 4 | all | 7405 | 0.326941 | 0.183588 |
| full_context | 4 | 31777 | 2809 | 0.526522 | 0.229895 |
| full_context | 4 | 33471 | 1542 | 0.085603 | 0.058871 |
| full_context | 4 | 89443 | 3054 | 0.265226 | 0.165351 |
| question_plus_answer | 0 | all | 7686 | 0.253058 | 0.079496 |
| question_plus_answer | 0 | 31772 | 4857 | 0.330451 | 0.082792 |
| question_plus_answer | 0 | 32829 | 2156 | 0.104360 | 0.078773 |
| question_plus_answer | 0 | 104665 | 673 | 0.170877 | 0.048646 |
| question_plus_answer | 1 | all | 7023 | 0.260430 | 0.097688 |
| question_plus_answer | 1 | 31778 | 3640 | 0.313187 | 0.079498 |
| question_plus_answer | 1 | 32835 | 2332 | 0.112350 | 0.033667 |
| question_plus_answer | 1 | 109465 | 1051 | 0.406280 | 0.096301 |
| question_plus_answer | 2 | all | 7491 | 0.386464 | 0.157026 |
| question_plus_answer | 2 | 31774 | 3115 | 0.504976 | 0.166097 |
| question_plus_answer | 2 | 33474 | 1766 | 0.382786 | 0.092274 |
| question_plus_answer | 2 | 91695 | 2610 | 0.247510 | 0.066134 |
| question_plus_answer | 3 | all | 7091 | 0.279509 | 0.120650 |
| question_plus_answer | 3 | 32833 | 3105 | 0.397746 | 0.094854 |
| question_plus_answer | 3 | 33472 | 2800 | 0.163214 | 0.046771 |
| question_plus_answer | 3 | 76870 | 1186 | 0.244519 | 0.065492 |
| question_plus_answer | 4 | all | 7405 | 0.204321 | 0.056552 |
| question_plus_answer | 4 | 31777 | 2809 | 0.138839 | 0.040638 |
| question_plus_answer | 4 | 33471 | 1542 | 0.279507 | 0.072816 |
| question_plus_answer | 4 | 89443 | 3054 | 0.226588 | 0.061577 |

## Every fixed review budget and fold

| Arm | Fold | Review % | Retained n | Risk | MAP@3 | ECE | Brier |
|---|---:|---:|---:|---:|---:|---:|---:|
| frequency | 0 | 0 | 7686 | 0.514182 | 0.591812 | 0.112647 | 0.755854 |
| frequency | 0 | 10 | 6918 | 0.513877 | 0.593380 | 0.112952 | 0.754674 |
| frequency | 0 | 20 | 6149 | 0.515043 | 0.592942 | 0.111785 | 0.755079 |
| frequency | 0 | 30 | 5381 | 0.512730 | 0.595986 | 0.114098 | 0.752794 |
| frequency | 0 | 40 | 4612 | 0.510191 | 0.598620 | 0.116638 | 0.750879 |
| frequency | 0 | 50 | 3843 | 0.513401 | 0.596192 | 0.113427 | 0.752719 |
| question_plus_explanation | 0 | 0 | 7686 | 0.607858 | 0.521598 | 0.232242 | 0.846189 |
| question_plus_explanation | 0 | 10 | 6918 | 0.593958 | 0.529151 | 0.254073 | 0.850146 |
| question_plus_explanation | 0 | 20 | 6149 | 0.591804 | 0.528758 | 0.281226 | 0.858213 |
| question_plus_explanation | 0 | 30 | 5381 | 0.580561 | 0.535031 | 0.297545 | 0.860231 |
| question_plus_explanation | 0 | 40 | 4612 | 0.560494 | 0.554459 | 0.302490 | 0.847922 |
| question_plus_explanation | 0 | 50 | 3843 | 0.534478 | 0.578151 | 0.300571 | 0.826619 |
| frequency | 1 | 0 | 7023 | 0.641037 | 0.501804 | 0.055844 | 0.823525 |
| frequency | 1 | 10 | 6321 | 0.642778 | 0.500026 | 0.057586 | 0.824955 |
| frequency | 1 | 20 | 5619 | 0.640861 | 0.501987 | 0.055669 | 0.823350 |
| frequency | 1 | 30 | 4917 | 0.643075 | 0.499695 | 0.057883 | 0.825261 |
| frequency | 1 | 40 | 4214 | 0.645230 | 0.499011 | 0.060038 | 0.825864 |
| frequency | 1 | 50 | 3512 | 0.645501 | 0.499525 | 0.060309 | 0.825560 |
| question_plus_explanation | 1 | 0 | 7023 | 0.699701 | 0.471356 | 0.149953 | 0.848766 |
| question_plus_explanation | 1 | 10 | 6321 | 0.690081 | 0.479117 | 0.157953 | 0.846248 |
| question_plus_explanation | 1 | 20 | 5619 | 0.681438 | 0.485614 | 0.166273 | 0.844479 |
| question_plus_explanation | 1 | 30 | 4917 | 0.670938 | 0.493153 | 0.173503 | 0.841474 |
| question_plus_explanation | 1 | 40 | 4214 | 0.659231 | 0.504786 | 0.181052 | 0.834787 |
| question_plus_explanation | 1 | 50 | 3512 | 0.644362 | 0.516562 | 0.187775 | 0.827802 |
| frequency | 2 | 0 | 7491 | 0.604592 | 0.538824 | 0.045889 | 0.793789 |
| frequency | 2 | 10 | 6742 | 0.602937 | 0.540146 | 0.044234 | 0.792633 |
| frequency | 2 | 20 | 5993 | 0.601201 | 0.541354 | 0.042498 | 0.791444 |
| frequency | 2 | 30 | 5244 | 0.601831 | 0.540427 | 0.043128 | 0.792258 |
| frequency | 2 | 40 | 4495 | 0.601780 | 0.540860 | 0.043077 | 0.791877 |
| frequency | 2 | 50 | 3746 | 0.606781 | 0.535549 | 0.048078 | 0.796601 |
| question_plus_explanation | 2 | 0 | 7491 | 0.649846 | 0.508121 | 0.042552 | 0.790732 |
| question_plus_explanation | 2 | 10 | 6742 | 0.637051 | 0.520444 | 0.046279 | 0.782241 |
| question_plus_explanation | 2 | 20 | 5993 | 0.623561 | 0.531592 | 0.049049 | 0.774337 |
| question_plus_explanation | 2 | 30 | 5244 | 0.606407 | 0.544209 | 0.049019 | 0.764921 |
| question_plus_explanation | 2 | 40 | 4495 | 0.593548 | 0.555209 | 0.055179 | 0.755175 |
| question_plus_explanation | 2 | 50 | 3746 | 0.569941 | 0.573056 | 0.053304 | 0.740500 |
| frequency | 3 | 0 | 7091 | 0.631223 | 0.501222 | 0.048873 | 0.822135 |
| frequency | 3 | 10 | 6382 | 0.631934 | 0.500392 | 0.049584 | 0.822824 |
| frequency | 3 | 20 | 5673 | 0.633175 | 0.499412 | 0.050825 | 0.823753 |
| frequency | 3 | 30 | 4964 | 0.631144 | 0.500168 | 0.048795 | 0.822993 |
| frequency | 3 | 40 | 4255 | 0.630552 | 0.500627 | 0.048203 | 0.822585 |
| frequency | 3 | 50 | 3546 | 0.631698 | 0.500611 | 0.049348 | 0.822761 |
| question_plus_explanation | 3 | 0 | 7091 | 0.594556 | 0.522211 | 0.073886 | 0.803090 |
| question_plus_explanation | 3 | 10 | 6382 | 0.575838 | 0.536457 | 0.080645 | 0.795531 |
| question_plus_explanation | 3 | 20 | 5673 | 0.565662 | 0.536136 | 0.086201 | 0.797325 |
| question_plus_explanation | 3 | 30 | 4964 | 0.558018 | 0.536060 | 0.094966 | 0.798095 |
| question_plus_explanation | 3 | 40 | 4255 | 0.546651 | 0.539130 | 0.109254 | 0.797338 |
| question_plus_explanation | 3 | 50 | 3546 | 0.542865 | 0.534546 | 0.133122 | 0.804113 |
| frequency | 4 | 0 | 7405 | 0.598920 | 0.562413 | 0.018103 | 0.779983 |
| frequency | 4 | 10 | 6665 | 0.598050 | 0.562891 | 0.017233 | 0.779532 |
| frequency | 4 | 20 | 5924 | 0.597063 | 0.563611 | 0.016246 | 0.778807 |
| frequency | 4 | 30 | 5184 | 0.595486 | 0.564525 | 0.014669 | 0.777913 |
| frequency | 4 | 40 | 4443 | 0.595994 | 0.562158 | 0.015177 | 0.779515 |
| frequency | 4 | 50 | 3703 | 0.594113 | 0.561797 | 0.013296 | 0.779434 |
| question_plus_explanation | 4 | 0 | 7405 | 0.566509 | 0.576570 | 0.043984 | 0.739861 |
| question_plus_explanation | 4 | 10 | 6665 | 0.544336 | 0.592648 | 0.042869 | 0.729349 |
| question_plus_explanation | 4 | 20 | 5924 | 0.529372 | 0.600523 | 0.048534 | 0.722609 |
| question_plus_explanation | 4 | 30 | 5184 | 0.511574 | 0.609600 | 0.053348 | 0.715208 |
| question_plus_explanation | 4 | 40 | 4443 | 0.487734 | 0.621952 | 0.054324 | 0.704484 |
| question_plus_explanation | 4 | 50 | 3703 | 0.473670 | 0.624269 | 0.060095 | 0.700289 |
| full_context | 0 | 0 | 7686 | 0.560630 | 0.553387 | 0.082716 | 0.749948 |
| full_context | 0 | 10 | 6918 | 0.546979 | 0.560350 | 0.088761 | 0.742377 |
| full_context | 0 | 20 | 6149 | 0.523012 | 0.580609 | 0.088688 | 0.722636 |
| full_context | 0 | 30 | 5381 | 0.493217 | 0.608406 | 0.085793 | 0.695255 |
| full_context | 0 | 40 | 4612 | 0.458586 | 0.637070 | 0.083209 | 0.666991 |
| full_context | 0 | 50 | 3843 | 0.412438 | 0.675514 | 0.076935 | 0.626992 |
| full_context | 1 | 0 | 7023 | 0.793393 | 0.387560 | 0.371960 | 1.046789 |
| full_context | 1 | 10 | 6321 | 0.796235 | 0.377709 | 0.404799 | 1.072751 |
| full_context | 1 | 20 | 5619 | 0.802812 | 0.363677 | 0.440882 | 1.104648 |
| full_context | 1 | 30 | 4917 | 0.811470 | 0.346960 | 0.480674 | 1.141833 |
| full_context | 1 | 40 | 4214 | 0.813716 | 0.335311 | 0.516640 | 1.178897 |
| full_context | 1 | 50 | 3512 | 0.815774 | 0.320568 | 0.555959 | 1.221890 |
| full_context | 2 | 0 | 7491 | 0.583500 | 0.558403 | 0.084856 | 0.753934 |
| full_context | 2 | 10 | 6742 | 0.560961 | 0.581529 | 0.092575 | 0.736392 |
| full_context | 2 | 20 | 5993 | 0.543301 | 0.598198 | 0.096523 | 0.721135 |
| full_context | 2 | 30 | 5244 | 0.522502 | 0.615783 | 0.102168 | 0.704678 |
| full_context | 2 | 40 | 4495 | 0.500779 | 0.629848 | 0.106436 | 0.689678 |
| full_context | 2 | 50 | 3746 | 0.477843 | 0.646645 | 0.109193 | 0.669926 |
| full_context | 3 | 0 | 7091 | 0.572557 | 0.527946 | 0.179996 | 0.854134 |
| full_context | 3 | 10 | 6382 | 0.569101 | 0.520187 | 0.190281 | 0.867023 |
| full_context | 3 | 20 | 5673 | 0.573770 | 0.503819 | 0.202188 | 0.888848 |
| full_context | 3 | 30 | 4964 | 0.576753 | 0.491472 | 0.228253 | 0.910290 |
| full_context | 3 | 40 | 4255 | 0.585664 | 0.473913 | 0.265967 | 0.938854 |
| full_context | 3 | 50 | 3546 | 0.601523 | 0.451072 | 0.312347 | 0.978126 |
| full_context | 4 | 0 | 7405 | 0.647130 | 0.532140 | 0.028603 | 0.785613 |
| full_context | 4 | 10 | 6665 | 0.636759 | 0.540260 | 0.026717 | 0.779656 |
| full_context | 4 | 20 | 5924 | 0.620189 | 0.554552 | 0.032019 | 0.770536 |
| full_context | 4 | 30 | 5184 | 0.605324 | 0.565747 | 0.035074 | 0.762440 |
| full_context | 4 | 40 | 4443 | 0.584290 | 0.577950 | 0.043024 | 0.754330 |
| full_context | 4 | 50 | 3703 | 0.566568 | 0.585066 | 0.045857 | 0.748651 |
| question_plus_answer | 0 | 0 | 7686 | 0.857923 | 0.291786 | 0.084472 | 0.919376 |
| question_plus_answer | 0 | 10 | 6918 | 0.863111 | 0.284523 | 0.093372 | 0.921006 |
| question_plus_answer | 0 | 20 | 6149 | 0.866808 | 0.272646 | 0.101554 | 0.925855 |
| question_plus_answer | 0 | 30 | 5381 | 0.870842 | 0.257108 | 0.113091 | 0.932180 |
| question_plus_answer | 0 | 40 | 4612 | 0.880312 | 0.229510 | 0.133355 | 0.943260 |
| question_plus_answer | 0 | 50 | 3843 | 0.895134 | 0.193599 | 0.160167 | 0.957336 |
| question_plus_answer | 1 | 0 | 7023 | 0.739570 | 0.452537 | 0.090762 | 0.841900 |
| question_plus_answer | 1 | 10 | 6321 | 0.721405 | 0.457206 | 0.078479 | 0.844703 |
| question_plus_answer | 1 | 20 | 5619 | 0.699769 | 0.462597 | 0.064196 | 0.848305 |
| question_plus_answer | 1 | 30 | 4917 | 0.676429 | 0.467358 | 0.050308 | 0.853311 |
| question_plus_answer | 1 | 40 | 4214 | 0.674656 | 0.457523 | 0.057250 | 0.865871 |
| question_plus_answer | 1 | 50 | 3512 | 0.687642 | 0.433941 | 0.078098 | 0.887000 |
| question_plus_answer | 2 | 0 | 7491 | 0.665065 | 0.514017 | 0.102058 | 0.792869 |
| question_plus_answer | 2 | 10 | 6742 | 0.663156 | 0.529739 | 0.125124 | 0.777949 |
| question_plus_answer | 2 | 20 | 5993 | 0.675788 | 0.527282 | 0.166561 | 0.771065 |
| question_plus_answer | 2 | 30 | 5244 | 0.654653 | 0.544273 | 0.177866 | 0.758987 |
| question_plus_answer | 2 | 40 | 4495 | 0.599110 | 0.615239 | 0.161267 | 0.711503 |
| question_plus_answer | 2 | 50 | 3746 | 0.571276 | 0.679035 | 0.186064 | 0.664653 |
| question_plus_answer | 3 | 0 | 7091 | 0.720491 | 0.438279 | 0.251503 | 0.962803 |
| question_plus_answer | 3 | 10 | 6382 | 0.734879 | 0.439308 | 0.290679 | 0.968826 |
| question_plus_answer | 3 | 20 | 5673 | 0.717786 | 0.440243 | 0.295011 | 0.988559 |
| question_plus_answer | 3 | 30 | 4964 | 0.760475 | 0.412168 | 0.345763 | 1.032097 |
| question_plus_answer | 3 | 40 | 4255 | 0.839718 | 0.343361 | 0.435623 | 1.117862 |
| question_plus_answer | 3 | 50 | 3546 | 0.934010 | 0.254700 | 0.544720 | 1.225090 |
| question_plus_answer | 4 | 0 | 7405 | 0.778258 | 0.472744 | 0.082816 | 0.894333 |
| question_plus_answer | 4 | 10 | 6665 | 0.770143 | 0.490298 | 0.089011 | 0.889872 |
| question_plus_answer | 4 | 20 | 5924 | 0.781229 | 0.491560 | 0.076385 | 0.889430 |
| question_plus_answer | 4 | 30 | 5184 | 0.795910 | 0.490484 | 0.059726 | 0.890070 |
| question_plus_answer | 4 | 40 | 4443 | 0.812289 | 0.493398 | 0.040707 | 0.889472 |
| question_plus_answer | 4 | 50 | 3703 | 0.826357 | 0.492033 | 0.023595 | 0.891724 |

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
  "git_revision": "97afd8414e33f8dec08f984577d139e5bb618081",
  "docker_image_id": "sha256:464fc81faf49a6355e4bd0f55956243cc0fee586f657937f495975c2268e6fe0",
  "lock_sha256": "05a203f9fe979213820ceed3a1e9723bf98cc159c74d8d21a6c9f0656235c094",
  "data_sha256": "0a5e4523ec9b1656b979002a58e7cb743d02c9ac2697cc154008f971d413686c",
  "manifest_sha256": "93a25f33389b68487c09c5e9b34cfd10ca0d03b9b6438a53e2c385b2e87a7b94",
  "assignments_sha256": "b0211bafc055aedcd334877782d8db818a7c0a05873f1826ad32f0c17a61c9dd",
  "e011_sha256": null,
  "started_utc": "2026-10-13T22:59:51.038142+00:00",
  "finished_utc": "2026-10-13T23:10:49.790107+00:00",
  "wall_seconds": 658.8027697899379,
  "uid": 10001,
  "gid": 10001,
  "seed": 20260831,
  "model_fits": 150,
  "fit_warnings": 0,
  "preserved_files": 163,
  "preservation_verified": true,
  "global_freeze_verified": true,
  "reproduction_checks": 30,
  "frozen_development_sha256": "1e0ac6aa51a61aa68492ce68774dbf700d2318f8108e6f8fa8e3efd221ce3ceb",
  "row_level_outputs": false
}
```

The accompanying aggregate JSON includes full five-value summary statistics, selection scores, temperatures, counts and eligibility. No row-level prediction, response, selected-answer text or fitted parameter is published.
