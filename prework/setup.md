
# Set Up

## Prerequisites

**IMPORTANT:** Make sure you've completed the Code Fellows [Basic Computer Setup](https://codefellows.github.io/setup-guide){:target="_blank"} Guide



## Update Terminal/Environment

Make a back up of existing '.profile'

```bash
mv ~/.profile ~/.profile.bak
```

Create new `~/.profile` and add text below

```bash
#Linuxbrew (if needed)
if [ -d /home/linuxbrew ]; then
  eval $(/home/linuxbrew/.linuxbrew/bin/brew shellenv)
fi

#NVM
if [ -f $(brew --prefix nvm)/nvm.sh ]; then
  source $(brew --prefix nvm)/nvm.sh
fi

# Python
if command -v pyenv 1>/dev/null 2>&1; then
  eval "$(pyenv init -)"
fi

```

## Install Zsh

**Note:** this section has OS specific steps

### WSL/Linux
```console
sudo apt-get install zsh
```

### Mac

```console
brew install zsh
chsh -s /usr/local/bin/zsh
```

## Oh My Zsh


Once Zsh has been installed let's give it super powers by adding `oh-my-zsh`

```console
sh -c "$(curl -fsSL https://raw.github.com/ohmyzsh/ohmyzsh/master/tools/install.sh)"
```

Say `yes` if asked if you want to make zsh the default shell.

Last thing to do is to add instructions to load your profile.

Enter the text below in terminal.

```console
cat >> ~/.zshrc<<EOF

# Source .profile, if present.
if [ -f "$HOME/.profile" ]; then
  source "$HOME/.profile"
fi
EOF
```

Oh My Zsh is a very handy and powerful tool. Checkout the [Cheat Sheet](https://github.com/ohmyzsh/ohmyzsh/wiki/Cheatsheet) if you're interested

## Install Python Tools

- Mac
  - `xcode-select --install`
  - `brew install openssl readline sqlite3 xz zlib`
- WSL/Linux
  - `brew install bzip2 libffi libxml2 libxmlsec1 openssl readline sqlite xz zlib`
- `brew install pyenv`
- `pyenv install 3.8.5`
  - This command downloads and builds Python interpreter
  - In case of failure
    - WSL/Linux: Refer to [Pyenv Common Problems](https://github.com/pyenv/pyenv/wiki/Common-build-problems){:target="_blank"} and run the `apt-get` command at top of page under the **Ubuntu/Debian** section.
    - Mac: Make sure the Mac specific steps above were followed.
- `pyenv global 3.8.5`
- `python --version`
  - If error then restart terminal
- `brew install poetry`
- `poetry config virtualenvs.in-project true`
  - If error then restart terminal
- `poetry new python-fun`
- `cd python-fun`
- `poetry shell`
- `poetry install`
- `pytest`
- `nvm --version`

If no commands failed then you're all done.
