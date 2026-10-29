# Data directory

All files in this directory are **synthetic** and are provided only to
demonstrate the workflow. They do not contain real patient data.

## expression_matrix.csv

Synthetic gene-level expression matrix used as input to `main.py`.

- Rows: genes (`gene_id`)
- Columns: samples, including the divergent sample `PC_345813A`
- Values: normalized, non-negative, unlogged expression values

Replace this file with your own normalized expression matrix before running
the analysis on real data.

## reads_coverage.csv (optional)

Synthetic reads-coverage distribution per sample, provided as a QC summary.

- `sample`: sample identifier
- `percent_covered`: coverage interval (0-10, 10-20, ..., 90-100)
- `percent_transcript`: percentage of transcripts in that interval

If you do not include this file, the workflow still runs; it is provided only
as an optional QC example.
