# Gentile introduction to Docker Container

> Docker container images is a lightweight, standalone, executable package of software that includes everything needed to run an application: code, runtime, system tools, system libraries, and settings.

Docker containers are built from `images`. These images are line-by-line instructions on how to build a container. Please take a look at the example from: [here](/Dockerfile) read and understand the comment of each line on the `Dockerfile` to understand how the docker container is being built.

The `docker-compose.yml` file is used to make it easier to put the container together rather than using lower-level `docker` commends.

After having the docker container instruction in the compose file. You can run:

```bash
docker-compose build
```

You should see it build the container like the one below
![docker building](/Doc/img/dockerImg/docker-container-building.PNG)
to build the containers.

After the container is built the image is also created locally with the image id and all the necessary attributes to start the container. To see this you can use the lower level `docker ps` command or the `docker-compose ps` command.

NOTE: you will not see anything since there is no container running at this time. To bring the container up you can run the command below.

```bash
docker-compose up
```

You should see a similar output to the one below.

![docker building](/Doc/img/dockerImg/start-up.PNG)

NOW if you run the command

```bash
docker-compose ps
```

You will see all the container that are running and their status. Like this:

![docker ps](/Doc/img/dockerImg/docker-compose-ps.PNG)

From the image above we can see that the two containers (`db` and `svc`) are running perfectly. While the `ui` container is trying `Restarting`.

If your containers are `healthy` you should see them.

![docker containers running properly](/Doc/img/dockerImg/properly_running.PNG)

## Container Resource

While containers are isolated from your host machine. There are resources that they use and share with the host machine. For instance, container share volume (memory), ports (network) etc.

There are different network configurations in docker-compose files. Which defines the interaction among containers and also with the host machine. The process of specifying this is called mapping.

This is a vast topic in itself. For network configuration the two widely used are [host network](https://docs.docker.com/network/host/) and [bridge network](https://docs.docker.com/network/bridge/). For volume, we have shared volume and mount. [Here](https://docs.docker.com/storage/volumes/) is more information.

There are different commands to manage this resource both on the host side and in the container.
