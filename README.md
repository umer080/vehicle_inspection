# vehicle_inspection
 
## Description

This Django application allows users to upload, store, and search vehicle inspection data. Users can upload a JSON file containing vehicle inspection records, which are then stored in a relational database. The application provides a live search feature, allowing users to search existing database rows using a free-text search box without reloading the page.

## Features

- **File Upload:** Users can upload a JSON file containing vehicle inspection data via a form.
- **Data Storage:** Uploaded data is stored in a relational database. Recurring uploads update existing database rows instead of duplicating the data.
- **Live Search:** Users can search existing database rows using a free-text search box. Search results are dynamically updated without page reloads and are limited to 50 records.

## Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/umer080/vehicle_inspection.git
    ```

2. Navigate to the project directory:

    ```bash
    cd vehicle_inspection
    ```

4. Apply database migrations:

    ```bash
    python manage.py migrate
    ```

5. Run the development server:

    ```bash
    python manage.py runserver
    ```

6. Visit `http://127.0.0.1:8000/` in your web browser to access the application.

## Usage

1. **File Upload:**
    - Visit the homepage and click on the "Upload Vehicle Data" button.
    - Choose a JSON file containing vehicle inspection data and click "Upload."

2. **Search:**
    - Use the search box at the top to perform a live search.
    - Type in any text, and the application will dynamically update the table with matching records.

## Technologies Used

- Python
- Django
- JavaScript
- HTML/CSS
