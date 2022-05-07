# chat-forum

<img src="https://user-images.githubusercontent.com/84562594/167248134-dcef39b7-ba77-4856-a7bc-01b2ae65f8fa.png" width=20% height=20%>

 A Chat Forum Application powered by Django Channels, WebSockets, Django Redis and Asyncio enabling real time chat servers.

It uses `django-channels` to implement `WebSockets`

And `django-redis` to manage cache.

# Installation
 ## Clone
 ##### Clone using the url given below
 
 `https://github.com/Jeswin-8802/chat-forum.git`
 
 ## Setup
 ##### In the project directory:
 > Type the following command to create a virtual envieonment and initialize it with the necessary pacakges
 
 `pipenv install`
 
 > Note that this may take upto 5-10 minutes
 
 > If you don't have pipenv installed on your system, refer: https://docs.pipenv.org/
 
 > Type the following command to open a shell in the virtual environment
 
 `pipenv shell`
 
 `py manage.py makemigrations`
 
 `py manage.py migrate`
 
 `docker run -p 6379:6379 -d redis:5`
 
 > If you don't have docker installed on your system, refer the docs here: https://docs.docker.com/get-docker/
 
 `py manage.py runserver`
 
 #### You're good to go!
 
 #
 
 > If you wish to exit the virtual environment, type
 
 `exit`
 
 > Or, if you wish to remove the virtual environment created
 
 `pipenv --rm`
 
 #
 
 
 
