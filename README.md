# ERP Analysis: Decoding Brain Responses to Finger Movements

This project analyzes **Event-Related Potentials (ERP)** to understand brain responses during finger movements. By aligning finger movement events with brain signals recorded via ECoG electrodes, we compute the mean brain response for each finger over multiple trials. The project provides robust insights into neural activity during motor tasks.

## Features
- Extracts brain signal slices (200 ms before to 1000 ms after each event) for every finger movement.
- Computes the **mean ERP** for each finger across multiple trials.
- Generates **visualizations** of brain responses for all fingers.
- Implements efficient signal processing and data handling with Python.

## What to Expect
- A **5x1201 matrix** representing the mean brain response for each finger.
  - Rows correspond to the five fingers.
  - Columns represent time points (-200ms to +1000ms).
- Visualizations of the mean brain response for each finger, helping you analyze neural patterns during motor tasks.
- Clean, modular, and reusable Python code.

---

## Requirements
To run this project, you need:
- Python 3.8+
- Required Python libraries:
  - `pandas`: For data manipulation.
  - `matplotlib`: For plotting.

You can install the required libraries using the following command:
```bash
pip install pandas matplotlib


