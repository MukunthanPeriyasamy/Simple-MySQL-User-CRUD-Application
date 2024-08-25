# MySQL User Management Script

This script allows you to perform basic CRUD (Create, Read, Update, Delete) operations on a MySQL database table named `users`. It uses the `mysql-connector-python` library for database interactions and `tabulate` for displaying results in a tabular format.

## Requirements

- Python 3.x
- `mysql-connector-python` library
- `tabulate` library

You can install the required libraries using pip.

## Setup

1. **Database Setup:**
   Ensure you have a MySQL server running and create a database named `dummy` with a table named `users`. The table should have the necessary schema.

2. **Configuration:**
   Update the database connection settings in the script with your MySQL server credentials.

## Usage

Run the script using Python.

You will see a menu with the following options:

1. **INSERT**: Add a new user to the database.
2. **UPDATE**: Update an existing user's details by ID.
3. **SELECT**: Display all users in the database.
4. **DELETE**: Delete a user by ID.
5. **EXIT**: Exit the program.

### Example

To insert a new user, choose option `1` and provide the user's name, age, and city. To update an existing user, choose option `2`, and provide the new details along with the user's ID. To view all users, choose option `3`. To delete a user, choose option `4` and provide the user's ID.

## Notes

- Make sure your MySQL server is running and accessible.
- Ensure the database and table exist before running the script.
- The script assumes that the `users` table has columns `id`, `name`, `age`, and `city`.

