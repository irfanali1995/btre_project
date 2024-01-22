# BT Real Estate App

This is a real estate listing web application built with Django.

# Technology Stack
- Django
- Python
- SQLite Database
- Bootstrap CSS Framework

# Features
- Home, About, Listings, Single Listing, Search, Register, Login, and Dashboard pages
- Mobile friendly responsive design
- Search listings by keyword, city, state, bedrooms and price
- Paginated listings
- Listing page with images, details, inquiry form
- Contact form inquiries emailed to realtors
- Admin dashboard to manage listings, realtors, inquiries
- Role based users (staff vs non-staff)

# App Walkthrough
- Homepage - Hero image and search bar
- About - List of realtors
- Featured Listings - Paginated list of properties
- Single Listing - Detailed view with images and inquiry form
- Search Results - Returns filtered listings
- Register - User signup
- Login - User login
- Dashboard - Shows user inquiries

# Running the Project
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

- Migrate Datebase 
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
