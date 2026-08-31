# E003 results — support-stratified E001 reproduction

**Status:** completed 2026-08-31; aggregate-only output SHA-256 `e6abcc46affe10545c4d4f1620d0fd153017b7cc97a0db4698de70dee9ecf64f`.

The primary all-row question-held-out results exactly reproduce E001: question-plus-explanation TF–IDF + logistic regression has MAP@3 0.520 versus 0.539 for frequency.

On the preregistered secondary subset whose labels occur in fold-local training, mean MAP@3 was 0.668 for TF–IDF versus 0.689 for frequency; top-1 accuracy was 0.483 versus 0.512. Explanation-only results were likewise lower for TF–IDF (0.640) than frequency (0.689) on MAP@3.

Thus unavailable labels explain part of the task difficulty but do not reverse E001's negative lexical-baseline conclusion. The subset is diagnostic only and does not replace the full primary score. E004 should move to a small, licensed semantic-embedding baseline only after a fresh preregistration and literature/license check.
