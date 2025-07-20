# Mental Health EDA & Prediction

This project provides a comprehensive workflow for exploratory data analysis (EDA) and predictive modeling on global mental health datasets. The primary analysis and modeling are performed in the `main.ipynb` notebook, which guides users through data loading, preprocessing, visualization, and machine learning.

## Project Structure

```
main.ipynb
calldata.py
FunctionalDescribe.py
requirement.py
test.py
Dataset/
    Adult Population Major Depression Data.csv
    Anxiety Disorders Treatment Gap.csv
    Depressive Symptoms US Population.csv
    Mental Health Adult Population Data.csv
    Mental Health Burden by Illness.csv
    Mental Health Countries Data.csv
    Mental Illnesses Prevalence.csv
```

## Getting Started

### Prerequisites

- Python 3.8 or higher

### Installation

Install the required Python packages before running the project:

```sh
pip install -r requirement.py
```

### Usage

1. Ensure all datasets are placed in the `Dataset/` directory.
2. Open and run `main.ipynb` in Jupyter Notebook or VS Code. The notebook covers:
    - Data loading and preprocessing
    - Exploratory data analysis and visualization (with Matplotlib, Seaborn, and Plotly)
    - Feature engineering and normalization
    - Correlation analysis
    - Predictive modeling using linear regression
    - Model evaluation and visualization of results

Scripts such as `calldata.py`, `FunctionalDescribe.py`, and `test.py` are provided for modular data processing and testing, but the main workflow is in `main.ipynb`.

## File Descriptions

- **main.ipynb**: The primary notebook for EDA, visualization, and predictive modeling.
- **calldata.py**: Script for data loading and initial preprocessing.
- **FunctionalDescribe.py**: Provides descriptive statistics and visualizations.
- **requirement.py**: Lists all required Python packages.
- **test.py**: Contains model testing and evaluation code.
- **Dataset/**: Directory containing all raw datasets.

## Data Sources

The original sources for each dataset are documented within the `Dataset/` folder.

## Contributing

Contributions and feedback are welcome. Please open an issue or submit a pull request.

## Contact

For questions or feedback, please contact [Your Name or Email].

---

Welcome contributions and feedback!
