# PyInstaller (+Kivy) Examples
Here are seven examples, of roughly increasing complexity, that demonstrate how to package python applications using the basic commands of [PyInstaller](https://www.pyinstaller.org/). The later examples also demonstrate how to package a basic Kivy GUI app.


## Requirements
We recommend that this code is run inside a [virtual environment](https://www.pythonforbeginners.com/basics/how-to-use-python-virtualenv/).

- Python (Tested on 2.7)
- PyInstaller
- Numpy (To test non-standard library imports)
- Pandas (To process a csv file)
- Cython (Kivy dependency)
- Kivy (For apps 6 & 7, Tested on v1.10.1)
```
pip install pyinstaller
pip install numpy
pip install pandas
pip install cython
pip install kivy
```

## Running the Code
1. Download this repository
2. Install the requirements
3. Navigate to the app folder
4. Have a look at the files inside the app folder to see what they do 
   - The examples are all kept very short and basic
5. Run the corresponding PyInstaller command 
   - see 'Apps' section below
6. Have a look at the folders and files that are created 
    - see 'Expected output' section below
7. Try running the app 
    - The application is found inside the newly created `dist` folder





## Apps

### App1 - Simplest app possible
```
pyinstaller main.spec
```

### App2 - Import standard function
```
pyinstaller --name app_2 main.py
```

### App3 - Import a function from another script
```
pyinstaller --onefile --name app_3 main.py
```

### App4 - Include a single data file
```
pyinstaller--onefile --add-data="MOCK_DATA.csv:." --name app_4 main.py
```

### App5 - Include folders of data
```
pyinstaller --onefile --add-data "data:data" --name app_5 main.py
```

### App6 - Simple single file Kivy app 
```
pyinstaller --onefile --name app_6 main.py
```

### App7 - Kivy app with a separate kv file
```
pyinstaller --onefile --add-binary="style.kv:." --name app_7 main.py
```

## Expected Outcomes
The commands above produce two folders and a `.spec` file:
- The `build` folder contains temporary files that were used whilst the application was being built
- The `dist` folder contains the application itself, which can now be distributed to other users
- The `.spec` file tells PyInstaller how to process your script (see reference 2 for further info)

The application can be found inside the `dist` folder

## Location of Data and Binaries
At run-time, the app will create a temporary folder to store data and binary files. The path to this folder can be accessed by the environment variable `_MEIPASS` (only at run-time).

## References
1. [Useful Introduction video](https://www.youtube.com/watch?v=tOTLqUQC-k0)
2. [Spec files](https://pythonhosted.org/PyInstaller/spec-files.html)
3. [Including data with app](https://pyinstaller.readthedocs.io/en/v3.3.1/spec-files.html)
4. [Bundling data files using onefile](https://stackoverflow.com/questions/7674790/bundling-data-files-with-pyinstaller-onefile)
5. [Using onefile](https://stackoverflow.com/questions/51455765/build-multiple-py-files-into-a-single-executable-file-using-pyinstaller)
6. [Including data with PyInstaller](https://stackoverflow.com/questions/41870727/pyinstaller-adding-data-files)
7. [Basic Kivy App](https://kivy.org/doc/stable/guide/basic.html)
8. [Builder kivy options](https://kivy.org/doc/stable/guide/lang.html)
9. [CSV file generator 1](https://www.mockaroo.com/)
10. [CSV file generator 2](https://onlinerandomtools.com/generate-random-csv)

## Author
**[Mitchell Dawson](http://www.dtc.ox.ac.uk/people/14/dawsonm/)**