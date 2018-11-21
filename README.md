# learningObjectVoter

This application is used for [masteraula-back](https://github.com/mupi/masteraula-back).

Simple server to vote if the question has a learning object or not. 

# Configuration

Open the `server.desktop` and` server.sh` files in a text editor and edit the `path/to/` variables:

## server.desktop
```desktop
[Desktop Entry]
Type=Application
Terminal=true
Name=Escolhe objeto de apredizado
Exec=path/to/server.sh
```

## server.sh
```bash
#! /bin/bash

gnome-terminal --tab --title="Servidor" -e "/bin/bash -c 'cd path/to/learningObjectVoter/; python3 server.py'"
```

# Usage

## Running the server
Just run the `server.desktop` file or you can run the server file using `python3 server.py`

## Generating html file
In order to use this properly, you need to generate as html running the `generate_html.py` inside the shell in django application in [masteraula-back](https://github.com/mupi/masteraula-back).(`./manage.py shell`)

With the server running, open the file and select the checkbox if you think the question has a learning object.

## Gathering the results
The results will be at `results.json` file (this is not a json btw.
