# Healthcare Backend Setup Guide for Windows

## System Requirements
- Windows 10 or Windows 11
- At least 4GB RAM
- 2GB free disk space
- Internet connection

## Step 1: Install Python
1. Go to https://www.python.org/downloads/
2. Download Python 3.11 or 3.12 (latest stable version)
3. Run the installer
4. IMPORTANT: Check "Add Python to PATH" during installation
5. Click "Install Now"
6. Verify installation by opening Command Prompt and typing:
   ```
   python --version
   ```

## Step 2: Install PostgreSQL
1. Go to https://www.postgresql.org/download/windows/
2. Download PostgreSQL 15 or 16 (latest stable version)
3. Run the installer as Administrator
4. During installation:
   - Choose installation directory (default is fine)
   - Select all components (PostgreSQL Server, pgAdmin 4, Command Line Tools)
   - Choose data directory (default is fine)
   - Set superuser password (REMEMBER THIS PASSWORD!)
   - Port: 5432 (default)
   - Locale: Default locale
5. Complete the installation
6. PostgreSQL should start automatically

## Step 3: Setup PostgreSQL Database
1. Open pgAdmin 4 from Start Menu
2. Connect to PostgreSQL server:
   - Right-click "PostgreSQL 15" (or your version)
   - Click "Connect Server"
   - Enter the password you set during installation
3. Create database and user:
   - Right-click "Databases" → "Create" → "Database"
   - Database name: healthcare_db
   - Owner: postgres
   - Click "Save"
4. Create user for Django:
   - Right-click "Login/Group Roles" → "Create" → "Login/Group Role"
   - General tab: Name = healthcare_user
   - Definition tab: Password = healthcare123 (or your choice)
   - Privileges tab: Check "Can login?" and "Superuser"
   - Click "Save"

## Step 4: Download and Setup the Project
1. Download the project files (all Python files, frontend.html, etc.)
2. Create a folder on Desktop called "healthcare_backend"
3. Extract/copy all project files into this folder
4. The folder structure should look like:
   ```
   healthcare_backend/
   ├── manage.py
   ├── healthcare_backend/
   │   ├── __init__.py
   │   ├── settings.py
   │   ├── urls.py
   │   └── wsgi.py
   ├── authentication/
   ├── patients/
   ├── doctors/
   ├── mappings/
   ├── frontend.html
   └── requirements.txt
   ```

## Step 5: Create requirements.txt file
Create a file called requirements.txt in the main project folder with this content:
```
Django==4.2.7
djangorestframework==3.14.0
djangorestframework-simplejwt==5.3.0
psycopg2-binary==2.9.9
python-decouple==3.8
django-cors-headers==4.3.1
```

## Step 6: Create Virtual Environment
1. Open Command Prompt as Administrator
2. Navigate to your project folder:
   ```
   cd C:\Users\YourUsername\Desktop\healthcare_backend
   ```
3. Create virtual environment:
   ```
   python -m venv healthcare_env
   ```
4. Activate virtual environment:
   ```
   healthcare_env\Scripts\activate
   ```
   You should see (healthcare_env) at the beginning of your command prompt

## Step 7: Install Required Packages
With virtual environment activated, run:
```
pip install -r requirements.txt
```

If you get errors, install packages individually:
```
pip install Django
pip install djangorestframework
pip install djangorestframework-simplejwt
pip install psycopg2-binary
pip install python-decouple
pip install django-cors-headers
```

## Step 8: Create Environment File
1. Create a file called .env in the main project folder (same level as manage.py)
2. Add this content to the .env file:
```
SECRET_KEY=evdustp*mh(=47(e@iednx2icg=@+(go3&1ah6x%_uz@@8%jm$
DEBUG=True
DB_NAME=healthcare_db
DB_USER=healthcare_user
DB_PASSWORD=healthcare123
DB_HOST=localhost
DB_PORT=5432
```
Note: Replace healthcare123 with the password you set for healthcare_user

## Step 9: Create Django Apps
Run these commands one by one:
```
python manage.py startapp authentication
python manage.py startapp patients
python manage.py startapp doctors
python manage.py startapp mappings
```

## Step 10: Setup Project Files
You need to create the following files with the provided code:

### A. Update healthcare_backend/settings.py
Replace the content with the settings.py code from the guide

### B. Create authentication/models.py
Add the CustomUser model code

### C. Create patients/models.py
Add the Patient model code

### D. Create doctors/models.py
Add the Doctor model code

### E. Create mappings/models.py
Add the PatientDoctorMapping model code

### F. Create all serializers files:
- authentication/serializers.py
- patients/serializers.py
- doctors/serializers.py
- mappings/serializers.py

### G. Create all views files:
- authentication/views.py
- patients/views.py
- doctors/views.py
- mappings/views.py

### H. Create all URL files:
- healthcare_backend/urls.py (main URLs)
- authentication/urls.py
- patients/urls.py
- doctors/urls.py
- mappings/urls.py

## Step 11: Database Migration
Run these commands in order:
```
python manage.py makemigrations
python manage.py migrate
```

If you get errors, try:
```
python manage.py makemigrations authentication
python manage.py makemigrations patients
python manage.py makemigrations doctors
python manage.py makemigrations mappings
python manage.py migrate
```

## Step 12: Create Admin User (Optional)
```
python manage.py createsuperuser
```
Enter username, email, and password when prompted

## Step 13: Test the Server
1. Start the Django server:
   ```
   python manage.py runserver
   ```
2. You should see:
   ```
   Watching for file changes with StatReloader
   Performing system checks...
   System check identified no issues (0 silenced).
   Django version 4.2.7, using settings 'healthcare_backend.settings'
   Starting development server at http://127.0.0.1:8000/
   Quit the server with CTRL-BREAK.
   ```

## Step 14: Test the Frontend
1. Keep the Django server running
2. Open frontend.html in your web browser (double-click the file)
3. Try to register a new user
4. If registration works, you're all set!

## Common Issues and Solutions

### Issue 1: "python is not recognized as an internal or external command"
Solution: Reinstall Python and make sure "Add Python to PATH" is checked

### Issue 2: PostgreSQL connection failed
Solution: 
- Make sure PostgreSQL service is running (check Services in Windows)
- Verify username, password, and database name in .env file
- Check if the database healthcare_db exists in pgAdmin

### Issue 3: psycopg2-binary installation failed
Solution:
```
pip install --upgrade pip
pip install psycopg2-binary --no-cache-dir
```

### Issue 4: Module not found errors
Solution: Make sure virtual environment is activated:
```
healthcare_env\Scripts\activate
```

### Issue 5: CORS errors in browser
Solution: Make sure django-cors-headers is installed and properly configured in settings.py

### Issue 6: Database migration errors
Solution:
1. Delete migration files (keep __init__.py):
   ```
   del authentication\migrations\0*.py
   del patients\migrations\0*.py
   del doctors\migrations\0*.py
   del mappings\migrations\0*.py
   ```
2. Run migrations again:
   ```
   python manage.py makemigrations
   python manage.py migrate
   ```

## Testing the API Endpoints
Once everything is running, you can test these endpoints:

1. Register: http://localhost:8000/api/auth/register/
2. Login: http://localhost:8000/api/auth/login/
3. Patients: http://localhost:8000/api/patients/
4. Doctors: http://localhost:8000/api/doctors/
5. Mappings: http://localhost:8000/api/mappings/

## Stopping the Application
1. Press Ctrl+C in the Command Prompt to stop the Django server
2. Type: deactivate (to exit virtual environment)
3. Close Command Prompt

## Starting the Application Again
1. Open Command Prompt
2. Navigate to project folder:
   ```
   cd C:\Users\YourUsername\Desktop\healthcare_backend
   ```
3. Activate virtual environment:
   ```
   healthcare_env\Scripts\activate
   ```
4. Start server:
   ```
   python manage.py runserver
   ```
5. Open frontend.html in browser

## Project Structure Summary
```
healthcare_backend/
├── .env                          # Environment variables
├── manage.py                     # Django management script
├── requirements.txt              # Python dependencies
├── frontend.html                 # Web interface
├── healthcare_env/               # Virtual environment (auto-created)
├── healthcare_backend/           # Main Django app
│   ├── settings.py              # Django configuration
│   ├── urls.py                  # Main URL routing
│   └── ...
├── authentication/               # User authentication
│   ├── models.py                # User model
│   ├── serializers.py           # API serializers
│   ├── views.py                 # API views
│   └── urls.py                  # Auth URLs
├── patients/                     # Patient management
├── doctors/                      # Doctor management
└── mappings/                     # Patient-doctor assignments
```

## Support
If you encounter any issues:
1. Make sure all steps were followed correctly
2. Check that PostgreSQL is running
3. Verify virtual environment is activated
4. Check the Django server logs for error messages
5. Ensure all required files are created with correct content

