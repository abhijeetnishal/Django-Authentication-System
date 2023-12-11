# Django Authentication Project

## Introduction
This Django authentication project provides a robust authentication system for your web application, built on the Django framework. It includes features such as user registration, login, logout, password reset, and more.

## Features
- **User Registration**: Allow users to create accounts with a secure registration process.
- **Login and Logout**: Secure user authentication with login and logout functionality.
- **Password Reset**: Enable users to reset their passwords securely.
- **User Profile**: Customize user profiles with additional information.
- **Dockerized**: Easily deploy the application using Docker for consistent environments.

## Prerequisites
Make sure you have the following installed before running the application:
- [Docker](https://docs.docker.com/get-docker/)

## Running the Application using docker
1. Clone the repository:
```bash
   git clone https://github.com/abhijeetnishal/Django-Authentication-System.git
```
2. Navigate to the project directory:
```bash
    cd Django-Authentication-System
```
3. Make sure that docker is installed in your system. Run the below command to build docker image:
```bash
    docker build -t your_image_name .
```
4. Run a container based on your_image_name using below command, exposing port 8080 on the host machine and mapping it to port 8080 inside the container
```bash
    docker run -p 8080:8080 yor_image_name
```
5. Now open Postman or other API testing tool to test the API. 
    - POST /signup: http://localhost:8080/api/v1/auth/signup
    - POST /login: http://localhost:8080/api/v1/auth/login