<p align="center">
  <img src="assets/challenges/css/anfang1.jpeg">
</p>

<a href="#"><img src="https://img.shields.io/badge/version-1.0.1-brightgreen"></a>
<a href="#"><img src="https://img.shields.io/badge/Made%20with-Django-bright"></a>

## What is ANFANG?
 A collection of small web-security challenges for beginners to get awareness and train themselves with basics.

  <p align="center">
    <img src="assets/challenges/css/final_version.gif">
  </p>

## Features
- Create your own challenges, hints, and flags from the Admin Interface
- Leaderboard - Ordering based on timestamps and points

## Coming in the next versions
- Unlockable hints
- OAuth for Email verification during signup
- Pagination for Home page and Leaderboard
- Dynamic Scoring of Challenges

## Install
- Install all the required packages from the requirements.txt file using:
    ```
    pip3 install -r requirements.txt
    ```
- How to use PostgreSQL with the application
  - Configure Django database settings
    ```
    DATABASES = {
      'default': dj_database_url.config(default='postgresql://anfanguser:anfangphase2_@localhost/anfang', conn_max_age=600)
    }
    ```
  - Now that the Django settings are configured, we can migrate our data structures to our database and test out the server.
    ```
    python manage.py makemigrations
    python manage.py migrate
    ```


- For adding new challenges
  - Enter all the details of the challenge in the databse from the django admin page
    <p align="center">
      <img src="assets/challenges/css/new_challenge.jpeg">
    </p>
  - After adding the new challenge in the database, type the following in the python interactive shell
    ```
    >>> user_relation_when_new_challenge("The Robots")
    ```
    <p align="center">
      <img src="assets/challenges/css/Python_Shell.jpeg">
    </p>

 ## Team:
 ```ruby
 Paul Babu Kadali
 Binesh Munukurthi
 Abhijeet Mahapatra
 Vikranth Kumar Bala
 ```