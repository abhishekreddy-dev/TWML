# **Montclair State University Tutoring System**

![Montclair State University](static/montclair-logo-red.svg)

A modern and efficient web application designed to streamline the tutoring process at Montclair State University. This system allows students to log their visit details and administrators to manage tutoring records effectively through an intuitive interface. Built using **Flask**, **SQLite**, and **Pandas**, the system offers a seamless experience for both students and administrators.

## **Table of Contents**

- [About the Project](#about-the-project)
- [Features](#features)
- [Technologies Used](#technologies-used)
- [Project Structure](#project-structure)
- [Setup and Installation](#setup-and-installation)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)

---

## **About the Project**

The Montclair State University Tutoring System is built to automate the logging of student visits and facilitate the management of tutoring data. It includes an elegant student form to capture basic details such as name, semester, major, and the purpose of visit. Administrators can easily log in, view, filter, add, delete, and download student data via an intuitive dashboard.

This project emphasizes user experience, security, and data management with features like date filtering, CSV downloads, and admin authentication.

---

## **Features**

### **Student Side:**
- **Student Form**: A user-friendly form for students to input their name, semester, major, and other required details.
- **Real-time Timestamp**: Each submission is timestamped, ensuring accurate visit logs.

### **Admin Side:**
- **Secure Admin Login**: Only authenticated admins can access the dashboard.
- **Admin Dashboard**: View and manage student data with options to filter by date.
- **Add/Delete Students**: Ability to manually add or delete student records.
- **Download Data**: Download student data as an Excel file with a single click.
- **Dynamic Filtering**: Filter student records by visit dates using AJAX.

---

## **Technologies Used**

- **Frontend**:
  - HTML5, CSS3
  - JavaScript (for filtering and interactivity)
  - Bootstrap (for responsive design)
  
- **Backend**:
  - Python (Flask Framework)
  - SQLite (Database)
  - Pandas (for Excel export functionality)

- **Additional Libraries**:
  - Jinja2 Templating (for dynamic rendering)
  - JQuery (for AJAX filtering)

---

## **Project Structure**

```
📦 project-root/
├── app.py                # Flask app, routes, and backend logic
├── database.db           # SQLite database file
├── static/
│   ├── style.css         # Custom CSS styles
│   ├── ccis_building.jpg # Background image of CCIS building
│   ├── hawk-logo-color.svg
│   └── montclair-logo-red.svg
├── templates/
│   ├── form.html         # Student form
│   ├── admin_dashboard.html # Admin dashboard
│   ├── admin_login.html  # Admin login page
├── students_data.xlsx     # Excel file for exported data (generated dynamically)
├── README.md              # This file
└── requirements.txt       # List of dependencies
```

---

## **Setup and Installation**

Follow these steps to get the project up and running on your local machine.

### **Prerequisites**

Ensure you have the following installed:
- Python 3.x
- SQLite (comes with Python)
- Flask (use `pip` to install)
  
### **Installation Steps**

1. **Clone the repository:**
   ```bash
   git clone https://github.com/your-username/montclair-tutoring-system.git
   ```

2. **Navigate to the project directory:**
   ```bash
   cd montclair-tutoring-system
   ```

3. **Install required Python packages:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the application:**
   ```bash
   python app.py
   ```

5. **Access the application:**
   Open your browser and navigate to:
   ```
   http://127.0.0.1:5000
   ```

---

## **Usage**

### **For Students:**
- Open the form at the root URL (e.g., `http://127.0.0.1:5000`).
- Fill in the required details and submit the form.

### **For Admins:**
1. Go to the `/admin` URL (e.g., `http://127.0.0.1:5000/admin`).
2. Log in using the admin credentials.
3. Access the dashboard to view, filter, and manage student data.
4. Download the student data as an Excel file when needed.

## **Contributing**

We welcome contributions to improve the project. Feel free to submit pull requests or report issues.

To contribute:
1. Fork the project.
2. Create a new feature branch (`git checkout -b feature/AmazingFeature`).
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`).
4. Push to the branch (`git push origin feature/AmazingFeature`).
5. Open a Pull Request.

---

## **License**

Distributed under the **MIT License**. See `LICENSE` for more information.

---

### **Acknowledgments**

- **Montclair State University** for inspiring this project.
- The open-source community for providing amazing resources and tools.
