# 💰 Tip_Calculator

The Tip Calculator is a simple Python-based application that helps users calculate the appropriate tip amount based on their total bill. The program takes user input for the bill amount, the desired tip percentage, and optionally the number of people splitting the bill, and then computes:

The total tip amount

The total bill including tip

Each person's share (if splitting)

---

## 🧠 Project Description

This Tip Calculator is my first Python program that:
- Takes the total bill amount as input
- Asks for the desired tip percentage
- Optionally splits the bill between multiple people
- Outputs the tip amount, total bill including tip, and amount each person should pay


---

## 🛠️ Features

- Input:
  - Total bill amount
  - Tip percentage (e.g., 10%, 15%, 20%)
  - Number of people splitting the bill
- Output:
  - Calculated tip amount
  - Total bill including tip
  - Amount each person should pay (if split)

---

## 🧮 Formula Used

```python
tip = (meal / 100 * tip_percent)
cost = tip + meal
meal_1 = cost / members