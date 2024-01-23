<h1 align="center"> BT Real Estate  WebApp</h1>

## Table of Contents

- [About the Project](#chapter-1) 

- [Technology Stack](#chapter-2)

- [Features](#chapter-3)

- [App Walkthrough](#chapter-4)

- [Usage](#chapter-5)

- [Aknowledgement](#chapter-6)

## About the Project <a id="chapter-1"></a>
This is a real estate listing web application built with Django.

<img src="https://github.com/irfanali1995/btre_project/assets/75564524/94e86231-0a54-4e64-831d-e6d6a3bb02c1" width="200" height="150">

<img src="https://github.com/irfanali1995/btre_project/assets/75564524/db914a2e-a15f-457c-ab5e-4e455c75b003" width="200" height="150">

<img src="https://github.com/irfanali1995/btre_project/assets/75564524/482d1fb6-008a-4963-bc28-43b0a86b8e02" width="200" height="150">

<img src="https://github.com/irfanali1995/btre_project/assets/75564524/85fdb4b0-365a-40ec-b814-813437f6670d" width="200" height="150">

## Technology Stack <a id="chapter-2"></a>
- Django
- Python
- Postgresql Database
- Bootstrap CSS Framework

## Features <a id="chapter-3"></a>
- Home, About, Listings, Single Listing, Search, Register, Login, and Dashboard pages
- Mobile friendly responsive design
- Search listings by keyword, city, state, bedrooms and price
- Paginated listings
- Listing page with images, details, inquiry form
- Contact form inquiries emailed to realtors
- Admin dashboard to manage listings, realtors, inquiries
- Role based users (staff vs non-staff)

## App Walkthrough <a id="chapter-4"></a>
- Homepage - Hero image and search bar
- About - List of realtors
- Featured Listings - Paginated list of properties
- Single Listing - Detailed view with images and inquiry form
- Search Results - Returns filtered listings
- Register - User signup
- Login - User login
- Dashboard - Shows user inquiries

## Usage <a id="chapter-5"></a>
- Clone Repo using git
```
  git clone (repo-link)
```

- Initiate virtual envornment in project directory
```
  python3 -m venv env
```
  
- Activate virtual envornment (Mac)
```
  source env/bin/activate
```
- Activate virtual envornment (Mac)
```
  source env/bin/activate
```

- Migrate Datebase (**Note**:Before this step you need to install posgresql and pgadmin) 
```
python manage.py makemigrations
```

```
python manage.py migrate
```

- Create Admin User (Needed to access admin panel)
```
python manage.py createsuperuser
```

- Run Deployement Server 
```
python manage.py runserver 
```
The app will be served at http://127.0.0.1:8000 

## Aknowledgement <a id="chapter-6"></a>
- [Brad Traversy](https://github.com/bradtraversy)

  

