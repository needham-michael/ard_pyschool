# ARD Python Summer School

![](https://www.python.org/static/community_logos/python-logo-master-v3-TM-flattened.png)

## Welcome to the EPAR7 ARD Python Summer School!

This informal course is meant to provide a *gentile* introduction to computer programming with the __[Python](https://www.python.org/)__ language - __with no previous experience required__. 

---

## First Time Setup

This repository uses __[uv](https://docs.astral.sh/uv/)__ for Python project and environment management. If you are new to using a computer terminal, uv, Python environments, Jupyter notebooks—don’t worry! This guide will walk you through everything you need to get set up and verify that your system is ready.


> ### Before we jump in... 
> 
> Here are two quick things to know to help you follow this guide
> 
> #### 1. Computer Shell Command Blocks
> In this guide, whenever you see text located within a code block
>
> ```shell
> # which will look...
> ...something like this
> ```
>
> you can copy and paste these commands directly into your command prompt, Bash, PowerShell, or terminal window. Then press the `enter` key to run the command. __At some point you will get an error__, but that's what Google is for!
>
> #### 2. Navigating in a Computer Shell Window
>
> The blinking computer shell prompt may seem mysterious and intimidating, but it doesn't have to be! 
>
> When you open a computer shell (e.g., PowerShell, Bash, etc.) you are essentially dropped into some location on your computer system. In other words, you are within some folder of your file explorer.  We will call this your Current Working Directory or `CWD`. You can learn how to navigate through your computer file system using just the three commands below:
> 
> | Command | Short For | Purpose |
> | ------- | --------- | ------- |
> | `cd` | Change Directory | Move from the `CWD` to a new loction |
> | `pwd` | Print Working Directory | Print out the `CWD` | 
> | `ls` | List | List all files and folders within the `CWD` |
>
> For a more in-depth introduction, see this __[Blog Post](https://www.redhat.com/en/blog/navigating-filesystem-linux-terminal)__. It is written for a linux system, but the concepts (and the specific commands!) are directly transferrable to Windows.


### 1. Clone this repository (Optional, requires `git`)

If you're an entry-level user, the simplest way to follow along with the notebooks in this repository is to download the notebooks one-at-a-time as you need them, using the download icon on the GitHub webpage for each notebook. If this sounds like you, skip below to step 2!  

However if you would like, you can instead use `git` to `clone` the entire repository onto your local computer (which, of course, requires that you have `git` installed on your system). In your shell window, navigate to the location where you want to clone the repository

```shell
# Navigate to the desired location
cd /path/to/desired/location
```

Once you are at the correct location, verify that git has been installed correctly

```shell
git --version
```

Finally, use the `git clone` command to clone the repository.

```shell
# clone the repository
git clone https://github.com/needham-michael/ard_pyschool.git
```

### 2. Install and Verify `uv`

`uv` is a fast Python package and environment manager. You can install it using the instructions from the __[uv documentation](https://docs.astral.sh/uv/getting-started/installation/)__

Once `uv` has been installed, run this simple test:

```shell
uv --version
```

If you see a version number (for example: `uv 0.10.4`), you're all set!

### 3. Set Up the Project Environment

Once `uv` is installed and verified we will use it to create a containerized __[virtual environment](https://docs.astral.sh/uv/pip/environments/)__ (commonly `venv` or `.venv`) where we can download any extra third-party packages needed for our python programs and notebooks. The steps are slightly different based on whether or not you cloned the repository. 

Either way, navigate to your project folder (either the cloned repository, or where you will download notebooks).

```shell
cd path/to/folder
```

> #### If you did not clone the repository
>
> To duplicate the virtual environment that was used to write the notebooks in this repository, you will need the `pyproject.toml` and `uv.lock` files. Download those two files from GitHub into your local project folder. 

Use `uv` to install all of the required packages for the project:

```shell
uv sync
```

This will:

- Create a virtual python environment specific to the project  
- Install all packages listed in the `pyproject.toml` file with the exact versions specified in the `uv.lock` file.
- Ensure the correct version of Python is installed.

**If you run into an error**, try cleaning the cache with `uv cache clean` and then rerunning the `uv sync` command.

### 4. Launch Jupyter Lab to View Notebooks

With the environment ready, start Jupyter Lab:

```shell
uv run jupyter lab
```

or, for the older Jupyter Notebook interface:

```shell
uv run jupyter notebook
```

Launching jupyter through `uv` will ensure that the notebooks use the correct project virtual environment created by `uv sync`.

---

*Some of the content of thise `README.md` was created with the assistance from a generative AI tool. The content has been reviewed and edited by humans*