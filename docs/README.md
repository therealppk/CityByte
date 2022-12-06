
# CITYBYTES

## SOFTWARE CODE DOCUMENTATION

## CityByte Version 2:

New and improved! Add more description here...

Below are the new features and improvements we made:

1. Implemented a wish-list/to-go list to save interesting locations so you can come back and look at them later
2. Implement Caching to get API results faster
3. Created a signup/login page - having an account goes a long way when we add new features that are customized for the user!
4. Comment Page - you can comment on the place and look at all the other comments that have been posted!
5. Fixed WeatherApi Bug

## Quick Start

#### 1. Clone the repository:  

   `git clone https://github.com/rohitgeddam/CityByte.git`

#### 2. Setup the virtual environment:  
    
`
    python -m venv venv
`


#### 3. Activate the virtual environment:  

    On Mac/Linux:    

`
      source venv/bin/activate
`
      
    On Windows:    
    
`
      venv\Scripts\activate
`
   

#### 4. Install required modules and libraries:  

`
    pip install -r requirements.txt
`


#### 5. Create .env file at ./CityByte using the below template.
   
```
    GEODB_X_RAPID_API_KEY=0ebeca3f10msha647955d4a03bd3p16b08bjsn3570b7991a4c
    GEODB_X_RAPID_API_HOST=wft-geo-db.p.rapidapi.com
    AMADEUS_API_KEY=eNJXGmjjlYYikHyfAGXRZDGG0q5NaN2q
    AMADEUS_API_SECRET_KEY=YGgltYGVEjdk1tZ0
    UNSPLASH_API_KEY=OWiI5nfmGz_dY1-T0m_vCOGqwGzpUo-QeuO2nil8MaY
    FOURSQUARE_API_KEY="fsq3owEliIvoxcep8TxUmUh35FtlvyZxtIIuOJAXl+A9UlY="
    WEATHER_BIT_X_RAPID_API_KEY=0ebeca3f10msha647955d4a03bd3p16b08bjsn3570b7991a4c
    WEATHER_BIT_X_RAPID_API_HOST=weatherbit-v1-mashape.p.rapidapi.com
```
Create an account in the below websites to Fetch API keys and use them in the above template.  
* [GeoDB Cities API](https://rapidapi.com/wirefreethought/api/geodb-cities/details)
* [Weather API](https://rapidapi.com/weatherbit/api/weather)
* [Amadeus API](https://developers.amadeus.com/)
* [Unsplash API](https://unsplash.com/developers)
* [Foursquare API](https://location.foursquare.com/developer/)  

#### 6. Set-up REDIS
* Follow the instructions in [Getting Started](https://redis.io/docs/getting-started/) to Install Redis in your local environment.
* Start the Redis Server: Open a terminal and run the following command:
```
   redis-server
```
* Open another terminal to start the REDIS CLI:
```
   redis-cli
```

Now, you can run the application.
#### 7. Run the application:  
   
   ``` 
   python manage.py migrate
   python manage.py runserver
   ```
  
## After adding another field to Model
Django's way of propagating changes you make to your models (adding a field, deleting a model, etc.) into your database schema.

   ```
   python manage.py makemigrations
   python manage.py migrate
   ```

## Automatic tools - GitHub Actions
 
We use GitHub actions to automate tasks of linting, code coverage, build, tests, and security checks. The codes that perform these actions are stored as `.yml` files in the `.github/workflows` directory. The GitHub actions are triggered whenever something is pushed (or pulled) into the remote repository. The results of these automated tasks are shown as badges at the top of this README.md file. 

### Unit tests:

Unit test are performed everytime there is a push or pull into the repository. They are present in `/search/tests.py`. 


### Code Coverage: 

Code Coverage is an important metric that allows us to understand how much of the codebase is tested. `django.yml` performs this task. For more information about Code Coverage, please visit this [link](https://www.atlassian.com/continuous-delivery/software-testing/code-coverage). 

### Flake8 - Code Linting:

We are using Flake8 for linting and syntax checking, and it is performed by `Linting.yml`. For more information about Flake8, please visit this [link](https://medium.com/python-pandemonium/what-is-flake8-and-why-we-should-use-it-b89bd78073f2).
Use flake8 before you push code to GitHub. </br>
Config file present in `setup.cfg`.

```
flake8 <directory>
```

### Black - Code Formatter

We are using the Black code formatter to format our code before pushing it to GitHub. For more information about Black, please visit this [link](https://black.readthedocs.io/en/stable/).


Run the line below everytime you push to GitHub.</br>
Config file present in `pyproject.toml`
```
black --line-length 120 <filename>
```

If you prefer using Black in VSCode, you can add the below settings in your vscode settings:

```
{
    "python.formatting.provider": "black",
    "python.formatting.blackArgs": ["--line-length", "120"],
    "python.linting.enabled": true
}
```
  
### Pre Commit Hooks for Black Code formatting and Flake8 Linting
* run  `pre-commit install`
* Now everytime you commit, Black and Flake8 will run automatically and will not allow you to push if the code standards are not met.
<img width="694" alt="Screenshot 2022-10-07 at 11 35 40 AM" src="https://user-images.githubusercontent.com/48797475/194592802-e7d7c951-9694-4260-b537-fc017a5fd06c.png">

<sub>Image from [Ji Miranda](https://ljvmiranda921.github.io/assets/png/tuts/precommit_pipeline.png).<sub>

## Team Members
1. Rohit Geddam: sgeddam2@ncsu.edu
2. Arun Kumar Ramesh - arames25@ncsu.edu
3. Kiron Jayesh - kjayesh@ncsu.edu
4. Sai Krishna Teja Varma - smanthe@ncsu.edu
5. Shandler Mason - samason4@ncsu.edu

## Support

Concerns with the software? Please get in touch with us via one of the methods below. We are delighted to address any queries you may have about the program.

Please contact us if you experience any problems with the program, such as problems with joining up, logging in, or any other functions.

<a href = "mailto:citybyte.support@proton.me">
<img width = "35px" src = "https://user-images.githubusercontent.com/73664200/194786335-12b1d3a6-b272-4896-9bd7-d615e28847f3.png"/>
</a>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
<a href = "https://twitter.com/CityByteSupport">  
<img width = "35px" src = "https://raw.githubusercontent.com/peterthehan/peterthehan/master/assets/twitter.svg"/>
</a> 

## Project 1 Docs:

## INTRODUCTION

Moving to a new location can be a daunting endeavor, especially when you have the entire United States to choose from. Finding a new home from scratch while prioritizing certain aspects might be very challenging given the variety of nations and cities. However, with the advancement of technology, information from earlier times can now be leveraged to offer a number of vital insights about a certain location. Our project succeeds in one of those objectives. We seek to present that information in our project because there are many other elements that are taken into consideration when choosing a place to reside, such as weather, temperature, entertainment options, landmark locations, education, and many more. The project is totally created using a variety of technologies, including some of the accessible APIs that are utilized to fetch real-time data.

Although this project is still in its early phases of development, it can be expanded up even further by including multiple features that can benefit society in a variety of different ways. This article offers a critical viewpoint that users can use to comprehend the project, adopt it as open source software, and add further features before releasing it to the market. The document also serves as a starting point for the project and helps developers understand the code.

The technologies listed below were used to build the entire project, and it is advised that the group of developers who take on this project in the future retain these tools on hand.
* Python
* Django
* Pytest
* HTML
* CSS
* JavaScript
* BootStrap

Although we have used HTML, CSS and Bootstrap for the frontend logic the user can use any technologies and combine it with backend such as Angular, React etc.

## CODE FUNCTIONALITIES

The project basically uses Django for the backend logic. Django is a Python framework that is useful to build websites. It uses model view and templates architecture. Some of the files used in Django are as follows:-
* Views.py:- Backend logic is being written in this file. It takes http requests as arguments, imports relevant models and figures out what data needs to be sent to the template and returns the final result.
* Models.py:- Django has Object Relational Mapping which makes it easier to work with databases.The model provides data from the database.
* templates/:- They are used to store templates for frontend development and html files.
* Urls.py:- They are used to set the urls of the django project and apps. The endpoints created are stored in the urls files.
* Tests.py:- They are used to write the test cases for the code. They are used to check the code.
* Settings.py:- It has the basic information about the various api’s used and initializes the environment required for the project.

## HOW DOES CITYBYTE WORK?

Firstly, there is a project that needs to be created in Django named CityByte. Then there are two apps named as info and search in the directory. The urls are set in the urls.py file. Both the apps use utils and helper functions which are used to call the api to fetch the real time data. The frontend logic is written using the JavaScript, HTML , CSS and Bootstrap in the templates directory. Most of the backend logic is written in the views.py file which uses utils and helpers to give the desired output. We will be talking about different endpoints which are rendered using functions in the views file. Hence this section of the documentation will further explain various functions written in the views file.

1. def main_page: Main page is used to render the HTML template which has some front-end logic written in javascript. It is used to run the first page of our website.
2. def info_page: Info page takes two request params namely city and country, which provides city and country respectively. The “weather info” variable includes the WeatherBitHelper function which uses WeatherUtilBase to get the data of city and country. The weather_info delivers the information of sunrise, sunset, and timezone of that particular city. The “dining info” variable takes the FourSquarePlacesHelper function that uses FourSquarePlacesUtilBase to get the dining information of that city. The variable “outdoor info” receives the information about places to visit outdoors from the FourSquarePlacesHelper function that uses FourSquarePlacesUtilBase. Similarly, “airport info” and “arts info” variable stores the information regarding airport and arts places respectively, from the FourSquarePlacesHelper function that uses FourSquarePlacesUtilBase. The “photo link” variable generates the photo of the entered city using the UnplashCityPhotoHelper function which uses PhotoUtilBase in the Unsplash class. All the following variables is passed to context using jinja templating.
3. def city_suggestions: City suggestion function receives the user city input, and request to the GenericDBSearchAutoCompleteHelper function that uses SearchAutoCompleteHelperBase class, which collects all the necessary information of that particular city and provide JSON response, which is reflected in the first page of our website.
4. def city_photo: The City photo function uses the “photo link” variable that receives the information from UnplashCityPhotoHelper, and returns the JSON response which includes the path of the photo link and not the photo itself.
5. def place_photo: The function place photo has the “photo link” variable that uses fsq_id unique ID for that particular place and renders the photo link.

The below screenshots give the glance of the working of our project.

![city 1](https://github.com/therealppk/CityByte/blob/main/docs/assets/City%201.png)

![city2](https://github.com/therealppk/CityByte/blob/main/docs/assets/City%202.png)

![city3](https://github.com/therealppk/CityByte/blob/main/docs/assets/City%203.png)

![city4](https://github.com/therealppk/CityByte/blob/main/docs/assets/City%204.png)

![city5](https://github.com/therealppk/CityByte/blob/main/docs/assets/City%205.png)

## FUNCTIONAL TESTING
For functional testing of the code, a separate testing script is written to validate the output generated by the CityBytes.
The scripts are written in 
CityByte\search\tests\test_photo.py
Initially there are four test cases that have been used for validation of the software.

Test Case 1: test_main_page is the first test case that renders the search.html template which runs the main page of our website.

Test Case 2: test_info_page is the second test case for the validation of user request fetching, when a user is entering a city, the test case would check whether the information in the request has been received. After that the information fetched is checked which includes the data regarding weather, time zone, dining information, outdoor information, airport details and arts & museum data. At the end it verifies the rendering of the request for all the given features: weather_info, dining_info, outdoor_info, airport_info, photo_link, & arts_link.

Test Case 3: test_photo is our third test case that checks the photo_link, and makes sure that the photo is not fetched instead of the url from the http request.

Test Case 4: test_cityphoto is the test case for testing the UnplashCityPhotoHelper which is redirected from photo_link to site, to get the header of the http request. This test case checks whether the content type is an image.

## FUTURE SCOPE

* Chasing results from API using Redis in order to improve the performance.
* Addition of search bar with category filter, that will help the user to search based on his/ her requirements.
* To run multiple API requests simultaneously, multithreading will be used.
* Various multiple features about cities can be added as per the user requirements and customer segmentation.

## TEAM MEMBERS

| Name | UnityID |
|--------|--------|
|Nirav Shah | nshah28 |
| Vishwa Gandhi | vgandhi |
| Pradymna Khawas | ppkhawas | 
| Vrushanki Patel | vpatel25 |
| Priya Saroj | pbsaroj | 
