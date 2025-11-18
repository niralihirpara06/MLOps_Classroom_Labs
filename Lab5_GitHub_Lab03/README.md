# Lab 5: Automated ML Pipeline with GitHub Actions and GCP

## Project Overview
This lab demonstrates an end-to-end automated machine learning workflow using GitHub Actions and Google Cloud Platform. The pipeline trains a classification model and automatically deploys it to Google Cloud Storage, showcasing modern MLOps practices.

---

## 🎯 Learning Objectives
- Set up CI/CD pipeline for machine learning using GitHub Actions
- Integrate GitHub Actions with Google Cloud Platform
- Automate model training and cloud deployment
- Implement comprehensive model evaluation metrics
- Manage cloud credentials securely using GitHub Secrets

---

## 🔧 Technologies & Tools
- **Python 3.10** - Programming language
- **scikit-learn** - Machine learning framework
- **Google Cloud Storage** - Model storage and versioning
- **GitHub Actions** - CI/CD automation
- **Pandas** - Data manipulation
- **Logistic Regression** - Classification algorithm

---

## 📊 Model & Dataset

### Dataset: Breast Cancer Wisconsin
- **Samples**: 569 instances
- **Features**: 30 numerical features (cell measurements)
- **Classes**: Binary classification (Malignant vs Benign)
- **Split**: 80% training, 20% testing
- **Source**: scikit-learn datasets

### Model: Logistic Regression
- **Algorithm**: Logistic Regression Classifier
- **Parameters**: 
  - `max_iter=10000` (for convergence)
  - `random_state=42` (reproducibility)
- **Advantages**: Simple, interpretable, fast training

---

## 📈 Model Performance Metrics

Our trained model achieved excellent results on the test set:

| Metric | Score | Description |
|--------|-------|-------------|
| **Accuracy** | **95.61%** | Overall correct predictions |
| **Precision** | **94.59%** | Accuracy of positive predictions |
| **Recall** | **98.59%** | Ability to find all positive cases |
| **F1-Score** | **96.55%** | Harmonic mean of precision and recall |

### What These Metrics Mean:
- **High Accuracy (95.61%)**: The model correctly classifies 95.61% of all cases
- **High Precision (94.59%)**: When the model predicts malignant, it's correct 94.59% of the time
- **Excellent Recall (98.59%)**: The model catches 98.59% of all actual malignant cases (critical for medical diagnosis!)
- **Strong F1-Score (96.55%)**: Balanced performance between precision and recall

---

## 🔄 Key Modifications from Template

### 1. **Model Change**
- ❌ Original: Random Forest Classifier (100 estimators)
- ✅ Modified: **Logistic Regression** (simpler, faster, more interpretable)

### 2. **Dataset Change**
- ❌ Original: Iris dataset (150 samples, 4 features)
- ✅ Modified: **Breast Cancer dataset** (569 samples, 30 features)

### 3. **Enhanced Evaluation Metrics**
- ❌ Original: Only Accuracy
- ✅ Modified: **Accuracy + Precision + Recall + F1-Score**

### 4. **Workflow Customization**
- ❌ Original: "Train and save model to GCS"
- ✅ Modified: **"ML Model Training Pipeline"**

### 5. **Model File Naming**
- ❌ Original: `model_{timestamp}.joblib`
- ✅ Modified: **`logistic_model_{timestamp}.joblib`**

### 6. **Execution Mode**
- ❌ Original: Automatic daily runs (cron schedule)
- ✅ Modified: **Manual trigger only** (workflow_dispatch)

---

## 📁 Project Structure
```
Lab5_GitHub_Lab03/
├── train_and_save_model.py    # ML training script with 4 evaluation metrics
├── requirements.txt            # Python dependencies
└── README.md                   # Project documentation

.github/workflows/
└── run.yaml                    # GitHub Actions workflow configuration
```

---

## ⚙️ Setup & Configuration

### Prerequisites
1. ✅ GitHub account
2. ✅ Google Cloud Platform account
3. ✅ GCP Service Account with `Storage Admin` role
4. ✅ GCS bucket created

### Step 1: GCP Setup
```bash
# 1. Create GCP Project: mlops-github-actions-lab
# 2. Create Service Account: github-actions-lab03
# 3. Assign Role: Storage Admin
# 4. Generate JSON key and download securely
```

### Step 2: Create GCS Bucket
```bash
# Bucket Name: mlops-lab03-github-actions
# Region: us-east1 (or your preferred region)
# Storage Class: Standard
# Access Control: Uniform
```

### Step 3: Configure GitHub Secrets
1. Go to Repository → Settings → Secrets and variables → Actions
2. Create new secret:
   - **Name**: `GCP_GITHUB_ACTION_KEY`
   - **Value**: Paste entire JSON key content

### Step 4: Install Dependencies
```bash
pip install -r requirements.txt
```

---

## 🚀 Running the Pipeline

### Option 1: Manual Trigger (GitHub Actions)
1. Go to repository **Actions** tab
2. Select **"ML Model Training Pipeline"**
3. Click **"Run workflow"**
4. Select branch: **main**
5. Click **"Run workflow"** button
6. Monitor progress and check logs

### Option 2: Run Locally
```bash
# Set GCP credentials
export GOOGLE_APPLICATION_CREDENTIALS="path/to/service-account-key.json"

# Run training script
python train_and_save_model.py
```

Expected output:
```
Model Accuracy: 0.9561
Model Precision: 0.9459
Model Recall: 0.9859
Model F1-Score: 0.9655
Model saved to gs://mlops-lab03-github-actions/trained_models/logistic_model_20251118023447.joblib
```

---

## 🔐 GitHub Actions Workflow

### Workflow File: `.github/workflows/run.yaml`

**Trigger**: Manual only (`workflow_dispatch`)

**Steps**:
1. 📥 **Checkout code** - Clone repository
2. 🐍 **Setup Python 3.10** - Configure environment
3. 💾 **Cache dependencies** - Speed up builds
4. 📦 **Install packages** - Install requirements
5. 🔑 **Authenticate GCP** - Use service account key
6. 🤖 **Train model** - Execute training script
7. ☁️ **Upload to GCS** - Save model with timestamp

---

## 📦 Cloud Storage Structure
```
gs://mlops-lab03-github-actions/
└── trained_models/
    ├── logistic_model_20251118023447.joblib  # Latest model
    └── model_20251118022243.joblib           # Previous RandomForest model
```

Each model is timestamped for version tracking and comparison.

---

## 🧪 Code Highlights

### Training Function
```python
def train_model(X_train, y_train):
    model = LogisticRegression(max_iter=10000, random_state=42)
    model.fit(X_train, y_train)
    return model
```

### Comprehensive Evaluation
```python
accuracy = accuracy_score(y_test, y_pred)
precision = precision_score(y_test, y_pred)
recall = recall_score(y_test, y_pred)
f1 = f1_score(y_test, y_pred)
```

---

## 🎓 What I Learned
1. ✅ Setting up automated ML pipelines with GitHub Actions
2. ✅ Integrating cloud services (GCP) with CI/CD workflows
3. ✅ Secure credential management using GitHub Secrets
4. ✅ Implementing comprehensive model evaluation
5. ✅ Version control for ML models using timestamps
6. ✅ Best practices for MLOps workflows

---

## 🔮 Future Improvements
- [ ] Add hyperparameter tuning with GridSearchCV
- [ ] Implement model comparison and A/B testing
- [ ] Deploy model as REST API endpoint
- [ ] Add email notifications on workflow completion
- [ ] Create model performance dashboard
- [ ] Implement automatic retraining on data drift

---

## 📚 References
- [GitHub Actions Documentation](https://docs.github.com/en/actions)
- [Google Cloud Storage Python Client](https://cloud.google.com/storage/docs/reference/libraries)
- [scikit-learn User Guide](https://scikit-learn.org/stable/user_guide.html)
- [Breast Cancer Dataset](https://scikit-learn.org/stable/datasets/toy_dataset.html#breast-cancer-dataset)

---