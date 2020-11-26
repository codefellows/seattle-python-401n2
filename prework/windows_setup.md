# Python Development on Windows : Set up

## Prerequisites

- Make sure you've followed the Code Fellows  [Set Up Guide](https://codefellows.github.io/setup-guide/windows/terminal/setup.html){:target="_blank"}
- [Install Homebrew](https://docs.brew.sh/Homebrew-on-Linux){:target="_blank"} which now runs on Windows using WSL.
  - If you don't already have WSL installed see **WSL** installation steps below.

## Overview

While Python itself runs fine on Windows, many of the tools that a Python developer needs can behave unexpectedly on Windows.

The fact is that most Python development assumes you'll be working on a Unix based system.

The good news is that Windows has made it (relatively) easy to get such a Unix based system running right within Windows itself.

There is a tool called WSL (or Windows Subsytem for Linux) that will need to be installed so that all our supporting tools (Poetry, VS Code, multiple versions of Python) can play well together.

I have tried a Windows native solution and it worked on my machine. But the native solution has not yet been consistent enough on different computers so we're going to stick with WSL for the time being.

Listed below are the steps to get all set up on Windows. It takes a while to complete all the steps. But most of the time is spent waiting for things to install and build.

Please let me know if you have any issues.

**Note:** the > character represents your terminal prompt. Do NOT enter that part.

E.g. `> pyenv -h` means to enter `pyenv -h` at your terminal prompt.

## WSL

- [Install WSL](https://codefellows.github.io/code-201-prework/prework/windows/02_WSL_Ubuntu_setup.html){:target="_blank"}
  - Stop at end of page 1

## Pyenv

- [Pyenv Installer](https://github.com/pyenv/pyenv-installer){:target="_blank"}
  - Make sure to [install prerequisite](https://github.com/pyenv/pyenv/wiki/Common-build-problems){:target="_blank"} libraries following instructions for Ubuntu/Debian
  - Note **warning** at bottom of installer feedback in terminal regarding adding to .bashrc

## Installing Python

Now we can (finally) install Python

`> pyenv install 3.8.2`

This will take a while but when it's all done...

`> pyenv versions`

should show Python 3.8.2 available. Let's make it the default version

`> pyenv global 3.8.2`

check python version again

`> python —-version`

Should now be 3.8.2

## Poetry

- [Install Poetry](https://python-poetry.org/docs/#installation){:target="_blank"}
  - Use **osx / linux / bashonwindows install instructions**
  - After install run `> poetry config virtualenvs.in-project true` in terminal
- `> poetry -h`
- `> poetry new python-fun`
- `> cd python-fun`
- `> poetry shell`
  - You may get an error here regarding permissions on .config folder.
    - If so ```> sudo chown your_unix_username /home/your_unix_username/.config```
- `> poetry install`
- `> pytest`
  - Should be all green

## VS Code - WSL Integration

- Install the [Remote - WSL Extension](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-wsl){:target="_blank"} on VS Code
  - This allows you to use WSL as your integrated development environment and will handle compatibility and pathing for you. Learn more.
- Restart VS Code
- Install [Python Extension](https://marketplace.visualstudio.com/items?itemName=ms-python.python){:target="_blank"}
  - Takes a while to fully install, Check status in Extensions panel
  - Restart VS Code
- Open python file in editor
  - Notice wrong virtual environment
- Restart VS Code
- Select correct virtual environment from dropdown when you click on Python Interpreter
  - Usually at bottom left of screen
  - will have your folder name as part of it
- Next time you start VS Code should hold on to it
