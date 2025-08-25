# Financial Transaction Anomaly Detection using K-Means Clustering

[![Python](https://img.shields.io/badge/python-v3.8+-blue.svg)](https://www.python.org/downloads/)
[![scikit-learn](https://img.shields.io/badge/scikit--learn-latest-orange.svg)](https://scikit-learn.org/)
[![pandas](https://img.shields.io/badge/pandas-latest-green.svg)](https://pandas.pydata.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

##  Project Overview

This project implements an unsupervised machine learning approach to detect anomalous financial transactions using K-Means clustering algorithm. The system analyzes transaction patterns based on amount and timing to identify potentially fraudulent activities in financial data.

**Key Features:**
- Distance-based anomaly detection using K-Means clustering
- Automated threshold calculation (95th percentile)
- Boundary transaction handling for edge cases
- Comprehensive statistical analysis and reporting
- Synthetic dataset for educational purposes

##  Project Objectives

- Implement K-Means clustering for financial anomaly detection
- Develop a robust threshold-based classification system
- Analyze transaction patterns and clustering behavior
- Create actionable insights for fraud detection
- Demonstrate unsupervised learning techniques in financial context

##  Technologies Used

### Programming Languages
- **Python 3.8+** - Core programming language

### Libraries & Frameworks
- **pandas** - Data manipulation and analysis
- **numpy** - Numerical computations
- **scikit-learn** - Machine learning algorithms
  - `KMeans` - Clustering algorithm
  - `StandardScaler` - Feature standardization
- **matplotlib** - Data visualization (referenced)
- **seaborn** - Statistical data visualization (referenced)

### Development Tools
- **Jupyter Notebook** / **Python IDE**
- **CSV** - Data storage format

##  Repository Structure

```
financial-anomaly-detection/
│
├── README.md                           # Project documentation
├── SUMMARY.md                          # Executive summary
│
├── src/                                # Source code
│   ├── anomaly_detection.py           # Main analysis script
│   ├── threshold.py                   # Threshold calculation utilities
│   └── boundary_handling.py           # Boundary transaction analysis
│
├── data/
│   ├── synthetic_transactions.csv.csv # Synthetic dataset (100 transactions)
│   └── transactions_nigeria.csv       # Dataset reference
│
├── docs/
│   └── Financial_Fraud_Detection_ML_Project_Report.pdf  # Detailed project report
│
└── requirements.txt                   # Python dependencies
```

##  Quick Start

### Prerequisites

Ensure you have Python 3.8+ installed on your system.

### Installation

1. **Clone the repository:**
```bash
git clone https://github.com/yourusername/financial-anomaly-detection.git
cd financial-anomaly-detection
```

2. **Install dependencies:**
```bash
pip install -r requirements.txt
```

### Usage

1. **Run the main anomaly detection analysis:**
```bash
python src/anomaly_detection.py
```

2. **Calculate threshold values:**
```bash
python src/threshold.py
```

3. **Analyze boundary transactions:**
```bash
python src/boundary_handling.py
```

## 📊 Dataset Information

**Synthetic Transaction Dataset:**
- **Size:** 100 transactions
- **Features:** TransactionID, Name, Amount (₦), Time
- **Amount Range:** ₦23.80 - ₦1,200.00
- **Time Range:** 20.41 - 500.00 time units
- **Purpose:** Educational demonstration (no real financial data)

##  Methodology

### Algorithm Workflow

1. **Data Preprocessing**
   - Load synthetic transaction data
   - Extract Amount and Time features
   - Standardize features using Z-score normalization

2. **K-Means Clustering**
   - Set k=4 clusters
   - Fit model with 10 random initializations
   - Calculate distances to cluster centers

3. **Anomaly Detection**
   - Compute minimum distance to any cluster center
   - Apply 95th percentile threshold
   - Flag transactions exceeding threshold as anomalous

4. **Analysis & Reporting**
   - Generate cluster analysis
   - Identify boundary transactions
   - Provide actionable insights

### Key Parameters
- **Clusters (k):** 4
- **Threshold:** 95th percentile of distances
- **Features:** Amount, Time (standardized)
- **Random State:** 42 (for reproducibility)

##  Results Summary

### Detection Performance
- **Total Transactions:** 100
- **Anomalies Detected:** 5
- **Anomaly Rate:** 5.00%
- **Threshold Value:** 0.1668

### Key Findings
- Anomalous transactions average **10.87x** higher amounts than normal transactions
- Anomalies occur at **8.52x** longer processing times (suggesting after-hours activity)
- 80% of anomalies fall in the top 10% of transaction amounts
- Clear clustering separation between normal and fraudulent patterns

### Most Anomalous Transactions
| Transaction ID | Amount (₦) | Time | Anomaly Score |
|----------------|------------|------|---------------|
| 100 | 1,200.00 | 500.00 | 2,502.4% of threshold |
| 99 | 1,000.00 | 450.00 | 2,127.4% of threshold |
| 98 | 700.00 | 400.00 | 1,752.5% of threshold |

##  Educational Value

This project demonstrates:
- **Unsupervised Learning:** K-Means clustering application
- **Feature Engineering:** Standardization and preprocessing
- **Anomaly Detection:** Distance-based threshold methods
- **Statistical Analysis:** Percentile-based threshold selection
- **Data Science Workflow:** End-to-end analysis pipeline
- **Financial Domain Knowledge:** Fraud detection patterns

## Limitations

1. **Feature Limitation:** Only uses Amount and Time features
2. **Algorithm Constraints:** K-Means assumes spherical clusters
3. **Static Threshold:** Fixed 95th percentile threshold
4. **Synthetic Data:** Results based on artificially generated data

##  Future Enhancements

- [ ] **Feature Engineering:** Add merchant category, location, frequency
- [ ] **Hybrid Algorithms:** Combine with Isolation Forest or One-Class SVM
- [ ] **Dynamic Thresholding:** Implement adaptive threshold mechanisms
- [ ] **Real-time Processing:** Stream processing capabilities
- [ ] **Advanced Visualization:** Interactive dashboards and plots
- [ ] **Model Evaluation:** ROC curves, precision-recall analysis

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request. For major changes, please open an issue first to discuss what you would like to change.

1. Fork the project
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

##  Author

**Oreoluwa Anjorin**
- 📧 [anjorinoreoluwa19@gmail.com](mailto:anjorinoreoluwa19@gmail.com)
- 💼 [LinkedIn](https://www.linkedin.com/in/oreoluwa-anjorin-69a4441aa/)
- 🐙 [@OreoluwaAnjorin](https://github.com/OreoluwaAnjorin)

## ⚠️ Disclaimer

This project uses synthetic data generated for educational purposes only. No real financial or personal data was used in this analysis. The results and patterns identified are based on artificially created transaction data and should not be used for actual fraud detection without proper validation on real-world datasets.
---

**⭐ If you found this project helpful, please give it a star!**
