**PURPOSE:**
--

This repository contains files required for creating topsis package on pipy.org

The below files must be first created
1. setup.py 
2. README.md
3. LICENSE(optional)

After creating the above metioned files run the following commands on the command prompt
```sh
python setup.py sdist
pip install twine
twine upload dist/*
```
