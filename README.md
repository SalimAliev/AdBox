
<!-- PROJECT LOGO -->
<br />
<div align="center">


  <h1 align="center">AdBox</h1>

  <p align="center">
    This is an API application for viewing and adding attachments
  </p>
</div>

<!-- ABOUT THE PROJECT -->
## About The Project

This web api application has the following methods:
* Method of getting the list of ads
* Method of getting a specific ad
* Ad creation method



### Built With

This section should list any major frameworks/libraries used to bootstrap your project. Leave any add-ons/plugins for the acknowledgements section. Here are a few examples.

* Python 3.10.8
* Django 4.2.1

<!-- GETTING STARTED -->
## Getting Started

### Installation

To install the application, follow these steps

1. Clone the repo
   ```sh
   git clone https://github.com/SalimAliev/AdBox.git
   ```
2. Go to the project directory and install the python virtual environment
   ```sh
   
   python -m venv venv
   ```
3. Activate the virtual environment with the command
   ```sh
   # For Windows
   .\venv\Scripts\activate
   
   # For Linux
   source venv/bin/activate
   ```
4. Install dependencies with the command
   ```sh
   pip install -r requirements.txt
   ```

<!-- USAGE EXAMPLES -->
## Launch

To launch the application, follow these steps

1. Perform migrations with the command
   ```sh
   python manage.py migrate
   ```
2. Start the server with the command   
   ```sh
   python manage.py runserver
   ```
   
## Using
Open your browser
1. To get a list of ads, send a GET request to the URL: http://127.0.0.1:8000/advertisements/
2. To get one of the ads, send a GET request to the URL: http://127.0.0.1:8000/advertisements/1 (at the end, specify the ad id)
   1. To get an ad with a description, add the optional "description" field. Example (http://127.0.0.1:8000/advertisements/1?field=description)
   2. To get an ad with links to all photos, add the optional "photos" field. Example (http://127.0.0.1:8000/advertisements/1?field=photos)
3. To add an ad to the database, send a POST request to the URL (http://127.0.0.1:8000/advertisements/create/). Request body example:
   ```json
   {
    "title": "Advertisement 1",
    "image_paths": ["/image_path"],
    "description": "Advertisement 1",
    "price": 100
    }
   ```

<!-- CONTACT -->
## Contact

Salim Aliev - email@example.com

Project Link: [https://github.com/SalimAliev/AdBox.git](https://github.com/SalimAliev/AdBox.git)
