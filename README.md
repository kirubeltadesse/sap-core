# sap-web

Scholar Academy Project

## Workflow

Under the `install` folder you will find `macInstall.sh` or `windowInstall.bat` base on your OS you can run either or. Once you run the installers, you should have Docker and VScode installed. If you are on windows you will have `wsl2` installed on your machine.

If that went perfectly, you can run

```bash
./vsextensionInstaller.sh
```

you should see something like

![Installation in prograss](/Doc/img/runvsextinstaller.PNG)

Once that is finished the install package will show up on VScode.

![Vscode extension](/Doc/img/extenstion_installed.PNG)

on your terminal (`wsl` if you are on windows). This will install all the necessary extension for you to work with `docker` on VScode.

<details>
    <summary> <b> VScode configuration </b> </summary>

### Keybindings and settings

Inside the extension installing script there is copy bash statement that directly copy to the location where vscode is expecting to get the `settings.json` and `keybindings.json` files

However, the link is commented out because of the path difference in user vscode depending on ower installation.

Therefore, please refer to them if you need addition tricks. However, I strongly recommend copy the `keybindings.json` to help you on your development.

### Formatting

Press `ctrl + shift + P` and type `Preferences: Open Workspace Settings`

![preference window](/Doc/img/preferences.png)

Under `Workspace` search for Formatting and check `Format On Save`

Make sure the `prettier` is selected under `Text` in side the `Workspace`

Search for `prettier` under the extension change the `Tab Width` to 4 space

### Font Settings

In the workspace, you should set the `Font Family` to `Cascadia Code, Fira Code`

![font view](/Doc/img/FontChange.PNG)

You should be able to see a clear font difference on your editor.

### Todo Tree

By default should have `BUG`, `HACK`, `FIXME`, and `TODO`

</details>

## Project Overview

This is how the container will be setup.

...

```mermaid

    graph LR;
        Client> Client]-->|request|Server(<img src='https://www.docker.com/wp-content/uploads/2022/03/Moby-logo.png' width='120' height='120' /> Server)
        Server -.->|response|Client
        Server -->|request|Database(<img src='https://www.docker.com/wp-content/uploads/2022/03/Moby-logo.png' width='120' height='120' /> Database)
        Database -.->|response|Server
        Server-.->|response|Test(<img src='https://www.docker.com/wp-content/uploads/2022/03/Moby-logo.png' width='120' height='120' /> Test)
        Test-->|request|Server
```

---

<details>

<summary> FAQ working with vs code </summary>

## Mac
Make sure you have [code](https://code.visualstudio.com/docs/setup/mac) command installed in your path.

![walkthrough](https://user-images.githubusercontent.com/32272045/168448980-c8fcf5b3-9fad-4898-b7cc-a22dd256b19f.png)
## Windows
-   `code .` is not openning on `wsl`

-   ANS: Linking VScode [locally](https://stackoverflow.com/questions/57868950/wsl2-terminal-does-not-recognize-visual-studio-code)

</details>
