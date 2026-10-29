"""
pca_analysis.py

Exploratory PCA of a small RNA-seq expression matrix, with a targeted
sensitivity analysis omitting the divergent sample PC_345813A.

Input
-----
CSV expression matrix:
  - rows    = genes
  - columns = samples (including PC_345813A)
  - values  = normalized, non-negative, unlogged expression values

Output
------
  - pca_explained_variance.csv
  - pca_scores_full_dataset.csv
  - pca_scores_without_PC_345813A.csv
"""

from __future__ import annotations

import argparse
from pathlib import Path

import numpy as np
import pandas as pd
from sklearn.decomposition import PCA

DIVERGENT_SAMPLE = "PC_345813A"
VARIANCE_EPS = 1e-12


def load_expression_matrix(path: Path) -> pd.DataFrame:
    """Load and validate the expression matrix."""
    expression = pd.read_csv(path, index_col=0)

    if expression.empty:
        raise ValueError("Expression matrix is empty.")

    if DIVERGENT_SAMPLE not in expression.columns:
        raise KeyError(
            f"Divergent sample '{DIVERGENT_SAMPLE}' not found in expression matrix."
        )

    values = expression.to_numpy()
    if not np.isfinite(values).all():
        raise ValueError("Expression matrix contains non-finite values.")
    if (values < 0).any():
        raise ValueError("Expression matrix contains negative values.")

    return expression


def log_transform(expression: pd.DataFrame) -> pd.DataFrame:
    """Apply log2(x + 1) to normalized, non-negative expression values."""
    return np.log2(expression + 1)


def select_variable_genes(
    full: pd.DataFrame,
    reduced: pd.DataFrame,
    eps: float = VARIANCE_EPS,
) -> tuple[pd.DataFrame, pd.DataFrame]:
    """Keep genes with non-zero variance in both analyses."""
    keep = (full.var(axis=1) > eps) & (reduced.var(axis=1) > eps)
    return full.loc[keep], reduced.loc[keep]


def run_pca(matrix: pd.DataFrame, label: str, n_components: int = 2) -> tuple[pd.DataFrame, pd.DataFrame]:
    """Run PCA on samples (rows) and return scores and variance table."""
    pca = PCA(n_components=n_components, svd_solver="full", random_state=0)
    scores_array = pca.fit_transform(matrix.T)

    scores = pd.DataFrame(
        scores_array,
        index=matrix.columns,
        columns=[f"PC{i + 1}" for i in range(n_components)],
    )
    scores.index.name = "sample"

    variance = pd.DataFrame(
        {
            "analysis": label,
            "component": [f"PC{i + 1}" for i in range(n_components)],
            "explained_variance_ratio": pca.explained_variance_ratio_,
        }
    )

    return scores, variance


def main(input_csv: Path, output_dir: Path) -> None:
    output_dir.mkdir(parents=True, exist_ok=True)

    expression = load_expression_matrix(input_csv)
    log_expression = log_transform(expression)
    reduced = log_expression.drop(columns=DIVERGENT_SAMPLE)

    full_keep, reduced_keep = select_variable_genes(log_expression, reduced)

    variance_tables = []
    for label, matrix, filename in [
        ("Full dataset", full_keep, "pca_scores_full_dataset.csv"),
        ("Without PC_345813A", reduced_keep, "pca_scores_without_PC_345813A.csv"),
    ]:
        scores, variance = run_pca(matrix, label)
        scores.to_csv(output_dir / filename)
        variance_tables.append(variance)
        print(f"{label}: explained variance ratio = {variance['explained_variance_ratio'].tolist()}")

    pd.concat(variance_tables, ignore_index=True).to_csv(
        output_dir / "pca_explained_variance.csv", index=False
    )


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Exploratory PCA with sensitivity analysis.")
    parser.add_argument("input_csv", type=Path, help="Path to expression matrix CSV.")
    parser.add_argument(
        "--output-dir",
        type=Path,
        default=Path("results"),
        help="Directory for output tables (default: results).",
    )
    args = parser.parse_args()
    main(args.input_csv, args.output_dir)