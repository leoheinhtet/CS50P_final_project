# Terminal Store: A Simple CLI Shopping System  
#### Video Demo: <URL HERE>  
#### Description:

**Terminal Store** is a command-line Python application that simulates a shopping experience similar to what you might see in a small retail store, with inventory tracking, cart management, and sales recording. The program is designed as a final project for CS50’s Introduction to Programming with Python.

### Features

- View available items with live stock levels that reflect reserved cart quantities.
- Add and remove items from a shopping cart.
- Automatically generate incremental receipt IDs (e.g., R0001, R0002...).
- Checkout and record transactions with timestamped entries in `sales.csv`.
- Prevents overselling by validating stock against cart contents before checkout.
- Provides a printable summary of cart contents before purchase.

### Design Decisions

- The project separates concerns with 3 key classes:
  - `Item` class encapsulates data and input validation.
  - `Inventory` class handles loading, checking, and updating inventory from `inventory.csv`.
  - `Cart` class manages cart contents, additions, removals, and total cost.

- Instead of reducing inventory stock immediately after items are added to the cart (which could cause issues if the customer never checks out), inventory is only updated at the point of checkout. To reflect real-time stock availability, the display subtracts quantities already in the cart.

- Three core functions were designed and tested:
  - `generate_receipt_id()` for incremental unique receipt IDs.
  - `validate_add_to_cart()` to enforce stock limits before items are added.
  - `format_cart_summary()` for user-friendly cart display.

These functions were chosen because they represent critical business logic and are highly testable in isolation.

### File Overview

- `project.py`: Main entry point. Handles the app loop and includes all custom logic.
- `inventory.py`: Defines the `Inventory` class and manages CSV-based stock data.
- `cart.py`: Defines the `Cart` class for cart operations and price calculations.
- `item.py`: Defines the `Item` class with property validation for item attributes.
- `sales.csv`: Automatically generated and updated to track all completed purchases.
- `receipt_counter.txt`: Keeps track of the most recent receipt ID.
- `test_project.py`: Contains unit tests for three functions using `pytest`.
- `requirements.txt`: Lists required Python libraries (only `pytest` needed).
- `README.md`: This file — documentation and project summary.

### Testing

- Tests are written in `test_project.py` using `pytest`.
- Temporary inventory and counter files are used to ensure isolation.
- Each required custom function is covered by multiple test cases.

### Reflections

Creating a full-fledged CLI application was both challenging and rewarding. I focused on keeping the interface clean while building functionality that resembles real-world store systems. The modular design allows for future upgrades such as category filtering, discount handling, or customer accounts.

This project helped me practice file I/O, data validation, error handling, and test-driven development — all in Python.



