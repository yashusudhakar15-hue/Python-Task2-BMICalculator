# BMI Calculator

## Project Description
The BMI Calculator is a simple Python application that calculates a person's Body Mass Index (BMI) using their weight and height.

It also displays the corresponding BMI category based on the calculated value.

## Features
- Accepts weight in kilograms.
- Accepts height in metres.
- Calculates BMI automatically.
- Displays BMI up to two decimal places.
- Identifies BMI categories:
  - Underweight
  - Normal
  - Overweight
  - Obese
- Handles invalid numeric inputs.
- Checks for non-positive weight and height values.

## Technologies Used
- Python 3

## Formula

BMI = Weight (kg) / Height (m)²

## How to Run

1. Install Python 3.
2. Open the project folder in Visual Studio Code.
3. Open the terminal.
4. Execute the following command:

```bash
py bmi_calculator.py
```

5. Enter your weight in kilograms.
6. Enter your height in metres.
7. View your BMI and category.

## Example Output

```text
================================
       BMI CALCULATOR
================================
Enter your weight in kg: 55
Enter your height in metres: 1.65

Your BMI is: 20.2
BMI Category: Normal
```

## Project Structure

```text
Python-Task2-BMICalculator/
│
├── bmi_calculator.py
└── README.md
```

## Conclusion
This project demonstrates basic Python programming concepts such as user input, conditional statements, exception handling, mathematical calculations and output formatting.