# Data Analytics Project: Player Similarity Analysis

## Table of Contents
1. [Overview](#overview)  
2. [Problem Statement](#problem-statement)  
3. [Datasets](#datasets)  
4. [Data Cleaning and Preprocessing](#data-cleaning-and-preprocessing)  
5. [Feature Selection](#feature-selection)  
6. [Encoding Techniques](#encoding-techniques)  
7. [Similarity Analysis](#similarity-analysis)  
8. [Conclusion](#conclusion)

---

## Overview  
This project analyzes player similarities using data from Kaggle. The goal is to identify comparable players based on selected features using cosine similarity.

---

## Problem Statement  
The idea was to get user build a player for them, and get similar players with regards to attributes filled by the user. Which can then be used for building more use cases on top of it.

---

## Datasets  
- **Source:** Kaggle  
- **Selection Process:** Multiple datasets were analyzed based on completeness, relevance, and alignment with the problem statement.  
- **Final Dataset:** [FIFA 22 Dataset]  
  - I first fbref website and some other places like trnaferMarkt to scrape the data for the project, but then realised maybe it shouldnt be so in the first place, as what i wanted was to have a simulation game like experience, and this would have made it really complex. So went with really basic more enjoyable by general public, player dataset from FIFA 22.

---

## Data Cleaning and Preprocessing  
- Removed missing and inconsistent entries.  
- Normalized and standardized numerical values for consistency.  
- Handled outliers and imbalanced data where necessary.  

---

## Feature Selection  
- Selected **7 features** critical for player comparison, such as:  
  1. Position  
  2. Speed  
  3. Passing  
  4. Dribbling  
  5. Defense  
  6. Physic
  7. Shooting  
- **Rationale:** These features were chosen for their direct influence on the objective of the analysis (e.g., performance metrics, position-based attributes) and are easy for a generic user to fill up and make a deicion upon.  

---

## Encoding Techniques  
- **Why Encoding?** To convert categorical data into numerical format for similarity calculations.  
- **Why One-Hot Encoding?**  
  - Preserves category uniqueness.  
  - Avoids ordinal assumptions inherent in label encoding.  

---

## Similarity Analysis  
- **Approach:** Cosine Similarity  
- **Why Cosine Similarity?**  
  - Measures similarity based on the orientation rather than magnitude.  
  - Effective for high-dimensional sparse data.  
  - Ensures that the results are not skewed by the scale of features.  

---

## Conclusion  
- Identified players with high similarity scores.  
- The methodology demonstrates the utility of cosine similarity in sports analytics.  
- Insights can support team formation, player recruitment, and performance comparison.
- we will need to add more features as search does gives the result, but they are not always what we want, we want more filters on top of it to get a much better selection.