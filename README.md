# ARD Python Summer School

![](https://www.python.org/static/community_logos/python-logo-master-v3-TM-flattened.png)

## Welcome to the EPAR7 ARD Python Summer School!

This informal course is meant to provide a *gentile* introduction to computer programming with the __[Python](https://www.python.org/)__ language - __with no previous experience required__. 

---

## First Time Setup

This repository uses __[uv](https://docs.astral.sh/uv/)__ for Python project and environment management. If you are new to using a  computer terminal, uv, Python environments, Jupyter notebooks—don’t worry! This guide will walk you through everything you need to get set up and verify that your system is ready.

> #### Computer Shell Command Blocks
> In this guide, whenever you see text located within a code block
>
> ```shell
> # which will look...
> ...something like this
> ```
>
> you can copy and paste these commands directly into your command prompt, Bash, PowerShell, or terminal window. 


### 1. Install and Verify `uv`

`uv` is a fast Python package and environment manager. You can install it using the instructions from the __[uv documentation](https://docs.astral.sh/uv/getting-started/installation/)__

Once `uv` has been installed, run this simple test:

```shell
uv --version
```

If you see a version number (for example: `uv 0.10.4`), you're all set!

### 2. Set Up the Project Environment

Once `uv` is installed and verified, navigate to the root of the repository:

```shell
cd path/to/this/repository
```

Then use `uv` to install all of the required packages for the project:


```shell
uv sync
```

This will:

- Create a virtual python environment specific to the project  
- Install all dependencies exactly as pinned in `uv.lock`  
- Ensure the correct version of Python is installed (to match the `.python-version` file)

### 3. Launch Jupyter Lab to View Notebooks

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