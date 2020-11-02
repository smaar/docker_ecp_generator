## What is it

Docker eCommerce platforms is a web interface that comes pre-packaged with localhost Docker Compose projects.

The aim of this project is to provide developers minimal effort to set up eCommerce platforms to test extensions or to get a feel of the platform.

## Getting started (normal)
Run the following command in terminal:

UNIX
```
docker run -d --name docker-ecps -p 5000:5000 -w /opt/docker-compose-projects/ -v /var/run/docker.sock:/var/run/docker.sock matt1919/docker-ecps
```

WINDOWS
```
docker run -d --name docker-ecps -p 5000:5000 -w //opt/docker-compose-projects/ -v //var/run/docker.sock:/var/run/docker.sock matt1919/docker-ecps
```

You can then connect to the UI at `http://localhost:5000`

## Getting started (development)

Run the following command in terminal:
```
docker build --tag docker-ecps .
```

Then run the command below that matches your OS:

UNIX
```
docker run -d --name docker-ecps -p 5000:5000 -w /opt/docker-compose-projects/ -v /var/run/docker.sock:/var/run/docker.sock docker-ecps
```

WINDOWS
```
docker run -d --name docker-ecps -p 5000:5000 -w //opt/docker-compose-projects/ -v //var/run/docker.sock:/var/run/docker.sock docker-ecps
```

You can then connect to the UI at `http://localhost:5000`

When done with your changes, you can push to DockerHub by running the 2 commands below. Only do this if you have permissions to do so:
```
docker tag docker-ecps matt1919/docker-ecps:latest
docker push matt1919/docker-ecps
```

## Monitoring
You can use anything you want!  I personally use Docker Desktop or Portainer depending on the environment.

## Add your own docker-compose projects
You add projects into `demo-projects/*` and rebuild the image for them to take affect.

## Notes
- Main code for web UI and functionality taken from https://github.com/francescou/docker-compose-ui
- Since you're running Docker Compose inside a container you must pay attention to volumes mounted with relative paths, see [Issue #6](https://github.com/francescou/docker-compose-ui/issues/6)
