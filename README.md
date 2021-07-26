# MCQ Platform

**The project is a digital platform to create & attemp tests for practice along with detailed statistical analysis report, designed specifically for GATE Exam**

[Demo](https://mcq-platform.herokuapp.com/)

**Admin**
- Username: admin
- Password: admin

**User**
- Username: test
- Password: test12345

<details open="open">
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#features">Features</a>
      <ul>
        <li><a href="#to-do">To do/Future Work</a></li>
    </ul>
    </li>
    <li>
      <a href="#built-with">Built With</a>
    </li>
    <li> 
      <a href="#built-with">Images</a>
      <ul>
        <li><a href="#user-interface">User Interface</a></li>
        <li><a href="#test-interface">Test Interface</a></li>
        <li><a href="#detailed-analysis">Detailed Analysis & Report</a></li>
        <li><a href="#admin">Admin Interface</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#contact">Contact</a></li>
    <li><a href="#acknowledgements">Acknowledgements</a></li>
  </ol>
</details>

### Features

* Admins / Staff can create Practice Tests / Grand Tests from Admin Panel
* Add different types of questions to tests like MCQ / MSQ / NAT.
* Images support for options and questions.
* Uses built-in auth system of django for users.
* Automatic evaluation of marks and other detailed statistical analysis with solution report.
* Users & Staff, Staff can appoint any user to be able to create and manage tests
* Clean and nice admin-interface to create & manage tests/questions.
* Any user can take available test, view result and see correct answers.
* Detailed statistical analysis and solution report for user
* Auto Submit Test if user is out of time.
* Users can attempt a test for multiple number of times.
* Using imgur as a cloud image storage for image uploads.

### To do

- More detailed analysis using charts/graphs.
- Add messages framework
- Time taken per question.
- Create tests for specific subjects tags
- Question tags
- Support for multiple exams like JEE, CAT, CET, NEET, etc.
- Ability for users to create private/public tests and share link to others to attemp the test

### User-Interface

![picture 1](https://i.imgur.com/tijxFba.png)  

![picture 2](https://i.imgur.com/F3hpSkS.png)  

 
### Test Interface

![picture 3](https://i.imgur.com/Uoj0hsC.png)  


### Detailed Analysis

![picture 4](https://i.imgur.com/L5ZnBn2.png)  

![picture 5](https://i.imgur.com/NSGSKgQ.png)  


### Admin

![picture 6](https://i.imgur.com/Tlpv3xK.png)  

![picture 7](https://i.imgur.com/rQ8yUwp.png)  
 

### Built-with

* Python 3.9
* Django 3.2
* HTML, CSS , JS, Bootstrap

## Getting Started

### Prerequisites

You should have latest version of python installed.

### Installation

1. Clone this repository and extract
    ```
    git clone https://github.com/fnxL/mcq-platform.git
    ```
2. Create python virtual environment in root directory.

    ```
    python -m venv env
    ```
3. Activate the environment. (In command prompt)

    ```
    cd env/Scripts/
    activate.bat
    ```
4. Install requirements

    ```
    pip install -r requirements.txt
    ```
5. Run these commands

    ```
    python maange.py migrate
    python manage.py makemigrations
    python manage.py migrate
    ```
6. Create a superuser account

    ```
    python manage.py createsuperuser
    ```

7. Once super user is created, you can run the server.
    ```
    python manage.py runserver
    ```

**If there are no errors website will be running on http://127.0.0.1:8000/ (default)**

**Access the django admin panel on http://127.0.0.1:800/django to assign staff to users** 


### Contact

Ajay Kanki - ajaykanki.2e@gmail.com
Project Link - https://github.com/fnxL/mcq-platform

### Acknowledgements

* Boostrap 5
* Dash UI bootstrap UI Kit
* Datatables
* [Imgurstorage for django](https://github.com/preetamherald/django-imgur) 
* Font Awesome
