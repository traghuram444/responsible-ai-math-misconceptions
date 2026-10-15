# E013 numerical results

Equal-fold summaries and shuffle dispersion are descriptive only. No interpretation or next-experiment proposal is included.

## Aggregate exact label performance

| Model | Original MAP@3 | Explanation shuffle MAP@3 | Pair shuffle MAP@3 | Original accuracy |
|---|---|---|---|---|
| E011 | 0.511887 | 0.485204 | 0.465728 | 0.368558 |
| E012 | 0.537228 | 0.536613 | 0.536338 | 0.402374 |
| frequency | 0.539215 | 0.539215 | 0.539215 | 0.402009 |

## Registered explanation criteria

| Model | Delta mean | Fold SD | Positive folds | Criterion met |
|---|---|---|---|---|
| E011 | 0.026683 | 0.006820 | 5/5 | True |
| E012 | 0.000616 | 0.000797 | 4/5 | False |

## Complete fold performance and paired differences

| Model | Fold | Original MAP@3 | Explanation MAP@3 | Explanation delta | Pair MAP@3 | Pair delta | Original accuracy | Explanation accuracy | Pair accuracy |
|---|---|---|---|---|---|---|---|---|---|
| E011 | 0 | 0.553387 | 0.535442 | 0.017945 | 0.516556 | 0.036831 | 0.439370 | 0.413994 | 0.383119 |
| E012 | 0 | 0.592354 | 0.591855 | 0.000499 | 0.591647 | 0.000707 | 0.485948 | 0.485747 | 0.485656 |
| frequency | 0 | 0.591812 | 0.591812 | 0.000000 | 0.591812 | 0.000000 | 0.485818 | 0.485818 | 0.485818 |
| E011 | 1 | 0.387560 | 0.365408 | 0.022152 | 0.351796 | 0.035764 | 0.206607 | 0.196071 | 0.186650 |
| E012 | 1 | 0.503061 | 0.503154 | -0.000093 | 0.501087 | 0.001975 | 0.358963 | 0.358616 | 0.358767 |
| frequency | 1 | 0.501804 | 0.501804 | 0.000000 | 0.501804 | 0.000000 | 0.358963 | 0.358963 | 0.358963 |
| E011 | 2 | 0.558403 | 0.531791 | 0.026613 | 0.480456 | 0.077948 | 0.416500 | 0.372897 | 0.299214 |
| E012 | 2 | 0.536755 | 0.536570 | 0.000185 | 0.533370 | 0.003385 | 0.395408 | 0.395408 | 0.395408 |
| frequency | 2 | 0.538824 | 0.538824 | 0.000000 | 0.538824 | 0.000000 | 0.395408 | 0.395408 | 0.395408 |
| E011 | 3 | 0.527946 | 0.494313 | 0.033633 | 0.462419 | 0.065527 | 0.427443 | 0.377356 | 0.325917 |
| E012 | 3 | 0.499953 | 0.497984 | 0.001969 | 0.500773 | -0.000820 | 0.370470 | 0.369385 | 0.368374 |
| frequency | 3 | 0.501222 | 0.501222 | 0.000000 | 0.501222 | 0.000000 | 0.368777 | 0.368777 | 0.368777 |
| E011 | 4 | 0.532140 | 0.499067 | 0.033073 | 0.517415 | 0.014725 | 0.352870 | 0.309945 | 0.335622 |
| E012 | 4 | 0.554018 | 0.553500 | 0.000518 | 0.554813 | -0.000796 | 0.401080 | 0.401080 | 0.401080 |
| frequency | 4 | 0.562413 | 0.562413 | 0.000000 | 0.562413 | 0.000000 | 0.401080 | 0.401080 | 0.401080 |

## All aggregate support and shuffle dispersion summaries

Percentiles describe the 100 label-blind assignments, not population confidence intervals. Fold SD is across the five replicate-mean effects.

| Model | Stratum | Metric | Condition | Original mean | Shuffled mean | Delta mean | Delta fold SD | Defined folds | Delta shuffle SD | Delta p2.5 | Delta p97.5 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| E011 | all | map_at_3 | explanation_shuffle | 0.511887 | 0.485204 | 0.026683 | 0.006820 | 5 | 0.000670 | 0.025473 | 0.027837 |
| E011 | all | map_at_3 | pair_shuffle | 0.511887 | 0.465728 | 0.046159 | 0.025341 | 5 | 0.001005 | 0.044190 | 0.048133 |
| E011 | all | top1_accuracy | explanation_shuffle | 0.368558 | 0.334053 | 0.034505 | 0.016235 | 5 | 0.000976 | 0.032876 | 0.036334 |
| E011 | all | top1_accuracy | pair_shuffle | 0.368558 | 0.306104 | 0.062454 | 0.045884 | 5 | 0.001489 | 0.059468 | 0.065259 |
| E011 | unsupported | map_at_3 | explanation_shuffle | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 5 | 0.000000 | 0.000000 | 0.000000 |
| E011 | unsupported | map_at_3 | pair_shuffle | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 5 | 0.000000 | 0.000000 | 0.000000 |
| E011 | unsupported | top1_accuracy | explanation_shuffle | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 5 | 0.000000 | 0.000000 | 0.000000 |
| E011 | unsupported | top1_accuracy | pair_shuffle | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 5 | 0.000000 | 0.000000 | 0.000000 |
| E011 | rare | map_at_3 | explanation_shuffle | null | null | null | null | 0 | null | null | null |
| E011 | rare | map_at_3 | pair_shuffle | null | null | null | null | 0 | null | null | null |
| E011 | rare | top1_accuracy | explanation_shuffle | null | null | null | null | 0 | null | null | null |
| E011 | rare | top1_accuracy | pair_shuffle | null | null | null | null | 0 | null | null | null |
| E011 | frequent | map_at_3 | explanation_shuffle | 0.656817 | 0.621938 | 0.034880 | 0.011485 | 5 | 0.000882 | 0.033282 | 0.036347 |
| E011 | frequent | map_at_3 | pair_shuffle | 0.656817 | 0.595941 | 0.060876 | 0.037493 | 5 | 0.001319 | 0.058316 | 0.063610 |
| E011 | frequent | top1_accuracy | explanation_shuffle | 0.472586 | 0.427287 | 0.045299 | 0.024199 | 5 | 0.001296 | 0.043088 | 0.047757 |
| E011 | frequent | top1_accuracy | pair_shuffle | 0.472586 | 0.390009 | 0.082578 | 0.065919 | 5 | 0.001943 | 0.078661 | 0.086254 |
| E011 | well_supported | map_at_3 | explanation_shuffle | 0.671376 | 0.635791 | 0.035585 | 0.011050 | 5 | 0.000905 | 0.033941 | 0.037112 |
| E011 | well_supported | map_at_3 | pair_shuffle | 0.671376 | 0.609455 | 0.061921 | 0.036939 | 5 | 0.001347 | 0.059274 | 0.064680 |
| E011 | well_supported | top1_accuracy | explanation_shuffle | 0.481773 | 0.435878 | 0.045895 | 0.023742 | 5 | 0.001318 | 0.043658 | 0.048403 |
| E011 | well_supported | top1_accuracy | pair_shuffle | 0.481773 | 0.398274 | 0.083499 | 0.065201 | 5 | 0.001974 | 0.079528 | 0.087242 |
| E012 | all | map_at_3 | explanation_shuffle | 0.537228 | 0.536613 | 0.000616 | 0.000797 | 5 | 0.000137 | 0.000359 | 0.000919 |
| E012 | all | map_at_3 | pair_shuffle | 0.537228 | 0.536338 | 0.000890 | 0.001817 | 5 | 0.000182 | 0.000546 | 0.001273 |
| E012 | all | top1_accuracy | explanation_shuffle | 0.402374 | 0.402047 | 0.000327 | 0.000448 | 5 | 0.000073 | 0.000152 | 0.000464 |
| E012 | all | top1_accuracy | pair_shuffle | 0.402374 | 0.401857 | 0.000517 | 0.000892 | 5 | 0.000112 | 0.000303 | 0.000730 |
| E012 | unsupported | map_at_3 | explanation_shuffle | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 5 | 0.000000 | 0.000000 | 0.000000 |
| E012 | unsupported | map_at_3 | pair_shuffle | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 5 | 0.000000 | 0.000000 | 0.000000 |
| E012 | unsupported | top1_accuracy | explanation_shuffle | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 5 | 0.000000 | 0.000000 | 0.000000 |
| E012 | unsupported | top1_accuracy | pair_shuffle | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 5 | 0.000000 | 0.000000 | 0.000000 |
| E012 | rare | map_at_3 | explanation_shuffle | null | null | null | null | 0 | null | null | null |
| E012 | rare | map_at_3 | pair_shuffle | null | null | null | null | 0 | null | null | null |
| E012 | rare | top1_accuracy | explanation_shuffle | null | null | null | null | 0 | null | null | null |
| E012 | rare | top1_accuracy | pair_shuffle | null | null | null | null | 0 | null | null | null |
| E012 | frequent | map_at_3 | explanation_shuffle | 0.686659 | 0.685829 | 0.000830 | 0.001158 | 5 | 0.000179 | 0.000496 | 0.001208 |
| E012 | frequent | map_at_3 | pair_shuffle | 0.686659 | 0.685515 | 0.001145 | 0.002460 | 5 | 0.000241 | 0.000681 | 0.001649 |
| E012 | frequent | top1_accuracy | explanation_shuffle | 0.512122 | 0.511677 | 0.000445 | 0.000651 | 5 | 0.000099 | 0.000220 | 0.000625 |
| E012 | frequent | top1_accuracy | pair_shuffle | 0.512122 | 0.511406 | 0.000716 | 0.001293 | 5 | 0.000151 | 0.000439 | 0.001011 |
| E012 | well_supported | map_at_3 | explanation_shuffle | 0.703312 | 0.702598 | 0.000714 | 0.001210 | 5 | 0.000179 | 0.000396 | 0.001079 |
| E012 | well_supported | map_at_3 | pair_shuffle | 0.703312 | 0.702281 | 0.001031 | 0.002686 | 5 | 0.000255 | 0.000530 | 0.001580 |
| E012 | well_supported | top1_accuracy | explanation_shuffle | 0.525069 | 0.524615 | 0.000454 | 0.000650 | 5 | 0.000103 | 0.000212 | 0.000648 |
| E012 | well_supported | top1_accuracy | pair_shuffle | 0.525069 | 0.524347 | 0.000722 | 0.001290 | 5 | 0.000158 | 0.000424 | 0.001028 |
| frequency | all | map_at_3 | explanation_shuffle | 0.539215 | 0.539215 | 0.000000 | 0.000000 | 5 | 0.000000 | 0.000000 | 0.000000 |
| frequency | all | map_at_3 | pair_shuffle | 0.539215 | 0.539215 | 0.000000 | 0.000000 | 5 | 0.000000 | 0.000000 | 0.000000 |
| frequency | all | top1_accuracy | explanation_shuffle | 0.402009 | 0.402009 | 0.000000 | 0.000000 | 5 | 0.000000 | 0.000000 | 0.000000 |
| frequency | all | top1_accuracy | pair_shuffle | 0.402009 | 0.402009 | 0.000000 | 0.000000 | 5 | 0.000000 | 0.000000 | 0.000000 |
| frequency | unsupported | map_at_3 | explanation_shuffle | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 5 | 0.000000 | 0.000000 | 0.000000 |
| frequency | unsupported | map_at_3 | pair_shuffle | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 5 | 0.000000 | 0.000000 | 0.000000 |
| frequency | unsupported | top1_accuracy | explanation_shuffle | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 5 | 0.000000 | 0.000000 | 0.000000 |
| frequency | unsupported | top1_accuracy | pair_shuffle | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 5 | 0.000000 | 0.000000 | 0.000000 |
| frequency | rare | map_at_3 | explanation_shuffle | null | null | null | null | 0 | null | null | null |
| frequency | rare | map_at_3 | pair_shuffle | null | null | null | null | 0 | null | null | null |
| frequency | rare | top1_accuracy | explanation_shuffle | null | null | null | null | 0 | null | null | null |
| frequency | rare | top1_accuracy | pair_shuffle | null | null | null | null | 0 | null | null | null |
| frequency | frequent | map_at_3 | explanation_shuffle | 0.689284 | 0.689284 | 0.000000 | 0.000000 | 5 | 0.000000 | 0.000000 | 0.000000 |
| frequency | frequent | map_at_3 | pair_shuffle | 0.689284 | 0.689284 | 0.000000 | 0.000000 | 5 | 0.000000 | 0.000000 | 0.000000 |
| frequency | frequent | top1_accuracy | explanation_shuffle | 0.511607 | 0.511607 | 0.000000 | 0.000000 | 5 | 0.000000 | 0.000000 | 0.000000 |
| frequency | frequent | top1_accuracy | pair_shuffle | 0.511607 | 0.511607 | 0.000000 | 0.000000 | 5 | 0.000000 | 0.000000 | 0.000000 |
| frequency | well_supported | map_at_3 | explanation_shuffle | 0.706722 | 0.706722 | 0.000000 | 0.000000 | 5 | 0.000000 | 0.000000 | 0.000000 |
| frequency | well_supported | map_at_3 | pair_shuffle | 0.706722 | 0.706722 | 0.000000 | 0.000000 | 5 | 0.000000 | 0.000000 | 0.000000 |
| frequency | well_supported | top1_accuracy | explanation_shuffle | 0.524554 | 0.524554 | 0.000000 | 0.000000 | 5 | 0.000000 | 0.000000 | 0.000000 |
| frequency | well_supported | top1_accuracy | pair_shuffle | 0.524554 | 0.524554 | 0.000000 | 0.000000 | 5 | 0.000000 | 0.000000 | 0.000000 |

## All fold and question support results

| Model | Fold | Question | Stratum | n | Metric | Original | Explanation mean | Explanation delta | Pair mean | Pair delta |
|---|---|---|---|---|---|---|---|---|---|---|
| E011 | 0 | all | all | 7686 | map_at_3 | 0.553387 | 0.535442 | 0.017945 | 0.516556 | 0.036831 |
| E011 | 0 | all | all | 7686 | top1_accuracy | 0.439370 | 0.413994 | 0.025376 | 0.383119 | 0.056252 |
| E011 | 0 | all | unsupported | 407 | map_at_3 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 |
| E011 | 0 | all | unsupported | 407 | top1_accuracy | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 |
| E011 | 0 | all | rare | 0 | map_at_3 | null | null | null | null | null |
| E011 | 0 | all | rare | 0 | top1_accuracy | null | null | null | null | null |
| E011 | 0 | all | frequent | 7279 | map_at_3 | 0.584329 | 0.565381 | 0.018948 | 0.545439 | 0.038891 |
| E011 | 0 | all | frequent | 7279 | top1_accuracy | 0.463937 | 0.437142 | 0.026795 | 0.404540 | 0.059397 |
| E011 | 0 | all | well_supported | 7025 | map_at_3 | 0.605457 | 0.585823 | 0.019633 | 0.565160 | 0.040297 |
| E011 | 0 | all | well_supported | 7025 | top1_accuracy | 0.480712 | 0.452948 | 0.027764 | 0.419167 | 0.061544 |
| E011 | 0 | 31772 | all | 4857 | map_at_3 | 0.498765 | 0.489199 | 0.009565 | 0.476632 | 0.022132 |
| E011 | 0 | 31772 | all | 4857 | top1_accuracy | 0.379246 | 0.360793 | 0.018454 | 0.335874 | 0.043372 |
| E011 | 0 | 31772 | unsupported | 16 | map_at_3 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 |
| E011 | 0 | 31772 | unsupported | 16 | top1_accuracy | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 |
| E011 | 0 | 31772 | rare | 0 | map_at_3 | null | null | null | null | null |
| E011 | 0 | 31772 | rare | 0 | top1_accuracy | null | null | null | null | null |
| E011 | 0 | 31772 | frequent | 4841 | map_at_3 | 0.500413 | 0.490816 | 0.009597 | 0.478208 | 0.022205 |
| E011 | 0 | 31772 | frequent | 4841 | top1_accuracy | 0.380500 | 0.361985 | 0.018515 | 0.336984 | 0.043516 |
| E011 | 0 | 31772 | well_supported | 4587 | map_at_3 | 0.528123 | 0.517995 | 0.010128 | 0.504688 | 0.023435 |
| E011 | 0 | 31772 | well_supported | 4587 | top1_accuracy | 0.401570 | 0.382030 | 0.019540 | 0.355644 | 0.045925 |
| E011 | 0 | 32829 | all | 2156 | map_at_3 | 0.759972 | 0.721700 | 0.038272 | 0.660866 | 0.099106 |
| E011 | 0 | 32829 | all | 2156 | top1_accuracy | 0.686456 | 0.637862 | 0.048595 | 0.560269 | 0.126187 |
| E011 | 0 | 32829 | unsupported | 272 | map_at_3 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 |
| E011 | 0 | 32829 | unsupported | 272 | top1_accuracy | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 |
| E011 | 0 | 32829 | rare | 0 | map_at_3 | null | null | null | null | null |
| E011 | 0 | 32829 | rare | 0 | top1_accuracy | null | null | null | null | null |
| E011 | 0 | 32829 | frequent | 1884 | map_at_3 | 0.869692 | 0.825894 | 0.043798 | 0.756277 | 0.113415 |
| E011 | 0 | 32829 | frequent | 1884 | top1_accuracy | 0.785563 | 0.729952 | 0.055610 | 0.641157 | 0.144406 |
| E011 | 0 | 32829 | well_supported | 1884 | map_at_3 | 0.869692 | 0.825894 | 0.043798 | 0.756277 | 0.113415 |
| E011 | 0 | 32829 | well_supported | 1884 | top1_accuracy | 0.785563 | 0.729952 | 0.055610 | 0.641157 | 0.144406 |
| E011 | 0 | 104665 | all | 673 | map_at_3 | 0.285785 | 0.272486 | 0.013299 | 0.342375 | -0.056590 |
| E011 | 0 | 104665 | all | 673 | top1_accuracy | 0.081724 | 0.080773 | 0.000951 | 0.156568 | -0.074844 |
| E011 | 0 | 104665 | unsupported | 119 | map_at_3 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 |
| E011 | 0 | 104665 | unsupported | 119 | top1_accuracy | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 |
| E011 | 0 | 104665 | rare | 0 | map_at_3 | null | null | null | null | null |
| E011 | 0 | 104665 | rare | 0 | top1_accuracy | null | null | null | null | null |
| E011 | 0 | 104665 | frequent | 554 | map_at_3 | 0.347172 | 0.331017 | 0.016155 | 0.415918 | -0.068745 |
| E011 | 0 | 104665 | frequent | 554 | top1_accuracy | 0.099278 | 0.098123 | 0.001155 | 0.190199 | -0.090921 |
| E011 | 0 | 104665 | well_supported | 554 | map_at_3 | 0.347172 | 0.331017 | 0.016155 | 0.415918 | -0.068745 |
| E011 | 0 | 104665 | well_supported | 554 | top1_accuracy | 0.099278 | 0.098123 | 0.001155 | 0.190199 | -0.090921 |
| E012 | 0 | all | all | 7686 | map_at_3 | 0.592354 | 0.591855 | 0.000499 | 0.591647 | 0.000707 |
| E012 | 0 | all | all | 7686 | top1_accuracy | 0.485948 | 0.485747 | 0.000202 | 0.485656 | 0.000293 |
| E012 | 0 | all | unsupported | 407 | map_at_3 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 |
| E012 | 0 | all | unsupported | 407 | top1_accuracy | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 |
| E012 | 0 | all | rare | 0 | map_at_3 | null | null | null | null | null |
| E012 | 0 | all | rare | 0 | top1_accuracy | null | null | null | null | null |
| E012 | 0 | all | frequent | 7279 | map_at_3 | 0.625475 | 0.624948 | 0.000527 | 0.624728 | 0.000747 |
| E012 | 0 | all | frequent | 7279 | top1_accuracy | 0.513120 | 0.512907 | 0.000213 | 0.512811 | 0.000309 |
| E012 | 0 | all | well_supported | 7025 | map_at_3 | 0.648090 | 0.647544 | 0.000546 | 0.647316 | 0.000774 |
| E012 | 0 | all | well_supported | 7025 | top1_accuracy | 0.531673 | 0.531452 | 0.000221 | 0.531352 | 0.000320 |
| E012 | 0 | 31772 | all | 4857 | map_at_3 | 0.486068 | 0.486026 | 0.000042 | 0.485815 | 0.000254 |
| E012 | 0 | 31772 | all | 4857 | top1_accuracy | 0.353922 | 0.353922 | 0.000000 | 0.353922 | 0.000000 |
| E012 | 0 | 31772 | unsupported | 16 | map_at_3 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 |
| E012 | 0 | 31772 | unsupported | 16 | top1_accuracy | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 |
| E012 | 0 | 31772 | rare | 0 | map_at_3 | null | null | null | null | null |
| E012 | 0 | 31772 | rare | 0 | top1_accuracy | null | null | null | null | null |
| E012 | 0 | 31772 | frequent | 4841 | map_at_3 | 0.487675 | 0.487633 | 0.000042 | 0.487420 | 0.000254 |
| E012 | 0 | 31772 | frequent | 4841 | top1_accuracy | 0.355092 | 0.355092 | 0.000000 | 0.355092 | 0.000000 |
| E012 | 0 | 31772 | well_supported | 4587 | map_at_3 | 0.514679 | 0.514635 | 0.000044 | 0.514411 | 0.000269 |
| E012 | 0 | 31772 | well_supported | 4587 | top1_accuracy | 0.374755 | 0.374755 | 0.000000 | 0.374755 | 0.000000 |
| E012 | 0 | 32829 | all | 2156 | map_at_3 | 0.792285 | 0.790601 | 0.001684 | 0.790335 | 0.001950 |
| E012 | 0 | 32829 | all | 2156 | top1_accuracy | 0.733302 | 0.732583 | 0.000719 | 0.732259 | 0.001044 |
| E012 | 0 | 32829 | unsupported | 272 | map_at_3 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 |
| E012 | 0 | 32829 | unsupported | 272 | top1_accuracy | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 |
| E012 | 0 | 32829 | rare | 0 | map_at_3 | null | null | null | null | null |
| E012 | 0 | 32829 | rare | 0 | top1_accuracy | null | null | null | null | null |
| E012 | 0 | 32829 | frequent | 1884 | map_at_3 | 0.906670 | 0.904743 | 0.001928 | 0.904439 | 0.002231 |
| E012 | 0 | 32829 | frequent | 1884 | top1_accuracy | 0.839172 | 0.838349 | 0.000823 | 0.837978 | 0.001194 |
| E012 | 0 | 32829 | well_supported | 1884 | map_at_3 | 0.906670 | 0.904743 | 0.001928 | 0.904439 | 0.002231 |
| E012 | 0 | 32829 | well_supported | 1884 | top1_accuracy | 0.839172 | 0.838349 | 0.000823 | 0.837978 | 0.001194 |
| E012 | 0 | 104665 | all | 673 | map_at_3 | 0.718920 | 0.718920 | 0.000000 | 0.718920 | 0.000000 |
| E012 | 0 | 104665 | all | 673 | top1_accuracy | 0.646360 | 0.646360 | 0.000000 | 0.646360 | 0.000000 |
| E012 | 0 | 104665 | unsupported | 119 | map_at_3 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 |
| E012 | 0 | 104665 | unsupported | 119 | top1_accuracy | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 |
| E012 | 0 | 104665 | rare | 0 | map_at_3 | null | null | null | null | null |
| E012 | 0 | 104665 | rare | 0 | top1_accuracy | null | null | null | null | null |
| E012 | 0 | 104665 | frequent | 554 | map_at_3 | 0.873345 | 0.873345 | 0.000000 | 0.873345 | 0.000000 |
| E012 | 0 | 104665 | frequent | 554 | top1_accuracy | 0.785199 | 0.785199 | 0.000000 | 0.785199 | 0.000000 |
| E012 | 0 | 104665 | well_supported | 554 | map_at_3 | 0.873345 | 0.873345 | 0.000000 | 0.873345 | 0.000000 |
| E012 | 0 | 104665 | well_supported | 554 | top1_accuracy | 0.785199 | 0.785199 | 0.000000 | 0.785199 | 0.000000 |
| frequency | 0 | all | all | 7686 | map_at_3 | 0.591812 | 0.591812 | 0.000000 | 0.591812 | 0.000000 |
| frequency | 0 | all | all | 7686 | top1_accuracy | 0.485818 | 0.485818 | 0.000000 | 0.485818 | 0.000000 |
| frequency | 0 | all | unsupported | 407 | map_at_3 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 |
| frequency | 0 | all | unsupported | 407 | top1_accuracy | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 |
| frequency | 0 | all | rare | 0 | map_at_3 | null | null | null | null | null |
| frequency | 0 | all | rare | 0 | top1_accuracy | null | null | null | null | null |
| frequency | 0 | all | frequent | 7279 | map_at_3 | 0.624903 | 0.624903 | 0.000000 | 0.624903 | 0.000000 |
| frequency | 0 | all | frequent | 7279 | top1_accuracy | 0.512983 | 0.512983 | 0.000000 | 0.512983 | 0.000000 |
| frequency | 0 | all | well_supported | 7025 | map_at_3 | 0.647497 | 0.647497 | 0.000000 | 0.647497 | 0.000000 |
| frequency | 0 | all | well_supported | 7025 | top1_accuracy | 0.531530 | 0.531530 | 0.000000 | 0.531530 | 0.000000 |
| frequency | 0 | 31772 | all | 4857 | map_at_3 | 0.485862 | 0.485862 | 0.000000 | 0.485862 | 0.000000 |
| frequency | 0 | 31772 | all | 4857 | top1_accuracy | 0.353922 | 0.353922 | 0.000000 | 0.353922 | 0.000000 |
| frequency | 0 | 31772 | unsupported | 16 | map_at_3 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 |
| frequency | 0 | 31772 | unsupported | 16 | top1_accuracy | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 |
| frequency | 0 | 31772 | rare | 0 | map_at_3 | null | null | null | null | null |
| frequency | 0 | 31772 | rare | 0 | top1_accuracy | null | null | null | null | null |
| frequency | 0 | 31772 | frequent | 4841 | map_at_3 | 0.487468 | 0.487468 | 0.000000 | 0.487468 | 0.000000 |
| frequency | 0 | 31772 | frequent | 4841 | top1_accuracy | 0.355092 | 0.355092 | 0.000000 | 0.355092 | 0.000000 |
| frequency | 0 | 31772 | well_supported | 4587 | map_at_3 | 0.514461 | 0.514461 | 0.000000 | 0.514461 | 0.000000 |
| frequency | 0 | 31772 | well_supported | 4587 | top1_accuracy | 0.374755 | 0.374755 | 0.000000 | 0.374755 | 0.000000 |
| frequency | 0 | 32829 | all | 2156 | map_at_3 | 0.790816 | 0.790816 | 0.000000 | 0.790816 | 0.000000 |
| frequency | 0 | 32829 | all | 2156 | top1_accuracy | 0.732839 | 0.732839 | 0.000000 | 0.732839 | 0.000000 |
| frequency | 0 | 32829 | unsupported | 272 | map_at_3 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 |
| frequency | 0 | 32829 | unsupported | 272 | top1_accuracy | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 |
| frequency | 0 | 32829 | rare | 0 | map_at_3 | null | null | null | null | null |
| frequency | 0 | 32829 | rare | 0 | top1_accuracy | null | null | null | null | null |
| frequency | 0 | 32829 | frequent | 1884 | map_at_3 | 0.904989 | 0.904989 | 0.000000 | 0.904989 | 0.000000 |
| frequency | 0 | 32829 | frequent | 1884 | top1_accuracy | 0.838641 | 0.838641 | 0.000000 | 0.838641 | 0.000000 |
| frequency | 0 | 32829 | well_supported | 1884 | map_at_3 | 0.904989 | 0.904989 | 0.000000 | 0.904989 | 0.000000 |
| frequency | 0 | 32829 | well_supported | 1884 | top1_accuracy | 0.838641 | 0.838641 | 0.000000 | 0.838641 | 0.000000 |
| frequency | 0 | 104665 | all | 673 | map_at_3 | 0.718920 | 0.718920 | 0.000000 | 0.718920 | 0.000000 |
| frequency | 0 | 104665 | all | 673 | top1_accuracy | 0.646360 | 0.646360 | 0.000000 | 0.646360 | 0.000000 |
| frequency | 0 | 104665 | unsupported | 119 | map_at_3 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 |
| frequency | 0 | 104665 | unsupported | 119 | top1_accuracy | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 |
| frequency | 0 | 104665 | rare | 0 | map_at_3 | null | null | null | null | null |
| frequency | 0 | 104665 | rare | 0 | top1_accuracy | null | null | null | null | null |
| frequency | 0 | 104665 | frequent | 554 | map_at_3 | 0.873345 | 0.873345 | 0.000000 | 0.873345 | 0.000000 |
| frequency | 0 | 104665 | frequent | 554 | top1_accuracy | 0.785199 | 0.785199 | 0.000000 | 0.785199 | 0.000000 |
| frequency | 0 | 104665 | well_supported | 554 | map_at_3 | 0.873345 | 0.873345 | 0.000000 | 0.873345 | 0.000000 |
| frequency | 0 | 104665 | well_supported | 554 | top1_accuracy | 0.785199 | 0.785199 | 0.000000 | 0.785199 | 0.000000 |
| E011 | 1 | all | all | 7023 | map_at_3 | 0.387560 | 0.365408 | 0.022152 | 0.351796 | 0.035764 |
| E011 | 1 | all | all | 7023 | top1_accuracy | 0.206607 | 0.196071 | 0.010535 | 0.186650 | 0.019957 |
| E011 | 1 | all | unsupported | 1613 | map_at_3 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 |
| E011 | 1 | all | unsupported | 1613 | top1_accuracy | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 |
| E011 | 1 | all | rare | 0 | map_at_3 | null | null | null | null | null |
| E011 | 1 | all | rare | 0 | top1_accuracy | null | null | null | null | null |
| E011 | 1 | all | frequent | 5410 | map_at_3 | 0.503112 | 0.474355 | 0.028757 | 0.456684 | 0.046428 |
| E011 | 1 | all | frequent | 5410 | top1_accuracy | 0.268207 | 0.254530 | 0.013677 | 0.242299 | 0.025908 |
| E011 | 1 | all | well_supported | 5005 | map_at_3 | 0.543823 | 0.512739 | 0.031084 | 0.493638 | 0.050184 |
| E011 | 1 | all | well_supported | 5005 | top1_accuracy | 0.289910 | 0.275127 | 0.014783 | 0.261906 | 0.028004 |
| E011 | 1 | 31778 | all | 3640 | map_at_3 | 0.309753 | 0.272455 | 0.037298 | 0.247266 | 0.062486 |
| E011 | 1 | 31778 | all | 3640 | top1_accuracy | 0.187912 | 0.177154 | 0.010758 | 0.161217 | 0.026695 |
| E011 | 1 | 31778 | unsupported | 1017 | map_at_3 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 |
| E011 | 1 | 31778 | unsupported | 1017 | top1_accuracy | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 |
| E011 | 1 | 31778 | rare | 0 | map_at_3 | null | null | null | null | null |
| E011 | 1 | 31778 | rare | 0 | top1_accuracy | null | null | null | null | null |
| E011 | 1 | 31778 | frequent | 2623 | map_at_3 | 0.429851 | 0.378093 | 0.051759 | 0.343138 | 0.086714 |
| E011 | 1 | 31778 | frequent | 2623 | top1_accuracy | 0.260770 | 0.245841 | 0.014929 | 0.223725 | 0.037045 |
| E011 | 1 | 31778 | well_supported | 2218 | map_at_3 | 0.508341 | 0.447131 | 0.061210 | 0.405794 | 0.102547 |
| E011 | 1 | 31778 | well_supported | 2218 | top1_accuracy | 0.308386 | 0.290730 | 0.017656 | 0.264576 | 0.043810 |
| E011 | 1 | 32835 | all | 2332 | map_at_3 | 0.412521 | 0.410034 | 0.002487 | 0.414326 | -0.001805 |
| E011 | 1 | 32835 | all | 2332 | top1_accuracy | 0.132933 | 0.128739 | 0.004194 | 0.137075 | -0.004142 |
| E011 | 1 | 32835 | unsupported | 399 | map_at_3 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 |
| E011 | 1 | 32835 | unsupported | 399 | top1_accuracy | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 |
| E011 | 1 | 32835 | rare | 0 | map_at_3 | null | null | null | null | null |
| E011 | 1 | 32835 | rare | 0 | top1_accuracy | null | null | null | null | null |
| E011 | 1 | 32835 | frequent | 1933 | map_at_3 | 0.497672 | 0.494671 | 0.003001 | 0.499849 | -0.002177 |
| E011 | 1 | 32835 | frequent | 1933 | top1_accuracy | 0.160372 | 0.155313 | 0.005059 | 0.165370 | -0.004997 |
| E011 | 1 | 32835 | well_supported | 1933 | map_at_3 | 0.497672 | 0.494671 | 0.003001 | 0.499849 | -0.002177 |
| E011 | 1 | 32835 | well_supported | 1933 | top1_accuracy | 0.160372 | 0.155313 | 0.005059 | 0.165370 | -0.004997 |
| E011 | 1 | 109465 | all | 1051 | map_at_3 | 0.601649 | 0.588317 | 0.013332 | 0.575073 | 0.026576 |
| E011 | 1 | 109465 | all | 1051 | top1_accuracy | 0.434824 | 0.410990 | 0.023834 | 0.384729 | 0.050095 |
| E011 | 1 | 109465 | unsupported | 197 | map_at_3 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 |
| E011 | 1 | 109465 | unsupported | 197 | top1_accuracy | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 |
| E011 | 1 | 109465 | rare | 0 | map_at_3 | null | null | null | null | null |
| E011 | 1 | 109465 | rare | 0 | top1_accuracy | null | null | null | null | null |
| E011 | 1 | 109465 | frequent | 854 | map_at_3 | 0.740437 | 0.724030 | 0.016407 | 0.707730 | 0.032707 |
| E011 | 1 | 109465 | frequent | 854 | top1_accuracy | 0.535129 | 0.505796 | 0.029333 | 0.473478 | 0.061651 |
| E011 | 1 | 109465 | well_supported | 854 | map_at_3 | 0.740437 | 0.724030 | 0.016407 | 0.707730 | 0.032707 |
| E011 | 1 | 109465 | well_supported | 854 | top1_accuracy | 0.535129 | 0.505796 | 0.029333 | 0.473478 | 0.061651 |
| E012 | 1 | all | all | 7023 | map_at_3 | 0.503061 | 0.503154 | -0.000093 | 0.501087 | 0.001975 |
| E012 | 1 | all | all | 7023 | top1_accuracy | 0.358963 | 0.358616 | 0.000347 | 0.358767 | 0.000196 |
| E012 | 1 | all | unsupported | 1613 | map_at_3 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 |
| E012 | 1 | all | unsupported | 1613 | top1_accuracy | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 |
| E012 | 1 | all | rare | 0 | map_at_3 | null | null | null | null | null |
| E012 | 1 | all | rare | 0 | top1_accuracy | null | null | null | null | null |
| E012 | 1 | all | frequent | 5410 | map_at_3 | 0.653050 | 0.653170 | -0.000120 | 0.650486 | 0.002563 |
| E012 | 1 | all | frequent | 5410 | top1_accuracy | 0.465989 | 0.465538 | 0.000451 | 0.465734 | 0.000255 |
| E012 | 1 | all | well_supported | 5005 | map_at_3 | 0.705894 | 0.706024 | -0.000130 | 0.703123 | 0.002771 |
| E012 | 1 | all | well_supported | 5005 | top1_accuracy | 0.503696 | 0.503209 | 0.000488 | 0.503421 | 0.000276 |
| E012 | 1 | 31778 | all | 3640 | map_at_3 | 0.438324 | 0.438853 | -0.000529 | 0.434769 | 0.003555 |
| E012 | 1 | 31778 | all | 3640 | top1_accuracy | 0.313187 | 0.313187 | 0.000000 | 0.313187 | 0.000000 |
| E012 | 1 | 31778 | unsupported | 1017 | map_at_3 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 |
| E012 | 1 | 31778 | unsupported | 1017 | top1_accuracy | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 |
| E012 | 1 | 31778 | rare | 0 | map_at_3 | null | null | null | null | null |
| E012 | 1 | 31778 | rare | 0 | top1_accuracy | null | null | null | null | null |
| E012 | 1 | 31778 | frequent | 2623 | map_at_3 | 0.608273 | 0.609007 | -0.000735 | 0.603339 | 0.004934 |
| E012 | 1 | 31778 | frequent | 2623 | top1_accuracy | 0.434617 | 0.434617 | 0.000000 | 0.434617 | 0.000000 |
| E012 | 1 | 31778 | well_supported | 2218 | map_at_3 | 0.719342 | 0.720210 | -0.000869 | 0.713507 | 0.005835 |
| E012 | 1 | 31778 | well_supported | 2218 | top1_accuracy | 0.513977 | 0.513977 | 0.000000 | 0.513977 | 0.000000 |
| E012 | 1 | 32835 | all | 2332 | map_at_3 | 0.565609 | 0.565465 | 0.000144 | 0.565430 | 0.000179 |
| E012 | 1 | 32835 | all | 2332 | top1_accuracy | 0.409091 | 0.408851 | 0.000240 | 0.408937 | 0.000154 |
| E012 | 1 | 32835 | unsupported | 399 | map_at_3 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 |
| E012 | 1 | 32835 | unsupported | 399 | top1_accuracy | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 |
| E012 | 1 | 32835 | rare | 0 | map_at_3 | null | null | null | null | null |
| E012 | 1 | 32835 | rare | 0 | top1_accuracy | null | null | null | null | null |
| E012 | 1 | 32835 | frequent | 1933 | map_at_3 | 0.682359 | 0.682185 | 0.000174 | 0.682143 | 0.000216 |
| E012 | 1 | 32835 | frequent | 1933 | top1_accuracy | 0.493533 | 0.493244 | 0.000290 | 0.493347 | 0.000186 |
| E012 | 1 | 32835 | well_supported | 1933 | map_at_3 | 0.682359 | 0.682185 | 0.000174 | 0.682143 | 0.000216 |
| E012 | 1 | 32835 | well_supported | 1933 | top1_accuracy | 0.493533 | 0.493244 | 0.000290 | 0.493347 | 0.000186 |
| E012 | 1 | 109465 | all | 1051 | map_at_3 | 0.588487 | 0.587593 | 0.000894 | 0.588002 | 0.000485 |
| E012 | 1 | 109465 | all | 1051 | top1_accuracy | 0.406280 | 0.404491 | 0.001789 | 0.405309 | 0.000971 |
| E012 | 1 | 109465 | unsupported | 197 | map_at_3 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 |
| E012 | 1 | 109465 | unsupported | 197 | top1_accuracy | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 |
| E012 | 1 | 109465 | rare | 0 | map_at_3 | null | null | null | null | null |
| E012 | 1 | 109465 | rare | 0 | top1_accuracy | null | null | null | null | null |
| E012 | 1 | 109465 | frequent | 854 | map_at_3 | 0.724239 | 0.723138 | 0.001101 | 0.723642 | 0.000597 |
| E012 | 1 | 109465 | frequent | 854 | top1_accuracy | 0.500000 | 0.497799 | 0.002201 | 0.498806 | 0.001194 |
| E012 | 1 | 109465 | well_supported | 854 | map_at_3 | 0.724239 | 0.723138 | 0.001101 | 0.723642 | 0.000597 |
| E012 | 1 | 109465 | well_supported | 854 | top1_accuracy | 0.500000 | 0.497799 | 0.002201 | 0.498806 | 0.001194 |
| frequency | 1 | all | all | 7023 | map_at_3 | 0.501804 | 0.501804 | 0.000000 | 0.501804 | 0.000000 |
| frequency | 1 | all | all | 7023 | top1_accuracy | 0.358963 | 0.358963 | 0.000000 | 0.358963 | 0.000000 |
| frequency | 1 | all | unsupported | 1613 | map_at_3 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 |
| frequency | 1 | all | unsupported | 1613 | top1_accuracy | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 |
| frequency | 1 | all | rare | 0 | map_at_3 | null | null | null | null | null |
| frequency | 1 | all | rare | 0 | top1_accuracy | null | null | null | null | null |
| frequency | 1 | all | frequent | 5410 | map_at_3 | 0.651417 | 0.651417 | 0.000000 | 0.651417 | 0.000000 |
| frequency | 1 | all | frequent | 5410 | top1_accuracy | 0.465989 | 0.465989 | 0.000000 | 0.465989 | 0.000000 |
| frequency | 1 | all | well_supported | 5005 | map_at_3 | 0.704129 | 0.704129 | 0.000000 | 0.704129 | 0.000000 |
| frequency | 1 | all | well_supported | 5005 | top1_accuracy | 0.503696 | 0.503696 | 0.000000 | 0.503696 | 0.000000 |
| frequency | 1 | 31778 | all | 3640 | map_at_3 | 0.435989 | 0.435989 | 0.000000 | 0.435989 | 0.000000 |
| frequency | 1 | 31778 | all | 3640 | top1_accuracy | 0.313187 | 0.313187 | 0.000000 | 0.313187 | 0.000000 |
| frequency | 1 | 31778 | unsupported | 1017 | map_at_3 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 |
| frequency | 1 | 31778 | unsupported | 1017 | top1_accuracy | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 |
| frequency | 1 | 31778 | rare | 0 | map_at_3 | null | null | null | null | null |
| frequency | 1 | 31778 | rare | 0 | top1_accuracy | null | null | null | null | null |
| frequency | 1 | 31778 | frequent | 2623 | map_at_3 | 0.605032 | 0.605032 | 0.000000 | 0.605032 | 0.000000 |
| frequency | 1 | 31778 | frequent | 2623 | top1_accuracy | 0.434617 | 0.434617 | 0.000000 | 0.434617 | 0.000000 |
| frequency | 1 | 31778 | well_supported | 2218 | map_at_3 | 0.715509 | 0.715509 | 0.000000 | 0.715509 | 0.000000 |
| frequency | 1 | 31778 | well_supported | 2218 | top1_accuracy | 0.513977 | 0.513977 | 0.000000 | 0.513977 | 0.000000 |
| frequency | 1 | 32835 | all | 2332 | map_at_3 | 0.565466 | 0.565466 | 0.000000 | 0.565466 | 0.000000 |
| frequency | 1 | 32835 | all | 2332 | top1_accuracy | 0.409091 | 0.409091 | 0.000000 | 0.409091 | 0.000000 |
| frequency | 1 | 32835 | unsupported | 399 | map_at_3 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 |
| frequency | 1 | 32835 | unsupported | 399 | top1_accuracy | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 |
| frequency | 1 | 32835 | rare | 0 | map_at_3 | null | null | null | null | null |
| frequency | 1 | 32835 | rare | 0 | top1_accuracy | null | null | null | null | null |
| frequency | 1 | 32835 | frequent | 1933 | map_at_3 | 0.682187 | 0.682187 | 0.000000 | 0.682187 | 0.000000 |
| frequency | 1 | 32835 | frequent | 1933 | top1_accuracy | 0.493533 | 0.493533 | 0.000000 | 0.493533 | 0.000000 |
| frequency | 1 | 32835 | well_supported | 1933 | map_at_3 | 0.682187 | 0.682187 | 0.000000 | 0.682187 | 0.000000 |
| frequency | 1 | 32835 | well_supported | 1933 | top1_accuracy | 0.493533 | 0.493533 | 0.000000 | 0.493533 | 0.000000 |
| frequency | 1 | 109465 | all | 1051 | map_at_3 | 0.588487 | 0.588487 | 0.000000 | 0.588487 | 0.000000 |
| frequency | 1 | 109465 | all | 1051 | top1_accuracy | 0.406280 | 0.406280 | 0.000000 | 0.406280 | 0.000000 |
| frequency | 1 | 109465 | unsupported | 197 | map_at_3 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 |
| frequency | 1 | 109465 | unsupported | 197 | top1_accuracy | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 |
| frequency | 1 | 109465 | rare | 0 | map_at_3 | null | null | null | null | null |
| frequency | 1 | 109465 | rare | 0 | top1_accuracy | null | null | null | null | null |
| frequency | 1 | 109465 | frequent | 854 | map_at_3 | 0.724239 | 0.724239 | 0.000000 | 0.724239 | 0.000000 |
| frequency | 1 | 109465 | frequent | 854 | top1_accuracy | 0.500000 | 0.500000 | 0.000000 | 0.500000 | 0.000000 |
| frequency | 1 | 109465 | well_supported | 854 | map_at_3 | 0.724239 | 0.724239 | 0.000000 | 0.724239 | 0.000000 |
| frequency | 1 | 109465 | well_supported | 854 | top1_accuracy | 0.500000 | 0.500000 | 0.000000 | 0.500000 | 0.000000 |
| E011 | 2 | all | all | 7491 | map_at_3 | 0.558403 | 0.531791 | 0.026613 | 0.480456 | 0.077948 |
| E011 | 2 | all | all | 7491 | top1_accuracy | 0.416500 | 0.372897 | 0.043603 | 0.299214 | 0.117286 |
| E011 | 2 | all | unsupported | 1985 | map_at_3 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 |
| E011 | 2 | all | unsupported | 1985 | top1_accuracy | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 |
| E011 | 2 | all | rare | 0 | map_at_3 | null | null | null | null | null |
| E011 | 2 | all | rare | 0 | top1_accuracy | null | null | null | null | null |
| E011 | 2 | all | frequent | 5506 | map_at_3 | 0.759717 | 0.723510 | 0.036207 | 0.653668 | 0.106049 |
| E011 | 2 | all | frequent | 5506 | top1_accuracy | 0.566655 | 0.507332 | 0.059323 | 0.407085 | 0.159570 |
| E011 | 2 | all | well_supported | 5506 | map_at_3 | 0.759717 | 0.723510 | 0.036207 | 0.653668 | 0.106049 |
| E011 | 2 | all | well_supported | 5506 | top1_accuracy | 0.566655 | 0.507332 | 0.059323 | 0.407085 | 0.159570 |
| E011 | 2 | 31774 | all | 3115 | map_at_3 | 0.632798 | 0.609745 | 0.023053 | 0.544604 | 0.088194 |
| E011 | 2 | 31774 | all | 3115 | top1_accuracy | 0.498234 | 0.459390 | 0.038844 | 0.383913 | 0.114321 |
| E011 | 2 | 31774 | unsupported | 637 | map_at_3 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 |
| E011 | 2 | 31774 | unsupported | 637 | top1_accuracy | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 |
| E011 | 2 | 31774 | rare | 0 | map_at_3 | null | null | null | null | null |
| E011 | 2 | 31774 | rare | 0 | top1_accuracy | null | null | null | null | null |
| E011 | 2 | 31774 | frequent | 2478 | map_at_3 | 0.795467 | 0.766488 | 0.028979 | 0.684601 | 0.110866 |
| E011 | 2 | 31774 | frequent | 2478 | top1_accuracy | 0.626312 | 0.577482 | 0.048830 | 0.482603 | 0.143709 |
| E011 | 2 | 31774 | well_supported | 2478 | map_at_3 | 0.795467 | 0.766488 | 0.028979 | 0.684601 | 0.110866 |
| E011 | 2 | 31774 | well_supported | 2478 | top1_accuracy | 0.626312 | 0.577482 | 0.048830 | 0.482603 | 0.143709 |
| E011 | 2 | 33474 | all | 1766 | map_at_3 | 0.440732 | 0.392433 | 0.048299 | 0.368931 | 0.071802 |
| E011 | 2 | 33474 | all | 1766 | top1_accuracy | 0.309173 | 0.230651 | 0.078522 | 0.197084 | 0.112089 |
| E011 | 2 | 33474 | unsupported | 683 | map_at_3 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 |
| E011 | 2 | 33474 | unsupported | 683 | top1_accuracy | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 |
| E011 | 2 | 33474 | rare | 0 | map_at_3 | null | null | null | null | null |
| E011 | 2 | 33474 | rare | 0 | top1_accuracy | null | null | null | null | null |
| E011 | 2 | 33474 | frequent | 1083 | map_at_3 | 0.718683 | 0.639923 | 0.078760 | 0.601599 | 0.117084 |
| E011 | 2 | 33474 | frequent | 1083 | top1_accuracy | 0.504155 | 0.376113 | 0.128042 | 0.321376 | 0.182779 |
| E011 | 2 | 33474 | well_supported | 1083 | map_at_3 | 0.718683 | 0.639923 | 0.078760 | 0.601599 | 0.117084 |
| E011 | 2 | 33474 | well_supported | 1083 | top1_accuracy | 0.504155 | 0.376113 | 0.128042 | 0.321376 | 0.182779 |
| E011 | 2 | 91695 | all | 2610 | map_at_3 | 0.549234 | 0.533047 | 0.016187 | 0.479357 | 0.069877 |
| E011 | 2 | 91695 | all | 2610 | top1_accuracy | 0.391571 | 0.365916 | 0.025655 | 0.267230 | 0.124341 |
| E011 | 2 | 91695 | unsupported | 665 | map_at_3 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 |
| E011 | 2 | 91695 | unsupported | 665 | top1_accuracy | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 |
| E011 | 2 | 91695 | rare | 0 | map_at_3 | null | null | null | null | null |
| E011 | 2 | 91695 | rare | 0 | top1_accuracy | null | null | null | null | null |
| E011 | 2 | 91695 | frequent | 1945 | map_at_3 | 0.737018 | 0.715296 | 0.021722 | 0.643250 | 0.093768 |
| E011 | 2 | 91695 | frequent | 1945 | top1_accuracy | 0.525450 | 0.491023 | 0.034427 | 0.358596 | 0.166853 |
| E011 | 2 | 91695 | well_supported | 1945 | map_at_3 | 0.737018 | 0.715296 | 0.021722 | 0.643250 | 0.093768 |
| E011 | 2 | 91695 | well_supported | 1945 | top1_accuracy | 0.525450 | 0.491023 | 0.034427 | 0.358596 | 0.166853 |
| E012 | 2 | all | all | 7491 | map_at_3 | 0.536755 | 0.536570 | 0.000185 | 0.533370 | 0.003385 |
| E012 | 2 | all | all | 7491 | top1_accuracy | 0.395408 | 0.395408 | 0.000000 | 0.395408 | 0.000000 |
| E012 | 2 | all | unsupported | 1985 | map_at_3 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 |
| E012 | 2 | all | unsupported | 1985 | top1_accuracy | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 |
| E012 | 2 | all | rare | 0 | map_at_3 | null | null | null | null | null |
| E012 | 2 | all | rare | 0 | top1_accuracy | null | null | null | null | null |
| E012 | 2 | all | frequent | 5506 | map_at_3 | 0.730264 | 0.730012 | 0.000252 | 0.725658 | 0.004606 |
| E012 | 2 | all | frequent | 5506 | top1_accuracy | 0.537959 | 0.537959 | 0.000000 | 0.537959 | 0.000000 |
| E012 | 2 | all | well_supported | 5506 | map_at_3 | 0.730264 | 0.730012 | 0.000252 | 0.725658 | 0.004606 |
| E012 | 2 | all | well_supported | 5506 | top1_accuracy | 0.537959 | 0.537959 | 0.000000 | 0.537959 | 0.000000 |
| E012 | 2 | 31774 | all | 3115 | map_at_3 | 0.596415 | 0.596104 | 0.000311 | 0.589002 | 0.007413 |
| E012 | 2 | 31774 | all | 3115 | top1_accuracy | 0.451043 | 0.451043 | 0.000000 | 0.451043 | 0.000000 |
| E012 | 2 | 31774 | unsupported | 637 | map_at_3 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 |
| E012 | 2 | 31774 | unsupported | 637 | top1_accuracy | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 |
| E012 | 2 | 31774 | rare | 0 | map_at_3 | null | null | null | null | null |
| E012 | 2 | 31774 | rare | 0 | top1_accuracy | null | null | null | null | null |
| E012 | 2 | 31774 | frequent | 2478 | map_at_3 | 0.749731 | 0.749340 | 0.000391 | 0.740412 | 0.009319 |
| E012 | 2 | 31774 | frequent | 2478 | top1_accuracy | 0.566990 | 0.566990 | 0.000000 | 0.566990 | 0.000000 |
| E012 | 2 | 31774 | well_supported | 2478 | map_at_3 | 0.749731 | 0.749340 | 0.000391 | 0.740412 | 0.009319 |
| E012 | 2 | 31774 | well_supported | 2478 | top1_accuracy | 0.566990 | 0.566990 | 0.000000 | 0.566990 | 0.000000 |
| E012 | 2 | 33474 | all | 1766 | map_at_3 | 0.354473 | 0.354714 | -0.000241 | 0.354551 | -0.000077 |
| E012 | 2 | 33474 | all | 1766 | top1_accuracy | 0.182899 | 0.182899 | 0.000000 | 0.182899 | 0.000000 |
| E012 | 2 | 33474 | unsupported | 683 | map_at_3 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 |
| E012 | 2 | 33474 | unsupported | 683 | top1_accuracy | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 |
| E012 | 2 | 33474 | rare | 0 | map_at_3 | null | null | null | null | null |
| E012 | 2 | 33474 | rare | 0 | top1_accuracy | null | null | null | null | null |
| E012 | 2 | 33474 | frequent | 1083 | map_at_3 | 0.578024 | 0.578416 | -0.000392 | 0.578150 | -0.000126 |
| E012 | 2 | 33474 | frequent | 1083 | top1_accuracy | 0.298246 | 0.298246 | 0.000000 | 0.298246 | 0.000000 |
| E012 | 2 | 33474 | well_supported | 1083 | map_at_3 | 0.578024 | 0.578416 | -0.000392 | 0.578150 | -0.000126 |
| E012 | 2 | 33474 | well_supported | 1083 | top1_accuracy | 0.298246 | 0.298246 | 0.000000 | 0.298246 | 0.000000 |
| E012 | 2 | 91695 | all | 2610 | map_at_3 | 0.588889 | 0.588566 | 0.000322 | 0.587968 | 0.000921 |
| E012 | 2 | 91695 | all | 2610 | top1_accuracy | 0.472797 | 0.472797 | 0.000000 | 0.472797 | 0.000000 |
| E012 | 2 | 91695 | unsupported | 665 | map_at_3 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 |
| E012 | 2 | 91695 | unsupported | 665 | top1_accuracy | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 |
| E012 | 2 | 91695 | rare | 0 | map_at_3 | null | null | null | null | null |
| E012 | 2 | 91695 | rare | 0 | top1_accuracy | null | null | null | null | null |
| E012 | 2 | 91695 | frequent | 1945 | map_at_3 | 0.790231 | 0.789799 | 0.000433 | 0.788996 | 0.001236 |
| E012 | 2 | 91695 | frequent | 1945 | top1_accuracy | 0.634447 | 0.634447 | 0.000000 | 0.634447 | 0.000000 |
| E012 | 2 | 91695 | well_supported | 1945 | map_at_3 | 0.790231 | 0.789799 | 0.000433 | 0.788996 | 0.001236 |
| E012 | 2 | 91695 | well_supported | 1945 | top1_accuracy | 0.634447 | 0.634447 | 0.000000 | 0.634447 | 0.000000 |
| frequency | 2 | all | all | 7491 | map_at_3 | 0.538824 | 0.538824 | 0.000000 | 0.538824 | 0.000000 |
| frequency | 2 | all | all | 7491 | top1_accuracy | 0.395408 | 0.395408 | 0.000000 | 0.395408 | 0.000000 |
| frequency | 2 | all | unsupported | 1985 | map_at_3 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 |
| frequency | 2 | all | unsupported | 1985 | top1_accuracy | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 |
| frequency | 2 | all | rare | 0 | map_at_3 | null | null | null | null | null |
| frequency | 2 | all | rare | 0 | top1_accuracy | null | null | null | null | null |
| frequency | 2 | all | frequent | 5506 | map_at_3 | 0.733079 | 0.733079 | 0.000000 | 0.733079 | 0.000000 |
| frequency | 2 | all | frequent | 5506 | top1_accuracy | 0.537959 | 0.537959 | 0.000000 | 0.537959 | 0.000000 |
| frequency | 2 | all | well_supported | 5506 | map_at_3 | 0.733079 | 0.733079 | 0.000000 | 0.733079 | 0.000000 |
| frequency | 2 | all | well_supported | 5506 | top1_accuracy | 0.537959 | 0.537959 | 0.000000 | 0.537959 | 0.000000 |
| frequency | 2 | 31774 | all | 3115 | map_at_3 | 0.593847 | 0.593847 | 0.000000 | 0.593847 | 0.000000 |
| frequency | 2 | 31774 | all | 3115 | top1_accuracy | 0.451043 | 0.451043 | 0.000000 | 0.451043 | 0.000000 |
| frequency | 2 | 31774 | unsupported | 637 | map_at_3 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 |
| frequency | 2 | 31774 | unsupported | 637 | top1_accuracy | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 |
| frequency | 2 | 31774 | rare | 0 | map_at_3 | null | null | null | null | null |
| frequency | 2 | 31774 | rare | 0 | top1_accuracy | null | null | null | null | null |
| frequency | 2 | 31774 | frequent | 2478 | map_at_3 | 0.746503 | 0.746503 | 0.000000 | 0.746503 | 0.000000 |
| frequency | 2 | 31774 | frequent | 2478 | top1_accuracy | 0.566990 | 0.566990 | 0.000000 | 0.566990 | 0.000000 |
| frequency | 2 | 31774 | well_supported | 2478 | map_at_3 | 0.746503 | 0.746503 | 0.000000 | 0.746503 | 0.000000 |
| frequency | 2 | 31774 | well_supported | 2478 | top1_accuracy | 0.566990 | 0.566990 | 0.000000 | 0.566990 | 0.000000 |
| frequency | 2 | 33474 | all | 1766 | map_at_3 | 0.368913 | 0.368913 | 0.000000 | 0.368913 | 0.000000 |
| frequency | 2 | 33474 | all | 1766 | top1_accuracy | 0.182899 | 0.182899 | 0.000000 | 0.182899 | 0.000000 |
| frequency | 2 | 33474 | unsupported | 683 | map_at_3 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 |
| frequency | 2 | 33474 | unsupported | 683 | top1_accuracy | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 |
| frequency | 2 | 33474 | rare | 0 | map_at_3 | null | null | null | null | null |
| frequency | 2 | 33474 | rare | 0 | top1_accuracy | null | null | null | null | null |
| frequency | 2 | 33474 | frequent | 1083 | map_at_3 | 0.601570 | 0.601570 | 0.000000 | 0.601570 | 0.000000 |
| frequency | 2 | 33474 | frequent | 1083 | top1_accuracy | 0.298246 | 0.298246 | 0.000000 | 0.298246 | 0.000000 |
| frequency | 2 | 33474 | well_supported | 1083 | map_at_3 | 0.601570 | 0.601570 | 0.000000 | 0.601570 | 0.000000 |
| frequency | 2 | 33474 | well_supported | 1083 | top1_accuracy | 0.298246 | 0.298246 | 0.000000 | 0.298246 | 0.000000 |
| frequency | 2 | 91695 | all | 2610 | map_at_3 | 0.588123 | 0.588123 | 0.000000 | 0.588123 | 0.000000 |
| frequency | 2 | 91695 | all | 2610 | top1_accuracy | 0.472797 | 0.472797 | 0.000000 | 0.472797 | 0.000000 |
| frequency | 2 | 91695 | unsupported | 665 | map_at_3 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 |
| frequency | 2 | 91695 | unsupported | 665 | top1_accuracy | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 |
| frequency | 2 | 91695 | rare | 0 | map_at_3 | null | null | null | null | null |
| frequency | 2 | 91695 | rare | 0 | top1_accuracy | null | null | null | null | null |
| frequency | 2 | 91695 | frequent | 1945 | map_at_3 | 0.789203 | 0.789203 | 0.000000 | 0.789203 | 0.000000 |
| frequency | 2 | 91695 | frequent | 1945 | top1_accuracy | 0.634447 | 0.634447 | 0.000000 | 0.634447 | 0.000000 |
| frequency | 2 | 91695 | well_supported | 1945 | map_at_3 | 0.789203 | 0.789203 | 0.000000 | 0.789203 | 0.000000 |
| frequency | 2 | 91695 | well_supported | 1945 | top1_accuracy | 0.634447 | 0.634447 | 0.000000 | 0.634447 | 0.000000 |
| E011 | 3 | all | all | 7091 | map_at_3 | 0.527946 | 0.494313 | 0.033633 | 0.462419 | 0.065527 |
| E011 | 3 | all | all | 7091 | top1_accuracy | 0.427443 | 0.377356 | 0.050087 | 0.325917 | 0.101526 |
| E011 | 3 | all | unsupported | 2162 | map_at_3 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 |
| E011 | 3 | all | unsupported | 2162 | top1_accuracy | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 |
| E011 | 3 | all | rare | 0 | map_at_3 | null | null | null | null | null |
| E011 | 3 | all | rare | 0 | top1_accuracy | null | null | null | null | null |
| E011 | 3 | all | frequent | 4929 | map_at_3 | 0.759518 | 0.711133 | 0.048385 | 0.665250 | 0.094269 |
| E011 | 3 | all | frequent | 4929 | top1_accuracy | 0.614932 | 0.542875 | 0.072057 | 0.468874 | 0.146058 |
| E011 | 3 | all | well_supported | 4929 | map_at_3 | 0.759518 | 0.711133 | 0.048385 | 0.665250 | 0.094269 |
| E011 | 3 | all | well_supported | 4929 | top1_accuracy | 0.614932 | 0.542875 | 0.072057 | 0.468874 | 0.146058 |
| E011 | 3 | 32833 | all | 3105 | map_at_3 | 0.476651 | 0.438704 | 0.037946 | 0.460088 | 0.016563 |
| E011 | 3 | 32833 | all | 3105 | top1_accuracy | 0.399678 | 0.345849 | 0.053829 | 0.360712 | 0.038966 |
| E011 | 3 | 32833 | unsupported | 1124 | map_at_3 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 |
| E011 | 3 | 32833 | unsupported | 1124 | top1_accuracy | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 |
| E011 | 3 | 32833 | rare | 0 | map_at_3 | null | null | null | null | null |
| E011 | 3 | 32833 | rare | 0 | top1_accuracy | null | null | null | null | null |
| E011 | 3 | 32833 | frequent | 1981 | map_at_3 | 0.747097 | 0.687621 | 0.059477 | 0.721137 | 0.025960 |
| E011 | 3 | 32833 | frequent | 1981 | top1_accuracy | 0.626451 | 0.542080 | 0.084372 | 0.565376 | 0.061075 |
| E011 | 3 | 32833 | well_supported | 1981 | map_at_3 | 0.747097 | 0.687621 | 0.059477 | 0.721137 | 0.025960 |
| E011 | 3 | 32833 | well_supported | 1981 | top1_accuracy | 0.626451 | 0.542080 | 0.084372 | 0.565376 | 0.061075 |
| E011 | 3 | 33472 | all | 2800 | map_at_3 | 0.592917 | 0.556865 | 0.036051 | 0.478306 | 0.114611 |
| E011 | 3 | 33472 | all | 2800 | top1_accuracy | 0.477143 | 0.421089 | 0.056054 | 0.317229 | 0.159914 |
| E011 | 3 | 33472 | unsupported | 652 | map_at_3 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 |
| E011 | 3 | 33472 | unsupported | 652 | top1_accuracy | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 |
| E011 | 3 | 33472 | rare | 0 | map_at_3 | null | null | null | null | null |
| E011 | 3 | 33472 | rare | 0 | top1_accuracy | null | null | null | null | null |
| E011 | 3 | 33472 | frequent | 2148 | map_at_3 | 0.772890 | 0.725895 | 0.046994 | 0.623490 | 0.149399 |
| E011 | 3 | 33472 | frequent | 2148 | top1_accuracy | 0.621974 | 0.548906 | 0.073068 | 0.413520 | 0.208454 |
| E011 | 3 | 33472 | well_supported | 2148 | map_at_3 | 0.772890 | 0.725895 | 0.046994 | 0.623490 | 0.149399 |
| E011 | 3 | 33472 | well_supported | 2148 | top1_accuracy | 0.621974 | 0.548906 | 0.073068 | 0.413520 | 0.208454 |
| E011 | 3 | 76870 | all | 1186 | map_at_3 | 0.508853 | 0.492223 | 0.016630 | 0.431017 | 0.077836 |
| E011 | 3 | 76870 | all | 1186 | top1_accuracy | 0.382799 | 0.356594 | 0.026206 | 0.255337 | 0.127462 |
| E011 | 3 | 76870 | unsupported | 386 | map_at_3 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 |
| E011 | 3 | 76870 | unsupported | 386 | top1_accuracy | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 |
| E011 | 3 | 76870 | rare | 0 | map_at_3 | null | null | null | null | null |
| E011 | 3 | 76870 | rare | 0 | top1_accuracy | null | null | null | null | null |
| E011 | 3 | 76870 | frequent | 800 | map_at_3 | 0.754375 | 0.729721 | 0.024654 | 0.638983 | 0.115392 |
| E011 | 3 | 76870 | frequent | 800 | top1_accuracy | 0.567500 | 0.528650 | 0.038850 | 0.378537 | 0.188963 |
| E011 | 3 | 76870 | well_supported | 800 | map_at_3 | 0.754375 | 0.729721 | 0.024654 | 0.638983 | 0.115392 |
| E011 | 3 | 76870 | well_supported | 800 | top1_accuracy | 0.567500 | 0.528650 | 0.038850 | 0.378537 | 0.188963 |
| E012 | 3 | all | all | 7091 | map_at_3 | 0.499953 | 0.497984 | 0.001969 | 0.500773 | -0.000820 |
| E012 | 3 | all | all | 7091 | top1_accuracy | 0.370470 | 0.369385 | 0.001084 | 0.368374 | 0.002096 |
| E012 | 3 | all | unsupported | 2162 | map_at_3 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 |
| E012 | 3 | all | unsupported | 2162 | top1_accuracy | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 |
| E012 | 3 | all | rare | 0 | map_at_3 | null | null | null | null | null |
| E012 | 3 | all | rare | 0 | top1_accuracy | null | null | null | null | null |
| E012 | 3 | all | frequent | 4929 | map_at_3 | 0.719247 | 0.716414 | 0.002832 | 0.720426 | -0.001179 |
| E012 | 3 | all | frequent | 4929 | top1_accuracy | 0.532968 | 0.531408 | 0.001560 | 0.529953 | 0.003015 |
| E012 | 3 | all | well_supported | 4929 | map_at_3 | 0.719247 | 0.716414 | 0.002832 | 0.720426 | -0.001179 |
| E012 | 3 | all | well_supported | 4929 | top1_accuracy | 0.532968 | 0.531408 | 0.001560 | 0.529953 | 0.003015 |
| E012 | 3 | 32833 | all | 3105 | map_at_3 | 0.492646 | 0.489389 | 0.003258 | 0.496978 | -0.004332 |
| E012 | 3 | 32833 | all | 3105 | top1_accuracy | 0.397746 | 0.397746 | 0.000000 | 0.397746 | 0.000000 |
| E012 | 3 | 32833 | unsupported | 1124 | map_at_3 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 |
| E012 | 3 | 32833 | unsupported | 1124 | top1_accuracy | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 |
| E012 | 3 | 32833 | rare | 0 | map_at_3 | null | null | null | null | null |
| E012 | 3 | 32833 | rare | 0 | top1_accuracy | null | null | null | null | null |
| E012 | 3 | 32833 | frequent | 1981 | map_at_3 | 0.772169 | 0.767063 | 0.005106 | 0.778958 | -0.006790 |
| E012 | 3 | 32833 | frequent | 1981 | top1_accuracy | 0.623423 | 0.623423 | 0.000000 | 0.623423 | 0.000000 |
| E012 | 3 | 32833 | well_supported | 1981 | map_at_3 | 0.772169 | 0.767063 | 0.005106 | 0.778958 | -0.006790 |
| E012 | 3 | 32833 | well_supported | 1981 | top1_accuracy | 0.623423 | 0.623423 | 0.000000 | 0.623423 | 0.000000 |
| E012 | 3 | 33472 | all | 2800 | map_at_3 | 0.520893 | 0.519471 | 0.001422 | 0.518079 | 0.002814 |
| E012 | 3 | 33472 | all | 2800 | top1_accuracy | 0.366429 | 0.363682 | 0.002746 | 0.361121 | 0.005307 |
| E012 | 3 | 33472 | unsupported | 652 | map_at_3 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 |
| E012 | 3 | 33472 | unsupported | 652 | top1_accuracy | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 |
| E012 | 3 | 33472 | rare | 0 | map_at_3 | null | null | null | null | null |
| E012 | 3 | 33472 | rare | 0 | top1_accuracy | null | null | null | null | null |
| E012 | 3 | 33472 | frequent | 2148 | map_at_3 | 0.679004 | 0.677150 | 0.001854 | 0.675335 | 0.003669 |
| E012 | 3 | 33472 | frequent | 2148 | top1_accuracy | 0.477654 | 0.474074 | 0.003580 | 0.470736 | 0.006918 |
| E012 | 3 | 33472 | well_supported | 2148 | map_at_3 | 0.679004 | 0.677150 | 0.001854 | 0.675335 | 0.003669 |
| E012 | 3 | 33472 | well_supported | 2148 | top1_accuracy | 0.477654 | 0.474074 | 0.003580 | 0.470736 | 0.006918 |
| E012 | 3 | 76870 | all | 1186 | map_at_3 | 0.469646 | 0.469761 | -0.000115 | 0.469851 | -0.000205 |
| E012 | 3 | 76870 | all | 1186 | top1_accuracy | 0.308600 | 0.308600 | 0.000000 | 0.308600 | 0.000000 |
| E012 | 3 | 76870 | unsupported | 386 | map_at_3 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 |
| E012 | 3 | 76870 | unsupported | 386 | top1_accuracy | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 |
| E012 | 3 | 76870 | rare | 0 | map_at_3 | null | null | null | null | null |
| E012 | 3 | 76870 | rare | 0 | top1_accuracy | null | null | null | null | null |
| E012 | 3 | 76870 | frequent | 800 | map_at_3 | 0.696250 | 0.696421 | -0.000171 | 0.696554 | -0.000304 |
| E012 | 3 | 76870 | frequent | 800 | top1_accuracy | 0.457500 | 0.457500 | 0.000000 | 0.457500 | 0.000000 |
| E012 | 3 | 76870 | well_supported | 800 | map_at_3 | 0.696250 | 0.696421 | -0.000171 | 0.696554 | -0.000304 |
| E012 | 3 | 76870 | well_supported | 800 | top1_accuracy | 0.457500 | 0.457500 | 0.000000 | 0.457500 | 0.000000 |
| frequency | 3 | all | all | 7091 | map_at_3 | 0.501222 | 0.501222 | 0.000000 | 0.501222 | 0.000000 |
| frequency | 3 | all | all | 7091 | top1_accuracy | 0.368777 | 0.368777 | 0.000000 | 0.368777 | 0.000000 |
| frequency | 3 | all | unsupported | 2162 | map_at_3 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 |
| frequency | 3 | all | unsupported | 2162 | top1_accuracy | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 |
| frequency | 3 | all | rare | 0 | map_at_3 | null | null | null | null | null |
| frequency | 3 | all | rare | 0 | top1_accuracy | null | null | null | null | null |
| frequency | 3 | all | frequent | 4929 | map_at_3 | 0.721073 | 0.721073 | 0.000000 | 0.721073 | 0.000000 |
| frequency | 3 | all | frequent | 4929 | top1_accuracy | 0.530534 | 0.530534 | 0.000000 | 0.530534 | 0.000000 |
| frequency | 3 | all | well_supported | 4929 | map_at_3 | 0.721073 | 0.721073 | 0.000000 | 0.721073 | 0.000000 |
| frequency | 3 | all | well_supported | 4929 | top1_accuracy | 0.530534 | 0.530534 | 0.000000 | 0.530534 | 0.000000 |
| frequency | 3 | 32833 | all | 3105 | map_at_3 | 0.497370 | 0.497370 | 0.000000 | 0.497370 | 0.000000 |
| frequency | 3 | 32833 | all | 3105 | top1_accuracy | 0.397746 | 0.397746 | 0.000000 | 0.397746 | 0.000000 |
| frequency | 3 | 32833 | unsupported | 1124 | map_at_3 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 |
| frequency | 3 | 32833 | unsupported | 1124 | top1_accuracy | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 |
| frequency | 3 | 32833 | rare | 0 | map_at_3 | null | null | null | null | null |
| frequency | 3 | 32833 | rare | 0 | top1_accuracy | null | null | null | null | null |
| frequency | 3 | 32833 | frequent | 1981 | map_at_3 | 0.779573 | 0.779573 | 0.000000 | 0.779573 | 0.000000 |
| frequency | 3 | 32833 | frequent | 1981 | top1_accuracy | 0.623423 | 0.623423 | 0.000000 | 0.623423 | 0.000000 |
| frequency | 3 | 32833 | well_supported | 1981 | map_at_3 | 0.779573 | 0.779573 | 0.000000 | 0.779573 | 0.000000 |
| frequency | 3 | 32833 | well_supported | 1981 | top1_accuracy | 0.623423 | 0.623423 | 0.000000 | 0.623423 | 0.000000 |
| frequency | 3 | 33472 | all | 2800 | map_at_3 | 0.518750 | 0.518750 | 0.000000 | 0.518750 | 0.000000 |
| frequency | 3 | 33472 | all | 2800 | top1_accuracy | 0.362143 | 0.362143 | 0.000000 | 0.362143 | 0.000000 |
| frequency | 3 | 33472 | unsupported | 652 | map_at_3 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 |
| frequency | 3 | 33472 | unsupported | 652 | top1_accuracy | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 |
| frequency | 3 | 33472 | rare | 0 | map_at_3 | null | null | null | null | null |
| frequency | 3 | 33472 | rare | 0 | top1_accuracy | null | null | null | null | null |
| frequency | 3 | 33472 | frequent | 2148 | map_at_3 | 0.676210 | 0.676210 | 0.000000 | 0.676210 | 0.000000 |
| frequency | 3 | 33472 | frequent | 2148 | top1_accuracy | 0.472067 | 0.472067 | 0.000000 | 0.472067 | 0.000000 |
| frequency | 3 | 33472 | well_supported | 2148 | map_at_3 | 0.676210 | 0.676210 | 0.000000 | 0.676210 | 0.000000 |
| frequency | 3 | 33472 | well_supported | 2148 | top1_accuracy | 0.472067 | 0.472067 | 0.000000 | 0.472067 | 0.000000 |
| frequency | 3 | 76870 | all | 1186 | map_at_3 | 0.469927 | 0.469927 | 0.000000 | 0.469927 | 0.000000 |
| frequency | 3 | 76870 | all | 1186 | top1_accuracy | 0.308600 | 0.308600 | 0.000000 | 0.308600 | 0.000000 |
| frequency | 3 | 76870 | unsupported | 386 | map_at_3 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 |
| frequency | 3 | 76870 | unsupported | 386 | top1_accuracy | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 |
| frequency | 3 | 76870 | rare | 0 | map_at_3 | null | null | null | null | null |
| frequency | 3 | 76870 | rare | 0 | top1_accuracy | null | null | null | null | null |
| frequency | 3 | 76870 | frequent | 800 | map_at_3 | 0.696667 | 0.696667 | 0.000000 | 0.696667 | 0.000000 |
| frequency | 3 | 76870 | frequent | 800 | top1_accuracy | 0.457500 | 0.457500 | 0.000000 | 0.457500 | 0.000000 |
| frequency | 3 | 76870 | well_supported | 800 | map_at_3 | 0.696667 | 0.696667 | 0.000000 | 0.696667 | 0.000000 |
| frequency | 3 | 76870 | well_supported | 800 | top1_accuracy | 0.457500 | 0.457500 | 0.000000 | 0.457500 | 0.000000 |
| E011 | 4 | all | all | 7405 | map_at_3 | 0.532140 | 0.499067 | 0.033073 | 0.517415 | 0.014725 |
| E011 | 4 | all | all | 7405 | top1_accuracy | 0.352870 | 0.309945 | 0.042925 | 0.335622 | 0.017248 |
| E011 | 4 | all | unsupported | 1588 | map_at_3 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 |
| E011 | 4 | all | unsupported | 1588 | top1_accuracy | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 |
| E011 | 4 | all | rare | 0 | map_at_3 | null | null | null | null | null |
| E011 | 4 | all | rare | 0 | top1_accuracy | null | null | null | null | null |
| E011 | 4 | all | frequent | 5817 | map_at_3 | 0.677411 | 0.635309 | 0.042102 | 0.658666 | 0.018745 |
| E011 | 4 | all | frequent | 5817 | top1_accuracy | 0.449201 | 0.394557 | 0.054643 | 0.427244 | 0.021956 |
| E011 | 4 | all | well_supported | 5722 | map_at_3 | 0.688367 | 0.645749 | 0.042618 | 0.669560 | 0.018807 |
| E011 | 4 | all | well_supported | 5722 | top1_accuracy | 0.456659 | 0.401108 | 0.055551 | 0.434338 | 0.022321 |
| E011 | 4 | 31777 | all | 2809 | map_at_3 | 0.710336 | 0.674840 | 0.035496 | 0.637425 | 0.072911 |
| E011 | 4 | 31777 | all | 2809 | top1_accuracy | 0.589178 | 0.533090 | 0.056088 | 0.464276 | 0.124902 |
| E011 | 4 | 31777 | unsupported | 314 | map_at_3 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 |
| E011 | 4 | 31777 | unsupported | 314 | top1_accuracy | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 |
| E011 | 4 | 31777 | rare | 0 | map_at_3 | null | null | null | null | null |
| E011 | 4 | 31777 | rare | 0 | top1_accuracy | null | null | null | null | null |
| E011 | 4 | 31777 | frequent | 2495 | map_at_3 | 0.799733 | 0.759770 | 0.039963 | 0.717646 | 0.082087 |
| E011 | 4 | 31777 | frequent | 2495 | top1_accuracy | 0.663327 | 0.600180 | 0.063146 | 0.522705 | 0.140621 |
| E011 | 4 | 31777 | well_supported | 2419 | map_at_3 | 0.824170 | 0.783385 | 0.040785 | 0.740114 | 0.084055 |
| E011 | 4 | 31777 | well_supported | 2419 | top1_accuracy | 0.684167 | 0.619037 | 0.065130 | 0.539128 | 0.145039 |
| E011 | 4 | 33471 | all | 1542 | map_at_3 | 0.380134 | 0.340052 | 0.040082 | 0.447089 | -0.066955 |
| E011 | 4 | 33471 | all | 1542 | top1_accuracy | 0.140078 | 0.102685 | 0.037393 | 0.277140 | -0.137062 |
| E011 | 4 | 33471 | unsupported | 418 | map_at_3 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 |
| E011 | 4 | 33471 | unsupported | 418 | top1_accuracy | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 |
| E011 | 4 | 33471 | rare | 0 | map_at_3 | null | null | null | null | null |
| E011 | 4 | 33471 | rare | 0 | top1_accuracy | null | null | null | null | null |
| E011 | 4 | 33471 | frequent | 1124 | map_at_3 | 0.521501 | 0.466512 | 0.054988 | 0.613356 | -0.091855 |
| E011 | 4 | 33471 | frequent | 1124 | top1_accuracy | 0.192171 | 0.140872 | 0.051299 | 0.380205 | -0.188034 |
| E011 | 4 | 33471 | well_supported | 1105 | map_at_3 | 0.530468 | 0.474534 | 0.055934 | 0.623860 | -0.093392 |
| E011 | 4 | 33471 | well_supported | 1105 | top1_accuracy | 0.195475 | 0.143294 | 0.052181 | 0.386742 | -0.191267 |
| E011 | 4 | 89443 | all | 3054 | map_at_3 | 0.444990 | 0.417684 | 0.027306 | 0.442541 | 0.002449 |
| E011 | 4 | 89443 | all | 3054 | top1_accuracy | 0.242960 | 0.209348 | 0.033612 | 0.246817 | -0.003857 |
| E011 | 4 | 89443 | unsupported | 856 | map_at_3 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 |
| E011 | 4 | 89443 | unsupported | 856 | top1_accuracy | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 |
| E011 | 4 | 89443 | rare | 0 | map_at_3 | null | null | null | null | null |
| E011 | 4 | 89443 | rare | 0 | top1_accuracy | null | null | null | null | null |
| E011 | 4 | 89443 | frequent | 2198 | map_at_3 | 0.618289 | 0.580349 | 0.037941 | 0.614886 | 0.003403 |
| E011 | 4 | 89443 | frequent | 2198 | top1_accuracy | 0.337580 | 0.290878 | 0.046702 | 0.342939 | -0.005359 |
| E011 | 4 | 89443 | well_supported | 2198 | map_at_3 | 0.618289 | 0.580349 | 0.037941 | 0.614886 | 0.003403 |
| E011 | 4 | 89443 | well_supported | 2198 | top1_accuracy | 0.337580 | 0.290878 | 0.046702 | 0.342939 | -0.005359 |
| E012 | 4 | all | all | 7405 | map_at_3 | 0.554018 | 0.553500 | 0.000518 | 0.554813 | -0.000796 |
| E012 | 4 | all | all | 7405 | top1_accuracy | 0.401080 | 0.401080 | 0.000000 | 0.401080 | 0.000000 |
| E012 | 4 | all | unsupported | 1588 | map_at_3 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 |
| E012 | 4 | all | unsupported | 1588 | top1_accuracy | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 |
| E012 | 4 | all | rare | 0 | map_at_3 | null | null | null | null | null |
| E012 | 4 | all | rare | 0 | top1_accuracy | null | null | null | null | null |
| E012 | 4 | all | frequent | 5817 | map_at_3 | 0.705260 | 0.704601 | 0.000659 | 0.706274 | -0.001013 |
| E012 | 4 | all | frequent | 5817 | top1_accuracy | 0.510572 | 0.510572 | 0.000000 | 0.510572 | 0.000000 |
| E012 | 4 | all | well_supported | 5722 | map_at_3 | 0.713067 | 0.712995 | 0.000071 | 0.714883 | -0.001816 |
| E012 | 4 | all | well_supported | 5722 | top1_accuracy | 0.519049 | 0.519049 | 0.000000 | 0.519049 | 0.000000 |
| E012 | 4 | 31777 | all | 2809 | map_at_3 | 0.700961 | 0.696632 | 0.004329 | 0.696450 | 0.004512 |
| E012 | 4 | 31777 | all | 2809 | top1_accuracy | 0.579566 | 0.579566 | 0.000000 | 0.579566 | 0.000000 |
| E012 | 4 | 31777 | unsupported | 314 | map_at_3 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 |
| E012 | 4 | 31777 | unsupported | 314 | top1_accuracy | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 |
| E012 | 4 | 31777 | rare | 0 | map_at_3 | null | null | null | null | null |
| E012 | 4 | 31777 | rare | 0 | top1_accuracy | null | null | null | null | null |
| E012 | 4 | 31777 | frequent | 2495 | map_at_3 | 0.789178 | 0.784305 | 0.004874 | 0.784099 | 0.005079 |
| E012 | 4 | 31777 | frequent | 2495 | top1_accuracy | 0.652505 | 0.652505 | 0.000000 | 0.652505 | 0.000000 |
| E012 | 4 | 31777 | well_supported | 2419 | map_at_3 | 0.804740 | 0.801203 | 0.003537 | 0.801499 | 0.003241 |
| E012 | 4 | 31777 | well_supported | 2419 | top1_accuracy | 0.673005 | 0.673005 | 0.000000 | 0.673005 | 0.000000 |
| E012 | 4 | 33471 | all | 1542 | map_at_3 | 0.560852 | 0.560549 | 0.000303 | 0.560166 | 0.000685 |
| E012 | 4 | 33471 | all | 1542 | top1_accuracy | 0.454604 | 0.454604 | 0.000000 | 0.454604 | 0.000000 |
| E012 | 4 | 33471 | unsupported | 418 | map_at_3 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 |
| E012 | 4 | 33471 | unsupported | 418 | top1_accuracy | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 |
| E012 | 4 | 33471 | rare | 0 | map_at_3 | null | null | null | null | null |
| E012 | 4 | 33471 | rare | 0 | top1_accuracy | null | null | null | null | null |
| E012 | 4 | 33471 | frequent | 1124 | map_at_3 | 0.769425 | 0.769009 | 0.000415 | 0.768485 | 0.000940 |
| E012 | 4 | 33471 | frequent | 1124 | top1_accuracy | 0.623665 | 0.623665 | 0.000000 | 0.623665 | 0.000000 |
| E012 | 4 | 33471 | well_supported | 1105 | map_at_3 | 0.782655 | 0.782072 | 0.000582 | 0.781397 | 0.001258 |
| E012 | 4 | 33471 | well_supported | 1105 | top1_accuracy | 0.634389 | 0.634389 | 0.000000 | 0.634389 | 0.000000 |
| E012 | 4 | 89443 | all | 3054 | map_at_3 | 0.415411 | 0.418290 | -0.002879 | 0.421837 | -0.006425 |
| E012 | 4 | 89443 | all | 3054 | top1_accuracy | 0.209889 | 0.209889 | 0.000000 | 0.209889 | 0.000000 |
| E012 | 4 | 89443 | unsupported | 856 | map_at_3 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 |
| E012 | 4 | 89443 | unsupported | 856 | top1_accuracy | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 |
| E012 | 4 | 89443 | rare | 0 | map_at_3 | null | null | null | null | null |
| E012 | 4 | 89443 | rare | 0 | top1_accuracy | null | null | null | null | null |
| E012 | 4 | 89443 | frequent | 2198 | map_at_3 | 0.577191 | 0.581191 | -0.004000 | 0.586119 | -0.008928 |
| E012 | 4 | 89443 | frequent | 2198 | top1_accuracy | 0.291629 | 0.291629 | 0.000000 | 0.291629 | 0.000000 |
| E012 | 4 | 89443 | well_supported | 2198 | map_at_3 | 0.577191 | 0.581191 | -0.004000 | 0.586119 | -0.008928 |
| E012 | 4 | 89443 | well_supported | 2198 | top1_accuracy | 0.291629 | 0.291629 | 0.000000 | 0.291629 | 0.000000 |
| frequency | 4 | all | all | 7405 | map_at_3 | 0.562413 | 0.562413 | 0.000000 | 0.562413 | 0.000000 |
| frequency | 4 | all | all | 7405 | top1_accuracy | 0.401080 | 0.401080 | 0.000000 | 0.401080 | 0.000000 |
| frequency | 4 | all | unsupported | 1588 | map_at_3 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 |
| frequency | 4 | all | unsupported | 1588 | top1_accuracy | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 |
| frequency | 4 | all | rare | 0 | map_at_3 | null | null | null | null | null |
| frequency | 4 | all | rare | 0 | top1_accuracy | null | null | null | null | null |
| frequency | 4 | all | frequent | 5817 | map_at_3 | 0.715948 | 0.715948 | 0.000000 | 0.715948 | 0.000000 |
| frequency | 4 | all | frequent | 5817 | top1_accuracy | 0.510572 | 0.510572 | 0.000000 | 0.510572 | 0.000000 |
| frequency | 4 | all | well_supported | 5722 | map_at_3 | 0.727834 | 0.727834 | 0.000000 | 0.727834 | 0.000000 |
| frequency | 4 | all | well_supported | 5722 | top1_accuracy | 0.519049 | 0.519049 | 0.000000 | 0.519049 | 0.000000 |
| frequency | 4 | 31777 | all | 2809 | map_at_3 | 0.704047 | 0.704047 | 0.000000 | 0.704047 | 0.000000 |
| frequency | 4 | 31777 | all | 2809 | top1_accuracy | 0.579566 | 0.579566 | 0.000000 | 0.579566 | 0.000000 |
| frequency | 4 | 31777 | unsupported | 314 | map_at_3 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 |
| frequency | 4 | 31777 | unsupported | 314 | top1_accuracy | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 |
| frequency | 4 | 31777 | rare | 0 | map_at_3 | null | null | null | null | null |
| frequency | 4 | 31777 | rare | 0 | top1_accuracy | null | null | null | null | null |
| frequency | 4 | 31777 | frequent | 2495 | map_at_3 | 0.792652 | 0.792652 | 0.000000 | 0.792652 | 0.000000 |
| frequency | 4 | 31777 | frequent | 2495 | top1_accuracy | 0.652505 | 0.652505 | 0.000000 | 0.652505 | 0.000000 |
| frequency | 4 | 31777 | well_supported | 2419 | map_at_3 | 0.817555 | 0.817555 | 0.000000 | 0.817555 | 0.000000 |
| frequency | 4 | 31777 | well_supported | 2419 | top1_accuracy | 0.673005 | 0.673005 | 0.000000 | 0.673005 | 0.000000 |
| frequency | 4 | 33471 | all | 1542 | map_at_3 | 0.562365 | 0.562365 | 0.000000 | 0.562365 | 0.000000 |
| frequency | 4 | 33471 | all | 1542 | top1_accuracy | 0.454604 | 0.454604 | 0.000000 | 0.454604 | 0.000000 |
| frequency | 4 | 33471 | unsupported | 418 | map_at_3 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 |
| frequency | 4 | 33471 | unsupported | 418 | top1_accuracy | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 |
| frequency | 4 | 33471 | rare | 0 | map_at_3 | null | null | null | null | null |
| frequency | 4 | 33471 | rare | 0 | top1_accuracy | null | null | null | null | null |
| frequency | 4 | 33471 | frequent | 1124 | map_at_3 | 0.771501 | 0.771501 | 0.000000 | 0.771501 | 0.000000 |
| frequency | 4 | 33471 | frequent | 1124 | top1_accuracy | 0.623665 | 0.623665 | 0.000000 | 0.623665 | 0.000000 |
| frequency | 4 | 33471 | well_supported | 1105 | map_at_3 | 0.784766 | 0.784766 | 0.000000 | 0.784766 | 0.000000 |
| frequency | 4 | 33471 | well_supported | 1105 | top1_accuracy | 0.634389 | 0.634389 | 0.000000 | 0.634389 | 0.000000 |
| frequency | 4 | 89443 | all | 3054 | map_at_3 | 0.432165 | 0.432165 | 0.000000 | 0.432165 | 0.000000 |
| frequency | 4 | 89443 | all | 3054 | top1_accuracy | 0.209889 | 0.209889 | 0.000000 | 0.209889 | 0.000000 |
| frequency | 4 | 89443 | unsupported | 856 | map_at_3 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 |
| frequency | 4 | 89443 | unsupported | 856 | top1_accuracy | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 |
| frequency | 4 | 89443 | rare | 0 | map_at_3 | null | null | null | null | null |
| frequency | 4 | 89443 | rare | 0 | top1_accuracy | null | null | null | null | null |
| frequency | 4 | 89443 | frequent | 2198 | map_at_3 | 0.600470 | 0.600470 | 0.000000 | 0.600470 | 0.000000 |
| frequency | 4 | 89443 | frequent | 2198 | top1_accuracy | 0.291629 | 0.291629 | 0.000000 | 0.291629 | 0.000000 |
| frequency | 4 | 89443 | well_supported | 2198 | map_at_3 | 0.600470 | 0.600470 | 0.000000 | 0.600470 | 0.000000 |
| frequency | 4 | 89443 | well_supported | 2198 | top1_accuracy | 0.291629 | 0.291629 | 0.000000 | 0.291629 | 0.000000 |

## Original predictions versus frequency

| Model | Fold | Question | Stratum | n | Top1 agreement | Ordered top3 agreement | RR wins | RR ties | RR losses | RR gain | RR loss | RR net | Accuracy wins | Accuracy ties | Accuracy losses |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| E011 | 0 | all | all | 7686 | 0.785714 | 0.679417 | 463 | 6475 | 748 | 0.025674 | 0.064099 | -0.038425 | 346 | 6637 | 703 |
| E011 | 0 | all | unsupported | 407 | 0.511057 | 0.272727 | 0 | 407 | 0 | 0.000000 | 0.000000 | 0.000000 | 0 | 407 | 0 |
| E011 | 0 | all | rare | 0 | null | null | 0 | 0 | 0 | null | null | null | 0 | 0 | 0 |
| E011 | 0 | all | frequent | 7279 | 0.801072 | 0.702157 | 463 | 6068 | 748 | 0.027110 | 0.067683 | -0.040573 | 346 | 6230 | 703 |
| E011 | 0 | all | well_supported | 7025 | 0.798292 | 0.695943 | 463 | 5814 | 748 | 0.028090 | 0.070130 | -0.042040 | 346 | 5976 | 703 |
| E011 | 0 | 31772 | all | 4857 | 0.896438 | 0.887585 | 195 | 4598 | 64 | 0.019319 | 0.006417 | 0.012902 | 184 | 4612 | 61 |
| E011 | 0 | 31772 | unsupported | 16 | 0.937500 | 0.937500 | 0 | 16 | 0 | 0.000000 | 0.000000 | 0.000000 | 0 | 16 | 0 |
| E011 | 0 | 31772 | rare | 0 | null | null | 0 | 0 | 0 | null | null | null | 0 | 0 | 0 |
| E011 | 0 | 31772 | frequent | 4841 | 0.896302 | 0.887420 | 195 | 4582 | 64 | 0.019383 | 0.006438 | 0.012945 | 184 | 4596 | 61 |
| E011 | 0 | 31772 | well_supported | 4587 | 0.897319 | 0.888162 | 195 | 4328 | 64 | 0.020456 | 0.006795 | 0.013662 | 184 | 4342 | 61 |
| E011 | 0 | 32829 | all | 2156 | 0.741187 | 0.395176 | 183 | 1713 | 260 | 0.035869 | 0.066713 | -0.030844 | 126 | 1804 | 226 |
| E011 | 0 | 32829 | unsupported | 272 | 0.525735 | 0.209559 | 0 | 272 | 0 | 0.000000 | 0.000000 | 0.000000 | 0 | 272 | 0 |
| E011 | 0 | 32829 | rare | 0 | null | null | 0 | 0 | 0 | null | null | null | 0 | 0 | 0 |
| E011 | 0 | 32829 | frequent | 1884 | 0.772293 | 0.421975 | 183 | 1441 | 260 | 0.041047 | 0.076345 | -0.035297 | 126 | 1532 | 226 |
| E011 | 0 | 32829 | well_supported | 1884 | 0.772293 | 0.421975 | 183 | 1441 | 260 | 0.041047 | 0.076345 | -0.035297 | 126 | 1532 | 226 |
| E011 | 0 | 104665 | all | 673 | 0.129272 | 0.087667 | 85 | 164 | 424 | 0.038881 | 0.472016 | -0.433135 | 36 | 221 | 416 |
| E011 | 0 | 104665 | unsupported | 119 | 0.420168 | 0.327731 | 0 | 119 | 0 | 0.000000 | 0.000000 | 0.000000 | 0 | 119 | 0 |
| E011 | 0 | 104665 | rare | 0 | null | null | 0 | 0 | 0 | null | null | null | 0 | 0 | 0 |
| E011 | 0 | 104665 | frequent | 554 | 0.066787 | 0.036101 | 85 | 45 | 424 | 0.047232 | 0.573406 | -0.526173 | 36 | 102 | 416 |
| E011 | 0 | 104665 | well_supported | 554 | 0.066787 | 0.036101 | 85 | 45 | 424 | 0.047232 | 0.573406 | -0.526173 | 36 | 102 | 416 |
| E012 | 0 | all | all | 7686 | 0.999740 | 0.989591 | 26 | 7657 | 3 | 0.000607 | 0.000065 | 0.000542 | 1 | 7685 | 0 |
| E012 | 0 | all | unsupported | 407 | 1.000000 | 0.958231 | 0 | 407 | 0 | 0.000000 | 0.000000 | 0.000000 | 0 | 407 | 0 |
| E012 | 0 | all | rare | 0 | null | null | 0 | 0 | 0 | null | null | null | 0 | 0 | 0 |
| E012 | 0 | all | frequent | 7279 | 0.999725 | 0.991345 | 26 | 7250 | 3 | 0.000641 | 0.000069 | 0.000572 | 1 | 7278 | 0 |
| E012 | 0 | all | well_supported | 7025 | 0.999715 | 0.991032 | 26 | 6996 | 3 | 0.000664 | 0.000071 | 0.000593 | 1 | 7024 | 0 |
| E012 | 0 | 31772 | all | 4857 | 1.000000 | 0.996088 | 6 | 4851 | 0 | 0.000206 | 0.000000 | 0.000206 | 0 | 4857 | 0 |
| E012 | 0 | 31772 | unsupported | 16 | 1.000000 | 0.937500 | 0 | 16 | 0 | 0.000000 | 0.000000 | 0.000000 | 0 | 16 | 0 |
| E012 | 0 | 31772 | rare | 0 | null | null | 0 | 0 | 0 | null | null | null | 0 | 0 | 0 |
| E012 | 0 | 31772 | frequent | 4841 | 1.000000 | 0.996282 | 6 | 4835 | 0 | 0.000207 | 0.000000 | 0.000207 | 0 | 4841 | 0 |
| E012 | 0 | 31772 | well_supported | 4587 | 1.000000 | 0.996076 | 6 | 4581 | 0 | 0.000218 | 0.000000 | 0.000218 | 0 | 4587 | 0 |
| E012 | 0 | 32829 | all | 2156 | 0.999072 | 0.971707 | 20 | 2133 | 3 | 0.001701 | 0.000232 | 0.001469 | 1 | 2155 | 0 |
| E012 | 0 | 32829 | unsupported | 272 | 1.000000 | 0.941176 | 0 | 272 | 0 | 0.000000 | 0.000000 | 0.000000 | 0 | 272 | 0 |
| E012 | 0 | 32829 | rare | 0 | null | null | 0 | 0 | 0 | null | null | null | 0 | 0 | 0 |
| E012 | 0 | 32829 | frequent | 1884 | 0.998938 | 0.976115 | 20 | 1861 | 3 | 0.001946 | 0.000265 | 0.001681 | 1 | 1883 | 0 |
| E012 | 0 | 32829 | well_supported | 1884 | 0.998938 | 0.976115 | 20 | 1861 | 3 | 0.001946 | 0.000265 | 0.001681 | 1 | 1883 | 0 |
| E012 | 0 | 104665 | all | 673 | 1.000000 | 1.000000 | 0 | 673 | 0 | 0.000000 | 0.000000 | 0.000000 | 0 | 673 | 0 |
| E012 | 0 | 104665 | unsupported | 119 | 1.000000 | 1.000000 | 0 | 119 | 0 | 0.000000 | 0.000000 | 0.000000 | 0 | 119 | 0 |
| E012 | 0 | 104665 | rare | 0 | null | null | 0 | 0 | 0 | null | null | null | 0 | 0 | 0 |
| E012 | 0 | 104665 | frequent | 554 | 1.000000 | 1.000000 | 0 | 554 | 0 | 0.000000 | 0.000000 | 0.000000 | 0 | 554 | 0 |
| E012 | 0 | 104665 | well_supported | 554 | 1.000000 | 1.000000 | 0 | 554 | 0 | 0.000000 | 0.000000 | 0.000000 | 0 | 554 | 0 |
| frequency | 0 | all | all | 7686 | 1.000000 | 1.000000 | 0 | 7686 | 0 | 0.000000 | 0.000000 | 0.000000 | 0 | 7686 | 0 |
| frequency | 0 | all | unsupported | 407 | 1.000000 | 1.000000 | 0 | 407 | 0 | 0.000000 | 0.000000 | 0.000000 | 0 | 407 | 0 |
| frequency | 0 | all | rare | 0 | null | null | 0 | 0 | 0 | null | null | null | 0 | 0 | 0 |
| frequency | 0 | all | frequent | 7279 | 1.000000 | 1.000000 | 0 | 7279 | 0 | 0.000000 | 0.000000 | 0.000000 | 0 | 7279 | 0 |
| frequency | 0 | all | well_supported | 7025 | 1.000000 | 1.000000 | 0 | 7025 | 0 | 0.000000 | 0.000000 | 0.000000 | 0 | 7025 | 0 |
| frequency | 0 | 31772 | all | 4857 | 1.000000 | 1.000000 | 0 | 4857 | 0 | 0.000000 | 0.000000 | 0.000000 | 0 | 4857 | 0 |
| frequency | 0 | 31772 | unsupported | 16 | 1.000000 | 1.000000 | 0 | 16 | 0 | 0.000000 | 0.000000 | 0.000000 | 0 | 16 | 0 |
| frequency | 0 | 31772 | rare | 0 | null | null | 0 | 0 | 0 | null | null | null | 0 | 0 | 0 |
| frequency | 0 | 31772 | frequent | 4841 | 1.000000 | 1.000000 | 0 | 4841 | 0 | 0.000000 | 0.000000 | 0.000000 | 0 | 4841 | 0 |
| frequency | 0 | 31772 | well_supported | 4587 | 1.000000 | 1.000000 | 0 | 4587 | 0 | 0.000000 | 0.000000 | 0.000000 | 0 | 4587 | 0 |
| frequency | 0 | 32829 | all | 2156 | 1.000000 | 1.000000 | 0 | 2156 | 0 | 0.000000 | 0.000000 | 0.000000 | 0 | 2156 | 0 |
| frequency | 0 | 32829 | unsupported | 272 | 1.000000 | 1.000000 | 0 | 272 | 0 | 0.000000 | 0.000000 | 0.000000 | 0 | 272 | 0 |
| frequency | 0 | 32829 | rare | 0 | null | null | 0 | 0 | 0 | null | null | null | 0 | 0 | 0 |
| frequency | 0 | 32829 | frequent | 1884 | 1.000000 | 1.000000 | 0 | 1884 | 0 | 0.000000 | 0.000000 | 0.000000 | 0 | 1884 | 0 |
| frequency | 0 | 32829 | well_supported | 1884 | 1.000000 | 1.000000 | 0 | 1884 | 0 | 0.000000 | 0.000000 | 0.000000 | 0 | 1884 | 0 |
| frequency | 0 | 104665 | all | 673 | 1.000000 | 1.000000 | 0 | 673 | 0 | 0.000000 | 0.000000 | 0.000000 | 0 | 673 | 0 |
| frequency | 0 | 104665 | unsupported | 119 | 1.000000 | 1.000000 | 0 | 119 | 0 | 0.000000 | 0.000000 | 0.000000 | 0 | 119 | 0 |
| frequency | 0 | 104665 | rare | 0 | null | null | 0 | 0 | 0 | null | null | null | 0 | 0 | 0 |
| frequency | 0 | 104665 | frequent | 554 | 1.000000 | 1.000000 | 0 | 554 | 0 | 0.000000 | 0.000000 | 0.000000 | 0 | 554 | 0 |
| frequency | 0 | 104665 | well_supported | 554 | 1.000000 | 1.000000 | 0 | 554 | 0 | 0.000000 | 0.000000 | 0.000000 | 0 | 554 | 0 |
| E011 | 1 | all | all | 7023 | 0.164032 | 0.139969 | 1682 | 3257 | 2084 | 0.082087 | 0.196331 | -0.114244 | 879 | 4195 | 1949 |
| E011 | 1 | all | unsupported | 1613 | 0.115313 | 0.099194 | 0 | 1613 | 0 | 0.000000 | 0.000000 | 0.000000 | 0 | 1613 | 0 |
| E011 | 1 | all | rare | 0 | null | null | 0 | 0 | 0 | null | null | null | 0 | 0 | 0 |
| E011 | 1 | all | frequent | 5410 | 0.178558 | 0.152126 | 1682 | 1644 | 2084 | 0.106562 | 0.254868 | -0.148306 | 879 | 2582 | 1949 |
| E011 | 1 | all | well_supported | 5005 | 0.192607 | 0.164036 | 1682 | 1239 | 2084 | 0.115185 | 0.275491 | -0.160306 | 879 | 2177 | 1949 |
| E011 | 1 | 31778 | all | 3640 | 0.040385 | 0.021978 | 833 | 1678 | 1129 | 0.089652 | 0.215888 | -0.126236 | 562 | 2060 | 1018 |
| E011 | 1 | 31778 | unsupported | 1017 | 0.010816 | 0.000983 | 0 | 1017 | 0 | 0.000000 | 0.000000 | 0.000000 | 0 | 1017 | 0 |
| E011 | 1 | 31778 | rare | 0 | null | null | 0 | 0 | 0 | null | null | null | 0 | 0 | 0 |
| E011 | 1 | 31778 | frequent | 2623 | 0.051849 | 0.030118 | 833 | 661 | 1129 | 0.124412 | 0.299593 | -0.175181 | 562 | 1043 | 1018 |
| E011 | 1 | 31778 | well_supported | 2218 | 0.060415 | 0.034716 | 833 | 256 | 1129 | 0.147130 | 0.354298 | -0.207169 | 562 | 638 | 1018 |
| E011 | 1 | 32835 | all | 2332 | 0.060463 | 0.048456 | 760 | 682 | 890 | 0.090051 | 0.242996 | -0.152945 | 241 | 1206 | 885 |
| E011 | 1 | 32835 | unsupported | 399 | 0.027569 | 0.022556 | 0 | 399 | 0 | 0.000000 | 0.000000 | 0.000000 | 0 | 399 | 0 |
| E011 | 1 | 32835 | rare | 0 | null | null | 0 | 0 | 0 | null | null | null | 0 | 0 | 0 |
| E011 | 1 | 32835 | frequent | 1933 | 0.067253 | 0.053802 | 760 | 283 | 890 | 0.108639 | 0.293154 | -0.184515 | 241 | 807 | 885 |
| E011 | 1 | 32835 | well_supported | 1933 | 0.067253 | 0.053802 | 760 | 283 | 890 | 0.108639 | 0.293154 | -0.184515 | 241 | 807 | 885 |
| E011 | 1 | 109465 | all | 1051 | 0.822074 | 0.751665 | 89 | 897 | 65 | 0.038218 | 0.025056 | 0.013162 | 76 | 929 | 46 |
| E011 | 1 | 109465 | unsupported | 197 | 0.832487 | 0.761421 | 0 | 197 | 0 | 0.000000 | 0.000000 | 0.000000 | 0 | 197 | 0 |
| E011 | 1 | 109465 | rare | 0 | null | null | 0 | 0 | 0 | null | null | null | 0 | 0 | 0 |
| E011 | 1 | 109465 | frequent | 854 | 0.819672 | 0.749415 | 89 | 700 | 65 | 0.047034 | 0.030835 | 0.016198 | 76 | 732 | 46 |
| E011 | 1 | 109465 | well_supported | 854 | 0.819672 | 0.749415 | 89 | 700 | 65 | 0.047034 | 0.030835 | 0.016198 | 76 | 732 | 46 |
| E012 | 1 | all | all | 7023 | 0.997722 | 0.799231 | 232 | 6612 | 179 | 0.005696 | 0.004438 | 0.001258 | 4 | 7015 | 4 |
| E012 | 1 | all | unsupported | 1613 | 0.998140 | 0.864228 | 0 | 1613 | 0 | 0.000000 | 0.000000 | 0.000000 | 0 | 1613 | 0 |
| E012 | 1 | all | rare | 0 | null | null | 0 | 0 | 0 | null | null | null | 0 | 0 | 0 |
| E012 | 1 | all | frequent | 5410 | 0.997597 | 0.779852 | 232 | 4999 | 179 | 0.007394 | 0.005761 | 0.001633 | 4 | 5402 | 4 |
| E012 | 1 | all | well_supported | 5005 | 0.997403 | 0.795205 | 232 | 4594 | 179 | 0.007992 | 0.006227 | 0.001765 | 4 | 4997 | 4 |
| E012 | 1 | 31778 | all | 3640 | 1.000000 | 0.618132 | 226 | 3239 | 175 | 0.010348 | 0.008013 | 0.002335 | 0 | 3640 | 0 |
| E012 | 1 | 31778 | unsupported | 1017 | 1.000000 | 0.787611 | 0 | 1017 | 0 | 0.000000 | 0.000000 | 0.000000 | 0 | 1017 | 0 |
| E012 | 1 | 31778 | rare | 0 | null | null | 0 | 0 | 0 | null | null | null | 0 | 0 | 0 |
| E012 | 1 | 31778 | frequent | 2623 | 1.000000 | 0.552421 | 226 | 2222 | 175 | 0.014360 | 0.011120 | 0.003241 | 0 | 2623 | 0 |
| E012 | 1 | 31778 | well_supported | 2218 | 1.000000 | 0.545537 | 226 | 1817 | 175 | 0.016982 | 0.013150 | 0.003832 | 0 | 2218 | 0 |
| E012 | 1 | 32835 | all | 2332 | 0.999571 | 0.997856 | 2 | 2330 | 0 | 0.000143 | 0.000000 | 0.000143 | 0 | 2332 | 0 |
| E012 | 1 | 32835 | unsupported | 399 | 1.000000 | 1.000000 | 0 | 399 | 0 | 0.000000 | 0.000000 | 0.000000 | 0 | 399 | 0 |
| E012 | 1 | 32835 | rare | 0 | null | null | 0 | 0 | 0 | null | null | null | 0 | 0 | 0 |
| E012 | 1 | 32835 | frequent | 1933 | 0.999483 | 0.997413 | 2 | 1931 | 0 | 0.000172 | 0.000000 | 0.000172 | 0 | 1933 | 0 |
| E012 | 1 | 32835 | well_supported | 1933 | 0.999483 | 0.997413 | 2 | 1931 | 0 | 0.000172 | 0.000000 | 0.000172 | 0 | 1933 | 0 |
| E012 | 1 | 109465 | all | 1051 | 0.985728 | 0.985728 | 4 | 1043 | 4 | 0.001903 | 0.001903 | 0.000000 | 4 | 1043 | 4 |
| E012 | 1 | 109465 | unsupported | 197 | 0.984772 | 0.984772 | 0 | 197 | 0 | 0.000000 | 0.000000 | 0.000000 | 0 | 197 | 0 |
| E012 | 1 | 109465 | rare | 0 | null | null | 0 | 0 | 0 | null | null | null | 0 | 0 | 0 |
| E012 | 1 | 109465 | frequent | 854 | 0.985948 | 0.985948 | 4 | 846 | 4 | 0.002342 | 0.002342 | 0.000000 | 4 | 846 | 4 |
| E012 | 1 | 109465 | well_supported | 854 | 0.985948 | 0.985948 | 4 | 846 | 4 | 0.002342 | 0.002342 | 0.000000 | 4 | 846 | 4 |
| frequency | 1 | all | all | 7023 | 1.000000 | 1.000000 | 0 | 7023 | 0 | 0.000000 | 0.000000 | 0.000000 | 0 | 7023 | 0 |
| frequency | 1 | all | unsupported | 1613 | 1.000000 | 1.000000 | 0 | 1613 | 0 | 0.000000 | 0.000000 | 0.000000 | 0 | 1613 | 0 |
| frequency | 1 | all | rare | 0 | null | null | 0 | 0 | 0 | null | null | null | 0 | 0 | 0 |
| frequency | 1 | all | frequent | 5410 | 1.000000 | 1.000000 | 0 | 5410 | 0 | 0.000000 | 0.000000 | 0.000000 | 0 | 5410 | 0 |
| frequency | 1 | all | well_supported | 5005 | 1.000000 | 1.000000 | 0 | 5005 | 0 | 0.000000 | 0.000000 | 0.000000 | 0 | 5005 | 0 |
| frequency | 1 | 31778 | all | 3640 | 1.000000 | 1.000000 | 0 | 3640 | 0 | 0.000000 | 0.000000 | 0.000000 | 0 | 3640 | 0 |
| frequency | 1 | 31778 | unsupported | 1017 | 1.000000 | 1.000000 | 0 | 1017 | 0 | 0.000000 | 0.000000 | 0.000000 | 0 | 1017 | 0 |
| frequency | 1 | 31778 | rare | 0 | null | null | 0 | 0 | 0 | null | null | null | 0 | 0 | 0 |
| frequency | 1 | 31778 | frequent | 2623 | 1.000000 | 1.000000 | 0 | 2623 | 0 | 0.000000 | 0.000000 | 0.000000 | 0 | 2623 | 0 |
| frequency | 1 | 31778 | well_supported | 2218 | 1.000000 | 1.000000 | 0 | 2218 | 0 | 0.000000 | 0.000000 | 0.000000 | 0 | 2218 | 0 |
| frequency | 1 | 32835 | all | 2332 | 1.000000 | 1.000000 | 0 | 2332 | 0 | 0.000000 | 0.000000 | 0.000000 | 0 | 2332 | 0 |
| frequency | 1 | 32835 | unsupported | 399 | 1.000000 | 1.000000 | 0 | 399 | 0 | 0.000000 | 0.000000 | 0.000000 | 0 | 399 | 0 |
| frequency | 1 | 32835 | rare | 0 | null | null | 0 | 0 | 0 | null | null | null | 0 | 0 | 0 |
| frequency | 1 | 32835 | frequent | 1933 | 1.000000 | 1.000000 | 0 | 1933 | 0 | 0.000000 | 0.000000 | 0.000000 | 0 | 1933 | 0 |
| frequency | 1 | 32835 | well_supported | 1933 | 1.000000 | 1.000000 | 0 | 1933 | 0 | 0.000000 | 0.000000 | 0.000000 | 0 | 1933 | 0 |
| frequency | 1 | 109465 | all | 1051 | 1.000000 | 1.000000 | 0 | 1051 | 0 | 0.000000 | 0.000000 | 0.000000 | 0 | 1051 | 0 |
| frequency | 1 | 109465 | unsupported | 197 | 1.000000 | 1.000000 | 0 | 197 | 0 | 0.000000 | 0.000000 | 0.000000 | 0 | 197 | 0 |
| frequency | 1 | 109465 | rare | 0 | null | null | 0 | 0 | 0 | null | null | null | 0 | 0 | 0 |
| frequency | 1 | 109465 | frequent | 854 | 1.000000 | 1.000000 | 0 | 854 | 0 | 0.000000 | 0.000000 | 0.000000 | 0 | 854 | 0 |
| frequency | 1 | 109465 | well_supported | 854 | 1.000000 | 1.000000 | 0 | 854 | 0 | 0.000000 | 0.000000 | 0.000000 | 0 | 854 | 0 |
| E011 | 2 | all | all | 7491 | 0.581631 | 0.225738 | 1410 | 5087 | 994 | 0.072887 | 0.053308 | 0.019579 | 845 | 5959 | 687 |
| E011 | 2 | all | unsupported | 1985 | 0.441310 | 0.220151 | 0 | 1985 | 0 | 0.000000 | 0.000000 | 0.000000 | 0 | 1985 | 0 |
| E011 | 2 | all | rare | 0 | null | null | 0 | 0 | 0 | null | null | null | 0 | 0 | 0 |
| E011 | 2 | all | frequent | 5506 | 0.632219 | 0.227752 | 1410 | 3102 | 994 | 0.099165 | 0.072527 | 0.026638 | 845 | 3974 | 687 |
| E011 | 2 | all | well_supported | 5506 | 0.632219 | 0.227752 | 1410 | 3102 | 994 | 0.099165 | 0.072527 | 0.026638 | 845 | 3974 | 687 |
| E011 | 2 | 31774 | all | 3115 | 0.764045 | 0.121027 | 640 | 2180 | 295 | 0.066132 | 0.027180 | 0.038951 | 250 | 2762 | 103 |
| E011 | 2 | 31774 | unsupported | 637 | 0.616954 | 0.332810 | 0 | 637 | 0 | 0.000000 | 0.000000 | 0.000000 | 0 | 637 | 0 |
| E011 | 2 | 31774 | rare | 0 | null | null | 0 | 0 | 0 | null | null | null | 0 | 0 | 0 |
| E011 | 2 | 31774 | frequent | 2478 | 0.801856 | 0.066586 | 640 | 1543 | 295 | 0.083132 | 0.034167 | 0.048964 | 250 | 2125 | 103 |
| E011 | 2 | 31774 | well_supported | 2478 | 0.801856 | 0.066586 | 640 | 1543 | 295 | 0.083132 | 0.034167 | 0.048964 | 250 | 2125 | 103 |
| E011 | 2 | 33474 | all | 1766 | 0.601925 | 0.233862 | 405 | 1206 | 155 | 0.095319 | 0.023499 | 0.071820 | 263 | 1463 | 40 |
| E011 | 2 | 33474 | unsupported | 683 | 0.616398 | 0.245974 | 0 | 683 | 0 | 0.000000 | 0.000000 | 0.000000 | 0 | 683 | 0 |
| E011 | 2 | 33474 | rare | 0 | null | null | 0 | 0 | 0 | null | null | null | 0 | 0 | 0 |
| E011 | 2 | 33474 | frequent | 1083 | 0.592798 | 0.226223 | 405 | 523 | 155 | 0.155432 | 0.038319 | 0.117113 | 263 | 780 | 40 |
| E011 | 2 | 33474 | well_supported | 1083 | 0.592798 | 0.226223 | 405 | 523 | 155 | 0.155432 | 0.038319 | 0.117113 | 263 | 780 | 40 |
| E011 | 2 | 91695 | all | 2610 | 0.350192 | 0.345211 | 365 | 1701 | 544 | 0.065773 | 0.104662 | -0.038889 | 332 | 1734 | 544 |
| E011 | 2 | 91695 | unsupported | 665 | 0.093233 | 0.085714 | 0 | 665 | 0 | 0.000000 | 0.000000 | 0.000000 | 0 | 665 | 0 |
| E011 | 2 | 91695 | rare | 0 | null | null | 0 | 0 | 0 | null | null | null | 0 | 0 | 0 |
| E011 | 2 | 91695 | frequent | 1945 | 0.438046 | 0.433933 | 365 | 1036 | 544 | 0.088260 | 0.140446 | -0.052185 | 332 | 1069 | 544 |
| E011 | 2 | 91695 | well_supported | 1945 | 0.438046 | 0.433933 | 365 | 1036 | 544 | 0.088260 | 0.140446 | -0.052185 | 332 | 1069 | 544 |
| E012 | 2 | all | all | 7491 | 1.000000 | 0.409959 | 746 | 5914 | 831 | 0.016598 | 0.018667 | -0.002069 | 0 | 7491 | 0 |
| E012 | 2 | all | unsupported | 1985 | 1.000000 | 0.435264 | 0 | 1985 | 0 | 0.000000 | 0.000000 | 0.000000 | 0 | 1985 | 0 |
| E012 | 2 | all | rare | 0 | null | null | 0 | 0 | 0 | null | null | null | 0 | 0 | 0 |
| E012 | 2 | all | frequent | 5506 | 1.000000 | 0.400835 | 746 | 3929 | 831 | 0.022581 | 0.025397 | -0.002815 | 0 | 5506 | 0 |
| E012 | 2 | all | well_supported | 5506 | 1.000000 | 0.400835 | 746 | 3929 | 831 | 0.022581 | 0.025397 | -0.002815 | 0 | 5506 | 0 |
| E012 | 2 | 31774 | all | 3115 | 1.000000 | 0.152167 | 443 | 2285 | 387 | 0.023703 | 0.021134 | 0.002568 | 0 | 3115 | 0 |
| E012 | 2 | 31774 | unsupported | 637 | 1.000000 | 0.298273 | 0 | 637 | 0 | 0.000000 | 0.000000 | 0.000000 | 0 | 637 | 0 |
| E012 | 2 | 31774 | rare | 0 | null | null | 0 | 0 | 0 | null | null | null | 0 | 0 | 0 |
| E012 | 2 | 31774 | frequent | 2478 | 1.000000 | 0.114609 | 443 | 1648 | 387 | 0.029796 | 0.026567 | 0.003228 | 0 | 2478 | 0 |
| E012 | 2 | 31774 | well_supported | 2478 | 1.000000 | 0.114609 | 443 | 1648 | 387 | 0.029796 | 0.026567 | 0.003228 | 0 | 2478 | 0 |
| E012 | 2 | 33474 | all | 1766 | 1.000000 | 0.024915 | 286 | 1041 | 439 | 0.026991 | 0.041431 | -0.014439 | 0 | 1766 | 0 |
| E012 | 2 | 33474 | unsupported | 683 | 1.000000 | 0.016105 | 0 | 683 | 0 | 0.000000 | 0.000000 | 0.000000 | 0 | 683 | 0 |
| E012 | 2 | 33474 | rare | 0 | null | null | 0 | 0 | 0 | null | null | null | 0 | 0 | 0 |
| E012 | 2 | 33474 | frequent | 1083 | 1.000000 | 0.030471 | 286 | 358 | 439 | 0.044014 | 0.067559 | -0.023546 | 0 | 1083 | 0 |
| E012 | 2 | 33474 | well_supported | 1083 | 1.000000 | 0.030471 | 286 | 358 | 439 | 0.044014 | 0.067559 | -0.023546 | 0 | 1083 | 0 |
| E012 | 2 | 91695 | all | 2610 | 1.000000 | 0.978161 | 17 | 2588 | 5 | 0.001086 | 0.000319 | 0.000766 | 0 | 2610 | 0 |
| E012 | 2 | 91695 | unsupported | 665 | 1.000000 | 0.996992 | 0 | 665 | 0 | 0.000000 | 0.000000 | 0.000000 | 0 | 665 | 0 |
| E012 | 2 | 91695 | rare | 0 | null | null | 0 | 0 | 0 | null | null | null | 0 | 0 | 0 |
| E012 | 2 | 91695 | frequent | 1945 | 1.000000 | 0.971722 | 17 | 1923 | 5 | 0.001457 | 0.000428 | 0.001028 | 0 | 1945 | 0 |
| E012 | 2 | 91695 | well_supported | 1945 | 1.000000 | 0.971722 | 17 | 1923 | 5 | 0.001457 | 0.000428 | 0.001028 | 0 | 1945 | 0 |
| frequency | 2 | all | all | 7491 | 1.000000 | 1.000000 | 0 | 7491 | 0 | 0.000000 | 0.000000 | 0.000000 | 0 | 7491 | 0 |
| frequency | 2 | all | unsupported | 1985 | 1.000000 | 1.000000 | 0 | 1985 | 0 | 0.000000 | 0.000000 | 0.000000 | 0 | 1985 | 0 |
| frequency | 2 | all | rare | 0 | null | null | 0 | 0 | 0 | null | null | null | 0 | 0 | 0 |
| frequency | 2 | all | frequent | 5506 | 1.000000 | 1.000000 | 0 | 5506 | 0 | 0.000000 | 0.000000 | 0.000000 | 0 | 5506 | 0 |
| frequency | 2 | all | well_supported | 5506 | 1.000000 | 1.000000 | 0 | 5506 | 0 | 0.000000 | 0.000000 | 0.000000 | 0 | 5506 | 0 |
| frequency | 2 | 31774 | all | 3115 | 1.000000 | 1.000000 | 0 | 3115 | 0 | 0.000000 | 0.000000 | 0.000000 | 0 | 3115 | 0 |
| frequency | 2 | 31774 | unsupported | 637 | 1.000000 | 1.000000 | 0 | 637 | 0 | 0.000000 | 0.000000 | 0.000000 | 0 | 637 | 0 |
| frequency | 2 | 31774 | rare | 0 | null | null | 0 | 0 | 0 | null | null | null | 0 | 0 | 0 |
| frequency | 2 | 31774 | frequent | 2478 | 1.000000 | 1.000000 | 0 | 2478 | 0 | 0.000000 | 0.000000 | 0.000000 | 0 | 2478 | 0 |
| frequency | 2 | 31774 | well_supported | 2478 | 1.000000 | 1.000000 | 0 | 2478 | 0 | 0.000000 | 0.000000 | 0.000000 | 0 | 2478 | 0 |
| frequency | 2 | 33474 | all | 1766 | 1.000000 | 1.000000 | 0 | 1766 | 0 | 0.000000 | 0.000000 | 0.000000 | 0 | 1766 | 0 |
| frequency | 2 | 33474 | unsupported | 683 | 1.000000 | 1.000000 | 0 | 683 | 0 | 0.000000 | 0.000000 | 0.000000 | 0 | 683 | 0 |
| frequency | 2 | 33474 | rare | 0 | null | null | 0 | 0 | 0 | null | null | null | 0 | 0 | 0 |
| frequency | 2 | 33474 | frequent | 1083 | 1.000000 | 1.000000 | 0 | 1083 | 0 | 0.000000 | 0.000000 | 0.000000 | 0 | 1083 | 0 |
| frequency | 2 | 33474 | well_supported | 1083 | 1.000000 | 1.000000 | 0 | 1083 | 0 | 0.000000 | 0.000000 | 0.000000 | 0 | 1083 | 0 |
| frequency | 2 | 91695 | all | 2610 | 1.000000 | 1.000000 | 0 | 2610 | 0 | 0.000000 | 0.000000 | 0.000000 | 0 | 2610 | 0 |
| frequency | 2 | 91695 | unsupported | 665 | 1.000000 | 1.000000 | 0 | 665 | 0 | 0.000000 | 0.000000 | 0.000000 | 0 | 665 | 0 |
| frequency | 2 | 91695 | rare | 0 | null | null | 0 | 0 | 0 | null | null | null | 0 | 0 | 0 |
| frequency | 2 | 91695 | frequent | 1945 | 1.000000 | 1.000000 | 0 | 1945 | 0 | 0.000000 | 0.000000 | 0.000000 | 0 | 1945 | 0 |
| frequency | 2 | 91695 | well_supported | 1945 | 1.000000 | 1.000000 | 0 | 1945 | 0 | 0.000000 | 0.000000 | 0.000000 | 0 | 1945 | 0 |
| E011 | 3 | all | all | 7091 | 0.713016 | 0.113101 | 1336 | 4922 | 833 | 0.072087 | 0.045363 | 0.026724 | 749 | 6009 | 333 |
| E011 | 3 | all | unsupported | 2162 | 0.679926 | 0.029140 | 0 | 2162 | 0 | 0.000000 | 0.000000 | 0.000000 | 0 | 2162 | 0 |
| E011 | 3 | all | rare | 0 | null | null | 0 | 0 | 0 | null | null | null | 0 | 0 | 0 |
| E011 | 3 | all | frequent | 4929 | 0.727531 | 0.149929 | 1336 | 2760 | 833 | 0.103706 | 0.065260 | 0.038446 | 749 | 3847 | 333 |
| E011 | 3 | all | well_supported | 4929 | 0.727531 | 0.149929 | 1336 | 2760 | 833 | 0.103706 | 0.065260 | 0.038446 | 749 | 3847 | 333 |
| E011 | 3 | 32833 | all | 3105 | 0.870531 | 0.060870 | 323 | 2295 | 487 | 0.039775 | 0.060494 | -0.020719 | 143 | 2825 | 137 |
| E011 | 3 | 32833 | unsupported | 1124 | 0.986655 | 0.003559 | 0 | 1124 | 0 | 0.000000 | 0.000000 | 0.000000 | 0 | 1124 | 0 |
| E011 | 3 | 32833 | rare | 0 | null | null | 0 | 0 | 0 | null | null | null | 0 | 0 | 0 |
| E011 | 3 | 32833 | frequent | 1981 | 0.804644 | 0.093387 | 323 | 1171 | 487 | 0.062342 | 0.094817 | -0.032475 | 143 | 1701 | 137 |
| E011 | 3 | 32833 | well_supported | 1981 | 0.804644 | 0.093387 | 323 | 1171 | 487 | 0.062342 | 0.094817 | -0.032475 | 143 | 1701 | 137 |
| E011 | 3 | 33472 | all | 2800 | 0.763571 | 0.146071 | 715 | 1934 | 151 | 0.087202 | 0.013036 | 0.074167 | 325 | 2472 | 3 |
| E011 | 3 | 33472 | unsupported | 652 | 0.541411 | 0.078221 | 0 | 652 | 0 | 0.000000 | 0.000000 | 0.000000 | 0 | 652 | 0 |
| E011 | 3 | 33472 | rare | 0 | null | null | 0 | 0 | 0 | null | null | null | 0 | 0 | 0 |
| E011 | 3 | 33472 | frequent | 2148 | 0.831006 | 0.166667 | 715 | 1282 | 151 | 0.113672 | 0.016993 | 0.096679 | 325 | 1820 | 3 |
| E011 | 3 | 33472 | well_supported | 2148 | 0.831006 | 0.166667 | 715 | 1282 | 151 | 0.113672 | 0.016993 | 0.096679 | 325 | 1820 | 3 |
| E011 | 3 | 76870 | all | 1186 | 0.181282 | 0.172007 | 298 | 693 | 195 | 0.120995 | 0.082069 | 0.038926 | 281 | 712 | 193 |
| E011 | 3 | 76870 | unsupported | 386 | 0.020725 | 0.020725 | 0 | 386 | 0 | 0.000000 | 0.000000 | 0.000000 | 0 | 386 | 0 |
| E011 | 3 | 76870 | rare | 0 | null | null | 0 | 0 | 0 | null | null | null | 0 | 0 | 0 |
| E011 | 3 | 76870 | frequent | 800 | 0.258750 | 0.245000 | 298 | 307 | 195 | 0.179375 | 0.121667 | 0.057708 | 281 | 326 | 193 |
| E011 | 3 | 76870 | well_supported | 800 | 0.258750 | 0.245000 | 298 | 307 | 195 | 0.179375 | 0.121667 | 0.057708 | 281 | 326 | 193 |
| E012 | 3 | all | all | 7091 | 0.998167 | 0.857143 | 60 | 6894 | 137 | 0.001974 | 0.003244 | -0.001269 | 12 | 7079 | 0 |
| E012 | 3 | all | unsupported | 2162 | 1.000000 | 0.682239 | 0 | 2162 | 0 | 0.000000 | 0.000000 | 0.000000 | 0 | 2162 | 0 |
| E012 | 3 | all | rare | 0 | null | null | 0 | 0 | 0 | null | null | null | 0 | 0 | 0 |
| E012 | 3 | all | frequent | 4929 | 0.997363 | 0.933861 | 60 | 4732 | 137 | 0.002840 | 0.004666 | -0.001826 | 12 | 4917 | 0 |
| E012 | 3 | all | well_supported | 4929 | 0.997363 | 0.933861 | 60 | 4732 | 137 | 0.002840 | 0.004666 | -0.001826 | 12 | 4917 | 0 |
| E012 | 3 | 32833 | all | 3105 | 1.000000 | 0.680515 | 48 | 2921 | 136 | 0.002576 | 0.007300 | -0.004724 | 0 | 3105 | 0 |
| E012 | 3 | 32833 | unsupported | 1124 | 1.000000 | 0.390569 | 0 | 1124 | 0 | 0.000000 | 0.000000 | 0.000000 | 0 | 1124 | 0 |
| E012 | 3 | 32833 | rare | 0 | null | null | 0 | 0 | 0 | null | null | null | 0 | 0 | 0 |
| E012 | 3 | 32833 | frequent | 1981 | 1.000000 | 0.845028 | 48 | 1797 | 136 | 0.004038 | 0.011442 | -0.007404 | 0 | 1981 | 0 |
| E012 | 3 | 32833 | well_supported | 1981 | 1.000000 | 0.845028 | 48 | 1797 | 136 | 0.004038 | 0.011442 | -0.007404 | 0 | 1981 | 0 |
| E012 | 3 | 33472 | all | 2800 | 0.995357 | 0.993214 | 12 | 2788 | 0 | 0.002143 | 0.000000 | 0.002143 | 12 | 2788 | 0 |
| E012 | 3 | 33472 | unsupported | 652 | 1.000000 | 0.996933 | 0 | 652 | 0 | 0.000000 | 0.000000 | 0.000000 | 0 | 652 | 0 |
| E012 | 3 | 33472 | rare | 0 | null | null | 0 | 0 | 0 | null | null | null | 0 | 0 | 0 |
| E012 | 3 | 33472 | frequent | 2148 | 0.993948 | 0.992086 | 12 | 2136 | 0 | 0.002793 | 0.000000 | 0.002793 | 12 | 2136 | 0 |
| E012 | 3 | 33472 | well_supported | 2148 | 0.993948 | 0.992086 | 12 | 2136 | 0 | 0.002793 | 0.000000 | 0.002793 | 12 | 2136 | 0 |
| E012 | 3 | 76870 | all | 1186 | 1.000000 | 0.998314 | 0 | 1185 | 1 | 0.000000 | 0.000281 | -0.000281 | 0 | 1186 | 0 |
| E012 | 3 | 76870 | unsupported | 386 | 1.000000 | 1.000000 | 0 | 386 | 0 | 0.000000 | 0.000000 | 0.000000 | 0 | 386 | 0 |
| E012 | 3 | 76870 | rare | 0 | null | null | 0 | 0 | 0 | null | null | null | 0 | 0 | 0 |
| E012 | 3 | 76870 | frequent | 800 | 1.000000 | 0.997500 | 0 | 799 | 1 | 0.000000 | 0.000417 | -0.000417 | 0 | 800 | 0 |
| E012 | 3 | 76870 | well_supported | 800 | 1.000000 | 0.997500 | 0 | 799 | 1 | 0.000000 | 0.000417 | -0.000417 | 0 | 800 | 0 |
| frequency | 3 | all | all | 7091 | 1.000000 | 1.000000 | 0 | 7091 | 0 | 0.000000 | 0.000000 | 0.000000 | 0 | 7091 | 0 |
| frequency | 3 | all | unsupported | 2162 | 1.000000 | 1.000000 | 0 | 2162 | 0 | 0.000000 | 0.000000 | 0.000000 | 0 | 2162 | 0 |
| frequency | 3 | all | rare | 0 | null | null | 0 | 0 | 0 | null | null | null | 0 | 0 | 0 |
| frequency | 3 | all | frequent | 4929 | 1.000000 | 1.000000 | 0 | 4929 | 0 | 0.000000 | 0.000000 | 0.000000 | 0 | 4929 | 0 |
| frequency | 3 | all | well_supported | 4929 | 1.000000 | 1.000000 | 0 | 4929 | 0 | 0.000000 | 0.000000 | 0.000000 | 0 | 4929 | 0 |
| frequency | 3 | 32833 | all | 3105 | 1.000000 | 1.000000 | 0 | 3105 | 0 | 0.000000 | 0.000000 | 0.000000 | 0 | 3105 | 0 |
| frequency | 3 | 32833 | unsupported | 1124 | 1.000000 | 1.000000 | 0 | 1124 | 0 | 0.000000 | 0.000000 | 0.000000 | 0 | 1124 | 0 |
| frequency | 3 | 32833 | rare | 0 | null | null | 0 | 0 | 0 | null | null | null | 0 | 0 | 0 |
| frequency | 3 | 32833 | frequent | 1981 | 1.000000 | 1.000000 | 0 | 1981 | 0 | 0.000000 | 0.000000 | 0.000000 | 0 | 1981 | 0 |
| frequency | 3 | 32833 | well_supported | 1981 | 1.000000 | 1.000000 | 0 | 1981 | 0 | 0.000000 | 0.000000 | 0.000000 | 0 | 1981 | 0 |
| frequency | 3 | 33472 | all | 2800 | 1.000000 | 1.000000 | 0 | 2800 | 0 | 0.000000 | 0.000000 | 0.000000 | 0 | 2800 | 0 |
| frequency | 3 | 33472 | unsupported | 652 | 1.000000 | 1.000000 | 0 | 652 | 0 | 0.000000 | 0.000000 | 0.000000 | 0 | 652 | 0 |
| frequency | 3 | 33472 | rare | 0 | null | null | 0 | 0 | 0 | null | null | null | 0 | 0 | 0 |
| frequency | 3 | 33472 | frequent | 2148 | 1.000000 | 1.000000 | 0 | 2148 | 0 | 0.000000 | 0.000000 | 0.000000 | 0 | 2148 | 0 |
| frequency | 3 | 33472 | well_supported | 2148 | 1.000000 | 1.000000 | 0 | 2148 | 0 | 0.000000 | 0.000000 | 0.000000 | 0 | 2148 | 0 |
| frequency | 3 | 76870 | all | 1186 | 1.000000 | 1.000000 | 0 | 1186 | 0 | 0.000000 | 0.000000 | 0.000000 | 0 | 1186 | 0 |
| frequency | 3 | 76870 | unsupported | 386 | 1.000000 | 1.000000 | 0 | 386 | 0 | 0.000000 | 0.000000 | 0.000000 | 0 | 386 | 0 |
| frequency | 3 | 76870 | rare | 0 | null | null | 0 | 0 | 0 | null | null | null | 0 | 0 | 0 |
| frequency | 3 | 76870 | frequent | 800 | 1.000000 | 1.000000 | 0 | 800 | 0 | 0.000000 | 0.000000 | 0.000000 | 0 | 800 | 0 |
| frequency | 3 | 76870 | well_supported | 800 | 1.000000 | 1.000000 | 0 | 800 | 0 | 0.000000 | 0.000000 | 0.000000 | 0 | 800 | 0 |
| E011 | 4 | all | all | 7405 | 0.487373 | 0.367454 | 1233 | 4567 | 1605 | 0.066892 | 0.097164 | -0.030272 | 826 | 5396 | 1183 |
| E011 | 4 | all | unsupported | 1588 | 0.571159 | 0.408690 | 0 | 1588 | 0 | 0.000000 | 0.000000 | 0.000000 | 0 | 1588 | 0 |
| E011 | 4 | all | rare | 0 | null | null | 0 | 0 | 0 | null | null | null | 0 | 0 | 0 |
| E011 | 4 | all | frequent | 5817 | 0.464501 | 0.356197 | 1233 | 2979 | 1605 | 0.085153 | 0.123689 | -0.038536 | 826 | 3808 | 1183 |
| E011 | 4 | all | well_supported | 5722 | 0.457008 | 0.348305 | 1228 | 2889 | 1605 | 0.086275 | 0.125743 | -0.039468 | 826 | 3713 | 1183 |
| E011 | 4 | 31777 | all | 2809 | 0.690993 | 0.602706 | 410 | 2073 | 326 | 0.063724 | 0.057434 | 0.006289 | 328 | 2180 | 301 |
| E011 | 4 | 31777 | unsupported | 314 | 0.707006 | 0.592357 | 0 | 314 | 0 | 0.000000 | 0.000000 | 0.000000 | 0 | 314 | 0 |
| E011 | 4 | 31777 | rare | 0 | null | null | 0 | 0 | 0 | null | null | null | 0 | 0 | 0 |
| E011 | 4 | 31777 | frequent | 2495 | 0.688978 | 0.604008 | 410 | 1759 | 326 | 0.071743 | 0.064663 | 0.007081 | 328 | 1866 | 301 |
| E011 | 4 | 31777 | well_supported | 2419 | 0.681273 | 0.595701 | 405 | 1688 | 326 | 0.073309 | 0.066694 | 0.006614 | 328 | 1790 | 301 |
| E011 | 4 | 33471 | all | 1542 | 0.425422 | 0.305447 | 134 | 735 | 673 | 0.036533 | 0.218764 | -0.182231 | 102 | 853 | 587 |
| E011 | 4 | 33471 | unsupported | 418 | 0.933014 | 0.760766 | 0 | 418 | 0 | 0.000000 | 0.000000 | 0.000000 | 0 | 418 | 0 |
| E011 | 4 | 33471 | rare | 0 | null | null | 0 | 0 | 0 | null | null | null | 0 | 0 | 0 |
| E011 | 4 | 33471 | frequent | 1124 | 0.236655 | 0.136121 | 134 | 317 | 673 | 0.050119 | 0.300119 | -0.250000 | 102 | 435 | 587 |
| E011 | 4 | 33471 | well_supported | 1105 | 0.226244 | 0.126697 | 134 | 298 | 673 | 0.050980 | 0.305279 | -0.254299 | 102 | 416 | 587 |
| E011 | 4 | 89443 | all | 3054 | 0.331369 | 0.182384 | 689 | 1759 | 606 | 0.085134 | 0.072310 | 0.012825 | 396 | 2363 | 295 |
| E011 | 4 | 89443 | unsupported | 856 | 0.344626 | 0.169393 | 0 | 856 | 0 | 0.000000 | 0.000000 | 0.000000 | 0 | 856 | 0 |
| E011 | 4 | 89443 | rare | 0 | null | null | 0 | 0 | 0 | null | null | null | 0 | 0 | 0 |
| E011 | 4 | 89443 | frequent | 2198 | 0.326206 | 0.187443 | 689 | 903 | 606 | 0.118289 | 0.100470 | 0.017819 | 396 | 1507 | 295 |
| E011 | 4 | 89443 | well_supported | 2198 | 0.326206 | 0.187443 | 689 | 903 | 606 | 0.118289 | 0.100470 | 0.017819 | 396 | 1507 | 295 |
| E012 | 4 | all | all | 7405 | 1.000000 | 0.597299 | 236 | 6660 | 509 | 0.006820 | 0.015215 | -0.008395 | 0 | 7405 | 0 |
| E012 | 4 | all | unsupported | 1588 | 1.000000 | 0.719144 | 0 | 1588 | 0 | 0.000000 | 0.000000 | 0.000000 | 0 | 1588 | 0 |
| E012 | 4 | all | rare | 0 | null | null | 0 | 0 | 0 | null | null | null | 0 | 0 | 0 |
| E012 | 4 | all | frequent | 5817 | 1.000000 | 0.564036 | 236 | 5072 | 509 | 0.008681 | 0.019369 | -0.010687 | 0 | 5817 | 0 |
| E012 | 4 | all | well_supported | 5722 | 1.000000 | 0.568508 | 169 | 5044 | 509 | 0.004923 | 0.019690 | -0.014768 | 0 | 5722 | 0 |
| E012 | 4 | 31777 | all | 2809 | 1.000000 | 0.313635 | 67 | 2649 | 93 | 0.007951 | 0.011036 | -0.003085 | 0 | 2809 | 0 |
| E012 | 4 | 31777 | unsupported | 314 | 1.000000 | 0.375796 | 0 | 314 | 0 | 0.000000 | 0.000000 | 0.000000 | 0 | 314 | 0 |
| E012 | 4 | 31777 | rare | 0 | null | null | 0 | 0 | 0 | null | null | null | 0 | 0 | 0 |
| E012 | 4 | 31777 | frequent | 2495 | 1.000000 | 0.305812 | 67 | 2335 | 93 | 0.008951 | 0.012425 | -0.003474 | 0 | 2495 | 0 |
| E012 | 4 | 31777 | well_supported | 2419 | 1.000000 | 0.311699 | 0 | 2326 | 93 | 0.000000 | 0.012815 | -0.012815 | 0 | 2419 | 0 |
| E012 | 4 | 33471 | all | 1542 | 1.000000 | 0.936446 | 0 | 1535 | 7 | 0.000000 | 0.001513 | -0.001513 | 0 | 1542 | 0 |
| E012 | 4 | 33471 | unsupported | 418 | 1.000000 | 0.904306 | 0 | 418 | 0 | 0.000000 | 0.000000 | 0.000000 | 0 | 418 | 0 |
| E012 | 4 | 33471 | rare | 0 | null | null | 0 | 0 | 0 | null | null | null | 0 | 0 | 0 |
| E012 | 4 | 33471 | frequent | 1124 | 1.000000 | 0.948399 | 0 | 1117 | 7 | 0.000000 | 0.002076 | -0.002076 | 0 | 1124 | 0 |
| E012 | 4 | 33471 | well_supported | 1105 | 1.000000 | 0.947511 | 0 | 1098 | 7 | 0.000000 | 0.002112 | -0.002112 | 0 | 1105 | 0 |
| E012 | 4 | 89443 | all | 3054 | 1.000000 | 0.686968 | 169 | 2476 | 409 | 0.009223 | 0.025977 | -0.016754 | 0 | 3054 | 0 |
| E012 | 4 | 89443 | unsupported | 856 | 1.000000 | 0.754673 | 0 | 856 | 0 | 0.000000 | 0.000000 | 0.000000 | 0 | 856 | 0 |
| E012 | 4 | 89443 | rare | 0 | null | null | 0 | 0 | 0 | null | null | null | 0 | 0 | 0 |
| E012 | 4 | 89443 | frequent | 2198 | 1.000000 | 0.660601 | 169 | 1620 | 409 | 0.012815 | 0.036093 | -0.023279 | 0 | 2198 | 0 |
| E012 | 4 | 89443 | well_supported | 2198 | 1.000000 | 0.660601 | 169 | 1620 | 409 | 0.012815 | 0.036093 | -0.023279 | 0 | 2198 | 0 |
| frequency | 4 | all | all | 7405 | 1.000000 | 1.000000 | 0 | 7405 | 0 | 0.000000 | 0.000000 | 0.000000 | 0 | 7405 | 0 |
| frequency | 4 | all | unsupported | 1588 | 1.000000 | 1.000000 | 0 | 1588 | 0 | 0.000000 | 0.000000 | 0.000000 | 0 | 1588 | 0 |
| frequency | 4 | all | rare | 0 | null | null | 0 | 0 | 0 | null | null | null | 0 | 0 | 0 |
| frequency | 4 | all | frequent | 5817 | 1.000000 | 1.000000 | 0 | 5817 | 0 | 0.000000 | 0.000000 | 0.000000 | 0 | 5817 | 0 |
| frequency | 4 | all | well_supported | 5722 | 1.000000 | 1.000000 | 0 | 5722 | 0 | 0.000000 | 0.000000 | 0.000000 | 0 | 5722 | 0 |
| frequency | 4 | 31777 | all | 2809 | 1.000000 | 1.000000 | 0 | 2809 | 0 | 0.000000 | 0.000000 | 0.000000 | 0 | 2809 | 0 |
| frequency | 4 | 31777 | unsupported | 314 | 1.000000 | 1.000000 | 0 | 314 | 0 | 0.000000 | 0.000000 | 0.000000 | 0 | 314 | 0 |
| frequency | 4 | 31777 | rare | 0 | null | null | 0 | 0 | 0 | null | null | null | 0 | 0 | 0 |
| frequency | 4 | 31777 | frequent | 2495 | 1.000000 | 1.000000 | 0 | 2495 | 0 | 0.000000 | 0.000000 | 0.000000 | 0 | 2495 | 0 |
| frequency | 4 | 31777 | well_supported | 2419 | 1.000000 | 1.000000 | 0 | 2419 | 0 | 0.000000 | 0.000000 | 0.000000 | 0 | 2419 | 0 |
| frequency | 4 | 33471 | all | 1542 | 1.000000 | 1.000000 | 0 | 1542 | 0 | 0.000000 | 0.000000 | 0.000000 | 0 | 1542 | 0 |
| frequency | 4 | 33471 | unsupported | 418 | 1.000000 | 1.000000 | 0 | 418 | 0 | 0.000000 | 0.000000 | 0.000000 | 0 | 418 | 0 |
| frequency | 4 | 33471 | rare | 0 | null | null | 0 | 0 | 0 | null | null | null | 0 | 0 | 0 |
| frequency | 4 | 33471 | frequent | 1124 | 1.000000 | 1.000000 | 0 | 1124 | 0 | 0.000000 | 0.000000 | 0.000000 | 0 | 1124 | 0 |
| frequency | 4 | 33471 | well_supported | 1105 | 1.000000 | 1.000000 | 0 | 1105 | 0 | 0.000000 | 0.000000 | 0.000000 | 0 | 1105 | 0 |
| frequency | 4 | 89443 | all | 3054 | 1.000000 | 1.000000 | 0 | 3054 | 0 | 0.000000 | 0.000000 | 0.000000 | 0 | 3054 | 0 |
| frequency | 4 | 89443 | unsupported | 856 | 1.000000 | 1.000000 | 0 | 856 | 0 | 0.000000 | 0.000000 | 0.000000 | 0 | 856 | 0 |
| frequency | 4 | 89443 | rare | 0 | null | null | 0 | 0 | 0 | null | null | null | 0 | 0 | 0 |
| frequency | 4 | 89443 | frequent | 2198 | 1.000000 | 1.000000 | 0 | 2198 | 0 | 0.000000 | 0.000000 | 0.000000 | 0 | 2198 | 0 |
| frequency | 4 | 89443 | well_supported | 2198 | 1.000000 | 1.000000 | 0 | 2198 | 0 | 0.000000 | 0.000000 | 0.000000 | 0 | 2198 | 0 |

## Calibration aggregates

| Model | Stratum | Metric | Raw mean | Scaled mean | Paired raw minus scaled | Paired fold SD | Eligible paired folds |
|---|---|---|---|---|---|---|---|
| E011 | all | accuracy | 0.368558 | 0.368558 | 0.000000 | 0.000000 | 5 |
| E011 | all | mean_confidence | 0.525008 | 0.453010 | 0.071998 | 0.088064 | 5 |
| E011 | all | confidence_minus_accuracy | 0.156450 | 0.084452 | 0.071998 | 0.088064 | 5 |
| E011 | all | ece | 0.171323 | 0.149626 | 0.021697 | 0.039293 | 5 |
| E011 | all | brier | 0.838401 | 0.838084 | 0.000317 | 0.017156 | 5 |
| E011 | unsupported | accuracy | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 5 |
| E011 | unsupported | mean_confidence | 0.534617 | 0.465572 | 0.069045 | 0.086577 | 5 |
| E011 | unsupported | confidence_minus_accuracy | 0.534617 | 0.465572 | 0.069045 | 0.086577 | 5 |
| E011 | unsupported | ece | null | null | null | null | 0 |
| E011 | unsupported | brier | null | null | null | null | 0 |
| E011 | rare | accuracy | null | null | null | null | 0 |
| E011 | rare | mean_confidence | null | null | null | null | 0 |
| E011 | rare | confidence_minus_accuracy | null | null | null | null | 0 |
| E011 | rare | ece | null | null | null | null | 0 |
| E011 | rare | brier | null | null | null | null | 0 |
| E011 | frequent | accuracy | 0.472586 | 0.472586 | 0.000000 | 0.000000 | 5 |
| E011 | frequent | mean_confidence | 0.520517 | 0.447533 | 0.072984 | 0.088600 | 5 |
| E011 | frequent | confidence_minus_accuracy | 0.047931 | -0.025053 | 0.072984 | 0.088600 | 5 |
| E011 | frequent | ece | 0.099232 | 0.171524 | -0.072292 | 0.065650 | 5 |
| E011 | frequent | brier | 0.678410 | 0.703866 | -0.025456 | 0.024727 | 5 |
| E011 | well_supported | accuracy | 0.481773 | 0.481773 | 0.000000 | 0.000000 | 5 |
| E011 | well_supported | mean_confidence | 0.517778 | 0.444842 | 0.072937 | 0.088500 | 5 |
| E011 | well_supported | confidence_minus_accuracy | 0.036005 | -0.036932 | 0.072937 | 0.088500 | 5 |
| E011 | well_supported | ece | 0.090603 | 0.164786 | -0.074183 | 0.066923 | 5 |
| E011 | well_supported | brier | 0.661952 | 0.687643 | -0.025690 | 0.025105 | 5 |
| E012 | all | accuracy | 0.402374 | 0.402374 | 0.000000 | 0.000000 | 5 |
| E012 | all | mean_confidence | 0.024897 | 0.024904 | -0.000007 | 0.000001 | 5 |
| E012 | all | confidence_minus_accuracy | -0.377477 | -0.377470 | -0.000007 | 0.000001 | 5 |
| E012 | all | ece | 0.377477 | 0.377470 | 0.000007 | 0.000001 | 5 |
| E012 | all | brier | 0.985669 | 0.985662 | 0.000007 | 0.000001 | 5 |
| E012 | unsupported | accuracy | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 5 |
| E012 | unsupported | mean_confidence | 0.024897 | 0.024904 | -0.000007 | 0.000001 | 5 |
| E012 | unsupported | confidence_minus_accuracy | 0.024897 | 0.024904 | -0.000007 | 0.000001 | 5 |
| E012 | unsupported | ece | null | null | null | null | 0 |
| E012 | unsupported | brier | null | null | null | null | 0 |
| E012 | rare | accuracy | null | null | null | null | 0 |
| E012 | rare | mean_confidence | null | null | null | null | 0 |
| E012 | rare | confidence_minus_accuracy | null | null | null | null | 0 |
| E012 | rare | ece | null | null | null | null | 0 |
| E012 | rare | brier | null | null | null | null | 0 |
| E012 | frequent | accuracy | 0.512122 | 0.512122 | 0.000000 | 0.000000 | 5 |
| E012 | frequent | mean_confidence | 0.024897 | 0.024904 | -0.000007 | 0.000001 | 5 |
| E012 | frequent | confidence_minus_accuracy | -0.487225 | -0.487218 | -0.000007 | 0.000001 | 5 |
| E012 | frequent | ece | 0.487225 | 0.487218 | 0.000007 | 0.000001 | 5 |
| E012 | frequent | brier | 0.975103 | 0.975094 | 0.000009 | 0.000002 | 5 |
| E012 | well_supported | accuracy | 0.525069 | 0.525069 | 0.000000 | 0.000000 | 5 |
| E012 | well_supported | mean_confidence | 0.024897 | 0.024903 | -0.000007 | 0.000001 | 5 |
| E012 | well_supported | confidence_minus_accuracy | -0.500172 | -0.500165 | -0.000007 | 0.000001 | 5 |
| E012 | well_supported | ece | 0.500172 | 0.500165 | 0.000007 | 0.000001 | 5 |
| E012 | well_supported | brier | 0.975103 | 0.975094 | 0.000009 | 0.000002 | 5 |
| frequency | all | accuracy | 0.402009 | 0.402009 | 0.000000 | 0.000000 | 5 |
| frequency | all | mean_confidence | 0.413222 | 0.413222 | 0.000000 | 0.000000 | 5 |
| frequency | all | confidence_minus_accuracy | 0.011213 | 0.011213 | 0.000000 | 0.000000 | 5 |
| frequency | all | ece | 0.056271 | 0.056271 | 0.000000 | 0.000000 | 5 |
| frequency | all | brier | 0.795057 | 0.795057 | 0.000000 | 0.000000 | 5 |
| frequency | unsupported | accuracy | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 5 |
| frequency | unsupported | mean_confidence | 0.413222 | 0.413222 | 0.000000 | 0.000000 | 5 |
| frequency | unsupported | confidence_minus_accuracy | 0.413222 | 0.413222 | 0.000000 | 0.000000 | 5 |
| frequency | unsupported | ece | null | null | null | null | 0 |
| frequency | unsupported | brier | null | null | null | null | 0 |
| frequency | rare | accuracy | null | null | null | null | 0 |
| frequency | rare | mean_confidence | null | null | null | null | 0 |
| frequency | rare | confidence_minus_accuracy | null | null | null | null | 0 |
| frequency | rare | ece | null | null | null | null | 0 |
| frequency | rare | brier | null | null | null | null | 0 |
| frequency | frequent | accuracy | 0.511607 | 0.511607 | 0.000000 | 0.000000 | 5 |
| frequency | frequent | mean_confidence | 0.413222 | 0.413222 | 0.000000 | 0.000000 | 5 |
| frequency | frequent | confidence_minus_accuracy | -0.098385 | -0.098385 | 0.000000 | 0.000000 | 5 |
| frequency | frequent | ece | 0.098385 | 0.098385 | 0.000000 | 0.000000 | 5 |
| frequency | frequent | brier | 0.671611 | 0.671611 | 0.000000 | 0.000000 | 5 |
| frequency | well_supported | accuracy | 0.524554 | 0.524554 | 0.000000 | 0.000000 | 5 |
| frequency | well_supported | mean_confidence | 0.413222 | 0.413222 | 0.000000 | 0.000000 | 5 |
| frequency | well_supported | confidence_minus_accuracy | -0.111332 | -0.111332 | 0.000000 | 0.000000 | 5 |
| frequency | well_supported | ece | 0.111332 | 0.111332 | 0.000000 | 0.000000 | 5 |
| frequency | well_supported | brier | 0.658169 | 0.658169 | 0.000000 | 0.000000 | 5 |

## Complete original input calibration diagnostics

| Model | Fold | Question | Stratum | Scale | n | Correct | Accuracy | Confidence | Confidence minus accuracy | ECE | Brier | Exclusions |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| E011 | 0 | all | all | raw | 7686 | 3377 | 0.439370 | 0.456483 | 0.017113 | 0.081279 | 0.749873 | eligible |
| E011 | 0 | all | all | scaled | 7686 | 3377 | 0.439370 | 0.460223 | 0.020853 | 0.082716 | 0.749948 | eligible |
| E011 | 0 | all | unsupported | raw | 407 | 0 | 0.000000 | 0.465799 | 0.465799 | null | null | correct_below_20 |
| E011 | 0 | all | unsupported | scaled | 407 | 0 | 0.000000 | 0.469563 | 0.469563 | null | null | correct_below_20 |
| E011 | 0 | all | rare | raw | 0 | 0 | null | null | null | null | null | n_below_200, correct_below_20, incorrect_below_20 |
| E011 | 0 | all | rare | scaled | 0 | 0 | null | null | null | null | null | n_below_200, correct_below_20, incorrect_below_20 |
| E011 | 0 | all | frequent | raw | 7279 | 3377 | 0.463937 | 0.455963 | -0.007975 | 0.084534 | 0.718557 | eligible |
| E011 | 0 | all | frequent | scaled | 7279 | 3377 | 0.463937 | 0.459701 | -0.004237 | 0.085549 | 0.718406 | eligible |
| E011 | 0 | all | well_supported | raw | 7025 | 3377 | 0.480712 | 0.457175 | -0.023537 | 0.077369 | 0.698409 | eligible |
| E011 | 0 | all | well_supported | scaled | 7025 | 3377 | 0.480712 | 0.460932 | -0.019780 | 0.078633 | 0.698122 | eligible |
| E011 | 0 | 31772 | all | raw | 4857 | 1842 | 0.379246 | 0.461846 | 0.082600 | 0.123206 | 0.805349 | eligible |
| E011 | 0 | 31772 | all | scaled | 4857 | 1842 | 0.379246 | 0.465523 | 0.086276 | 0.123951 | 0.805976 | eligible |
| E011 | 0 | 31772 | unsupported | raw | 16 | 0 | 0.000000 | 0.463848 | 0.463848 | null | null | n_below_200, correct_below_20, incorrect_below_20 |
| E011 | 0 | 31772 | unsupported | scaled | 16 | 0 | 0.000000 | 0.467457 | 0.467457 | null | null | n_below_200, correct_below_20, incorrect_below_20 |
| E011 | 0 | 31772 | rare | raw | 0 | 0 | null | null | null | null | null | n_below_200, correct_below_20, incorrect_below_20 |
| E011 | 0 | 31772 | rare | scaled | 0 | 0 | null | null | null | null | null | n_below_200, correct_below_20, incorrect_below_20 |
| E011 | 0 | 31772 | frequent | raw | 4841 | 1842 | 0.380500 | 0.461840 | 0.081340 | 0.123115 | 0.803670 | eligible |
| E011 | 0 | 31772 | frequent | scaled | 4841 | 1842 | 0.380500 | 0.465516 | 0.085016 | 0.123859 | 0.804287 | eligible |
| E011 | 0 | 31772 | well_supported | raw | 4587 | 1842 | 0.401570 | 0.464022 | 0.062453 | 0.113960 | 0.777527 | eligible |
| E011 | 0 | 31772 | well_supported | scaled | 4587 | 1842 | 0.401570 | 0.467724 | 0.066154 | 0.115069 | 0.777977 | eligible |
| E011 | 0 | 32829 | all | raw | 2156 | 1480 | 0.686456 | 0.476845 | -0.209611 | 0.228430 | 0.561832 | eligible |
| E011 | 0 | 32829 | all | scaled | 2156 | 1480 | 0.686456 | 0.480849 | -0.205608 | 0.225021 | 0.560049 | eligible |
| E011 | 0 | 32829 | unsupported | raw | 272 | 0 | 0.000000 | 0.522256 | 0.522256 | null | null | correct_below_20 |
| E011 | 0 | 32829 | unsupported | scaled | 272 | 0 | 0.000000 | 0.526416 | 0.526416 | null | null | correct_below_20 |
| E011 | 0 | 32829 | rare | raw | 0 | 0 | null | null | null | null | null | n_below_200, correct_below_20, incorrect_below_20 |
| E011 | 0 | 32829 | rare | scaled | 0 | 0 | null | null | null | null | null | n_below_200, correct_below_20, incorrect_below_20 |
| E011 | 0 | 32829 | frequent | raw | 1884 | 1480 | 0.785563 | 0.470289 | -0.315274 | 0.316980 | 0.447580 | eligible |
| E011 | 0 | 32829 | frequent | scaled | 1884 | 1480 | 0.785563 | 0.474270 | -0.311293 | 0.313014 | 0.444865 | eligible |
| E011 | 0 | 32829 | well_supported | raw | 1884 | 1480 | 0.785563 | 0.470289 | -0.315274 | 0.316980 | 0.447580 | eligible |
| E011 | 0 | 32829 | well_supported | scaled | 1884 | 1480 | 0.785563 | 0.474270 | -0.311293 | 0.313014 | 0.444865 | eligible |
| E011 | 0 | 104665 | all | raw | 673 | 55 | 0.081724 | 0.352549 | 0.270825 | 0.270825 | 0.951906 | eligible |
| E011 | 0 | 104665 | all | scaled | 673 | 55 | 0.081724 | 0.355900 | 0.274176 | 0.274176 | 0.953946 | eligible |
| E011 | 0 | 104665 | unsupported | raw | 119 | 0 | 0.000000 | 0.337015 | 0.337015 | null | null | n_below_200, correct_below_20 |
| E011 | 0 | 104665 | unsupported | scaled | 119 | 0 | 0.000000 | 0.339896 | 0.339896 | null | null | n_below_200, correct_below_20 |
| E011 | 0 | 104665 | rare | raw | 0 | 0 | null | null | null | null | null | n_below_200, correct_below_20, incorrect_below_20 |
| E011 | 0 | 104665 | rare | scaled | 0 | 0 | null | null | null | null | null | n_below_200, correct_below_20, incorrect_below_20 |
| E011 | 0 | 104665 | frequent | raw | 554 | 55 | 0.099278 | 0.355886 | 0.256608 | 0.256608 | 0.896330 | eligible |
| E011 | 0 | 104665 | frequent | scaled | 554 | 55 | 0.099278 | 0.359337 | 0.260059 | 0.260059 | 0.898195 | eligible |
| E011 | 0 | 104665 | well_supported | raw | 554 | 55 | 0.099278 | 0.355886 | 0.256608 | 0.256608 | 0.896330 | eligible |
| E011 | 0 | 104665 | well_supported | scaled | 554 | 55 | 0.099278 | 0.359337 | 0.260059 | 0.260059 | 0.898195 | eligible |
| E012 | 0 | all | all | raw | 7686 | 3735 | 0.485948 | 0.025641 | -0.460307 | 0.460307 | 0.977074 | eligible |
| E012 | 0 | all | all | scaled | 7686 | 3735 | 0.485948 | 0.025647 | -0.460301 | 0.460301 | 0.977067 | eligible |
| E012 | 0 | all | unsupported | raw | 407 | 0 | 0.000000 | 0.025641 | 0.025641 | null | null | correct_below_20 |
| E012 | 0 | all | unsupported | scaled | 407 | 0 | 0.000000 | 0.025647 | 0.025647 | null | null | correct_below_20 |
| E012 | 0 | all | rare | raw | 0 | 0 | null | null | null | null | null | n_below_200, correct_below_20, incorrect_below_20 |
| E012 | 0 | all | rare | scaled | 0 | 0 | null | null | null | null | null | n_below_200, correct_below_20, incorrect_below_20 |
| E012 | 0 | all | frequent | raw | 7279 | 3735 | 0.513120 | 0.025641 | -0.487479 | 0.487479 | 0.974359 | eligible |
| E012 | 0 | all | frequent | scaled | 7279 | 3735 | 0.513120 | 0.025647 | -0.487472 | 0.487472 | 0.974351 | eligible |
| E012 | 0 | all | well_supported | raw | 7025 | 3735 | 0.531673 | 0.025641 | -0.506031 | 0.506031 | 0.974359 | eligible |
| E012 | 0 | all | well_supported | scaled | 7025 | 3735 | 0.531673 | 0.025648 | -0.506025 | 0.506025 | 0.974351 | eligible |
| E012 | 0 | 31772 | all | raw | 4857 | 1719 | 0.353922 | 0.025641 | -0.328281 | 0.328281 | 0.974528 | eligible |
| E012 | 0 | 31772 | all | scaled | 4857 | 1719 | 0.353922 | 0.025647 | -0.328275 | 0.328275 | 0.974522 | eligible |
| E012 | 0 | 31772 | unsupported | raw | 16 | 0 | 0.000000 | 0.025641 | 0.025641 | null | null | n_below_200, correct_below_20, incorrect_below_20 |
| E012 | 0 | 31772 | unsupported | scaled | 16 | 0 | 0.000000 | 0.025647 | 0.025647 | null | null | n_below_200, correct_below_20, incorrect_below_20 |
| E012 | 0 | 31772 | rare | raw | 0 | 0 | null | null | null | null | null | n_below_200, correct_below_20, incorrect_below_20 |
| E012 | 0 | 31772 | rare | scaled | 0 | 0 | null | null | null | null | null | n_below_200, correct_below_20, incorrect_below_20 |
| E012 | 0 | 31772 | frequent | raw | 4841 | 1719 | 0.355092 | 0.025641 | -0.329451 | 0.329451 | 0.974359 | eligible |
| E012 | 0 | 31772 | frequent | scaled | 4841 | 1719 | 0.355092 | 0.025647 | -0.329445 | 0.329445 | 0.974353 | eligible |
| E012 | 0 | 31772 | well_supported | raw | 4587 | 1719 | 0.374755 | 0.025641 | -0.349113 | 0.349113 | 0.974359 | eligible |
| E012 | 0 | 31772 | well_supported | scaled | 4587 | 1719 | 0.374755 | 0.025647 | -0.349107 | 0.349107 | 0.974353 | eligible |
| E012 | 0 | 32829 | all | raw | 2156 | 1581 | 0.733302 | 0.025641 | -0.707661 | 0.707661 | 0.980828 | eligible |
| E012 | 0 | 32829 | all | scaled | 2156 | 1581 | 0.733302 | 0.025648 | -0.707654 | 0.707654 | 0.980817 | eligible |
| E012 | 0 | 32829 | unsupported | raw | 272 | 0 | 0.000000 | 0.025641 | 0.025641 | null | null | correct_below_20 |
| E012 | 0 | 32829 | unsupported | scaled | 272 | 0 | 0.000000 | 0.025647 | 0.025647 | null | null | correct_below_20 |
| E012 | 0 | 32829 | rare | raw | 0 | 0 | null | null | null | null | null | n_below_200, correct_below_20, incorrect_below_20 |
| E012 | 0 | 32829 | rare | scaled | 0 | 0 | null | null | null | null | null | n_below_200, correct_below_20, incorrect_below_20 |
| E012 | 0 | 32829 | frequent | raw | 1884 | 1581 | 0.839172 | 0.025641 | -0.813531 | 0.813531 | 0.974358 | eligible |
| E012 | 0 | 32829 | frequent | scaled | 1884 | 1581 | 0.839172 | 0.025648 | -0.813524 | 0.813524 | 0.974346 | eligible |
| E012 | 0 | 32829 | well_supported | raw | 1884 | 1581 | 0.839172 | 0.025641 | -0.813531 | 0.813531 | 0.974358 | eligible |
| E012 | 0 | 32829 | well_supported | scaled | 1884 | 1581 | 0.839172 | 0.025648 | -0.813524 | 0.813524 | 0.974346 | eligible |
| E012 | 0 | 104665 | all | raw | 673 | 435 | 0.646360 | 0.025641 | -0.620718 | 0.620718 | 0.983426 | eligible |
| E012 | 0 | 104665 | all | scaled | 673 | 435 | 0.646360 | 0.025646 | -0.620714 | 0.620714 | 0.983420 | eligible |
| E012 | 0 | 104665 | unsupported | raw | 119 | 0 | 0.000000 | 0.025641 | 0.025641 | null | null | n_below_200, correct_below_20 |
| E012 | 0 | 104665 | unsupported | scaled | 119 | 0 | 0.000000 | 0.025646 | 0.025646 | null | null | n_below_200, correct_below_20 |
| E012 | 0 | 104665 | rare | raw | 0 | 0 | null | null | null | null | null | n_below_200, correct_below_20, incorrect_below_20 |
| E012 | 0 | 104665 | rare | scaled | 0 | 0 | null | null | null | null | null | n_below_200, correct_below_20, incorrect_below_20 |
| E012 | 0 | 104665 | frequent | raw | 554 | 435 | 0.785199 | 0.025641 | -0.759557 | 0.759557 | 0.974359 | eligible |
| E012 | 0 | 104665 | frequent | scaled | 554 | 435 | 0.785199 | 0.025646 | -0.759553 | 0.759553 | 0.974351 | eligible |
| E012 | 0 | 104665 | well_supported | raw | 554 | 435 | 0.785199 | 0.025641 | -0.759557 | 0.759557 | 0.974359 | eligible |
| E012 | 0 | 104665 | well_supported | scaled | 554 | 435 | 0.785199 | 0.025646 | -0.759553 | 0.759553 | 0.974351 | eligible |
| frequency | 0 | all | all | raw | 7686 | 3734 | 0.485818 | 0.373172 | -0.112647 | 0.112647 | 0.755854 | eligible |
| frequency | 0 | all | all | scaled | 7686 | 3734 | 0.485818 | 0.373172 | -0.112647 | 0.112647 | 0.755854 | eligible |
| frequency | 0 | all | unsupported | raw | 407 | 0 | 0.000000 | 0.373172 | 0.373172 | null | null | correct_below_20 |
| frequency | 0 | all | unsupported | scaled | 407 | 0 | 0.000000 | 0.373172 | 0.373172 | null | null | correct_below_20 |
| frequency | 0 | all | rare | raw | 0 | 0 | null | null | null | null | null | n_below_200, correct_below_20, incorrect_below_20 |
| frequency | 0 | all | rare | scaled | 0 | 0 | null | null | null | null | null | n_below_200, correct_below_20, incorrect_below_20 |
| frequency | 0 | all | frequent | raw | 7279 | 3734 | 0.512983 | 0.373172 | -0.139811 | 0.139811 | 0.730497 | eligible |
| frequency | 0 | all | frequent | scaled | 7279 | 3734 | 0.512983 | 0.373172 | -0.139811 | 0.139811 | 0.730497 | eligible |
| frequency | 0 | all | well_supported | raw | 7025 | 3734 | 0.531530 | 0.373172 | -0.158359 | 0.158359 | 0.713308 | eligible |
| frequency | 0 | all | well_supported | scaled | 7025 | 3734 | 0.531530 | 0.373172 | -0.158359 | 0.158359 | 0.713308 | eligible |
| frequency | 0 | 31772 | all | raw | 4857 | 1719 | 0.353922 | 0.373172 | 0.019249 | 0.019249 | 0.831751 | eligible |
| frequency | 0 | 31772 | all | scaled | 4857 | 1719 | 0.353922 | 0.373172 | 0.019249 | 0.019249 | 0.831751 | eligible |
| frequency | 0 | 31772 | unsupported | raw | 16 | 0 | 0.000000 | 0.373172 | 0.373172 | null | null | n_below_200, correct_below_20, incorrect_below_20 |
| frequency | 0 | 31772 | unsupported | scaled | 16 | 0 | 0.000000 | 0.373172 | 0.373172 | null | null | n_below_200, correct_below_20, incorrect_below_20 |
| frequency | 0 | 31772 | rare | raw | 0 | 0 | null | null | null | null | null | n_below_200, correct_below_20, incorrect_below_20 |
| frequency | 0 | 31772 | rare | scaled | 0 | 0 | null | null | null | null | null | n_below_200, correct_below_20, incorrect_below_20 |
| frequency | 0 | 31772 | frequent | raw | 4841 | 1719 | 0.355092 | 0.373172 | 0.018080 | 0.018080 | 0.830503 | eligible |
| frequency | 0 | 31772 | frequent | scaled | 4841 | 1719 | 0.355092 | 0.373172 | 0.018080 | 0.018080 | 0.830503 | eligible |
| frequency | 0 | 31772 | well_supported | raw | 4587 | 1719 | 0.374755 | 0.373172 | -0.001583 | 0.001583 | 0.809714 | eligible |
| frequency | 0 | 31772 | well_supported | scaled | 4587 | 1719 | 0.374755 | 0.373172 | -0.001583 | 0.001583 | 0.809714 | eligible |
| frequency | 0 | 32829 | all | raw | 2156 | 1580 | 0.732839 | 0.373172 | -0.359667 | 0.359667 | 0.613243 | eligible |
| frequency | 0 | 32829 | all | scaled | 2156 | 1580 | 0.732839 | 0.373172 | -0.359667 | 0.359667 | 0.613243 | eligible |
| frequency | 0 | 32829 | unsupported | raw | 272 | 0 | 0.000000 | 0.373172 | 0.373172 | null | null | correct_below_20 |
| frequency | 0 | 32829 | unsupported | scaled | 272 | 0 | 0.000000 | 0.373172 | 0.373172 | null | null | correct_below_20 |
| frequency | 0 | 32829 | rare | raw | 0 | 0 | null | null | null | null | null | n_below_200, correct_below_20, incorrect_below_20 |
| frequency | 0 | 32829 | rare | scaled | 0 | 0 | null | null | null | null | null | n_below_200, correct_below_20, incorrect_below_20 |
| frequency | 0 | 32829 | frequent | raw | 1884 | 1580 | 0.838641 | 0.373172 | -0.465470 | 0.465470 | 0.527182 | eligible |
| frequency | 0 | 32829 | frequent | scaled | 1884 | 1580 | 0.838641 | 0.373172 | -0.465470 | 0.465470 | 0.527182 | eligible |
| frequency | 0 | 32829 | well_supported | raw | 1884 | 1580 | 0.838641 | 0.373172 | -0.465470 | 0.465470 | 0.527182 | eligible |
| frequency | 0 | 32829 | well_supported | scaled | 1884 | 1580 | 0.838641 | 0.373172 | -0.465470 | 0.465470 | 0.527182 | eligible |
| frequency | 0 | 104665 | all | raw | 673 | 435 | 0.646360 | 0.373172 | -0.273188 | 0.273188 | 0.664976 | eligible |
| frequency | 0 | 104665 | all | scaled | 673 | 435 | 0.646360 | 0.373172 | -0.273188 | 0.273188 | 0.664976 | eligible |
| frequency | 0 | 104665 | unsupported | raw | 119 | 0 | 0.000000 | 0.373172 | 0.373172 | null | null | n_below_200, correct_below_20 |
| frequency | 0 | 104665 | unsupported | scaled | 119 | 0 | 0.000000 | 0.373172 | 0.373172 | null | null | n_below_200, correct_below_20 |
| frequency | 0 | 104665 | rare | raw | 0 | 0 | null | null | null | null | null | n_below_200, correct_below_20, incorrect_below_20 |
| frequency | 0 | 104665 | rare | scaled | 0 | 0 | null | null | null | null | null | n_below_200, correct_below_20, incorrect_below_20 |
| frequency | 0 | 104665 | frequent | raw | 554 | 435 | 0.785199 | 0.373172 | -0.412027 | 0.412027 | 0.548044 | eligible |
| frequency | 0 | 104665 | frequent | scaled | 554 | 435 | 0.785199 | 0.373172 | -0.412027 | 0.412027 | 0.548044 | eligible |
| frequency | 0 | 104665 | well_supported | raw | 554 | 435 | 0.785199 | 0.373172 | -0.412027 | 0.412027 | 0.548044 | eligible |
| frequency | 0 | 104665 | well_supported | scaled | 554 | 435 | 0.785199 | 0.373172 | -0.412027 | 0.412027 | 0.548044 | eligible |
| E011 | 1 | all | all | raw | 7023 | 1451 | 0.206607 | 0.549729 | 0.343122 | 0.343248 | 1.023984 | eligible |
| E011 | 1 | all | all | scaled | 7023 | 1451 | 0.206607 | 0.578390 | 0.371783 | 0.371960 | 1.046789 | eligible |
| E011 | 1 | all | unsupported | raw | 1613 | 0 | 0.000000 | 0.552933 | 0.552933 | null | null | correct_below_20 |
| E011 | 1 | all | unsupported | scaled | 1613 | 0 | 0.000000 | 0.583987 | 0.583987 | null | null | correct_below_20 |
| E011 | 1 | all | rare | raw | 0 | 0 | null | null | null | null | null | n_below_200, correct_below_20, incorrect_below_20 |
| E011 | 1 | all | rare | scaled | 0 | 0 | null | null | null | null | null | n_below_200, correct_below_20, incorrect_below_20 |
| E011 | 1 | all | frequent | raw | 5410 | 1451 | 0.268207 | 0.548774 | 0.280567 | 0.281286 | 0.920046 | eligible |
| E011 | 1 | all | frequent | scaled | 5410 | 1451 | 0.268207 | 0.576721 | 0.308514 | 0.309355 | 0.938945 | eligible |
| E011 | 1 | all | well_supported | raw | 5005 | 1451 | 0.289910 | 0.535289 | 0.245379 | 0.246381 | 0.868927 | eligible |
| E011 | 1 | all | well_supported | scaled | 5005 | 1451 | 0.289910 | 0.563054 | 0.273144 | 0.274168 | 0.885859 | eligible |
| E011 | 1 | 31778 | all | raw | 3640 | 684 | 0.187912 | 0.669261 | 0.481349 | 0.481349 | 1.160323 | eligible |
| E011 | 1 | 31778 | all | scaled | 3640 | 684 | 0.187912 | 0.699099 | 0.511187 | 0.511187 | 1.192753 | eligible |
| E011 | 1 | 31778 | unsupported | raw | 1017 | 0 | 0.000000 | 0.616518 | 0.616518 | null | null | correct_below_20 |
| E011 | 1 | 31778 | unsupported | scaled | 1017 | 0 | 0.000000 | 0.648597 | 0.648597 | null | null | correct_below_20 |
| E011 | 1 | 31778 | rare | raw | 0 | 0 | null | null | null | null | null | n_below_200, correct_below_20, incorrect_below_20 |
| E011 | 1 | 31778 | rare | scaled | 0 | 0 | null | null | null | null | null | n_below_200, correct_below_20, incorrect_below_20 |
| E011 | 1 | 31778 | frequent | raw | 2623 | 684 | 0.260770 | 0.689711 | 0.428941 | 0.429779 | 1.053666 | eligible |
| E011 | 1 | 31778 | frequent | scaled | 2623 | 684 | 0.260770 | 0.718680 | 0.457910 | 0.460832 | 1.083233 | eligible |
| E011 | 1 | 31778 | well_supported | raw | 2218 | 684 | 0.308386 | 0.685016 | 0.376630 | 0.378129 | 0.962710 | eligible |
| E011 | 1 | 31778 | well_supported | scaled | 2218 | 684 | 0.308386 | 0.713761 | 0.405375 | 0.413433 | 0.989789 | eligible |
| E011 | 1 | 32835 | all | raw | 2332 | 310 | 0.132933 | 0.423825 | 0.290892 | 0.291272 | 0.940467 | eligible |
| E011 | 1 | 32835 | all | scaled | 2332 | 310 | 0.132933 | 0.451764 | 0.318831 | 0.319364 | 0.958863 | eligible |
| E011 | 1 | 32835 | unsupported | raw | 399 | 0 | 0.000000 | 0.454995 | 0.454995 | null | null | correct_below_20 |
| E011 | 1 | 32835 | unsupported | scaled | 399 | 0 | 0.000000 | 0.485627 | 0.485627 | null | null | correct_below_20 |
| E011 | 1 | 32835 | rare | raw | 0 | 0 | null | null | null | null | null | n_below_200, correct_below_20, incorrect_below_20 |
| E011 | 1 | 32835 | rare | scaled | 0 | 0 | null | null | null | null | null | n_below_200, correct_below_20, incorrect_below_20 |
| E011 | 1 | 32835 | frequent | raw | 1933 | 310 | 0.160372 | 0.417392 | 0.257019 | 0.257477 | 0.872570 | eligible |
| E011 | 1 | 32835 | frequent | scaled | 1933 | 310 | 0.160372 | 0.444774 | 0.284402 | 0.285044 | 0.888448 | eligible |
| E011 | 1 | 32835 | well_supported | raw | 1933 | 310 | 0.160372 | 0.417392 | 0.257019 | 0.257477 | 0.872570 | eligible |
| E011 | 1 | 32835 | well_supported | scaled | 1933 | 310 | 0.160372 | 0.444774 | 0.284402 | 0.285044 | 0.888448 | eligible |
| E011 | 1 | 109465 | all | raw | 1051 | 457 | 0.434824 | 0.415107 | -0.019717 | 0.051437 | 0.737108 | eligible |
| E011 | 1 | 109465 | all | scaled | 1051 | 457 | 0.434824 | 0.441290 | 0.006466 | 0.035263 | 0.736359 | eligible |
| E011 | 1 | 109465 | unsupported | raw | 197 | 0 | 0.000000 | 0.423043 | 0.423043 | null | null | n_below_200, correct_below_20 |
| E011 | 1 | 109465 | unsupported | scaled | 197 | 0 | 0.000000 | 0.449660 | 0.449660 | null | null | n_below_200, correct_below_20 |
| E011 | 1 | 109465 | rare | raw | 0 | 0 | null | null | null | null | null | n_below_200, correct_below_20, incorrect_below_20 |
| E011 | 1 | 109465 | rare | scaled | 0 | 0 | null | null | null | null | null | n_below_200, correct_below_20, incorrect_below_20 |
| E011 | 1 | 109465 | frequent | raw | 854 | 457 | 0.535129 | 0.413276 | -0.121853 | 0.121853 | 0.617106 | eligible |
| E011 | 1 | 109465 | frequent | scaled | 854 | 457 | 0.535129 | 0.439359 | -0.095770 | 0.095770 | 0.610075 | eligible |
| E011 | 1 | 109465 | well_supported | raw | 854 | 457 | 0.535129 | 0.413276 | -0.121853 | 0.121853 | 0.617106 | eligible |
| E011 | 1 | 109465 | well_supported | scaled | 854 | 457 | 0.535129 | 0.439359 | -0.095770 | 0.095770 | 0.610075 | eligible |
| E012 | 1 | all | all | raw | 7023 | 2521 | 0.358963 | 0.025641 | -0.333322 | 0.333322 | 0.986137 | eligible |
| E012 | 1 | all | all | scaled | 7023 | 2521 | 0.358963 | 0.025648 | -0.333316 | 0.333316 | 0.986131 | eligible |
| E012 | 1 | all | unsupported | raw | 1613 | 0 | 0.000000 | 0.025641 | 0.025641 | null | null | correct_below_20 |
| E012 | 1 | all | unsupported | scaled | 1613 | 0 | 0.000000 | 0.025648 | 0.025648 | null | null | correct_below_20 |
| E012 | 1 | all | rare | raw | 0 | 0 | null | null | null | null | null | n_below_200, correct_below_20, incorrect_below_20 |
| E012 | 1 | all | rare | scaled | 0 | 0 | null | null | null | null | null | n_below_200, correct_below_20, incorrect_below_20 |
| E012 | 1 | all | frequent | raw | 5410 | 2521 | 0.465989 | 0.025641 | -0.440348 | 0.440348 | 0.974359 | eligible |
| E012 | 1 | all | frequent | scaled | 5410 | 2521 | 0.465989 | 0.025648 | -0.440341 | 0.440341 | 0.974351 | eligible |
| E012 | 1 | all | well_supported | raw | 5005 | 2521 | 0.503696 | 0.025641 | -0.478055 | 0.478055 | 0.974359 | eligible |
| E012 | 1 | all | well_supported | scaled | 5005 | 2521 | 0.503696 | 0.025647 | -0.478049 | 0.478049 | 0.974350 | eligible |
| E012 | 1 | 31778 | all | raw | 3640 | 1140 | 0.313187 | 0.025642 | -0.287545 | 0.287545 | 0.988687 | eligible |
| E012 | 1 | 31778 | all | scaled | 3640 | 1140 | 0.313187 | 0.025651 | -0.287536 | 0.287536 | 0.988679 | eligible |
| E012 | 1 | 31778 | unsupported | raw | 1017 | 0 | 0.000000 | 0.025641 | 0.025641 | null | null | correct_below_20 |
| E012 | 1 | 31778 | unsupported | scaled | 1017 | 0 | 0.000000 | 0.025650 | 0.025650 | null | null | correct_below_20 |
| E012 | 1 | 31778 | rare | raw | 0 | 0 | null | null | null | null | null | n_below_200, correct_below_20, incorrect_below_20 |
| E012 | 1 | 31778 | rare | scaled | 0 | 0 | null | null | null | null | null | n_below_200, correct_below_20, incorrect_below_20 |
| E012 | 1 | 31778 | frequent | raw | 2623 | 1140 | 0.434617 | 0.025642 | -0.408975 | 0.408975 | 0.974358 | eligible |
| E012 | 1 | 31778 | frequent | scaled | 2623 | 1140 | 0.434617 | 0.025651 | -0.408966 | 0.408966 | 0.974348 | eligible |
| E012 | 1 | 31778 | well_supported | raw | 2218 | 1140 | 0.513977 | 0.025642 | -0.488335 | 0.488335 | 0.974358 | eligible |
| E012 | 1 | 31778 | well_supported | scaled | 2218 | 1140 | 0.513977 | 0.025651 | -0.488326 | 0.488326 | 0.974346 | eligible |
| E012 | 1 | 32835 | all | raw | 2332 | 954 | 0.409091 | 0.025641 | -0.383450 | 0.383450 | 0.983133 | eligible |
| E012 | 1 | 32835 | all | scaled | 2332 | 954 | 0.409091 | 0.025645 | -0.383446 | 0.383446 | 0.983128 | eligible |
| E012 | 1 | 32835 | unsupported | raw | 399 | 0 | 0.000000 | 0.025641 | 0.025641 | null | null | correct_below_20 |
| E012 | 1 | 32835 | unsupported | scaled | 399 | 0 | 0.000000 | 0.025645 | 0.025645 | null | null | correct_below_20 |
| E012 | 1 | 32835 | rare | raw | 0 | 0 | null | null | null | null | null | n_below_200, correct_below_20, incorrect_below_20 |
| E012 | 1 | 32835 | rare | scaled | 0 | 0 | null | null | null | null | null | n_below_200, correct_below_20, incorrect_below_20 |
| E012 | 1 | 32835 | frequent | raw | 1933 | 954 | 0.493533 | 0.025641 | -0.467892 | 0.467892 | 0.974359 | eligible |
| E012 | 1 | 32835 | frequent | scaled | 1933 | 954 | 0.493533 | 0.025645 | -0.467888 | 0.467888 | 0.974353 | eligible |
| E012 | 1 | 32835 | well_supported | raw | 1933 | 954 | 0.493533 | 0.025641 | -0.467892 | 0.467892 | 0.974359 | eligible |
| E012 | 1 | 32835 | well_supported | scaled | 1933 | 954 | 0.493533 | 0.025645 | -0.467888 | 0.467888 | 0.974353 | eligible |
| E012 | 1 | 109465 | all | raw | 1051 | 427 | 0.406280 | 0.025641 | -0.380639 | 0.380639 | 0.983971 | eligible |
| E012 | 1 | 109465 | all | scaled | 1051 | 427 | 0.406280 | 0.025643 | -0.380637 | 0.380637 | 0.983969 | eligible |
| E012 | 1 | 109465 | unsupported | raw | 197 | 0 | 0.000000 | 0.025641 | 0.025641 | null | null | n_below_200, correct_below_20 |
| E012 | 1 | 109465 | unsupported | scaled | 197 | 0 | 0.000000 | 0.025643 | 0.025643 | null | null | n_below_200, correct_below_20 |
| E012 | 1 | 109465 | rare | raw | 0 | 0 | null | null | null | null | null | n_below_200, correct_below_20, incorrect_below_20 |
| E012 | 1 | 109465 | rare | scaled | 0 | 0 | null | null | null | null | null | n_below_200, correct_below_20, incorrect_below_20 |
| E012 | 1 | 109465 | frequent | raw | 854 | 427 | 0.500000 | 0.025641 | -0.474359 | 0.474359 | 0.974359 | eligible |
| E012 | 1 | 109465 | frequent | scaled | 854 | 427 | 0.500000 | 0.025643 | -0.474357 | 0.474357 | 0.974356 | eligible |
| E012 | 1 | 109465 | well_supported | raw | 854 | 427 | 0.500000 | 0.025641 | -0.474359 | 0.474359 | 0.974359 | eligible |
| E012 | 1 | 109465 | well_supported | scaled | 854 | 427 | 0.500000 | 0.025643 | -0.474357 | 0.474357 | 0.974356 | eligible |
| frequency | 1 | all | all | raw | 7023 | 2521 | 0.358963 | 0.414808 | 0.055844 | 0.055844 | 0.823525 | eligible |
| frequency | 1 | all | all | scaled | 7023 | 2521 | 0.358963 | 0.414808 | 0.055844 | 0.055844 | 0.823525 | eligible |
| frequency | 1 | all | unsupported | raw | 1613 | 0 | 0.000000 | 0.414808 | 0.414808 | null | null | correct_below_20 |
| frequency | 1 | all | unsupported | scaled | 1613 | 0 | 0.000000 | 0.414808 | 0.414808 | null | null | correct_below_20 |
| frequency | 1 | all | rare | raw | 0 | 0 | null | null | null | null | null | n_below_200, correct_below_20, incorrect_below_20 |
| frequency | 1 | all | rare | scaled | 0 | 0 | null | null | null | null | null | n_below_200, correct_below_20, incorrect_below_20 |
| frequency | 1 | all | frequent | raw | 5410 | 2521 | 0.465989 | 0.414808 | -0.051181 | 0.051181 | 0.700869 | eligible |
| frequency | 1 | all | frequent | scaled | 5410 | 2521 | 0.465989 | 0.414808 | -0.051181 | 0.051181 | 0.700869 | eligible |
| frequency | 1 | all | well_supported | raw | 5005 | 2521 | 0.503696 | 0.414808 | -0.088889 | 0.088889 | 0.658084 | eligible |
| frequency | 1 | all | well_supported | scaled | 5005 | 2521 | 0.503696 | 0.414808 | -0.088889 | 0.088889 | 0.658084 | eligible |
| frequency | 1 | 31778 | all | raw | 3640 | 1140 | 0.313187 | 0.414808 | 0.101621 | 0.101621 | 0.877694 | eligible |
| frequency | 1 | 31778 | all | scaled | 3640 | 1140 | 0.313187 | 0.414808 | 0.101621 | 0.101621 | 0.877694 | eligible |
| frequency | 1 | 31778 | unsupported | raw | 1017 | 0 | 0.000000 | 0.414808 | 0.414808 | null | null | correct_below_20 |
| frequency | 1 | 31778 | unsupported | scaled | 1017 | 0 | 0.000000 | 0.414808 | 0.414808 | null | null | correct_below_20 |
| frequency | 1 | 31778 | rare | raw | 0 | 0 | null | null | null | null | null | n_below_200, correct_below_20, incorrect_below_20 |
| frequency | 1 | 31778 | rare | scaled | 0 | 0 | null | null | null | null | null | n_below_200, correct_below_20, incorrect_below_20 |
| frequency | 1 | 31778 | frequent | raw | 2623 | 1140 | 0.434617 | 0.414808 | -0.019809 | 0.019809 | 0.739192 | eligible |
| frequency | 1 | 31778 | frequent | scaled | 2623 | 1140 | 0.434617 | 0.414808 | -0.019809 | 0.019809 | 0.739192 | eligible |
| frequency | 1 | 31778 | well_supported | raw | 2218 | 1140 | 0.513977 | 0.414808 | -0.099169 | 0.099169 | 0.649644 | eligible |
| frequency | 1 | 31778 | well_supported | scaled | 2218 | 1140 | 0.513977 | 0.414808 | -0.099169 | 0.099169 | 0.649644 | eligible |
| frequency | 1 | 32835 | all | raw | 2332 | 954 | 0.409091 | 0.414808 | 0.005717 | 0.005717 | 0.769317 | eligible |
| frequency | 1 | 32835 | all | scaled | 2332 | 954 | 0.409091 | 0.414808 | 0.005717 | 0.005717 | 0.769317 | eligible |
| frequency | 1 | 32835 | unsupported | raw | 399 | 0 | 0.000000 | 0.414808 | 0.414808 | null | null | correct_below_20 |
| frequency | 1 | 32835 | unsupported | scaled | 399 | 0 | 0.000000 | 0.414808 | 0.414808 | null | null | correct_below_20 |
| frequency | 1 | 32835 | rare | raw | 0 | 0 | null | null | null | null | null | n_below_200, correct_below_20, incorrect_below_20 |
| frequency | 1 | 32835 | rare | scaled | 0 | 0 | null | null | null | null | null | n_below_200, correct_below_20, incorrect_below_20 |
| frequency | 1 | 32835 | frequent | raw | 1933 | 954 | 0.493533 | 0.414808 | -0.078726 | 0.078726 | 0.673211 | eligible |
| frequency | 1 | 32835 | frequent | scaled | 1933 | 954 | 0.493533 | 0.414808 | -0.078726 | 0.078726 | 0.673211 | eligible |
| frequency | 1 | 32835 | well_supported | raw | 1933 | 954 | 0.493533 | 0.414808 | -0.078726 | 0.078726 | 0.673211 | eligible |
| frequency | 1 | 32835 | well_supported | scaled | 1933 | 954 | 0.493533 | 0.414808 | -0.078726 | 0.078726 | 0.673211 | eligible |
| frequency | 1 | 109465 | all | raw | 1051 | 427 | 0.406280 | 0.414808 | 0.008528 | 0.008528 | 0.756196 | eligible |
| frequency | 1 | 109465 | all | scaled | 1051 | 427 | 0.406280 | 0.414808 | 0.008528 | 0.008528 | 0.756196 | eligible |
| frequency | 1 | 109465 | unsupported | raw | 197 | 0 | 0.000000 | 0.414808 | 0.414808 | null | null | n_below_200, correct_below_20 |
| frequency | 1 | 109465 | unsupported | scaled | 197 | 0 | 0.000000 | 0.414808 | 0.414808 | null | null | n_below_200, correct_below_20 |
| frequency | 1 | 109465 | rare | raw | 0 | 0 | null | null | null | null | null | n_below_200, correct_below_20, incorrect_below_20 |
| frequency | 1 | 109465 | rare | scaled | 0 | 0 | null | null | null | null | null | n_below_200, correct_below_20, incorrect_below_20 |
| frequency | 1 | 109465 | frequent | raw | 854 | 427 | 0.500000 | 0.414808 | -0.085192 | 0.085192 | 0.645766 | eligible |
| frequency | 1 | 109465 | frequent | scaled | 854 | 427 | 0.500000 | 0.414808 | -0.085192 | 0.085192 | 0.645766 | eligible |
| frequency | 1 | 109465 | well_supported | raw | 854 | 427 | 0.500000 | 0.414808 | -0.085192 | 0.085192 | 0.645766 | eligible |
| frequency | 1 | 109465 | well_supported | scaled | 854 | 427 | 0.500000 | 0.414808 | -0.085192 | 0.085192 | 0.645766 | eligible |
| E011 | 2 | all | all | raw | 7491 | 3120 | 0.416500 | 0.518246 | 0.101746 | 0.101746 | 0.752480 | eligible |
| E011 | 2 | all | all | scaled | 7491 | 3120 | 0.416500 | 0.333355 | -0.083145 | 0.084856 | 0.753934 | eligible |
| E011 | 2 | all | unsupported | raw | 1985 | 0 | 0.000000 | 0.470875 | 0.470875 | null | null | correct_below_20 |
| E011 | 2 | all | unsupported | scaled | 1985 | 0 | 0.000000 | 0.290226 | 0.290226 | null | null | correct_below_20 |
| E011 | 2 | all | rare | raw | 0 | 0 | null | null | null | null | null | n_below_200, correct_below_20, incorrect_below_20 |
| E011 | 2 | all | rare | scaled | 0 | 0 | null | null | null | null | null | n_below_200, correct_below_20, incorrect_below_20 |
| E011 | 2 | all | frequent | raw | 5506 | 3120 | 0.566655 | 0.535324 | -0.031330 | 0.050477 | 0.546271 | eligible |
| E011 | 2 | all | frequent | scaled | 5506 | 3120 | 0.566655 | 0.348903 | -0.217751 | 0.217751 | 0.611542 | eligible |
| E011 | 2 | all | well_supported | raw | 5506 | 3120 | 0.566655 | 0.535324 | -0.031330 | 0.050477 | 0.546271 | eligible |
| E011 | 2 | all | well_supported | scaled | 5506 | 3120 | 0.566655 | 0.348903 | -0.217751 | 0.217751 | 0.611542 | eligible |
| E011 | 2 | 31774 | all | raw | 3115 | 1552 | 0.498234 | 0.610961 | 0.112726 | 0.112726 | 0.669622 | eligible |
| E011 | 2 | 31774 | all | scaled | 3115 | 1552 | 0.498234 | 0.406295 | -0.091939 | 0.117331 | 0.671537 | eligible |
| E011 | 2 | 31774 | unsupported | raw | 637 | 0 | 0.000000 | 0.491006 | 0.491006 | null | null | correct_below_20 |
| E011 | 2 | 31774 | unsupported | scaled | 637 | 0 | 0.000000 | 0.307399 | 0.307399 | null | null | correct_below_20 |
| E011 | 2 | 31774 | rare | raw | 0 | 0 | null | null | null | null | null | n_below_200, correct_below_20, incorrect_below_20 |
| E011 | 2 | 31774 | rare | scaled | 0 | 0 | null | null | null | null | null | n_below_200, correct_below_20, incorrect_below_20 |
| E011 | 2 | 31774 | frequent | raw | 2478 | 1552 | 0.626312 | 0.641796 | 0.015485 | 0.028191 | 0.497128 | eligible |
| E011 | 2 | 31774 | frequent | scaled | 2478 | 1552 | 0.626312 | 0.431717 | -0.194594 | 0.194594 | 0.545716 | eligible |
| E011 | 2 | 31774 | well_supported | raw | 2478 | 1552 | 0.626312 | 0.641796 | 0.015485 | 0.028191 | 0.497128 | eligible |
| E011 | 2 | 31774 | well_supported | scaled | 2478 | 1552 | 0.626312 | 0.431717 | -0.194594 | 0.194594 | 0.545716 | eligible |
| E011 | 2 | 33474 | all | raw | 1766 | 546 | 0.309173 | 0.381341 | 0.072168 | 0.072168 | 0.872267 | eligible |
| E011 | 2 | 33474 | all | scaled | 1766 | 546 | 0.309173 | 0.249220 | -0.059953 | 0.067367 | 0.863028 | eligible |
| E011 | 2 | 33474 | unsupported | raw | 683 | 0 | 0.000000 | 0.372234 | 0.372234 | null | null | correct_below_20 |
| E011 | 2 | 33474 | unsupported | scaled | 683 | 0 | 0.000000 | 0.242511 | 0.242511 | null | null | correct_below_20 |
| E011 | 2 | 33474 | rare | raw | 0 | 0 | null | null | null | null | null | n_below_200, correct_below_20, incorrect_below_20 |
| E011 | 2 | 33474 | rare | scaled | 0 | 0 | null | null | null | null | null | n_below_200, correct_below_20, incorrect_below_20 |
| E011 | 2 | 33474 | frequent | raw | 1083 | 546 | 0.504155 | 0.387084 | -0.117071 | 0.124854 | 0.625338 | eligible |
| E011 | 2 | 33474 | frequent | scaled | 1083 | 546 | 0.504155 | 0.253451 | -0.250704 | 0.253648 | 0.692074 | eligible |
| E011 | 2 | 33474 | well_supported | raw | 1083 | 546 | 0.504155 | 0.387084 | -0.117071 | 0.124854 | 0.625338 | eligible |
| E011 | 2 | 33474 | well_supported | scaled | 1083 | 546 | 0.504155 | 0.253451 | -0.250704 | 0.253648 | 0.692074 | eligible |
| E011 | 2 | 91695 | all | raw | 2610 | 1022 | 0.391571 | 0.500226 | 0.108655 | 0.109893 | 0.770318 | eligible |
| E011 | 2 | 91695 | all | scaled | 2610 | 1022 | 0.391571 | 0.303229 | -0.088342 | 0.088929 | 0.778458 | eligible |
| E011 | 2 | 91695 | unsupported | raw | 665 | 0 | 0.000000 | 0.552902 | 0.552902 | null | null | correct_below_20 |
| E011 | 2 | 91695 | unsupported | scaled | 665 | 0 | 0.000000 | 0.322783 | 0.322783 | null | null | correct_below_20 |
| E011 | 2 | 91695 | rare | raw | 0 | 0 | null | null | null | null | null | n_below_200, correct_below_20, incorrect_below_20 |
| E011 | 2 | 91695 | rare | scaled | 0 | 0 | null | null | null | null | null | n_below_200, correct_below_20, incorrect_below_20 |
| E011 | 2 | 91695 | frequent | raw | 1945 | 1022 | 0.525450 | 0.482216 | -0.043233 | 0.050278 | 0.564855 | eligible |
| E011 | 2 | 91695 | frequent | scaled | 1945 | 1022 | 0.525450 | 0.296544 | -0.228906 | 0.229106 | 0.650567 | eligible |
| E011 | 2 | 91695 | well_supported | raw | 1945 | 1022 | 0.525450 | 0.482216 | -0.043233 | 0.050278 | 0.564855 | eligible |
| E011 | 2 | 91695 | well_supported | scaled | 1945 | 1022 | 0.525450 | 0.296544 | -0.228906 | 0.229106 | 0.650567 | eligible |
| E012 | 2 | all | all | raw | 7491 | 2962 | 0.395408 | 0.025000 | -0.370407 | 0.370407 | 0.988249 | eligible |
| E012 | 2 | all | all | scaled | 7491 | 2962 | 0.395408 | 0.025009 | -0.370399 | 0.370399 | 0.988241 | eligible |
| E012 | 2 | all | unsupported | raw | 1985 | 0 | 0.000000 | 0.025000 | 0.025000 | null | null | correct_below_20 |
| E012 | 2 | all | unsupported | scaled | 1985 | 0 | 0.000000 | 0.025009 | 0.025009 | null | null | correct_below_20 |
| E012 | 2 | all | rare | raw | 0 | 0 | null | null | null | null | null | n_below_200, correct_below_20, incorrect_below_20 |
| E012 | 2 | all | rare | scaled | 0 | 0 | null | null | null | null | null | n_below_200, correct_below_20, incorrect_below_20 |
| E012 | 2 | all | frequent | raw | 5506 | 2962 | 0.537959 | 0.025000 | -0.512958 | 0.512958 | 0.974999 | eligible |
| E012 | 2 | all | frequent | scaled | 5506 | 2962 | 0.537959 | 0.025009 | -0.512950 | 0.512950 | 0.974988 | eligible |
| E012 | 2 | all | well_supported | raw | 5506 | 2962 | 0.537959 | 0.025000 | -0.512958 | 0.512958 | 0.974999 | eligible |
| E012 | 2 | all | well_supported | scaled | 5506 | 2962 | 0.537959 | 0.025009 | -0.512950 | 0.512950 | 0.974988 | eligible |
| E012 | 2 | 31774 | all | raw | 3115 | 1405 | 0.451043 | 0.025001 | -0.426043 | 0.426043 | 0.985224 | eligible |
| E012 | 2 | 31774 | all | scaled | 3115 | 1405 | 0.451043 | 0.025011 | -0.426033 | 0.426033 | 0.985214 | eligible |
| E012 | 2 | 31774 | unsupported | raw | 637 | 0 | 0.000000 | 0.025001 | 0.025001 | null | null | correct_below_20 |
| E012 | 2 | 31774 | unsupported | scaled | 637 | 0 | 0.000000 | 0.025011 | 0.025011 | null | null | correct_below_20 |
| E012 | 2 | 31774 | rare | raw | 0 | 0 | null | null | null | null | null | n_below_200, correct_below_20, incorrect_below_20 |
| E012 | 2 | 31774 | rare | scaled | 0 | 0 | null | null | null | null | null | n_below_200, correct_below_20, incorrect_below_20 |
| E012 | 2 | 31774 | frequent | raw | 2478 | 1405 | 0.566990 | 0.025001 | -0.541989 | 0.541989 | 0.974999 | eligible |
| E012 | 2 | 31774 | frequent | scaled | 2478 | 1405 | 0.566990 | 0.025010 | -0.541979 | 0.541979 | 0.974986 | eligible |
| E012 | 2 | 31774 | well_supported | raw | 2478 | 1405 | 0.566990 | 0.025001 | -0.541989 | 0.541989 | 0.974999 | eligible |
| E012 | 2 | 31774 | well_supported | scaled | 2478 | 1405 | 0.566990 | 0.025010 | -0.541979 | 0.541979 | 0.974986 | eligible |
| E012 | 2 | 33474 | all | raw | 1766 | 323 | 0.182899 | 0.025001 | -0.157899 | 0.157899 | 0.994337 | eligible |
| E012 | 2 | 33474 | all | scaled | 1766 | 323 | 0.182899 | 0.025010 | -0.157889 | 0.157889 | 0.994331 | eligible |
| E012 | 2 | 33474 | unsupported | raw | 683 | 0 | 0.000000 | 0.025001 | 0.025001 | null | null | correct_below_20 |
| E012 | 2 | 33474 | unsupported | scaled | 683 | 0 | 0.000000 | 0.025010 | 0.025010 | null | null | correct_below_20 |
| E012 | 2 | 33474 | rare | raw | 0 | 0 | null | null | null | null | null | n_below_200, correct_below_20, incorrect_below_20 |
| E012 | 2 | 33474 | rare | scaled | 0 | 0 | null | null | null | null | null | n_below_200, correct_below_20, incorrect_below_20 |
| E012 | 2 | 33474 | frequent | raw | 1083 | 323 | 0.298246 | 0.025000 | -0.273245 | 0.273245 | 0.975000 | eligible |
| E012 | 2 | 33474 | frequent | scaled | 1083 | 323 | 0.298246 | 0.025010 | -0.273236 | 0.273236 | 0.974990 | eligible |
| E012 | 2 | 33474 | well_supported | raw | 1083 | 323 | 0.298246 | 0.025000 | -0.273245 | 0.273245 | 0.975000 | eligible |
| E012 | 2 | 33474 | well_supported | scaled | 1083 | 323 | 0.298246 | 0.025010 | -0.273236 | 0.273236 | 0.974990 | eligible |
| E012 | 2 | 91695 | all | raw | 2610 | 1234 | 0.472797 | 0.025000 | -0.447797 | 0.447797 | 0.987739 | eligible |
| E012 | 2 | 91695 | all | scaled | 2610 | 1234 | 0.472797 | 0.025006 | -0.447791 | 0.447791 | 0.987733 | eligible |
| E012 | 2 | 91695 | unsupported | raw | 665 | 0 | 0.000000 | 0.025000 | 0.025000 | null | null | correct_below_20 |
| E012 | 2 | 91695 | unsupported | scaled | 665 | 0 | 0.000000 | 0.025006 | 0.025006 | null | null | correct_below_20 |
| E012 | 2 | 91695 | rare | raw | 0 | 0 | null | null | null | null | null | n_below_200, correct_below_20, incorrect_below_20 |
| E012 | 2 | 91695 | rare | scaled | 0 | 0 | null | null | null | null | null | n_below_200, correct_below_20, incorrect_below_20 |
| E012 | 2 | 91695 | frequent | raw | 1945 | 1234 | 0.634447 | 0.025000 | -0.609447 | 0.609447 | 0.975000 | eligible |
| E012 | 2 | 91695 | frequent | scaled | 1945 | 1234 | 0.634447 | 0.025006 | -0.609441 | 0.609441 | 0.974991 | eligible |
| E012 | 2 | 91695 | well_supported | raw | 1945 | 1234 | 0.634447 | 0.025000 | -0.609447 | 0.609447 | 0.975000 | eligible |
| E012 | 2 | 91695 | well_supported | scaled | 1945 | 1234 | 0.634447 | 0.025006 | -0.609441 | 0.609441 | 0.974991 | eligible |
| frequency | 2 | all | all | raw | 7491 | 2962 | 0.395408 | 0.441297 | 0.045889 | 0.045889 | 0.793789 | eligible |
| frequency | 2 | all | all | scaled | 7491 | 2962 | 0.395408 | 0.441297 | 0.045889 | 0.045889 | 0.793789 | eligible |
| frequency | 2 | all | unsupported | raw | 1985 | 0 | 0.000000 | 0.441297 | 0.441297 | null | null | correct_below_20 |
| frequency | 2 | all | unsupported | scaled | 1985 | 0 | 0.000000 | 0.441297 | 0.441297 | null | null | correct_below_20 |
| frequency | 2 | all | rare | raw | 0 | 0 | null | null | null | null | null | n_below_200, correct_below_20, incorrect_below_20 |
| frequency | 2 | all | rare | scaled | 0 | 0 | null | null | null | null | null | n_below_200, correct_below_20, incorrect_below_20 |
| frequency | 2 | all | frequent | raw | 5506 | 2962 | 0.537959 | 0.441297 | -0.096662 | 0.096662 | 0.628435 | eligible |
| frequency | 2 | all | frequent | scaled | 5506 | 2962 | 0.537959 | 0.441297 | -0.096662 | 0.096662 | 0.628435 | eligible |
| frequency | 2 | all | well_supported | raw | 5506 | 2962 | 0.537959 | 0.441297 | -0.096662 | 0.096662 | 0.628435 | eligible |
| frequency | 2 | all | well_supported | scaled | 5506 | 2962 | 0.537959 | 0.441297 | -0.096662 | 0.096662 | 0.628435 | eligible |
| frequency | 2 | 31774 | all | raw | 3115 | 1405 | 0.451043 | 0.441297 | -0.009746 | 0.009746 | 0.744183 | eligible |
| frequency | 2 | 31774 | all | scaled | 3115 | 1405 | 0.451043 | 0.441297 | -0.009746 | 0.009746 | 0.744183 | eligible |
| frequency | 2 | 31774 | unsupported | raw | 637 | 0 | 0.000000 | 0.441297 | 0.441297 | null | null | correct_below_20 |
| frequency | 2 | 31774 | unsupported | scaled | 637 | 0 | 0.000000 | 0.441297 | 0.441297 | null | null | correct_below_20 |
| frequency | 2 | 31774 | rare | raw | 0 | 0 | null | null | null | null | null | n_below_200, correct_below_20, incorrect_below_20 |
| frequency | 2 | 31774 | rare | scaled | 0 | 0 | null | null | null | null | null | n_below_200, correct_below_20, incorrect_below_20 |
| frequency | 2 | 31774 | frequent | raw | 2478 | 1405 | 0.566990 | 0.441297 | -0.125693 | 0.125693 | 0.613528 | eligible |
| frequency | 2 | 31774 | frequent | scaled | 2478 | 1405 | 0.566990 | 0.441297 | -0.125693 | 0.125693 | 0.613528 | eligible |
| frequency | 2 | 31774 | well_supported | raw | 2478 | 1405 | 0.566990 | 0.441297 | -0.125693 | 0.125693 | 0.613528 | eligible |
| frequency | 2 | 31774 | well_supported | scaled | 2478 | 1405 | 0.566990 | 0.441297 | -0.125693 | 0.125693 | 0.613528 | eligible |
| frequency | 2 | 33474 | all | raw | 1766 | 323 | 0.182899 | 0.441297 | 0.258398 | 0.258398 | 0.950089 | eligible |
| frequency | 2 | 33474 | all | scaled | 1766 | 323 | 0.182899 | 0.441297 | 0.258398 | 0.258398 | 0.950089 | eligible |
| frequency | 2 | 33474 | unsupported | raw | 683 | 0 | 0.000000 | 0.441297 | 0.441297 | null | null | correct_below_20 |
| frequency | 2 | 33474 | unsupported | scaled | 683 | 0 | 0.000000 | 0.441297 | 0.441297 | null | null | correct_below_20 |
| frequency | 2 | 33474 | rare | raw | 0 | 0 | null | null | null | null | null | n_below_200, correct_below_20, incorrect_below_20 |
| frequency | 2 | 33474 | rare | scaled | 0 | 0 | null | null | null | null | null | n_below_200, correct_below_20, incorrect_below_20 |
| frequency | 2 | 33474 | frequent | raw | 1083 | 323 | 0.298246 | 0.441297 | 0.143051 | 0.143051 | 0.759404 | eligible |
| frequency | 2 | 33474 | frequent | scaled | 1083 | 323 | 0.298246 | 0.441297 | 0.143051 | 0.143051 | 0.759404 | eligible |
| frequency | 2 | 33474 | well_supported | raw | 1083 | 323 | 0.298246 | 0.441297 | 0.143051 | 0.143051 | 0.759404 | eligible |
| frequency | 2 | 33474 | well_supported | scaled | 1083 | 323 | 0.298246 | 0.441297 | 0.143051 | 0.143051 | 0.759404 | eligible |
| frequency | 2 | 91695 | all | raw | 2610 | 1234 | 0.472797 | 0.441297 | -0.031500 | 0.031500 | 0.747236 | eligible |
| frequency | 2 | 91695 | all | scaled | 2610 | 1234 | 0.472797 | 0.441297 | -0.031500 | 0.031500 | 0.747236 | eligible |
| frequency | 2 | 91695 | unsupported | raw | 665 | 0 | 0.000000 | 0.441297 | 0.441297 | null | null | correct_below_20 |
| frequency | 2 | 91695 | unsupported | scaled | 665 | 0 | 0.000000 | 0.441297 | 0.441297 | null | null | correct_below_20 |
| frequency | 2 | 91695 | rare | raw | 0 | 0 | null | null | null | null | null | n_below_200, correct_below_20, incorrect_below_20 |
| frequency | 2 | 91695 | rare | scaled | 0 | 0 | null | null | null | null | null | n_below_200, correct_below_20, incorrect_below_20 |
| frequency | 2 | 91695 | frequent | raw | 1945 | 1234 | 0.634447 | 0.441297 | -0.193150 | 0.193150 | 0.574502 | eligible |
| frequency | 2 | 91695 | frequent | scaled | 1945 | 1234 | 0.634447 | 0.441297 | -0.193150 | 0.193150 | 0.574502 | eligible |
| frequency | 2 | 91695 | well_supported | raw | 1945 | 1234 | 0.634447 | 0.441297 | -0.193150 | 0.193150 | 0.574502 | eligible |
| frequency | 2 | 91695 | well_supported | scaled | 1945 | 1234 | 0.634447 | 0.441297 | -0.193150 | 0.193150 | 0.574502 | eligible |
| E011 | 3 | all | all | raw | 7091 | 3031 | 0.427443 | 0.656539 | 0.229096 | 0.239003 | 0.879738 | eligible |
| E011 | 3 | all | all | scaled | 7091 | 3031 | 0.427443 | 0.566779 | 0.139336 | 0.179996 | 0.854134 | eligible |
| E011 | 3 | all | unsupported | raw | 2162 | 0 | 0.000000 | 0.749680 | 0.749680 | null | null | correct_below_20 |
| E011 | 3 | all | unsupported | scaled | 2162 | 0 | 0.000000 | 0.662770 | 0.662770 | null | null | correct_below_20 |
| E011 | 3 | all | rare | raw | 0 | 0 | null | null | null | null | null | n_below_200, correct_below_20, incorrect_below_20 |
| E011 | 3 | all | rare | scaled | 0 | 0 | null | null | null | null | null | n_below_200, correct_below_20, incorrect_below_20 |
| E011 | 3 | all | frequent | raw | 4929 | 3031 | 0.614932 | 0.615685 | 0.000753 | 0.062855 | 0.557491 | eligible |
| E011 | 3 | all | frequent | scaled | 4929 | 3031 | 0.614932 | 0.524675 | -0.090258 | 0.123364 | 0.570983 | eligible |
| E011 | 3 | all | well_supported | raw | 4929 | 3031 | 0.614932 | 0.615685 | 0.000753 | 0.062855 | 0.557491 | eligible |
| E011 | 3 | all | well_supported | scaled | 4929 | 3031 | 0.614932 | 0.524675 | -0.090258 | 0.123364 | 0.570983 | eligible |
| E011 | 3 | 32833 | all | raw | 3105 | 1241 | 0.399678 | 0.685590 | 0.285912 | 0.384158 | 1.022635 | eligible |
| E011 | 3 | 32833 | all | scaled | 3105 | 1241 | 0.399678 | 0.607600 | 0.207922 | 0.398513 | 0.998184 | eligible |
| E011 | 3 | 32833 | unsupported | raw | 1124 | 0 | 0.000000 | 0.843462 | 0.843462 | null | null | correct_below_20 |
| E011 | 3 | 32833 | unsupported | scaled | 1124 | 0 | 0.000000 | 0.775978 | 0.775978 | null | null | correct_below_20 |
| E011 | 3 | 32833 | rare | raw | 0 | 0 | null | null | null | null | null | n_below_200, correct_below_20, incorrect_below_20 |
| E011 | 3 | 32833 | rare | scaled | 0 | 0 | null | null | null | null | null | n_below_200, correct_below_20, incorrect_below_20 |
| E011 | 3 | 32833 | frequent | raw | 1981 | 1241 | 0.626451 | 0.596014 | -0.030437 | 0.179595 | 0.612906 | eligible |
| E011 | 3 | 32833 | frequent | scaled | 1981 | 1241 | 0.626451 | 0.512065 | -0.114387 | 0.230690 | 0.632703 | eligible |
| E011 | 3 | 32833 | well_supported | raw | 1981 | 1241 | 0.626451 | 0.596014 | -0.030437 | 0.179595 | 0.612906 | eligible |
| E011 | 3 | 32833 | well_supported | scaled | 1981 | 1241 | 0.626451 | 0.512065 | -0.114387 | 0.230690 | 0.632703 | eligible |
| E011 | 3 | 33472 | all | raw | 2800 | 1336 | 0.477143 | 0.673671 | 0.196528 | 0.196528 | 0.745744 | eligible |
| E011 | 3 | 33472 | all | scaled | 2800 | 1336 | 0.477143 | 0.574975 | 0.097832 | 0.097832 | 0.716028 | eligible |
| E011 | 3 | 33472 | unsupported | raw | 652 | 0 | 0.000000 | 0.685483 | 0.685483 | null | null | correct_below_20 |
| E011 | 3 | 33472 | unsupported | scaled | 652 | 0 | 0.000000 | 0.578598 | 0.578598 | null | null | correct_below_20 |
| E011 | 3 | 33472 | rare | raw | 0 | 0 | null | null | null | null | null | n_below_200, correct_below_20, incorrect_below_20 |
| E011 | 3 | 33472 | rare | scaled | 0 | 0 | null | null | null | null | null | n_below_200, correct_below_20, incorrect_below_20 |
| E011 | 3 | 33472 | frequent | raw | 2148 | 1336 | 0.621974 | 0.670086 | 0.048112 | 0.050592 | 0.510244 | eligible |
| E011 | 3 | 33472 | frequent | scaled | 2148 | 1336 | 0.621974 | 0.573875 | -0.048099 | 0.049563 | 0.512191 | eligible |
| E011 | 3 | 33472 | well_supported | raw | 2148 | 1336 | 0.621974 | 0.670086 | 0.048112 | 0.050592 | 0.510244 | eligible |
| E011 | 3 | 33472 | well_supported | scaled | 2148 | 1336 | 0.621974 | 0.573875 | -0.048099 | 0.049563 | 0.512191 | eligible |
| E011 | 3 | 76870 | all | raw | 1186 | 454 | 0.382799 | 0.540038 | 0.157239 | 0.157583 | 0.821969 | eligible |
| E011 | 3 | 76870 | all | scaled | 1186 | 454 | 0.382799 | 0.440559 | 0.057759 | 0.072269 | 0.803060 | eligible |
| E011 | 3 | 76870 | unsupported | raw | 386 | 0 | 0.000000 | 0.585029 | 0.585029 | null | null | correct_below_20 |
| E011 | 3 | 76870 | unsupported | scaled | 386 | 0 | 0.000000 | 0.475298 | 0.475298 | null | null | correct_below_20 |
| E011 | 3 | 76870 | rare | raw | 0 | 0 | null | null | null | null | null | n_below_200, correct_below_20, incorrect_below_20 |
| E011 | 3 | 76870 | rare | scaled | 0 | 0 | null | null | null | null | null | n_below_200, correct_below_20, incorrect_below_20 |
| E011 | 3 | 76870 | frequent | raw | 800 | 454 | 0.567500 | 0.518330 | -0.049170 | 0.062901 | 0.547128 | eligible |
| E011 | 3 | 76870 | frequent | scaled | 800 | 454 | 0.567500 | 0.423797 | -0.143703 | 0.143703 | 0.576003 | eligible |
| E011 | 3 | 76870 | well_supported | raw | 800 | 454 | 0.567500 | 0.518330 | -0.049170 | 0.062901 | 0.547128 | eligible |
| E011 | 3 | 76870 | well_supported | scaled | 800 | 454 | 0.567500 | 0.423797 | -0.143703 | 0.143703 | 0.576003 | eligible |
| E012 | 3 | all | all | raw | 7091 | 2627 | 0.370470 | 0.024391 | -0.346079 | 0.346079 | 0.990482 | eligible |
| E012 | 3 | all | all | scaled | 7091 | 2627 | 0.370470 | 0.024398 | -0.346071 | 0.346071 | 0.990475 | eligible |
| E012 | 3 | all | unsupported | raw | 2162 | 0 | 0.000000 | 0.024391 | 0.024391 | null | null | correct_below_20 |
| E012 | 3 | all | unsupported | scaled | 2162 | 0 | 0.000000 | 0.024399 | 0.024399 | null | null | correct_below_20 |
| E012 | 3 | all | rare | raw | 0 | 0 | null | null | null | null | null | n_below_200, correct_below_20, incorrect_below_20 |
| E012 | 3 | all | rare | scaled | 0 | 0 | null | null | null | null | null | n_below_200, correct_below_20, incorrect_below_20 |
| E012 | 3 | all | frequent | raw | 4929 | 2627 | 0.532968 | 0.024391 | -0.508577 | 0.508577 | 0.975609 | eligible |
| E012 | 3 | all | frequent | scaled | 4929 | 2627 | 0.532968 | 0.024398 | -0.508570 | 0.508570 | 0.975598 | eligible |
| E012 | 3 | all | well_supported | raw | 4929 | 2627 | 0.532968 | 0.024391 | -0.508577 | 0.508577 | 0.975609 | eligible |
| E012 | 3 | all | well_supported | scaled | 4929 | 2627 | 0.532968 | 0.024398 | -0.508570 | 0.508570 | 0.975598 | eligible |
| E012 | 3 | 32833 | all | raw | 3105 | 1235 | 0.397746 | 0.024391 | -0.373355 | 0.373355 | 0.993268 | eligible |
| E012 | 3 | 32833 | all | scaled | 3105 | 1235 | 0.397746 | 0.024400 | -0.373346 | 0.373346 | 0.993259 | eligible |
| E012 | 3 | 32833 | unsupported | raw | 1124 | 0 | 0.000000 | 0.024391 | 0.024391 | null | null | correct_below_20 |
| E012 | 3 | 32833 | unsupported | scaled | 1124 | 0 | 0.000000 | 0.024400 | 0.024400 | null | null | correct_below_20 |
| E012 | 3 | 32833 | rare | raw | 0 | 0 | null | null | null | null | null | n_below_200, correct_below_20, incorrect_below_20 |
| E012 | 3 | 32833 | rare | scaled | 0 | 0 | null | null | null | null | null | n_below_200, correct_below_20, incorrect_below_20 |
| E012 | 3 | 32833 | frequent | raw | 1981 | 1235 | 0.623423 | 0.024391 | -0.599032 | 0.599032 | 0.975609 | eligible |
| E012 | 3 | 32833 | frequent | scaled | 1981 | 1235 | 0.623423 | 0.024399 | -0.599023 | 0.599023 | 0.975596 | eligible |
| E012 | 3 | 32833 | well_supported | raw | 1981 | 1235 | 0.623423 | 0.024391 | -0.599032 | 0.599032 | 0.975609 | eligible |
| E012 | 3 | 32833 | well_supported | scaled | 1981 | 1235 | 0.623423 | 0.024399 | -0.599023 | 0.599023 | 0.975596 | eligible |
| E012 | 3 | 33472 | all | raw | 2800 | 1026 | 0.366429 | 0.024391 | -0.342038 | 0.342038 | 0.986968 | eligible |
| E012 | 3 | 33472 | all | scaled | 2800 | 1026 | 0.366429 | 0.024398 | -0.342030 | 0.342030 | 0.986960 | eligible |
| E012 | 3 | 33472 | unsupported | raw | 652 | 0 | 0.000000 | 0.024391 | 0.024391 | null | null | correct_below_20 |
| E012 | 3 | 33472 | unsupported | scaled | 652 | 0 | 0.000000 | 0.024398 | 0.024398 | null | null | correct_below_20 |
| E012 | 3 | 33472 | rare | raw | 0 | 0 | null | null | null | null | null | n_below_200, correct_below_20, incorrect_below_20 |
| E012 | 3 | 33472 | rare | scaled | 0 | 0 | null | null | null | null | null | n_below_200, correct_below_20, incorrect_below_20 |
| E012 | 3 | 33472 | frequent | raw | 2148 | 1026 | 0.477654 | 0.024391 | -0.453263 | 0.453263 | 0.975609 | eligible |
| E012 | 3 | 33472 | frequent | scaled | 2148 | 1026 | 0.477654 | 0.024399 | -0.453255 | 0.453255 | 0.975599 | eligible |
| E012 | 3 | 33472 | well_supported | raw | 2148 | 1026 | 0.477654 | 0.024391 | -0.453263 | 0.453263 | 0.975609 | eligible |
| E012 | 3 | 33472 | well_supported | scaled | 2148 | 1026 | 0.477654 | 0.024399 | -0.453255 | 0.453255 | 0.975599 | eligible |
| E012 | 3 | 76870 | all | raw | 1186 | 366 | 0.308600 | 0.024390 | -0.284210 | 0.284210 | 0.991486 | eligible |
| E012 | 3 | 76870 | all | scaled | 1186 | 366 | 0.308600 | 0.024395 | -0.284205 | 0.284205 | 0.991482 | eligible |
| E012 | 3 | 76870 | unsupported | raw | 386 | 0 | 0.000000 | 0.024390 | 0.024390 | null | null | correct_below_20 |
| E012 | 3 | 76870 | unsupported | scaled | 386 | 0 | 0.000000 | 0.024395 | 0.024395 | null | null | correct_below_20 |
| E012 | 3 | 76870 | rare | raw | 0 | 0 | null | null | null | null | null | n_below_200, correct_below_20, incorrect_below_20 |
| E012 | 3 | 76870 | rare | scaled | 0 | 0 | null | null | null | null | null | n_below_200, correct_below_20, incorrect_below_20 |
| E012 | 3 | 76870 | frequent | raw | 800 | 366 | 0.457500 | 0.024390 | -0.433110 | 0.433110 | 0.975609 | eligible |
| E012 | 3 | 76870 | frequent | scaled | 800 | 366 | 0.457500 | 0.024395 | -0.433105 | 0.433105 | 0.975603 | eligible |
| E012 | 3 | 76870 | well_supported | raw | 800 | 366 | 0.457500 | 0.024390 | -0.433110 | 0.433110 | 0.975609 | eligible |
| E012 | 3 | 76870 | well_supported | scaled | 800 | 366 | 0.457500 | 0.024395 | -0.433105 | 0.433105 | 0.975603 | eligible |
| frequency | 3 | all | all | raw | 7091 | 2615 | 0.368777 | 0.417651 | 0.048873 | 0.048873 | 0.822135 | eligible |
| frequency | 3 | all | all | scaled | 7091 | 2615 | 0.368777 | 0.417651 | 0.048873 | 0.048873 | 0.822135 | eligible |
| frequency | 3 | all | unsupported | raw | 2162 | 0 | 0.000000 | 0.417651 | 0.417651 | null | null | correct_below_20 |
| frequency | 3 | all | unsupported | scaled | 2162 | 0 | 0.000000 | 0.417651 | 0.417651 | null | null | correct_below_20 |
| frequency | 3 | all | rare | raw | 0 | 0 | null | null | null | null | null | n_below_200, correct_below_20, incorrect_below_20 |
| frequency | 3 | all | rare | scaled | 0 | 0 | null | null | null | null | null | n_below_200, correct_below_20, incorrect_below_20 |
| frequency | 3 | all | frequent | raw | 4929 | 2615 | 0.530534 | 0.417651 | -0.112883 | 0.112883 | 0.641079 | eligible |
| frequency | 3 | all | frequent | scaled | 4929 | 2615 | 0.530534 | 0.417651 | -0.112883 | 0.112883 | 0.641079 | eligible |
| frequency | 3 | all | well_supported | raw | 4929 | 2615 | 0.530534 | 0.417651 | -0.112883 | 0.112883 | 0.641079 | eligible |
| frequency | 3 | all | well_supported | scaled | 4929 | 2615 | 0.530534 | 0.417651 | -0.112883 | 0.112883 | 0.641079 | eligible |
| frequency | 3 | 32833 | all | raw | 3105 | 1235 | 0.397746 | 0.417651 | 0.019905 | 0.019905 | 0.824189 | eligible |
| frequency | 3 | 32833 | all | scaled | 3105 | 1235 | 0.397746 | 0.417651 | 0.019905 | 0.019905 | 0.824189 | eligible |
| frequency | 3 | 32833 | unsupported | raw | 1124 | 0 | 0.000000 | 0.417651 | 0.417651 | null | null | correct_below_20 |
| frequency | 3 | 32833 | unsupported | scaled | 1124 | 0 | 0.000000 | 0.417651 | 0.417651 | null | null | correct_below_20 |
| frequency | 3 | 32833 | rare | raw | 0 | 0 | null | null | null | null | null | n_below_200, correct_below_20, incorrect_below_20 |
| frequency | 3 | 32833 | rare | scaled | 0 | 0 | null | null | null | null | null | n_below_200, correct_below_20, incorrect_below_20 |
| frequency | 3 | 32833 | frequent | raw | 1981 | 1235 | 0.623423 | 0.417651 | -0.205772 | 0.205772 | 0.591150 | eligible |
| frequency | 3 | 32833 | frequent | scaled | 1981 | 1235 | 0.623423 | 0.417651 | -0.205772 | 0.205772 | 0.591150 | eligible |
| frequency | 3 | 32833 | well_supported | raw | 1981 | 1235 | 0.623423 | 0.417651 | -0.205772 | 0.205772 | 0.591150 | eligible |
| frequency | 3 | 32833 | well_supported | scaled | 1981 | 1235 | 0.623423 | 0.417651 | -0.205772 | 0.205772 | 0.591150 | eligible |
| frequency | 3 | 33472 | all | raw | 2800 | 1014 | 0.362143 | 0.417651 | 0.055508 | 0.055508 | 0.806528 | eligible |
| frequency | 3 | 33472 | all | scaled | 2800 | 1014 | 0.362143 | 0.417651 | 0.055508 | 0.055508 | 0.806528 | eligible |
| frequency | 3 | 33472 | unsupported | raw | 652 | 0 | 0.000000 | 0.417651 | 0.417651 | null | null | correct_below_20 |
| frequency | 3 | 33472 | unsupported | scaled | 652 | 0 | 0.000000 | 0.417651 | 0.417651 | null | null | correct_below_20 |
| frequency | 3 | 33472 | rare | raw | 0 | 0 | null | null | null | null | null | n_below_200, correct_below_20, incorrect_below_20 |
| frequency | 3 | 33472 | rare | scaled | 0 | 0 | null | null | null | null | null | n_below_200, correct_below_20, incorrect_below_20 |
| frequency | 3 | 33472 | frequent | raw | 2148 | 1014 | 0.472067 | 0.417651 | -0.054416 | 0.054416 | 0.676497 | eligible |
| frequency | 3 | 33472 | frequent | scaled | 2148 | 1014 | 0.472067 | 0.417651 | -0.054416 | 0.054416 | 0.676497 | eligible |
| frequency | 3 | 33472 | well_supported | raw | 2148 | 1014 | 0.472067 | 0.417651 | -0.054416 | 0.054416 | 0.676497 | eligible |
| frequency | 3 | 33472 | well_supported | scaled | 2148 | 1014 | 0.472067 | 0.417651 | -0.054416 | 0.054416 | 0.676497 | eligible |
| frequency | 3 | 76870 | all | raw | 1186 | 366 | 0.308600 | 0.417651 | 0.109050 | 0.109050 | 0.853601 | eligible |
| frequency | 3 | 76870 | all | scaled | 1186 | 366 | 0.308600 | 0.417651 | 0.109050 | 0.109050 | 0.853601 | eligible |
| frequency | 3 | 76870 | unsupported | raw | 386 | 0 | 0.000000 | 0.417651 | 0.417651 | null | null | correct_below_20 |
| frequency | 3 | 76870 | unsupported | scaled | 386 | 0 | 0.000000 | 0.417651 | 0.417651 | null | null | correct_below_20 |
| frequency | 3 | 76870 | rare | raw | 0 | 0 | null | null | null | null | null | n_below_200, correct_below_20, incorrect_below_20 |
| frequency | 3 | 76870 | rare | scaled | 0 | 0 | null | null | null | null | null | n_below_200, correct_below_20, incorrect_below_20 |
| frequency | 3 | 76870 | frequent | raw | 800 | 366 | 0.457500 | 0.417651 | -0.039849 | 0.039849 | 0.669619 | eligible |
| frequency | 3 | 76870 | frequent | scaled | 800 | 366 | 0.457500 | 0.417651 | -0.039849 | 0.039849 | 0.669619 | eligible |
| frequency | 3 | 76870 | well_supported | raw | 800 | 366 | 0.457500 | 0.417651 | -0.039849 | 0.039849 | 0.669619 | eligible |
| frequency | 3 | 76870 | well_supported | scaled | 800 | 366 | 0.457500 | 0.417651 | -0.039849 | 0.039849 | 0.669619 | eligible |
| E011 | 4 | all | all | raw | 7405 | 2613 | 0.352870 | 0.444044 | 0.091174 | 0.091340 | 0.785929 | eligible |
| E011 | 4 | all | all | scaled | 7405 | 2613 | 0.352870 | 0.326304 | -0.026565 | 0.028603 | 0.785613 | eligible |
| E011 | 4 | all | unsupported | raw | 1588 | 0 | 0.000000 | 0.433797 | 0.433797 | null | null | correct_below_20 |
| E011 | 4 | all | unsupported | scaled | 1588 | 0 | 0.000000 | 0.321312 | 0.321312 | null | null | correct_below_20 |
| E011 | 4 | all | rare | raw | 0 | 0 | null | null | null | null | null | n_below_200, correct_below_20, incorrect_below_20 |
| E011 | 4 | all | rare | scaled | 0 | 0 | null | null | null | null | null | n_below_200, correct_below_20, incorrect_below_20 |
| E011 | 4 | all | frequent | raw | 5817 | 2613 | 0.449201 | 0.446841 | -0.002360 | 0.017006 | 0.649686 | eligible |
| E011 | 4 | all | frequent | scaled | 5817 | 2613 | 0.449201 | 0.327667 | -0.121533 | 0.121598 | 0.679454 | eligible |
| E011 | 4 | all | well_supported | raw | 5722 | 2613 | 0.456659 | 0.445418 | -0.011240 | 0.015932 | 0.638665 | eligible |
| E011 | 4 | all | well_supported | scaled | 5722 | 2613 | 0.456659 | 0.326646 | -0.130013 | 0.130013 | 0.671706 | eligible |
| E011 | 4 | 31777 | all | raw | 2809 | 1655 | 0.589178 | 0.492702 | -0.096476 | 0.099441 | 0.593601 | eligible |
| E011 | 4 | 31777 | all | scaled | 2809 | 1655 | 0.589178 | 0.359608 | -0.229570 | 0.231549 | 0.645083 | eligible |
| E011 | 4 | 31777 | unsupported | raw | 314 | 0 | 0.000000 | 0.482507 | 0.482507 | null | null | correct_below_20 |
| E011 | 4 | 31777 | unsupported | scaled | 314 | 0 | 0.000000 | 0.348722 | 0.348722 | null | null | correct_below_20 |
| E011 | 4 | 31777 | rare | raw | 0 | 0 | null | null | null | null | null | n_below_200, correct_below_20, incorrect_below_20 |
| E011 | 4 | 31777 | rare | scaled | 0 | 0 | null | null | null | null | null | n_below_200, correct_below_20, incorrect_below_20 |
| E011 | 4 | 31777 | frequent | raw | 2495 | 1655 | 0.663327 | 0.493985 | -0.169342 | 0.169730 | 0.503394 | eligible |
| E011 | 4 | 31777 | frequent | scaled | 2495 | 1655 | 0.663327 | 0.360978 | -0.302349 | 0.302656 | 0.577696 | eligible |
| E011 | 4 | 31777 | well_supported | raw | 2419 | 1655 | 0.684167 | 0.492565 | -0.191602 | 0.192001 | 0.477878 | eligible |
| E011 | 4 | 31777 | well_supported | scaled | 2419 | 1655 | 0.684167 | 0.359954 | -0.324213 | 0.324374 | 0.559861 | eligible |
| E011 | 4 | 33471 | all | raw | 1542 | 216 | 0.140078 | 0.475631 | 0.335553 | 0.336370 | 1.008247 | eligible |
| E011 | 4 | 33471 | all | scaled | 1542 | 216 | 0.140078 | 0.342250 | 0.202172 | 0.202669 | 0.934733 | eligible |
| E011 | 4 | 33471 | unsupported | raw | 418 | 0 | 0.000000 | 0.536954 | 0.536954 | null | null | correct_below_20 |
| E011 | 4 | 33471 | unsupported | scaled | 418 | 0 | 0.000000 | 0.394131 | 0.394131 | null | null | correct_below_20 |
| E011 | 4 | 33471 | rare | raw | 0 | 0 | null | null | null | null | null | n_below_200, correct_below_20, incorrect_below_20 |
| E011 | 4 | 33471 | rare | scaled | 0 | 0 | null | null | null | null | null | n_below_200, correct_below_20, incorrect_below_20 |
| E011 | 4 | 33471 | frequent | raw | 1124 | 216 | 0.192171 | 0.452825 | 0.260654 | 0.262296 | 0.877281 | eligible |
| E011 | 4 | 33471 | frequent | scaled | 1124 | 216 | 0.192171 | 0.322956 | 0.130786 | 0.145550 | 0.831052 | eligible |
| E011 | 4 | 33471 | well_supported | raw | 1105 | 216 | 0.195475 | 0.451910 | 0.256435 | 0.258104 | 0.869922 | eligible |
| E011 | 4 | 33471 | well_supported | scaled | 1105 | 216 | 0.195475 | 0.322118 | 0.126643 | 0.144763 | 0.825586 | eligible |
| E011 | 4 | 89443 | all | raw | 3054 | 742 | 0.242960 | 0.383341 | 0.140381 | 0.140784 | 0.850576 | eligible |
| E011 | 4 | 89443 | all | scaled | 3054 | 742 | 0.242960 | 0.287621 | 0.044661 | 0.044661 | 0.839577 | eligible |
| E011 | 4 | 89443 | unsupported | raw | 856 | 0 | 0.000000 | 0.365556 | 0.365556 | null | null | correct_below_20 |
| E011 | 4 | 89443 | unsupported | scaled | 856 | 0 | 0.000000 | 0.275698 | 0.275698 | null | null | correct_below_20 |
| E011 | 4 | 89443 | rare | raw | 0 | 0 | null | null | null | null | null | n_below_200, correct_below_20, incorrect_below_20 |
| E011 | 4 | 89443 | rare | scaled | 0 | 0 | null | null | null | null | null | n_below_200, correct_below_20, incorrect_below_20 |
| E011 | 4 | 89443 | frequent | raw | 2198 | 742 | 0.337580 | 0.390267 | 0.052687 | 0.068242 | 0.699359 | eligible |
| E011 | 4 | 89443 | frequent | scaled | 2198 | 742 | 0.337580 | 0.292264 | -0.045316 | 0.047746 | 0.717438 | eligible |
| E011 | 4 | 89443 | well_supported | raw | 2198 | 742 | 0.337580 | 0.390267 | 0.052687 | 0.068242 | 0.699359 | eligible |
| E011 | 4 | 89443 | well_supported | scaled | 2198 | 742 | 0.337580 | 0.292264 | -0.045316 | 0.047746 | 0.717438 | eligible |
| E012 | 4 | all | all | raw | 7405 | 2970 | 0.401080 | 0.023810 | -0.377271 | 0.377271 | 0.986402 | eligible |
| E012 | 4 | all | all | scaled | 7405 | 2970 | 0.401080 | 0.023815 | -0.377265 | 0.377265 | 0.986396 | eligible |
| E012 | 4 | all | unsupported | raw | 1588 | 0 | 0.000000 | 0.023810 | 0.023810 | null | null | correct_below_20 |
| E012 | 4 | all | unsupported | scaled | 1588 | 0 | 0.000000 | 0.023815 | 0.023815 | null | null | correct_below_20 |
| E012 | 4 | all | rare | raw | 0 | 0 | null | null | null | null | null | n_below_200, correct_below_20, incorrect_below_20 |
| E012 | 4 | all | rare | scaled | 0 | 0 | null | null | null | null | null | n_below_200, correct_below_20, incorrect_below_20 |
| E012 | 4 | all | frequent | raw | 5817 | 2970 | 0.510572 | 0.023810 | -0.486763 | 0.486763 | 0.976190 | eligible |
| E012 | 4 | all | frequent | scaled | 5817 | 2970 | 0.510572 | 0.023815 | -0.486757 | 0.486757 | 0.976183 | eligible |
| E012 | 4 | all | well_supported | raw | 5722 | 2970 | 0.519049 | 0.023810 | -0.495239 | 0.495239 | 0.976190 | eligible |
| E012 | 4 | all | well_supported | scaled | 5722 | 2970 | 0.519049 | 0.023815 | -0.495234 | 0.495234 | 0.976183 | eligible |
| E012 | 4 | 31777 | all | raw | 2809 | 1628 | 0.579566 | 0.023810 | -0.555756 | 0.555756 | 0.981513 | eligible |
| E012 | 4 | 31777 | all | scaled | 2809 | 1628 | 0.579566 | 0.023816 | -0.555750 | 0.555750 | 0.981504 | eligible |
| E012 | 4 | 31777 | unsupported | raw | 314 | 0 | 0.000000 | 0.023810 | 0.023810 | null | null | correct_below_20 |
| E012 | 4 | 31777 | unsupported | scaled | 314 | 0 | 0.000000 | 0.023816 | 0.023816 | null | null | correct_below_20 |
| E012 | 4 | 31777 | rare | raw | 0 | 0 | null | null | null | null | null | n_below_200, correct_below_20, incorrect_below_20 |
| E012 | 4 | 31777 | rare | scaled | 0 | 0 | null | null | null | null | null | n_below_200, correct_below_20, incorrect_below_20 |
| E012 | 4 | 31777 | frequent | raw | 2495 | 1628 | 0.652505 | 0.023810 | -0.628695 | 0.628695 | 0.976190 | eligible |
| E012 | 4 | 31777 | frequent | scaled | 2495 | 1628 | 0.652505 | 0.023816 | -0.628689 | 0.628689 | 0.976180 | eligible |
| E012 | 4 | 31777 | well_supported | raw | 2419 | 1628 | 0.673005 | 0.023810 | -0.649196 | 0.649196 | 0.976190 | eligible |
| E012 | 4 | 31777 | well_supported | scaled | 2419 | 1628 | 0.673005 | 0.023816 | -0.649189 | 0.649189 | 0.976180 | eligible |
| E012 | 4 | 33471 | all | raw | 1542 | 701 | 0.454604 | 0.023810 | -0.430795 | 0.430795 | 0.989099 | eligible |
| E012 | 4 | 33471 | all | scaled | 1542 | 701 | 0.454604 | 0.023815 | -0.430790 | 0.430790 | 0.989093 | eligible |
| E012 | 4 | 33471 | unsupported | raw | 418 | 0 | 0.000000 | 0.023810 | 0.023810 | null | null | correct_below_20 |
| E012 | 4 | 33471 | unsupported | scaled | 418 | 0 | 0.000000 | 0.023815 | 0.023815 | null | null | correct_below_20 |
| E012 | 4 | 33471 | rare | raw | 0 | 0 | null | null | null | null | null | n_below_200, correct_below_20, incorrect_below_20 |
| E012 | 4 | 33471 | rare | scaled | 0 | 0 | null | null | null | null | null | n_below_200, correct_below_20, incorrect_below_20 |
| E012 | 4 | 33471 | frequent | raw | 1124 | 701 | 0.623665 | 0.023810 | -0.599856 | 0.599856 | 0.976190 | eligible |
| E012 | 4 | 33471 | frequent | scaled | 1124 | 701 | 0.623665 | 0.023815 | -0.599851 | 0.599851 | 0.976183 | eligible |
| E012 | 4 | 33471 | well_supported | raw | 1105 | 701 | 0.634389 | 0.023810 | -0.610579 | 0.610579 | 0.976190 | eligible |
| E012 | 4 | 33471 | well_supported | scaled | 1105 | 701 | 0.634389 | 0.023815 | -0.610575 | 0.610575 | 0.976183 | eligible |
| E012 | 4 | 89443 | all | raw | 3054 | 641 | 0.209889 | 0.023810 | -0.186079 | 0.186079 | 0.989537 | eligible |
| E012 | 4 | 89443 | all | scaled | 3054 | 641 | 0.209889 | 0.023815 | -0.186074 | 0.186074 | 0.989534 | eligible |
| E012 | 4 | 89443 | unsupported | raw | 856 | 0 | 0.000000 | 0.023810 | 0.023810 | null | null | correct_below_20 |
| E012 | 4 | 89443 | unsupported | scaled | 856 | 0 | 0.000000 | 0.023815 | 0.023815 | null | null | correct_below_20 |
| E012 | 4 | 89443 | rare | raw | 0 | 0 | null | null | null | null | null | n_below_200, correct_below_20, incorrect_below_20 |
| E012 | 4 | 89443 | rare | scaled | 0 | 0 | null | null | null | null | null | n_below_200, correct_below_20, incorrect_below_20 |
| E012 | 4 | 89443 | frequent | raw | 2198 | 641 | 0.291629 | 0.023810 | -0.267819 | 0.267819 | 0.976190 | eligible |
| E012 | 4 | 89443 | frequent | scaled | 2198 | 641 | 0.291629 | 0.023815 | -0.267814 | 0.267814 | 0.976185 | eligible |
| E012 | 4 | 89443 | well_supported | raw | 2198 | 641 | 0.291629 | 0.023810 | -0.267819 | 0.267819 | 0.976190 | eligible |
| E012 | 4 | 89443 | well_supported | scaled | 2198 | 641 | 0.291629 | 0.023815 | -0.267814 | 0.267814 | 0.976185 | eligible |
| frequency | 4 | all | all | raw | 7405 | 2970 | 0.401080 | 0.419183 | 0.018103 | 0.018103 | 0.779983 | eligible |
| frequency | 4 | all | all | scaled | 7405 | 2970 | 0.401080 | 0.419183 | 0.018103 | 0.018103 | 0.779983 | eligible |
| frequency | 4 | all | unsupported | raw | 1588 | 0 | 0.000000 | 0.419183 | 0.419183 | null | null | correct_below_20 |
| frequency | 4 | all | unsupported | scaled | 1588 | 0 | 0.000000 | 0.419183 | 0.419183 | null | null | correct_below_20 |
| frequency | 4 | all | rare | raw | 0 | 0 | null | null | null | null | null | n_below_200, correct_below_20, incorrect_below_20 |
| frequency | 4 | all | rare | scaled | 0 | 0 | null | null | null | null | null | n_below_200, correct_below_20, incorrect_below_20 |
| frequency | 4 | all | frequent | raw | 5817 | 2970 | 0.510572 | 0.419183 | -0.091389 | 0.091389 | 0.657173 | eligible |
| frequency | 4 | all | frequent | scaled | 5817 | 2970 | 0.510572 | 0.419183 | -0.091389 | 0.091389 | 0.657173 | eligible |
| frequency | 4 | all | well_supported | raw | 5722 | 2970 | 0.519049 | 0.419183 | -0.099866 | 0.099866 | 0.649938 | eligible |
| frequency | 4 | all | well_supported | scaled | 5722 | 2970 | 0.519049 | 0.419183 | -0.099866 | 0.099866 | 0.649938 | eligible |
| frequency | 4 | 31777 | all | raw | 2809 | 1628 | 0.579566 | 0.419183 | -0.160382 | 0.160382 | 0.656059 | eligible |
| frequency | 4 | 31777 | all | scaled | 2809 | 1628 | 0.579566 | 0.419183 | -0.160382 | 0.160382 | 0.656059 | eligible |
| frequency | 4 | 31777 | unsupported | raw | 314 | 0 | 0.000000 | 0.419183 | 0.419183 | null | null | correct_below_20 |
| frequency | 4 | 31777 | unsupported | scaled | 314 | 0 | 0.000000 | 0.419183 | 0.419183 | null | null | correct_below_20 |
| frequency | 4 | 31777 | rare | raw | 0 | 0 | null | null | null | null | null | n_below_200, correct_below_20, incorrect_below_20 |
| frequency | 4 | 31777 | rare | scaled | 0 | 0 | null | null | null | null | null | n_below_200, correct_below_20, incorrect_below_20 |
| frequency | 4 | 31777 | frequent | raw | 2495 | 1628 | 0.652505 | 0.419183 | -0.233322 | 0.233322 | 0.583847 | eligible |
| frequency | 4 | 31777 | frequent | scaled | 2495 | 1628 | 0.652505 | 0.419183 | -0.233322 | 0.233322 | 0.583847 | eligible |
| frequency | 4 | 31777 | well_supported | raw | 2419 | 1628 | 0.673005 | 0.419183 | -0.253822 | 0.253822 | 0.567852 | eligible |
| frequency | 4 | 31777 | well_supported | scaled | 2419 | 1628 | 0.673005 | 0.419183 | -0.253822 | 0.253822 | 0.567852 | eligible |
| frequency | 4 | 33471 | all | raw | 1542 | 701 | 0.454604 | 0.419183 | -0.035421 | 0.035421 | 0.770777 | eligible |
| frequency | 4 | 33471 | all | scaled | 1542 | 701 | 0.454604 | 0.419183 | -0.035421 | 0.035421 | 0.770777 | eligible |
| frequency | 4 | 33471 | unsupported | raw | 418 | 0 | 0.000000 | 0.419183 | 0.419183 | null | null | correct_below_20 |
| frequency | 4 | 33471 | unsupported | scaled | 418 | 0 | 0.000000 | 0.419183 | 0.419183 | null | null | correct_below_20 |
| frequency | 4 | 33471 | rare | raw | 0 | 0 | null | null | null | null | null | n_below_200, correct_below_20, incorrect_below_20 |
| frequency | 4 | 33471 | rare | scaled | 0 | 0 | null | null | null | null | null | n_below_200, correct_below_20, incorrect_below_20 |
| frequency | 4 | 33471 | frequent | raw | 1124 | 701 | 0.623665 | 0.419183 | -0.204482 | 0.204482 | 0.600056 | eligible |
| frequency | 4 | 33471 | frequent | scaled | 1124 | 701 | 0.623665 | 0.419183 | -0.204482 | 0.204482 | 0.600056 | eligible |
| frequency | 4 | 33471 | well_supported | raw | 1105 | 701 | 0.634389 | 0.419183 | -0.215206 | 0.215206 | 0.591581 | eligible |
| frequency | 4 | 33471 | well_supported | scaled | 1105 | 701 | 0.634389 | 0.419183 | -0.215206 | 0.215206 | 0.591581 | eligible |
| frequency | 4 | 89443 | all | raw | 3054 | 641 | 0.209889 | 0.419183 | 0.209295 | 0.209295 | 0.898613 | eligible |
| frequency | 4 | 89443 | all | scaled | 3054 | 641 | 0.209889 | 0.419183 | 0.209295 | 0.209295 | 0.898613 | eligible |
| frequency | 4 | 89443 | unsupported | raw | 856 | 0 | 0.000000 | 0.419183 | 0.419183 | null | null | correct_below_20 |
| frequency | 4 | 89443 | unsupported | scaled | 856 | 0 | 0.000000 | 0.419183 | 0.419183 | null | null | correct_below_20 |
| frequency | 4 | 89443 | rare | raw | 0 | 0 | null | null | null | null | null | n_below_200, correct_below_20, incorrect_below_20 |
| frequency | 4 | 89443 | rare | scaled | 0 | 0 | null | null | null | null | null | n_below_200, correct_below_20, incorrect_below_20 |
| frequency | 4 | 89443 | frequent | raw | 2198 | 641 | 0.291629 | 0.419183 | 0.127554 | 0.127554 | 0.769616 | eligible |
| frequency | 4 | 89443 | frequent | scaled | 2198 | 641 | 0.291629 | 0.419183 | 0.127554 | 0.127554 | 0.769616 | eligible |
| frequency | 4 | 89443 | well_supported | raw | 2198 | 641 | 0.291629 | 0.419183 | 0.127554 | 0.127554 | 0.769616 | eligible |
| frequency | 4 | 89443 | well_supported | scaled | 2198 | 641 | 0.291629 | 0.419183 | 0.127554 | 0.127554 | 0.769616 | eligible |

## Probability scale diagnostics

| Model | Fold | Temperature | Supported calibration n | Lower boundary | Upper boundary | Raw floor fraction | Top1 changes | Top3 changes |
|---|---|---|---|---|---|---|---|---|
| E011 | 0 | 0.991756 | 5259 | False | False | 0.000000 | 0.000000 | 0.000000 |
| E012 | 0 | 0.049787 | 5259 | True | False | 0.000000 | 0.000000 | 0.000000 |
| E011 | 1 | 0.944212 | 4726 | False | False | 0.000000 | 0.000000 | 0.000000 |
| E012 | 1 | 0.049787 | 4726 | True | False | 0.000000 | 0.000000 | 0.000000 |
| E011 | 2 | 1.529918 | 7973 | False | False | 0.000000 | 0.000000 | 0.000000 |
| E012 | 2 | 0.049787 | 7973 | True | False | 0.000000 | 0.000000 | 0.000000 |
| E011 | 3 | 1.192891 | 7640 | False | False | 0.000000 | 0.000000 | 0.000000 |
| E012 | 3 | 0.049787 | 7640 | True | False | 0.000000 | 0.000000 | 0.000000 |
| E011 | 4 | 1.293799 | 6881 | False | False | 0.000000 | 0.000000 | 0.000000 |
| E012 | 4 | 0.049787 | 6881 | True | False | 0.000000 | 0.000000 | 0.000000 |

## Permutation opportunity

| Fold | Question | Condition | n | Cells | Singleton rows | Movable rows | Label mixed rows | Label mixed share | Donor changes mean | Donor changes SD | Input changes mean | Input changes SD |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 0 | all | explanation_shuffle | 7686 | 12 | 0 | 7686 | 7686 | 1.000000 | 7673.420000 | 3.364040 | 7672.350000 | 3.456439 |
| 0 | 31772 | explanation_shuffle | 4857 | 4 | 0 | 4857 | 4857 | 1.000000 | 4852.630000 | 1.910392 | 4852.410000 | 1.891475 |
| 0 | 32829 | explanation_shuffle | 2156 | 4 | 0 | 2156 | 2156 | 1.000000 | 2151.700000 | 2.115360 | 2151.020000 | 2.210992 |
| 0 | 104665 | explanation_shuffle | 673 | 4 | 0 | 673 | 673 | 1.000000 | 669.090000 | 1.853716 | 668.920000 | 1.873149 |
| 0 | all | pair_shuffle | 7686 | 3 | 0 | 7686 | 7686 | 1.000000 | 7682.860000 | 1.775365 | 7682.290000 | 1.892543 |
| 0 | 31772 | pair_shuffle | 4857 | 1 | 0 | 4857 | 4857 | 1.000000 | 4855.980000 | 0.920913 | 4855.920000 | 0.950066 |
| 0 | 32829 | pair_shuffle | 2156 | 1 | 0 | 2156 | 2156 | 1.000000 | 2154.960000 | 1.109372 | 2154.520000 | 1.184752 |
| 0 | 104665 | pair_shuffle | 673 | 1 | 0 | 673 | 673 | 1.000000 | 671.920000 | 0.960640 | 671.850000 | 0.957427 |
| 1 | all | explanation_shuffle | 7023 | 12 | 0 | 7023 | 7023 | 1.000000 | 7010.570000 | 3.522668 | 7009.660000 | 3.513955 |
| 1 | 31778 | explanation_shuffle | 3640 | 4 | 0 | 3640 | 3640 | 1.000000 | 3635.990000 | 2.081642 | 3635.810000 | 2.135297 |
| 1 | 32835 | explanation_shuffle | 2332 | 4 | 0 | 2332 | 2332 | 1.000000 | 2327.910000 | 1.995424 | 2327.180000 | 2.016998 |
| 1 | 109465 | explanation_shuffle | 1051 | 4 | 0 | 1051 | 1051 | 1.000000 | 1046.670000 | 2.165174 | 1046.670000 | 2.165174 |
| 1 | all | pair_shuffle | 7023 | 3 | 0 | 7023 | 7023 | 1.000000 | 7020.160000 | 1.580947 | 7019.960000 | 1.620076 |
| 1 | 31778 | pair_shuffle | 3640 | 1 | 0 | 3640 | 3640 | 1.000000 | 3639.080000 | 0.960640 | 3639.020000 | 0.984527 |
| 1 | 32835 | pair_shuffle | 2332 | 1 | 0 | 2332 | 2332 | 1.000000 | 2331.130000 | 0.970837 | 2331.010000 | 1.019952 |
| 1 | 109465 | pair_shuffle | 1051 | 1 | 0 | 1051 | 1051 | 1.000000 | 1049.950000 | 1.113508 | 1049.930000 | 1.112418 |
| 2 | all | explanation_shuffle | 7491 | 12 | 0 | 7491 | 7491 | 1.000000 | 7478.640000 | 3.780653 | 7478.070000 | 3.859280 |
| 2 | 31774 | explanation_shuffle | 3115 | 4 | 0 | 3115 | 3115 | 1.000000 | 3111.110000 | 1.722665 | 3110.980000 | 1.797754 |
| 2 | 33474 | explanation_shuffle | 1766 | 4 | 0 | 1766 | 1766 | 1.000000 | 1761.590000 | 2.122962 | 1761.540000 | 2.124508 |
| 2 | 91695 | explanation_shuffle | 2610 | 4 | 0 | 2610 | 2610 | 1.000000 | 2605.940000 | 2.164078 | 2605.550000 | 2.289083 |
| 2 | all | pair_shuffle | 7491 | 3 | 0 | 7491 | 7491 | 1.000000 | 7487.940000 | 1.668605 | 7487.710000 | 1.653249 |
| 2 | 31774 | pair_shuffle | 3115 | 1 | 0 | 3115 | 3115 | 1.000000 | 3114.010000 | 0.989796 | 3113.960000 | 0.983911 |
| 2 | 33474 | pair_shuffle | 1766 | 1 | 0 | 1766 | 1766 | 1.000000 | 1764.880000 | 1.047170 | 1764.860000 | 1.054284 |
| 2 | 91695 | pair_shuffle | 2610 | 1 | 0 | 2610 | 2610 | 1.000000 | 2609.050000 | 0.967920 | 2608.890000 | 0.973331 |
| 3 | all | explanation_shuffle | 7091 | 12 | 0 | 7091 | 7091 | 1.000000 | 7079.260000 | 3.365361 | 7078.760000 | 3.354840 |
| 3 | 32833 | explanation_shuffle | 3105 | 4 | 0 | 3105 | 3105 | 1.000000 | 3100.960000 | 1.847302 | 3100.720000 | 1.842703 |
| 3 | 33472 | explanation_shuffle | 2800 | 4 | 0 | 2800 | 2800 | 1.000000 | 2796.010000 | 1.997448 | 2795.890000 | 1.999470 |
| 3 | 76870 | explanation_shuffle | 1186 | 4 | 0 | 1186 | 1186 | 1.000000 | 1182.290000 | 1.955541 | 1182.150000 | 1.961112 |
| 3 | all | pair_shuffle | 7091 | 3 | 0 | 7091 | 7091 | 1.000000 | 7087.890000 | 1.569244 | 7087.820000 | 1.597852 |
| 3 | 32833 | pair_shuffle | 3105 | 1 | 0 | 3105 | 3105 | 1.000000 | 3103.920000 | 0.971097 | 3103.890000 | 0.983654 |
| 3 | 33472 | pair_shuffle | 2800 | 1 | 0 | 2800 | 2800 | 1.000000 | 2799.100000 | 1.010051 | 2799.080000 | 1.011849 |
| 3 | 76870 | pair_shuffle | 1186 | 1 | 0 | 1186 | 1186 | 1.000000 | 1184.870000 | 1.021536 | 1184.850000 | 1.018763 |
| 4 | all | explanation_shuffle | 7405 | 12 | 0 | 7405 | 7405 | 1.000000 | 7393.560000 | 3.153706 | 7392.930000 | 3.361262 |
| 4 | 31777 | explanation_shuffle | 2809 | 4 | 0 | 2809 | 2809 | 1.000000 | 2804.920000 | 1.993322 | 2804.690000 | 2.013565 |
| 4 | 33471 | explanation_shuffle | 1542 | 4 | 0 | 1542 | 1542 | 1.000000 | 1538.320000 | 1.863417 | 1538.240000 | 1.912849 |
| 4 | 89443 | explanation_shuffle | 3054 | 4 | 0 | 3054 | 3054 | 1.000000 | 3050.320000 | 1.884975 | 3050.000000 | 1.954017 |
| 4 | all | pair_shuffle | 7405 | 3 | 0 | 7405 | 7405 | 1.000000 | 7402.090000 | 1.729687 | 7401.860000 | 1.885725 |
| 4 | 31777 | pair_shuffle | 2809 | 1 | 0 | 2809 | 2809 | 1.000000 | 2808.090000 | 0.865675 | 2807.940000 | 1.013246 |
| 4 | 33471 | pair_shuffle | 1542 | 1 | 0 | 1542 | 1542 | 1.000000 | 1540.910000 | 1.101835 | 1540.880000 | 1.130656 |
| 4 | 89443 | pair_shuffle | 3054 | 1 | 0 | 3054 | 3054 | 1.000000 | 3053.090000 | 0.877266 | 3053.040000 | 0.909212 |

Full replicate-level aggregates and all descriptive dispersion values are retained in [the aggregate artifact](../results/E013_aggregates.json). No row-level predictions or donor assignments are included.
