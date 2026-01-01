## Project Overview

FPCE (Fast Pseudo-Clique Enumerator) is an exact pseudo-clique detection algorithm that applies pruning techniques to reduce the search space and execution time.

The objective of this project is to optimize the execution of FPCE by focusing on the discovery of the Largest Pseudo-Clique (LPC) in real-world graphs. Cleaned and preprocessed graphs are converted into a standardized format and evaluated under different vertex orderings. Based on these evaluations, a machine-learning-based recommendation system is built to predict the ordering that identifies the Largest Pseudo-Clique with minimum runtime.

This approach reduces computational cost, improves scalability for large graphs, and addresses the challenge of maintaining efficient execution time for exact pseudo-clique detection.

## Objective

- Optimize FPCE runtime through intelligent ordering selection  
- Efficiently identify the Largest Pseudo-Clique  
- Use machine learning to recommend the best execution strategy  

## Methodology

### Graph Processing

- Clean and preprocess real-world graph datasets  
- Convert graphs into a standardized representation  
- Extract relevant structural features  
- Evaluate FPCE performance under multiple vertex orderings  

### Model Application

Several modeling approaches were explored:

Model_Apply:
- Regression-based experiments  

Model_Apply_1:
- Multi-label classification  
- Weight balancing  
- SMOTE for handling class imbalance  
- Feature selection  

Model_Apply_2 (Final):
- Multi-class classification  
- Class assignment based on closest difference  
- Feature scaling by dividing by the mean  

## Outcome

The final model recommends an optimal vertex ordering that minimizes FPCE runtime while accurately identifying the Largest Pseudo-Clique, enabling efficient analysis of large real-world graphs.
