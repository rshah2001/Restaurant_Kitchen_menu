# Restaurant Website

Welcome to the **Restaurant Website**! This project is a web application that allows users to explore a dynamic menu of meals and dishes offered by a restaurant. The application is built using Django and Bootstrap for a smooth user experience.

## Table of Contents

- [Features](#features)
- [Technologies](#technologies)
- [Setup](#setup)
- [Usage](#usage)
- [Screenshots](#screenshots)
- [Contributing](#contributing)
- [License](#license)

## Features

- Display a dynamic restaurant menu with categorized meals.
- Show available and unavailable meals, including pricing and descriptions.
- Navigate easily with a clean, modern user interface.
- Responsive design for mobile and desktop users.
- Simple call-to-action buttons to view more details about each meal.
- Easy-to-update menu items and categories.

## Technologies

- **Django**: Backend framework for managing the application.
- **HTML/CSS**: Frontend for structuring and styling pages.
- **Bootstrap**: For responsive and modern design.
- **SQLite**: Default Django database used for simplicity.
- **Python**: The core language for building the application.

## Setup

### Prerequisites

- Python 3.x installed on your machine.
- Django installed (`pip install django`).
- Git installed to clone this repository.

### Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/your-username/restaurant-website.git
    ```

2. Navigate to the project directory:

    ```bash
    cd restaurant-website
    ```

3. Install the required dependencies:

    ```bash
    pip install -r requirements.txt
    ```

4. Run database migrations:

    ```bash
    python manage.py migrate
    ```

5. Run the development server:

    ```bash
    python manage.py runserver
    ```

6. Open your browser and go to `http://127.0.0.1:8000/` to see the application in action.

## Usage

- Visit the homepage to explore the restaurant menu.
- Navigate through different categories of meals.
- Click on a meal item to see more details.
- Unavailable items are visually marked with a strikethrough.
- Use the admin panel to add new menu items or update existing ones.

## Screenshots

Here are some screenshots of the application in action:

### Welcome Page
<img width="781" alt="Screenshot 2024-09-14 at 1 59 18 PM" src="https://github.com/user-attachments/assets/f8f90d27-d930-43e7-982d-6ddded238ffd">

### Menu Page
<img width="983" alt="Screenshot 2024-09-14 at 1 59 41 PM" src="https://github.com/user-attachments/assets/ec1cea10-a54c-45d4-9a1c-e42b9c3ae6d9">

### Admin Page
<img width="1700" alt="Screenshot 2024-09-14 at 2 00 18 PM" src="https://github.com/user-attachments/assets/65054d9e-3cb7-4ccc-a355-2c90aa380c51">
<img width="737" alt="Screenshot 2024-09-14 at 2 00 36 PM" src="https://github.com/user-attachments/assets/13703e73-ed76-4664-8661-e3d2f4a0ab50">





## Contributing

We welcome contributions to improve this project. To contribute:

1. Fork the repository.
2. Create a new branch (`git checkout -b feature-branch`).
3. Make your changes.
4. Commit your changes (`git commit -m 'Add new feature'`).
5. Push to the branch (`git push origin feature-branch`).
6. Open a pull request.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.
