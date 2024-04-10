# SEA
Welcome to the SEA Customer Management System (CMS) README! This application was developed as part of a Software Engineering and Agile assignment. It serves as a basic yet robust system for managing customer information, focusing on customer profiles and their employment details. The system operates on a one-to-many relationship model, linking customer profiles to their respective employment profiles via a unique customer ID.

The primary objective of this CMS is to facilitate efficient management of customer data. It allows users, categorized into superusers and regular users, to interact with the system and perform various actions on customer and employment records.

## Access the webapp
The app can be accessed online via https://emlowood-sea-a10f0876665d.herokuapp.com/

## Features
User Access Levels: Two types of access are available: superuser and regular user, each with distinct privileges.
CRUD Operations: Superusers can perform Create, Read, Update, and Delete operations on both customer and employment records. Regular users can perform Create, Read, Update on customer records and Create, Read, Delete on employment records.
Unit Tests: Comprehensive unit tests have been developed to ensure the reliability and integrity of the models, views, and URLs.
Frontend Validation: Manual validation has been completed on the frontend to enhance data integrity and user experience.
Technologies Used: The application is built using VS Code as the development environment and Django framework. Default Django apps such as UserCreationForms and authentication mechanisms are utilized. Additionally, Django Crispy Forms, Bootstrap, and Font Awesome for icons are integrated into the frontend. The default SQLite database is employed for data storage, and Heroku is utilized for deployment.

### Note on Naming Conventions
In this project, the Django model classes are named using snake_case (all lowercase with underscores between words) instead of the typical CamelCase used in Python. This was an early design decision and changing it now could potentially break the code.

While this doesn't affect the functionality of the application, it's important to be aware of this if you're contributing to the project or using it as a reference. When referring to these models in your code, make sure to use the correct case.

For example, to import the `customer` model, you would use:

```python
from .models import customer
```

## Setup and Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/EmmagicalDay/sea.git
    ```

2. Navigate to the project directory:

    ```bash
    cd sea
    ```

3. Install the requirements:

    ```bash
    pip install -r requirements.txt
    ```

4. Run the server:

    ```bash
    python manage.py runserver
    ```

## Deploying to Heroku

1. Create a new Heroku app:

    ```bash
    heroku create
    ```

2. Push the code to Heroku:

    ```bash
    git push heroku master
    ```

3. Run the web process:

    ```bash
    heroku ps:scale web=1
    ```

## Setting Up a Superuser

To create a superuser for the Django admin interface, follow these steps:

1. Activate your virtual environment:

    ```bash
    source env/bin/activate  # On Windows, use `env\Scripts\activate`
    ```

2. Navigate to the project directory:

    ```bash
    cd sea
    ```

3. Run the following command:

    ```bash
    python manage.py createsuperuser
    ```

4. You will be prompted to enter a username, email address, and password for the superuser. Enter the information as prompted.

5. Once the superuser is created, you can access the Django admin interface by starting the server with `python manage.py runserver` and navigating to `http://localhost:8000/admin` in your web browser.


## Existing Superuser details
Username: admin
Password: seatemp123#

## Existing regular user details
Username: usertest1
Password: SEAtest2024

## Testing

The tests folder houses files for unit tests, as an example, `test_forms.py` file contains unit tests for the forms in the web application. These tests are designed to ensure that the forms behave as expected when given valid, invalid, and missing data.

### Test Cases

- **Test with valid data:** Each form has a test case where all fields are filled with valid data. The test asserts that the form is valid and doesn't have any errors.

- **Test with no data:** Each form has a test case where no data is provided. The test asserts that the form is invalid and counts the number of errors to ensure it matches the number of required fields.

- **Test with missing data on one field:** The `CreateEmploymentForm` has a test case where one field is left empty. The test asserts that the form is invalid and has one error.

- **Test with incorrect data type:** The `CreateEmploymentForm` has a test case where the `employment_salary` field is filled with a string instead of a number. The test asserts that the form is invalid and has one error.

### Running the Tests

To run the tests, navigate to the project directory in your terminal and run the following command:

```bash
python manage.py test webapp
```

Similar unit tests have been created for models, urls and views.


## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.
