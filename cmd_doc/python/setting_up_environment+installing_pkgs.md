**SETTING UP ENVIRONEMENT:**
--

**What is an environment?**
--

A virtual environment is a tool that helps to keep dependencies required by different projects separate by creating isolated python virtual environments for them. This is one of the most important tools that most of the Python developers use.


**ANACONDA COMMAND LINE:**
--

```sh

conda create -n 'environment-name'   #this will create required environemnt
conda activate 'environment-name'    #to activate required environment
conda deactivate 'environment-name'  #to deactivate required environment

#note: u can also create environments with different versions of python 
#conda create -n <env-name> python=2.7
#conda create -n <env-name python=3.7

conda env remove --name <env-name> #this will delete the environment
conda env list                     #list available environments
```

**INSTALLING PACKAGES INSIDE A ENVIRONMENT:**

```sh
conda list                     #list all packages in current env
conda install <package-name>   #to install some package in your current environment
conda install <package-1> <package-2> <package-3>
conda search <package-name>    #search for a package  in current env
conda remove <package-name>    #to remove some packhge in current env
```

**ON COMMAND PROMPT:**

```sh
python -m venv nameofenv
nameofenv/Scripts/activate
```
do this using administrator priviledges
