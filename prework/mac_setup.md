# Mac Set Up

## Prerequisites

Make sure you've followed the Code Fellows  [Set Up Guide](https://codefellows.github.io/setup-guide/mac/terminal/setup.html){:target="_blank"}

## Overview

Steps to get a professional Python development environment on Mac.

**Note:** the > character represents your terminal prompt. Do NOT enter that part.

E.g. `> pyenv -h` means to enter `pyenv -h` at your terminal prompt.

- Install [Pyenv](https://github.com/pyenv/pyenv#homebrew-on-macos){:target="_blank"} using Homebrew
  - Make sure to follow **Post Installation** steps
  - Getting everything set up right is spread across several documents. The links are all there in the docs but included here as well for reference.
    - [Post Installation](https://github.com/pyenv/pyenv#basic-github-checkout){:target="_blank"}
    - [Building Python](https://github.com/pyenv/pyenv/wiki){:target="_blank"}
    - [Common Problems](https://github.com/pyenv/pyenv/wiki/Common-build-problems){:target="_blank"}
- > pyenv install 3.8.2
- > pyenv global 3.8.2
- > python --version
  - Should say 3.8.2
- Install [Poetry](https://python-poetry.org/docs/#installation){:target="_blank"}
  - After install run `> poetry config virtualenvs.in-project true` in terminal
