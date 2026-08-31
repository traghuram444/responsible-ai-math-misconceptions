# E003 preregistration — support-stratified reproduction of E001

**Status:** completed 2026-08-31.

E002 found that 21.1% of held-out rows use a combined label unavailable to the fold-local training classifier. E003 therefore reproduces both grouped E001 baseline variants without changing folds, input, grid, calibration, or primary metric. It reports the original all-row evaluation first, then a secondary subset restricted to labels represented in the fold-local train classes.

The hypothesis is that scores improve on the supported subset but the TF–IDF baseline still does not reverse the all-row E001 decision. This is a diagnostic of closed-set label support, not permission to exclude unsupported labels from the primary conclusion. Outputs are aggregate-only; no predictions, text, or row-level memberships are written.
