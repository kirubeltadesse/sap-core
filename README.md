[![CircleCI](https://circleci.com/gh/Swarmies/sap-web/tree/develop.svg?style=svg)](https://circleci.com/gh/Swarmies/sap-web/tree/develop)

# sap-web

Scholar Academy Project is a website-based schedule system for students to make appointments with tutors/mentors. Which will tremendously help facilitate the tutorial process and monitor the effectiveness of the provided resources from the facility side.

## Prerequisites

Under the `install` folder you will find `macInstall.sh` or `windowInstall.bat` base on your OS you can run either-or. Once you run the installers, you should have Docker and VScode installed. If you are on windows you will have `wsl2` installed on your machine.

If that went perfectly, you can run

```bash
./vsextensionInstaller.sh
```

you should see something like

![Installation in progress](/Doc/img/runvsextinstaller.PNG)

Once that is finished the install package will show up on VScode.

![Vscode extension](/Doc/img/extenstion_installed.PNG)

on your terminal (`wsl` if you are on windows). This will install all the necessary extensions for you to work with `docker` on VScode.

To run the project locally you need to make sure you have [Docker Engine](https://docs.docker.com/engine/install/) and [Docker-Compose](https://docs.docker.com/compose/install/) installed. Docker makes it convenient to package every tooling needed for the project. Docker gets read of the headache of setting up a Virtual Environment, installing dependencies, creating a new Database in PostGradSQL, migrating the migrations in Django App, building the React App then finally running Django and Web-Pack-dev server.

## Terminology

**Dockerfile**: A set of commands to build an image to be run as a container.

**Docker-compose**: A file defining how to run a multi-container Docker application.

### Docker Documentation

NOTE: make sure that you are indirectly where you have the `docker-compose.yml` file. If you get an error at any steps
of the process below please refer to the `FAQ` section for guidance and quick answers.

To build the docker containers. Simply run the command below

```bash
docker-compose build
```

To build the container up (start a container)

```bash
docker-compose up <name-of-the-container>  # this is specified in the .docker-compose.yml file
```

To get inside the container and open the bash terminal

```bash
docker-compose exec <name-of-the-container> bash
```

To run the container and get inside it you can use the command below

```bash
docker-compose run --rm <name-of-the-container> <bash> # you can use the bash command to open bash terminal 
```

To properly close all containers use

```bash
docker-compose down
```

For more information on docker command you can find [here](/Doc/docker-command-guide.md)

<details>
    <summary> <b> VScode configuration </b> </summary>

### Keybindings and settings

Inside the extension installing a script, there is a copy bash statement that directly copies to the location where VS Code is expecting to get the `settings.json` and `keybindings.json` files

However, the link is commented out because of the path difference in user VS Code depending on ower installation.

Therefore, please refer to them if you need additional tricks. However, I strongly recommend copying the `keybindings.json`` to help you with your development.

### Formatting

Press `ctrl + shift + P` and type `Preferences: Open Workspace Settings`

![preference window](/Doc/img/preferences.png)

Under `Workspace` search for Formatting and check `Format On Save`

Make sure the `prettier` is selected under `Text` inside the `Workspace`

Search for `prettier` under the extension and change the `Tab` Width` to 4 space

### Font Settings

In the workspace, you should set the `Font Family` to `Cascadia Code, Fira Code`

![font view](/Doc/img/FontChange.PNG)

You should be able to see a clear font difference in your editor.

### Todo Tree

By default should have `BUG`, `HACK`, `FIXME`, and `TODO`

</details>

## Project Overview

This is how the container will be set up.

...

![Project container structure](/Doc/img/projectContainersSetup.PNG)

## Workflow

There is the process that we follow throughout our development cycle:

1. Fork this repository:
2. Clone your forked repository:
3. [Install the software](#prerequisites) and [VS code extensions](#formatting)
4. Build [docker containers](/Doc/docker-command-guide.md)
5. Make changes and push them to your Fork repository
6. Open up a Peer Review (PR)

## Tests and Databases

After creating a model you need to run the codes below

```bash
python manage.py makemigrations --dry-run --verbosity 3
```

then

```bash
python manage.py migrate 
```

To run coverage locally you can run

```bash
coverage run --omit='*/Doc/*' manage.py test
```

Now you can run the command below and open the html file in your fevorite edit and see what tests are missing

```bash
coverage html
```

To run the test you can just use the `pytest` package

```bash
pytest
```

---

<details>

<summary> <b> FAQ</b>
</summary>

## General Errors

* If you are getting an error from a node like the one below

![terminal image](/Doc/img/node-error.PNG)

> try running the command below and rebuilding the image.

```bash
rm -rf /usr/local/lib/node_modules/npm 
```

## Docker issues

* Permission error

![permission denied error](/Doc/img/permission_denied.PNG)

> you can run the command in as an admin that should solve it

* Why am I being asked to run the docker command as a root user (i.e sudo )?

> You probably have overlooked this [here](https://docs.docker.com/engine/install/linux-postinstall/)

* ERROR: Couldn't connect to Docker daemon at http+docker://localhost - is it running? link the one below.

![docker daemon](/Doc/img/docker%20daemon.PNG)

> The command below will fix your problem for now.

```bash
    sudo service docker start   # for work with SysVinit
    sudo systemctl start docker # for work with Systemd
```

> You probably have not configured docker to start on boot up here is a [link](https://docs.docker.com/engine/install/linux-postinstall/#configure-docker-to-start-on-boot) on how to do that

## Mac

Make sure you have a [code](https://code.visualstudio.com/docs/setup/mac) command installed in your path.

![walkthrough](https://user-images.githubusercontent.com/32272045/168448980-c8fcf5b3-9fad-4898-b7cc-a22dd256b19f.png)

## Windows

* `code .` is not opening on `wsl`

* ANS: Linking VScode [locally](https://stackoverflow.com/questions/57868950/wsl2-terminal-does-not-recognize-visual-studio-code)

</details>
