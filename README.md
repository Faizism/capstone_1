# Python CRUD Application for Smartphone Store Management

A comprehensive Python application for managing smartphone product data with Create, Read, Update, and Delete (CRUD) operations.

## Business Understanding

This project caters to the retail industry, specifically addressing the need to manage smartphone product data efficiently. Smartphone product information plays a crucial role in inventory management, sales processes, and customer service..

**Benefits:**

* Improved data accuracy and consistency in product listings
* Streamlined inventory management processes
* Enhanced decision-making through readily available product information
* Faster response times to customer inquiries about product specifications
* Simplified product updates for price changes or new models

**Target Users:**

This application is designed for inventory managers, sales representatives, and customer support agents within the organization to facilitate their tasks related to smartphone product management.

## Features
* **General Features:**
   * User-friendly main menu for navigating between CRUD operations.
   * Input validation to ensure data integrity and prevent errors.
   * Ability to return to the main menu from any sub-menu.
   * Clear error messages for invalid inputs or operations.

* **Create:**
   * Add new smartphone entries with details: product ID, name, price, and stock quantity.
   * Automatic generation of new product IDs based on existing entries.
   * Implement validation rules to ensure data integrity:
      * Unique product IDs in 'P##' format
      * Non-negative prices with at least 5 digits
      * Positive stock quantities
   * Confirmation prompt before saving new entries.

* **Read:**
   * Display all smartphone data in a formatted table.
   * Search and retrieve specific smartphone records by product ID.
   * User-friendly menu for navigating read operations
     
* **Update:**
   * Modify existing smartphone data: name, price, or stock quantity.
   * Search for products to update by ID.
   * Field-specific validation for updates.
   * Confirmation prompts before applying changes.
     
* **Delete:**
   * Remove smartphone entries by product ID.
   * Display product details before deletion for verification.
   * Confirmation prompt before deleting entries

## Installation

1. **Prerequisites:**
    * Python version 3.12 or later

2. **Installation:**
    ```bash
    git clone https://github.com/Faizism/capstone_1.git
    cd capstone_1
    ```

## Usage

1. **Run the application:**
    ```bash
    python main.py
    ```

2. **CRUD Operations:**
    * **Create:** Add a new smartphone record to the system. Provide details like ID, product name, price, and stock quantity.
    * **Read:** Display all smartphone records in a formatted table. Search and retrieve smartphone information by ID.
    * **Update:** Modify existing smartphone details.Update options include product name, price, or stock quantity. Input validation for updated fields
    * **Delete:** Remove a smartphone record from the system. Confirmation prompt before deletion to prevent accidental removals.
## Data Model
This project utilizes a list of dictionaries to represent smartphone data. Each smartphone record is stored as a dictionary within the list, with the following fields:

   * id: (String) - Unique identifier for each smartphone, format 'P##'.
   * nama produk: (String) - Name and series of the smartphone.
   * harga: (Integer) - Price of the smartphone in Indonesian Rupiah (IDR).
   * stok: (Integer) - Current stock quantity of the smartphone.

Example of a smartphone record:
    ```bash
    'id': 'P01',
    'nama produk': 'Redmi 12',
    'harga': 2_000_000,
    'stok': 12
    ```

## Contributing
We welcome contributions to this project! Please feel free to open a pull request, sent to ismail1.faiz1@gmail.com or submit an issue if you encounter any problems or have suggestions for improvements.

