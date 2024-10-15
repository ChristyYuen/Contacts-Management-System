# Contacts Management System

## Overview

The Contacts Management System is a web application developed using [Py4web](https://py4web.com/), a lightweight web framework designed for rapid development in Python. This application allows users to manage their contacts and associated phone numbers efficiently. Users can add, edit, and delete contacts and their phone numbers, ensuring that all data is properly organized and easily accessible.

## Features

- **Contacts List**: The main page displays a list of contacts, including first and last names, along with their associated phone numbers.
- **Edit/Delete Contact**: Users can edit or delete contacts directly from the list.
- **Manage Phone Numbers**: Each contact has a dedicated section for managing phone numbers:
  - View existing phone numbers.
  - Edit phone numbers associated with a contact.
  - Delete phone numbers.
  - Add new phone numbers to a contact.

## Functionality

- **Data Integrity**: The application ensures that no contact can have empty first or last names, and no phone numbers can be left blank.
- **Database Structure**: The application uses two database tables:
  - **Contacts Table**: Stores first names and last names of contacts.
  - **Phone Numbers Table**: Contains phone numbers associated with each contact, referencing the contacts table via a foreign key.
- **Cascade Deletion**: When a contact is deleted, all associated phone numbers are automatically removed, maintaining data integrity.

## Code Structure

The project's code is organized into several key files:
- `models.py`: Contains the definitions for the database tables and relationships.
- `controllers.py`: Manages the logic for handling user interactions.
- `views.py`: Defines the templates for rendering HTML pages.

## Installation

To run this project locally, clone the repository and follow these steps:

1. **Clone the repository**:
   ```bash
   git clone https://github.com/yourusername/contacts-management-system.git
   cd contacts-management-system

2. Set up a virtual environment (optional but recommended):
  ```bash
  python3 -m venv venv
  source venv/bin/activate  # On Windows use `venv\Scripts\activate`

3. Install Py4web:
  ```bash
  pip install py4web

4. Run the application:
  ```bash
  python3 wsgi.py

5. Open your browser and navigate to http://127.0.0.1:8000.

## Lessons Learned
During the development of this project, I learned the importance of maintaining data integrity in web applications. Implementing proper foreign key relationships ensured that when contacts were deleted, all associated data was also removed, preventing orphaned records in the database. This not only improved the application's reliability but also enhanced user experience by ensuring that users do not encounter outdated or irrelevant information.

## Conclusion
The Contacts Management System demonstrates how to build a functional web application with essential CRUD operations using Py4web. It highlights the significance of data management, user-friendly interfaces, and robust back-end logic to create a seamless user experience.