# Mini Python Projects 🚀

A collection of clean, modular Python scripts demonstrating Object-Oriented Programming (OOP) principles, custom data structures, and practical utility management algorithms.

## 📁 Project Structure & Overview

### 1. User Configuration Manager (`user_config_manager.py`)
* **Description:** A lightweight configuration management utility that safely handles dictionary-based settings[cite: 8].
* **Key Features:**
  * Add new settings with built-in duplicate validation[cite: 8].
  * Update existing key-value configurations seamlessly[cite: 8].
  * Delete or view current configurations dynamically[cite: 8].
  * Case-insensitive key processing[cite: 8].

### 2. Budget App (`budget_app.py`)
* **Description:** An object-oriented financial tracking application that manages category-based ledgers, fund transfers, and visual spending analytics[cite: 5].
* **Key Features:**
  * Track deposits, withdrawals, and inter-category transfers[cite: 5].
  * Automated budget calculations and real-time balance checks[cite: 5].
  * Custom text-based percentage spend charts via `create_spend_chart`[cite: 5].

### 3. Polygon Area Calculator (`polygon_calculator.py`)
* **Description:** An OOP implementation utilizing class inheritance to calculate geometric properties of shapes[cite: 7].
* **Key Features:**
  * `Rectangle` class with methods for area, perimeter, diagonal, and ASCII-art visual representation[cite: 7].
  * `Square` subclass inheriting from `Rectangle` with synchronized side lengths[cite: 7].
  * Calculates containment metrics (`get_amount_inside`) to see how many times one shape fits into another[cite: 7].

### 4. Custom Hash Table (`hash_table.py`)
* **Description:** A foundational data structure implementation built from scratch using Python dictionaries[cite: 6].
* **Key Features:**
  * Custom ASCII character summation hashing algorithm (`hash`)[cite: 6].
  * Core hash table operations: `add`, `remove`, and `lookup`[cite: 6].

## 🛠️ Requirements
* Python 3.x

## 🚀 Usage
You can run any script independently using your terminal:
```bash
python user_config_manager.py
python budget_app.py
python polygon_calculator.py
python hash_table.py