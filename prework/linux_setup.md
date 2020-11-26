# Ubuntu Set Up

## Prerequisites

- Make sure you've followed the Code Fellows  [Set Up Guide](https://codefellows.github.io/setup-guide/ubuntu_linux/terminal/setup.html){:target="_blank"}
- [Install Homebrew](https://docs.brew.sh/Homebrew-on-Linux){:target="_blank"} which now runs on Linux.

## Overview

Steps to get a professional Python development environment.

**Note:** the > character represents your terminal prompt. Do NOT enter that part.

E.g. `> pyenv -h` means to enter `pyenv -h` at your terminal prompt.

- > sudo apt install curl
- > sudo apt install git
- > brew install pyenv
  - see linuxbrew caveats in common build problems
    - > brew install [the additional dependencies]
- > pyenv install 3.8.2
- > pyenv global 3.8.2
- > python --version
  - should say 3.8.2
- Install [Poetry](https://python-poetry.org/docs/#installation){:target="_blank"}
  - After install run `poetry config virtualenvs.in-project true` in terminal
