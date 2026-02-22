🏫 Campus Management System (Django)

A Django-based Campus Management System where Students 👨‍🎓 and Faculty 👩‍🏫 can view:

🏢 Campus Blocks

🚪 Classrooms (Room Numbers)

📚 Courses

👨‍🏫 Faculty assigned to courses

📊 Block-wise utilization & workload

Admins 🔐 can manage (add/update/delete) data, while Students and Teachers have view-only access.

✨ Features
👨‍🎓 Students & 👩‍🏫 Faculty Can:

View all 🏢 campus blocks

Filter data based on selected block

View:

🚪 Classrooms under that block

📚 Courses assigned to that block

👨‍🏫 Faculty workload (number of assigned courses)

See which teacher is assigned to which course

🔐 Admin Can:

Add / Edit / Delete:

🏢 Campus Blocks

🚪 Classrooms

📚 Courses

👩‍🏫 Faculty

👨‍🎓 Students

Assign courses to faculty

Manage block-wise course allocation

🗂 Project Structure
📦 Models

CampusBlock

name

location

Classroom

block (ForeignKey)

name

capacity

Course

code

name

credits

block (ForeignKey)

Faculty

user (OneToOne with Django User)

courses (ManyToMany)

Student

user (OneToOne with Django User)

roll_no

courses (ManyToMany)

🔎 Dashboard Functionality

The dashboard:

Shows all blocks

Allows filtering by selected block

Displays:

Classrooms under selected block

Courses under selected block

Faculty workload (based only on selected block)

🛠 Tech Stack

🐍 Python

🌐 Django

🗄 SQLite (default)

🎨 HTML + Bootstrap (Frontend)

🚀 How to Run the Project
# Clone repository
git clone <your-repo-link>

# Move into project
cd project-folder

# Create virtual environment
python -m venv venv

# Activate virtual environment
# Windows
venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Apply migrations
python manage.py makemigrations
python manage.py migrate

# Create superuser
python manage.py createsuperuser

# Run server
python manage.py runserver

Open in browser:

http://127.0.0.1:8000/
🔐 Authentication Flow

Users login via Django authentication

After login → Redirect to Dashboard

Logout redirects to login page

📌 Future Improvements (Optional Ideas)

📅 Timetable management

📝 Attendance system integration

📊 Graphical analytics for block utilization

👥 Role-based dashboard (Separate Student/Faculty UI)

🍽 Food Stall module integration (as discussed 😄)
