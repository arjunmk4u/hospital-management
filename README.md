<h1>MEDICO Hospital Management application</h1>

MEDICO is a web based application that makes hospital management easy. <br>

The project is done using django, a web framework of python. For the front end styling, using the bootstrap 5.

  
  

<br>

  

## Application features,

<ul>

<li>A user based authentication system, also guest view</li>

<li>Book Appoinments for particular doctor </li>

<li> See department informations and overview </li>

<li> List doctor's from each department </li>

<li> Contact </li>

</ul>

## Building the application
Basically this app runs on python django framework. So you need to install python to run this. python 3.9 and above recommended.<br>
Steps to run the application locally<br>
You can run the build.sh file directly<br>
First you need a virtual environment to work with.
Steps to install and activate virtual environment
```
pip install virtualenv
virtualenv djangoenv
```
You've created a virtual environment named djangoenv. You can name whatever you want. <br>
Next activate the virtual environment
```
djangoenv\Scripts\activate
```
And then you've to install  the django. 
```
pip install django
```
Finally, you can run the application by entering this command
```
python manage.py runserver
```