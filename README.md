# AI4Metascience Hackathon

This repository contains Jupyter notebooks, scripts, and supporting materials for the **AI4Metascience NeurIPS Hackathon (10–17 November 2026)**.

## Purpose

The repository provides a shared starting point for participants to explore AI applications in metascience using the LUMI supercomputer.

Each participant receives an individual copy of the repository through the Jupyter for Courses environment on LUMI Open OnDemand (OOD).

## Repository structure

```text
.
├── notebooks/          # Jupyter notebooks
├── scripts/            # Scripts for running jobs on LUMI
├── docs/               # Setup guides and documentation
├── README.md
└── requirements.txt
```

The repository will be expanded with additional notebooks, scripts, and documentation as the hackathon materials develop.

## Getting started

### 1. Log in to LUMI

Go to the [LUMI Open OnDemand interface](https://www.lumi.csc.fi/public/) and click **Log in to LUMI**.

### 2. Select Jupyter for Courses

Navigate to **Jupyter for Courses** and select the AI4Metascience Hackathon environment.

### 3. Configure your interactive session

Use the following settings:

**Setup your environment**

- **Project:** `project_465002387`
- **Partition:** `dev-g`

**Resources**

- **Number of CPU cores:** `8`
- **Memory (GiB):** `16`
- **Number of GPUs:** `1`
- **Time:** `3:00:00`

**Settings**

- **Working directory:** `/projappl/project_465002387`
- **Show advanced settings:** Enable (`1`)

### 4. Launch JupyterLab

Launch the session and wait for JupyterLab to become available. Open the `notebooks/` directory and start working!

## Additional documentation

Guides and examples will be provided for:

- **Python packages:** How to add additional pip packages to the container.
- **SLURM jobs:** How to submit and manage computational jobs on LUMI.
- **API access:** How to use AITTA to generate API tokens and configure API access.

Detailed instructions and example scripts will be added to the `docs/` and `scripts/` directories.

## Hackathon

**AI4Metascience NeurIPS Hackathon**

10–17 November 2026

More information: https://luma.com/6b08hj2b
