# CarDealer Website

Welcome to the CarDealer website, a full-stack web application developed as a capstone project showcasing expertise in full-stack development. This project aims to provide a comprehensive platform for managing car dealership operations, including inventory management, customer interactions, and more.

## Features

- **Inventory Management**: Easily manage the inventory of new and used vehicles, including adding, updating, and removing listings.
- **User Authentication**: Secure user authentication system for both customers and administrators, allowing access to specific features based on user roles.
- **Search and Filter**: Convenient search and filter functionalities to help users find the perfect vehicle based on their preferences.
<!-- - **Sales and Transactions**: Facilitate sales transactions, including generating invoices, managing payments, and tracking sales history. -->
- **Responsive Design**: The website is built with a responsive design, ensuring optimal user experience across various devices and screen sizes.

## Technologies Used

- **Frontend**: HTML, CSS, JavaScript, Bootstrap
- **Backend**: Django (Python), Django REST Framework
- **Database**: PostgreSQL
- **Authentication**: Django Authentication System
- **Deployment**: 

## Installation and Setup

1. **Clone the repository:**

   ```bash
   git clone https://github.com/mb4y4/DriveWay-Deals


2. **Install dependencies:**

   ```bash
   pip install -r requirements.txt

3. **Set up the database:**

   ```bash
   python manage.py migrate

4. **Create a superuser for admin access:**

   ```bash
   python manage.py createsuperuser

5. **Run the development server:**

   ```bash
   python manage.py runserver

6. **Access the website:**

   - **Website:** [http://localhost:8000/](http://localhost:8000/)
   - **Admin Panel:** [http://localhost:8000/admin/](http://localhost:8000/admin/)

## Usage

- **Administrator:**
  Log in to the admin panel ([/admin/](http://localhost:8000/admin/)) to manage inventory, users, and other site configurations.

- **Customers:**
  Browse the inventory, search for vehicles, and initiate transactions as needed.
