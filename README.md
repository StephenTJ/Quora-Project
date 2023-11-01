# Quora Project

### Hosted on AWS Lambda and Postgresql Server Azure

https://rc1p0fogab.execute-api.ap-south-1.amazonaws.com/dev

**Note:** To ensure proper functioning, the application needs to be viewed on a desktop.

### Steps for running the project locally

1. **Create a Virtual Environment :**
  
  `python -m venv env`
  
2. **Activate the virtual Environment :**
  
  `env\Scripts\activate`
  
3. **Install Dependencies :**
  
  `pip install -r requirements.txt`
  
4. **Connect the database and run these commands :**
  
  1. **Create Initial Migrations:**
    
    `python manage.py makemigrations`
    
  2. **Apply Migrations to the Database**:
    
    `python manage.py migrate`
    
5. **Run the Development Server**:
  
  `python manage.py runserver`
  

---
