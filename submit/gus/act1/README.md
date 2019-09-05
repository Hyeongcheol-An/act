# Write

# 1. lession learned

- `docker build -t compose-flask .` is not necessary. It is automatically done by `docker-compose up`, but with different docker image name. It's image name is created with `<directory_name>_<service_name>`.

- If you use `Redis` in `app.py`, you can use python image instead in the `Dockerfile`. But for this case, we neglected using `Redis`, and therefore used Ubuntu docker image.
	- https://runnable.com/docker/python/docker-compose-with-flask-apps

- For more information about docker images:
	- https://medium.com/@mtngt/docker-flask-a-simple-tutorial-bbcb2f4110b5

# 2. process done

- Create a python application, which uses Flask library to easily create an Web Api.

- The application can be accessed through host's ip address.

- Used Docker and Docker-compose to launch the application in a container. And we named the container 'hello_sut'

- `app.py` takes optional argument `-p` for determining the port the app is run. This is implemented in both `app.py` and `Dockerfile`.

