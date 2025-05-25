# Emotion-Classifier-Using-SVM-From-Tweets

This project focuses on classifying the emotions expressed in tweets using **Support Vector Machines (SVM)**. It uses a Linear Kernel, which is well-suited for text classification tasks due to its efficiency and performance on high-dimensional data.

---

## Project Overview

- **Goal**: Identify the emotion (like happy, sad, angry, etc.) expressed in tweets.
- **Approach**: Preprocess raw tweet text, convert it into numerical features using TF-IDF, and classify it using an SVM model.

---

## Dataset

- A labeled dataset containing tweets and their corresponding emotion labels.
- Each entry in the dataset includes:
  - The **tweet text**
  - The **emotion label** (e.g., 0, 1, 2, etc.)

---

## Workflow

1. **Data Loading**  
   Load the dataset using `pandas`.

2. **Preprocessing**  
   - Convert to lowercase  
   - Remove punctuation and numbers  
   - Remove extra whitespace  
   - Tokenize and vectorize text using **TF-IDF**

3. **Model Training**  
   - Use **SVM with Linear Kernel and other Kernels**
   - Train on TF-IDF features

4. **Kernel Selection**  
   - Tested multiple kernels: **Linear, RBF, Polynomial**
   - **Linear kernel performed best** due to:
     - High-dimensionality of text data
     - Faster training and prediction
     - Better generalization (less overfitting)

5. **Evaluation**  
   - Accuracy  
   - Precision, Recall, F1-Score  
   - Confusion Matrix

---

## Results

- The SVM model with a **Linear Kernel** showed the best accuracy and generalization performance.
- Well-suited for real-world tweet classification due to the model's simplicity and effectiveness.

---

## Technologies Used

- Python
- Pandas
- Scikit-learn
- NumPy
- TF-IDF Vectorizer
- SVM Classifier

---

## How to Run

1. Clone the repo:
   ```bash
   git clone https://github.com/Jerinjc/Emotion-Classification-from-Tweets-using-SVM.git
   cd Emotion-Classification-from-Tweets-using-SVM
   
## Author

**Jerin John Chacko**  
MSc Data Analytics  
Digital University Kerala
GitHub: [@jerinjc](https://github.com/jerinjc)
