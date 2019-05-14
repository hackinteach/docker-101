# Docker 101

> Nuttapat Koonarangsri
>
> Pan Teparak
>
> Last edit : 14 May 2019 @1.44 am



[TOC]

## What is Docker

Check it out yourself [here](<https://opensource.com/resources/what-docker>)

**VM || Docker ??**

![docker-vm-container.png](https://zdnet2.cbsistatic.com/hub/i/r/2017/05/08/af178c5a-64dd-4900-8447-3abd739757e3/resize/770xauto/78abd09a8d41c182a28118ac0465c914/docker-vm-container.png)



## Get start

1. Install [Docker CE](<https://docs.docker.com/install/>) and [Docker Compose](<https://docs.docker.com/compose/install/>)
2. See if it works `docker version`, `docker-compose version`
3. More verification `docker run hello-world`



## Basic Terminology

### Image

​	A class of container. Think it as OS or base technology you want to use.

`docker images` or `docker image ls` 

Find online images : [Docker Hub]([https://hub.docker.com](https://hub.docker.com/))

Image name: `<image name> : <tag/version>` ex: `python:3.7-alpine`

### Container

​	A ‘running’ Docker image. Multiple containers can use the same image

`docker container ls`

### Network

`docker network ls`

### Volumes

​	See it like external disk attached to the container

`docker volumes` or `docker volumes ls`

## Dockerfile

​	A *definition* of Docker image

#### Intro to Dockerfile

Path : `d1`

`Dockerfile`

```dockerfile
FROM python:3.7-alpine # select base image, alpine is cheap
WORKDIR /app # initial path for working dir, create if not exists
RUN pwd # run some script
ADD . . # copy all files from d1/ (host) to /app (container)
RUN ls
CMD python app.py
```

Build and run it

```bash
# Build the image according to Dockerfile, with optional tag (image name)
docker build -t d1 . # notes the "."
# Run the built image with required arguments
docker run d1
```

---

***One more***

Path : `d2`

`Dockerfile`

```dockerfile
FROM python:3.7-alpine
WORKDIR /app
RUN pwd
ADD . .
RUN ls
CMD ["python", "app.py"]
```

Build and run it

```bash
docker build -t d2 .
# now run it as usual
docker run d2 1 2 # expected "Result: 3"
```

make change in `Dockerfile`

```dockerfile
FROM python:3.7-alpine
WORKDIR /app
RUN pwd
ADD . .
RUN ls
ENTRYPOINT ["python", "app.py"]
```

now build and re-run it.

---

***Connecting from outside world***

Path: `d3`

build and run it : `docker build -t d3 . && docker run d3`

- now try go to http://localhost:5000/hello/your-name

Try run with `docker run -p 5000:5000 d3` or `docker run --port 5000:5000 d3`

now try again

#### Task 1

1. Try adding `/blah` route that just return string `blah` to screen.
2. build the `Dockerfile` again
3. see if it works

**Now, What can we optimise here ?**

From observations, we know that

1. it install `req.txt` every time you change `app.py` but we don’t want that to run every time

Solution:

```dockerfile
FROM python:3.7-alpine
WORKDIR /app
ADD req.txt .
RUN pip install -r req.txt
ADD . .
CMD gunicorn -b 0.0.0.0:5000 app:app
```

Now try adding one more route, build, and see the change.

> Notes:
>
> you can run Docker in detached/daemon mode by adding `-d` flag
>
> try: `docker run -d d3`
>
> and it’ll go background !

---

### Using Volumes

#### Running Database Engine

[MySQL Docker](<https://docs.docker.com/samples/library/mysql/>)

**Step 1:** Starting a container: `docker run -d --name mysql_sample -p 3307:3306 -e MYSQL_ROOT_PASSWORD=milanomilano -e MYSQL_DATABASE=mydb mysql`

**Step 2: ** Get into it: `docker exec -it mysql_sample mysql -uroot -p`, enter password

```mysql
mysql> CREATE TABLE `mydb`.`user`  (
  `firstname` varchar(255) NULL,
  `lastname` varchar(255) NULL,
  `student_id` int(0) NULL
);
mysql > use mydb;
mysql > show tables;
mysql > exit; # or ctrl + d
```

Now you have a table `user` in your database. Now try to remove the container it. 

```bash
docker stop mysql_sample
docker rm mysql_sample

## OR
docker rm -f mysql_sample
```

**Step 3: **   start over from ***Step 1*** but with `-v ./mysql_data:/var/lib/mysql`

now do ***Step 2*** and try to start the ***Step 1*** again, see if your data is still there.

> Notes:
>
> You can specify 2 types of volumes: `./dir` will use the current directory and create the folder for it, `vol_1` will refer to `docker volume`. For second approach, you can do `docker volume create mysql_data` and `-v mysql_data:/var/lib/mysql`. Now with `docker volumes` you’ll see `mysql_data`

#### More on Volumes

path : `d3`

Goal: Want to see the change for Flask app right away.

We can do`gunicorn …… —reload`. 

1. Run `gunicorn` locally, make some changes, see what happen
2. build dockerfile
3. run it with `-d` flag
4. try changing some routes
5. see if it works
6. how to fix ??

**SOLUTION**

`docker run --name d3_vol -v “$(pwd):/app” -d d3`

- watch the log `docker logs --follow (or -f) --tail 5 d3_vol`

- make change to `app.py`, see the log
- try see the new change.

## DockerCompose

What if we have multiple `Dockerfile` or services that want to run together



## Refs

[Simple Commands](https://training.play-with-docker.com/ops-s1-hello/)

[Docker images](https://training.play-with-docker.com/ops-s1-images/)