# CarDealer Website

Welcome to the CarDealer website, a full-stack web application developed as a capstone project showcasing expertise in full-stack development. This project provides a comprehensive platform for managing car dealership operations, including inventory management, customer interactions, and more.

## Features

- **Inventory Management:** Easily manage the inventory of new and used vehicles, including adding, updating, and removing listings.
- **User Authentication:** Secure user authentication system for both customers and administrators, allowing access to specific features based on user roles.
- **Search and Filter:** Convenient search and filter functionalities to help users find the perfect vehicle based on their preferences.
- **Responsive Design:** The website is built with a responsive design, ensuring optimal user experience across various devices and screen sizes.
- **React Frontend:** The frontend is built using React, providing a dynamic and interactive user experience.

## Technologies Used

- **Frontend:** React, HTML, CSS, JavaScript, Bootstrap
- **Backend:** Django (Python), Django REST Framework
- **Database:** PostgreSQL
- **Authentication:** Django Authentication System
- **Deployment:** [Your Deployment Platform]

## Installation and Setup

1. Clone the repository:

```bash
git clone https://github.com/mb4y4/DriveWay-Deals

2. Install backend dependencies:

```bash
pip install -r requirements.txt

3. Set up the database:

   ```bash
   python manage.py migrate

4. Create a superuser for admin access:

   ```bash
   python manage.py createsuperuser

5. Install frontend dependencies:
   Navigate to the 'frontend' directory:

   ```bash
   cd frontend
   Then install dependencies:

      ```bash
      npm install

6. Build the React frontend:

   ```bash
   npm run build

7. Run the development server:

   ```bash
   python manage.py runserver

8. Access the website:
   - Website: http://localhost:8000/
   - Admin Panel: http://localhost:8000/admin/

## Usage

### Administrator:
- Log in to the admin panel (/admin/) to manage inventory, users, and other site configurations.

### Customers:
- Browse the inventory, search for vehicles, and initiate transactions as needed.