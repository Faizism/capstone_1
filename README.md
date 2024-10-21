# Python CRUD Application for Smartphone Store Management

A comprehensive Python application for managing smartphone product data with Create, Read, Update, and Delete (CRUD) operations.

## Business Understanding

This application manages a database for smartphone sales at Toko Smartphone Berkah Jaya. It provides a comprehensive set of features for inventory management, including creating, reading, updating, and deleting product information, as well as sorting and tracking changes to the database.

**Benefits:**

* Improved data accuracy and consistency in product listings.
* Streamlined inventory management processes.
* Enhanced decision-making through readily available product information.
* Faster response times to customer inquiries about product specifications.
* Simplified product updates for price changes or new models.
* Ability to track and review historical changes to product data.

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
      * Unique product IDs in 'P##' format.
      * Non-negative prices with at least 5 digits.
      * Positive stock quantities.
   * Confirmation prompt before saving new entries.

* **Read:**
   * Display all smartphone data in a formatted table.
   * Search and retrieve specific smartphone records by:
       * Product ID.
       * Brand name.
       * Price Range.
   * User-friendly menu for navigating read operations.
     
* **Update:**
   * Modify existing smartphone data: name, price, or stock quantity.
   * Search for products to update by ID.
   * Field-specific validation for updates.
   * Confirmation prompts before applying changes.
   * Automatic logging of all changes made to products.
     
* **Delete:**
   * Remove smartphone entries by product ID.
   * Display product details before deletion for verification.
   * Confirmation prompt before deleting entries.
 
* **Sort:**
   * Sort smartphone listings based on various criteria:
       * Price (ascending or descending).
       * Stock quantity (ascending or descending).
       * Product name (A-Z or Z-A).
    
* **Sort:**
   * Display a comprehensive history of all changes made to products.
   * View change history for a specific product by ID.
   * Each log entry includes:
       * Timestamp of the change.
       * Category of the change.
       * Old value.
       * New value.
    
## Installation

1. **Prerequisites:**
    * Python version 3.12 or later
    * datetime module (part of Python's standard library)

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
    * **Create:** Add a new smartphone record to the system. Provide details like ID, product name, price, and stock quantity. Input validation is applied to ensure accurate entries
    * **Read:** Display all smartphone records in a formatted table. Search and retrieve smartphone information by ID, brand name, and price range. 
    * **Update:** Modify existing smartphone details. Update options include product name, price, or stock quantity. Input validation for updated fields. Change logs are recorded with a timestamp to track the history of each modification.
    * **Delete:** Remove a smartphone record from the system. Confirmation prompt before deletion to prevent accidental removals.
## Data Model
This project utilizes a list of dictionaries to represent smartphone data. Each smartphone record is stored as a dictionary within the list, with the following fields:

   * id: (String) - Unique identifier for each smartphone, format 'P##'.
   * nama produk: (String) - Name and series of the smartphone.
   * harga: (Integer) - Price of the smartphone in Indonesian Rupiah (IDR).
   * stok: (Integer) - Current stock quantity of the smartphone.

The project also includes a change log to track modifications to the smartphone data. The change log is structured as a nested dictionary:

Each entry in the change log is associated with a product ID and contains a list of changes. Each change is represented by a dictionary with the following fields:

   * waktu: (String) - Timestamp of the change in 'YYYY-MM-DD HH:MM' format.
   * kategori: (String) - Category of the change (e.g., 'harga', 'stok', 'nama').
   * data lama: (String or Integer) - Previous value before the change.
   * data baru: (String or Integer) - New value after the change.

## Contributing
We welcome contributions to this project! Please feel free to open a pull request, sent to ismail1.faiz1@gmail.com or submit an issue if you encounter any problems or have suggestions for improvements.

