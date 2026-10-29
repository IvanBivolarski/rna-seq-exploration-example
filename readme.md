# Exploratory RNA-seq heterogeneity analysis with sensitivity analysis

A lightweight, reproducible Python workflow for exploring transcriptomic
heterogeneity in a small RNA sequencing dataset and for examining the influence
of a single divergent sample.

The workflow is demonstrated on **synthetic** gene-level expression data for
seven specimens. It combines principal component analysis (PCA), pairwise
Pearson correlations, and hierarchical clustering, and then repeats the
analysis after omitting the divergent sample `PC_345813A`.

The intended contribution is methodological: a transparent example of how
sample influence can be examined and documented before biological
interpretations are assigned.

## Scope

This is an exploratory, descriptive workflow. It does **not** perform:

- differential expression testing,
- batch correction,
- biological validation,
- clinical outcome prediction.

All data in this repository are synthetic and are provided only to demonstrate
the workflow.

## Repository structure
