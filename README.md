

---

# Technical Test API

## Project Description

This project is an API for managing an educational system, allowing for the management of students, teachers, subjects, enrollments, and curriculums. 
## Database Structure

### Main Models

- **Student**: Represents a student, with attributes such as `id_student`, `code`, and a one-to-one relationship with `Person`.

- **Teacher**: Represents a teacher with attributes like `id_teacher`, `name`, and other personal details.

- **Subject**: Represents a subject, with attributes such as `id_subject`, `code`, `name`, and a foreign key relationship with `Teacher`. It also includes a many-to-many relationship with itself for prerequisites.

- **Enrollment**: Represents the enrollment of a student in a subject, with attributes such as `student`, `subject`, `grade`, and foreign key relationships with `Subject` and `Student`.

- **Pensum**: Represents an academic curriculum, with attributes like `id_pensum`, `name`, `start_year`, `end_year`, and a many-to-many relationship with `Subject`.

## API Documentation

The API documentation is provided using Swagger, which offers a comprehensive overview of the available endpoints, including their parameters, request/response formats, and example data.

### How to Access Swagger Documentation

1. **Start the Development Server**

   ```bash
   python manage.py runserver
   ```

2. **Open Swagger Documentation**

   Navigate to `http://localhost:8000/swagger/` in your browser to view the interactive API documentation.

## Instructions to Run and Test the API

1. **Clone the Repository**

   ```bash
   git clone https://github.com/richardhbp99/TechnicalTest.git
   cd repository
   ```

2. **Create a Virtual Environment**

   ```bash
   python -m venv venv
   ```

3. **Activate the Virtual Environment**

   - On Windows:
     ```bash
     venv\Scripts\activate
     ```
   - On macOS/Linux:
     ```bash
     source venv/bin/activate
     ```

4. **Install Dependencies**

   ```bash
   pip install -r requirements.txt
   ```

5. **Apply Migrations**

   ```bash
   python manage.py migrate
   ```



6. **Run the Development Server**

   ```bash
   python manage.py runserver
   ```

7. **Test the API**

   Open your browser and go to `http://localhost:8000/swagger/` to access the Swagger documentation.

---
