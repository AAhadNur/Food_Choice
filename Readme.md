# <div style="text-align:center">Food Choice</div>

Welcome to the Brain Station 23 Lunch Voting App! This project is designed to provide the solution involves creating a dynamic voting app where employees can participate in deciding the menu for the day. The app ensures fairness and inclusivity by allowing everyone to vote for their favorite dishes, with the winning menu chosen for the day.

## Table of Contents

1. [Overview](#overview)
2. [Installation Process](#installation-process)
3. [API Documentation](#api-documentation)
   - [User Registration API](#user-registration-api)
   - [Login API](#login-api)
   - [Logout API](#logout-api)
   - [Restaurant List Create Api](#restaurant-list-create-api)
   - [Restaurant Detail Update Delete Api](#restaurant-detail-update-delete-api)
   - [Menu List Create Api](#menu-list-create-api)
   - [Menu Detail Update Delete Api](#menu-detail-update-delete-api)
   - [Current Day Menu Api](#current-day-menu-api)
   - [Vote Create Api](#vote-create-api)
   - [Feedback List Api](#feedback-list-api)
   - [Feedback Create Api](#feedback-create-api)
   - [Daily Results List Api](#daily-results-list-api)
   - [Daily Results Create Api](#daily-results-create-api)
   - [Current Date Result Api](#current-date-result-api)

## Overview

In Food Choice App, users can sign up and get associated with an employee profile by default. Superusers have the exclusive authority to upgrade users to administrators, who can then perform CRUD operations on restaurants and menus. Employee users, the majority of the users, have the ability to vote on menus and provide valuable feedback. I've implemented a daily results API that calculates and displays the winning restaurant and menu for the current day. To maintain fairness, this API ensures that no restaurant can win three consecutive working days. This user-centric approach, coupled with automated processes, ensures an inclusive, engaging, and fair lunch selection experience for all users.

### Project Features

- **User Authentication:** Secure registration, login, and logout functionalities.
- **User Profiles:** Automatic creation of user profiles with "employee" user type upon signup.
- **Administrator Privileges:** Superusers can upgrade users to "administrator," granting CRUD operations on restaurants and menus.
- **Restaurant Management:** CRUD operations for creating, updating, and deleting restaurant details.
- **Menu Management:** CRUD operations for managing restaurant menus, including retrieving the current day's menu.
- **Voting System:** Employees can cast votes for preferred menus.
- **Feedback System:** Users can provide feedback on menus.
- **Daily Results API:** Calculates and displays the winning restaurant and menu for the day.
- **Preventing Consecutive Wins:** Daily results API ensures no restaurant wins three consecutive working days.

### Project ER diagram

![ER Diagram](https://github.com/AAhadNur/Food_Choice/blob/main/static/diagrams/er.png)

Also, see my `SRS.md` and `DB_Schema.md` for more deatils.

## Installation Process

Al the things you need to do for installing this project on your computer are described properly in this section.

### Prerequisites

It is assumed that following prerequisites are already installed in your machine. If not, then install these before proceed

- Python
- MySQL Server

### Virtual Environment Setup

First, create an virtual environment

```bash
virtualenv venv
```

Then, activate the virtual environment

```bash
source venv/bin/activate
```

### Clone the repository

```bash
git clone https://github.com/AAhadNur/Food_Choice.git
cd Food_Choice
```

### Install Python Dependencies

```bash
pip install -r requirements.txt
```

### Environment variable configuration

I have put django secret key and database credentials in a seperate environment vaiable file in the base project directory and connected it with settings.py. So, you also need to configure your `.env` file with your own credentials.

- First, create the `.env` file in the base project directory where `manage.py` situated.
- Include the following variables in your `.env` file.

```bash
# Django settings
SECRET_KEY = django_secret_key
DEBUG = True

# Database configuration
DB_NAME = your_database_name
DB_USER = your_database_user
DB_PASSWORD = your_database_password_here
DB_HOST = localhost
DB_PORT = 3306
```

### Start the development server

Now, you are ready to go. Run the development server.

```bash
python3 manage.py runserver
```

Follow all the steps properly to install this project. If you face any problems or you have any suggestions please create an issue in this repository.

## API Documentation

## **User Registration API**

Returns json data about a single user.

- **URL**

  http://127.0.0.1:8000/api/signup/

- **Method:**

  `POST`

- **Data Params**

  ```
  {
    "username": "riad",
    "email": "riad@gmail.com",
    "password": "commonpass"
  }
  ```

- **Success Response:**

  - **Code:** 200 <br />
    **Content:**
    ```
    {
        "user": {
            "id": 4,
            "username": "riad",
            "email": "riad@gmail.com"
        },
        "token": "a5c51f653e217202a16f99dbb984e53ed38ce69c805ada01c37e0fbead2ac74f"
    }
    ```

## **Login API**

Logs in user with proper credentials.

- **URL**

  http://127.0.0.1:8000/api/login/

- **Method:**

  `POST`

- **Data Params**

  ```
  {
    "username": "riad",
    "password": "commonpass"
  }
  ```

- **Success Response:**

  - **Code:** 200 <br />
    **Content:**
    ```
    {
        "user": {
            "id": 4,
            "username": "riad",
            "email": "riad@gmail.com"
        },
        "token": "1e50625199477f652b72b776283c5e3a2818f1b896b60070c2d0678bba8ecbab",
        "details": "Logged in successfully"
    }
    ```

- **Error Response: (example)**

  - **Code:** 400 Bad Request <br />
    **Content:**
    ```
    {
        "non_field_errors": [
            "Unable to log in with provided credentials."
        ]
    }
    ```

## **Logout API**

Logout user by deleting token.

- **URL**

  http://127.0.0.1:8000/api/logout/

- **Method:**

  `POST`

- **Data Params**

  `None`

- **Success Response:**

  - **Code:** 200 <br />
    **Content:**
    ```
    {
        "details": "Successfully logged out"
    }
    ```

## **Restaurant List Create Api**

Listing all restaurants and creating new ones.

- **URL**

  http://127.0.0.1:8000/api/restaurants/

- **Method:**

  `GET`

- **Data Params**

  `None`

- **Success Response:**

  - **Code:** 200 <br />
    **Content:**
    ```
    [
        {
            "id": 1,
            "restaurant_name": "Food Panda",
            "description": "",
            "location": "Tejgaon",
            "contact_number": "+880171832736",
            "rating": "4.78",
            "restaurant_image": null,
            "winning_strike": 2,
            "managing_admin": 2
        }
    ]
    ```

- **Method:**

  `POST`

- **Data Params**

  ```
  {
      "id": 2,
      "restaurant_name": "Haji Kacchi",
      "description": "",
      "location": "Tejgaon",
      "contact_number": "+880171832736",
      "rating": "4.78",
      "restaurant_image": null,
      "winning_strike": 2,
      "managing_admin": 2
  }
  ```

- **Success Response:**

  - **Code:** 200 <br />
    **Content:**
    ```
    {
        "id": 2,
        "restaurant_name": "Haji Kacchi",
        "description": "",
        "location": "Tejgaon",
        "contact_number": "+880171832736",
        "rating": "4.78",
        "restaurant_image": null,
        "winning_strike": 2,
        "managing_admin": 2
    }
    ```

## **Restaurant Detail Update Delete Api**

API for retrieving, updating, and deleting individual restaurants.

- **URL**

  http://127.0.0.1:8000/api/restaurants/id/

- **Method:**

  `GET`

  - For retrieving specific restaurant

- **Method:**

  `PUT`

  - For updating specific restaurant

- **Method:**

  `DELETE`

  - For deleting specific restaurant

## **Menu List Create Api**

Listing all menus and creating new ones.

- **URL**

  http://127.0.0.1:8000/api/menus/

- **Method:**

  `GET`

- **Data Params**

  `None`

- **Success Response:**

  - **Code:** 200 <br />
    **Content:**
    ```
    [
        {
            "id": 1,
            "dish_name": "salad",
            "description": "carrot",
            "price": "20.00",
            "date": "2024-01-31",
            "restaurant": 1
        }
    ]
    ```

- **Method:**

  `POST`

- **Data Params**

  ```
  {
      "id": 1,
      "dish_name": "fried rice",
      "description": "",
      "price": "50.00",
      "date": "2024-01-31",
      "restaurant": 1
  }
  ```

- **Success Response:**

  - **Code:** 200 <br />
    **Content:**
    ```
    {
        "id": 1,
        "dish_name": "fried rice",
        "description": "",
        "price": "50.00",
        "date": "2024-01-31",
        "restaurant": 1
    }
    ```

## **Menu Detail Update Delete Api**

API for retrieving, updating, and deleting individual restaurants.

- **URL**

  http://127.0.0.1:8000/api/menus/id/

- **Method:**

  `GET`

  - For retrieving specific menu

- **Method:**

  `PUT`

  - For updating specific menu

- **Method:**

  `DELETE`

  - For deleting specific menu

## **Current Day Menu Api**

Retrieving the menu for the current day.

- **URL**

  http://127.0.0.1:8000/api/menus/current-day/

- **Method:**

  `GET`

- **Data Params**

  `None`

- **Success Response:**

  - **Code:** 200 <br />
    **Content:**
    ```
    [
        {
            "id": 1,
            "dish_name": "salad",
            "description": "carrot",
            "price": "20.00",
            "date": "2024-01-31",
            "restaurant": 1
        },
        {
            "id": 1,
            "dish_name": "fried rice",
            "description": "",
            "price": "50.00",
            "date": "2024-01-31",
            "restaurant": 1
        }
    ]
    ```

## **Vote Create Api**

Allowing employee-type users to vote on a specific menu.

- **URL**

  http://127.0.0.1:8000/api/vote-create/

- **Method:**

  `POST`

- **Data Params**

  ```
  {
    "voter":"riad",
    "menu":"fried rice"
  }
  ```

- **Success Response:**

  - **Code:** 200 <br />

## **Feedback List Api**

Listing all feedbacks.

- **URL**

  http://127.0.0.1:8000/api/feedbacks/

- **Method:**

  `GET`

- **Data Params**

  `None`

- **Success Response:**

  - **Code:** 200 <br />
    **Content:**
    ```
    [
        {
            "id": 1,
            "date_time": "2024-02-01T07:12:27.484834Z",
            "feedback_text": "nice",
            "employee": 1,
            "menu": 1
        }
    ]
    ```

## **Feedback Create Api**

Creating new feedback.

- **URL**

  http://127.0.0.1:8000/api/feedbacks/create/

- **Method:**

  `POST`

- **Data Params**

  ```
  {
      "id": 2,
      "date_time": "2024-02-01T07:12:27.484834Z",
      "feedback_text": "good",
      "employee": 1,
      "menu": 1
  }
  ```

- **Success Response:**

  - **Code:** 200 <br />

## **Daily Results List Api**

Listing all DailyResults.

- **URL**

  http://127.0.0.1:8000/api/daily-results/

- **Method:**

  `GET`

- **Data Params**

  `None`

- **Success Response:**

  - **Code:** 200 <br />
    **Content:**
    ```
    [
        {
            "id": 1,
            "result_date": "2024-01-31",
            "votecount": 5,
            "winning_menu": 1,
            "winning_restaurant": 1
        }
    ]
    ```

## **Daily Results Create Api**

Finds the winning restaurant of current date.

- **URL**

  http://127.0.0.1:8000/api/daily-results/create/

- **Method:**

  `GET`

- **Data Params**

  `None`

- **Success Response:**

  - **Code:** 200 <br />
    **Content:**
    ```
    {
        'winning menu': 'Salad',
        'winning restaurent': 'Food Panda',
        'details': 'Fair selection applied'
    }
    ```

## **Current Date Result Api**

Returns the DailyResults of the current date.

- **URL**

  http://127.0.0.1:8000/api/daily-results/current-date/

- **Method:**

  `GET`

- **Data Params**

  `None`

- **Success Response:**

  - **Code:** 200 <br />
    **Content:**
    ```
    {
        "id": 1,
        "result_date": "2024-01-31",
        "votecount": 5,
        "winning_menu": 1,
        "winning_restaurant": 1
    }
    ```

- **Error Response:**

  - **Code:** 404 NOT FOUND <br />
    **Content:** `{ "detail" : "No DailyResults found for the current date." }`
