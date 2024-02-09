# Projects
Projects I did in school or by myself

### Programs

I work with [Python Version 3.10](https://www.python.org/downloads/release/python-31011/). Most likely everything also works with the latest stable [Version 3.11](https://www.python.org/downloads/), but I haven't tested it.

Furthermore, it is recommended to use:
- [Visual Studio Code](https://code.visualstudio.com/)
- [GitHub Desktop](https://desktop.github.com/)

### Working Directory

Create a directory named *Projects* as a working environment for this repository, for example, named `Riccardo's Projects`, like this:

```
C:\Data\Riccardo_Projects
```

I set everything up so that this directory can be easily renamed or moved later.

### Clone GitHub Repository

Clone the [MMA GitHub Repository](https://github.com/visciric/Projects.git) into the working directory. You can use either *GitHub Desktop* or the following command in a terminal:

```
git clone https://github.com/visciric/Projects.git
```

where the current version of the repository is cloned. You can always update this with *GitHub Desktop* or the `git pull` command in the terminal when I push new content.

### Directory for Personal Work

For your personal work, you need another subdirectory. You can either create one immediately, for example, `My_Projects`, like this:

```
C:\Data\Riccardo_Projects\My_Projects
```

Or better yet, you create your own repository on GitHub or ZHAW GitHub Enterprise and clone it into the `Riccardo_Projects` working directory as well.

### Python Virtual Environment

I set up a Virtual Environment defined by the `requirements.txt` file. This ensures that you have the same packages installed. The environment should be located in the parent working directory so that it can be used in all subdirectories.

We perform the following steps in the terminal in the working directory (open the working directory in VS Code and open a new terminal there).

- Windows:
    1. Create a Virtual Environment named `venv`:
        ```
        python -m venv venv
        ```
    2. Activate the environment:
        ```
        venv\Scripts\activate
        ```
    3. Update pip:
        ```
        python -m pip install -U pip
        ```
    4. Install all required packages:
        ```
        pip install -r Projects\requirements.txt
        ```

- Mac:
    1. Create a Virtual Environment named `venv`:
        ```
        python3 -m venv venv
        ```
    2. Activate the environment:
        ```
        source venv/bin/activate
        ```
    3. Update pip:
        ```
        python3 -m pip install -U pip
        ```
    4. Install all required packages:
        ```
        python3 -m pip install -r Projects/requirements.txt
        ```

## Lizenz

[![Creative Commons Lizenzvertrag](https://i.creativecommons.org/l/by-sa/4.0/80x15.png)](http://creativecommons.org/licenses/by-sa/4.0/)  
Dieses Werk ist lizenziert unter einer [Creative Commons Namensnennung - Weitergabe unter gleichen Bedingungen 4.0 International Lizenz](http://creativecommons.org/licenses/by-sa/4.0/).
