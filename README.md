Eric Simon

Software Engineering for Data Science

Below is current summary of my notebook testing -- intend to transfer it off colab in the future.


**Summary of Current Work**

---

**Project Objective**

The goal of this project is to create a machine learning model to predict internal hemorrhage in patients using time-series lab test data from the MIMIC-IV database. By analyzing lab measurements over the first 48 hours of hospital admission, the model aims to help clinicians detect and intervene early for patients at risk of hemorrhage. This is relevant to an undergraduate hemorrhage project I had, so I want to try to take a ML approach to it.

---

**Data Source**

- **MIMIC-IV Database**: A publicly available dataset with de-identified health-related data from intensive care unit patients.
- **Data Access**: I used **Google BigQuery** to query and retrieve the required data directly from the MIMIC-IV dataset, avoiding large CSV downloads.

---

**Data Extraction and Preparation**

1. **Identifying Hemorrhage Cases**:
   - Queried the `diagnoses_icd` and `d_icd_diagnoses` tables for hospital admission IDs of patients diagnosed with hemorrhage using relevant ICD codes and diagnosis descriptions.

2. **Control Group Selection**:
   - Extracted admissions without hemorrhage diagnoses and randomly sampled them to balance the dataset with an equal number of hemorrhage and non-hemorrhage cases.

3. **Retrieving Relevant Lab Tests**:
   - Focused on lab tests related to hemorrhage detection: Hemoglobin, Hematocrit, Platelet Count, Prothrombin Time (PT), and International Normalized Ratio (INR).
   - Retrieved `itemid`s for these tests from the `d_labitems` table.

4. **Lab Event Extraction**:
   - Queried the `labevents` table to obtain lab data for the selected admissions and tests. Admissions were processed in chunks due to BigQuery limits.

5. **Merging and Time Alignment**:
   - Merged lab data with admission information and calculated the time difference between lab measurements and admission time, focusing on the first 48 hours.

---

**Data Preprocessing**

1. **Time-Series Preparation**:
   - Rounded time differences to the nearest hour and calculated the mean value for each lab test per hour.

2. **Handling Missing Values**:
   - Created uniform sequences (48 hours) for all patients, filling missing values using forward fill, backward fill, and then the mean of the respective lab test.

3. **Sequence Building**:
   - Constructed input sequences, creating a 3D array with dimensions `(number of samples, 48 hours, number of lab tests)`. Labels indicated hemorrhage presence (1) or absence (0).

4. **Data Splitting**:
   - Split the dataset into training and testing sets (80-20 split), preserving class distribution.

---

**Current Modeling**

1. **Model Selection**:
   - Used a **Long Short-Term Memory (LSTM)** neural network to model the sequential time-series data.

2. **Model Architecture**:
   - Input Layer: Sequences of shape (48, number of lab tests).
   - LSTM Layer: 64 units to capture temporal dependencies.
   - Output Layer: A Dense layer with sigmoid activation for binary classification.

3. **Compilation and Training**:
   - Loss: Binary Cross-Entropy.
   - Optimizer: Adam with a learning rate of 0.001.
   - Metrics: Accuracy monitored during 10 epochs with a batch size of 32.

