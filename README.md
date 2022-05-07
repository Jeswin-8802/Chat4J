# chat-forum

<img src="https://user-images.githubusercontent.com/84562594/167248134-dcef39b7-ba77-4856-a7bc-01b2ae65f8fa.png" width=20% height=20%>

 A Chat Forum Application powered by Django Channels, WebSockets, Django Redis and Asyncio enabling real time chat servers.

It uses `django-channels` to implement `WebSockets`

And `django-redis` to manage cache.
 
# Setup
##### In the project directory:
> Type the following command to create a virtual environment and initialize it with the necessary packages

`pipenv install`

> Note that this may take upto 5-10 minutes

> If you don't have pipenv installed on your system, refer: https://docs.pipenv.org/

`pipenv shell`

`py manage.py makemigrations`

`py manage.py migrate`

`docker run -p 6379:6379 -d redis:5`

> If you don't have docker installed on your system, refer: https://docs.docker.com/get-docker/

`py manage.py runserver`

#### You're good to go!

#

> If you wish to exit the virtual environment, type

`exit`

> Or, if you wish to delete the virtual environment created

`pipenv --rm`

 #
 
 ![login](https://user-images.githubusercontent.com/84562594/167248727-7fc3ec6c-c42c-47c3-b9e1-0aa8823c2e33.png)
 
 #
 
 ![signUp](https://user-images.githubusercontent.com/84562594/167248748-eeda8872-c9bf-44be-ad5d-e480850aa1d3.png)

#

> This is the home page and you will be redirected to this page once you log in.

> You can enter a forum by entering it's name.

![home](https://user-images.githubusercontent.com/84562594/167248762-038f4281-39c4-4b71-9df0-aef8411abc9c.png)

#

> chat away!

 ![forum](https://user-images.githubusercontent.com/84562594/167248769-80e05ad0-0f99-41b2-bac7-ee1148415521.png)

# References

* https://www.youtube.com/watch?v=Wv5jlmJs2sU&list=PLLRM7ROnmA9EnQmnfTgUzCfzbbnc-oEbZ
* https://www.youtube.com/watch?v=F4nwRQPXD8w&t=2679s
