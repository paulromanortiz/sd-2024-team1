
# Django Starter Project  

This is a basic Django starter project designed for learning purposes. It includes user authentication (using Django Allauth), a simple home page, and a protected dashboard with notifications. This project serves as an introduction to Django’s core concepts, such as views, templates, authentication, and static files.

---

## Features

- **User Authentication:** Login, signup, and logout functionality using [Django Allauth](https://django-allauth.readthedocs.io/).  
- **Home Page:** Public home page with links to login and dashboard.  
- **Dashboard:** Displays notifications, accessible only to logged-in users.  
- **Admin Panel:** Manage users and other site components via Django’s built-in admin.  
- **Modular Design:** Clean project structure for easy extension.

---

## Requirements

- Python 3.x  
- Django 4.x  
- Django Allauth  

---

## Setup Instructions

### 1. Clone the Repository  
```bash
git clone <repository-url>
cd <repository-folder>
```

### 2. Create a Virtual Environment (Optional but Recommended)  
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 3. Install Dependencies  
```bash
pip install django django-allauth
```

### 4. Configure the Database  
Run the following commands to apply migrations and create the initial database:

```bash
python manage.py makemigrations
python manage.py migrate
```

### 5. Create a Superuser  
Create an admin account to manage the site:

```bash
python manage.py createsuperuser
```

### 6. Run the Development Server  
Start the Django server locally:

```bash
python manage.py runserver
```

Visit [http://127.0.0.1:8000](http://127.0.0.1:8000) in your browser.

---

## Project Structure

```plaintext
myproject/
│
├── main/                      # Main Django app
│   ├── migrations/            # Database migrations
│   ├── templates/             # HTML templates
│   │   └── main/              # Templates specific to the main app
│   │       ├── home.html      # Home page template
│   │       └── dashboard.html # Dashboard template
│   ├── static/                # Static files (CSS, JS)
│   ├── views.py               # View logic for the app
│   ├── urls.py                # App URL configuration
│
├── myproject/                 # Main project folder
│   ├── settings.py            # Project settings
│   ├── urls.py                # Project URL configuration
│
└── manage.py                  # Django management script
```

---

## Usage

1. **Home Page:**  
   Open [http://127.0.0.1:8000](http://127.0.0.1:8000) to see the home page. You can access links to **Login**, **Signup**, and **Dashboard**.

2. **Admin Panel:**  
   Visit [http://127.0.0.1:8000/admin](http://127.0.0.1:8000/admin) to manage the site using the superuser account.

3. **Dashboard:**  
   After logging in, go to the dashboard at [http://127.0.0.1:8000/dashboard](http://127.0.0.1:8000/dashboard) to see notifications and other protected content.

---

## Extending the Project

- **Add New Models:** Define new models in `main/models.py` and create migrations using:
  ```bash
  python manage.py makemigrations
  python manage.py migrate
  ```

- **Add Views and Templates:** Add new views in `main/views.py` and create corresponding templates in `main/templates/main/`.

- **Customize Authentication:** Modify the authentication views using Django Allauth’s customization options.

---

## Troubleshooting

- **Static Files Not Loading:** Ensure `DEBUG=True` in `settings.py` for local development.  
- **Authentication Issues:** Make sure the database migrations are applied correctly.  
- **Error Accessing Admin Panel:** Double-check that you created a superuser with:
  ```bash
  python manage.py createsuperuser
  ```

---

## License

This project is open-source and available under the [MIT License](https://opensource.org/licenses/MIT).

---

## Contribution

Feel free to fork the repository, open issues, or submit pull requests to improve this project.

---

Happy coding! 🎉