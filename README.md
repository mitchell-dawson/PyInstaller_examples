# PyInstaller examples
Examples applications using PyInstaller

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

## References
- [Including data with app](https://pyinstaller.readthedocs.io/en/v3.3.1/spec-files.html)
- [Bundling data files using onefile](https://stackoverflow.com/questions/7674790/bundling-data-files-with-pyinstaller-onefile)
- [Using onefile](https://stackoverflow.com/questions/51455765/build-multiple-py-files-into-a-single-executable-file-using-pyinstaller)
- [Including data with PyInstaller](https://stackoverflow.com/questions/41870727/pyinstaller-adding-data-files)
- [Basic Kivy App](https://kivy.org/doc/stable/guide/basic.html)
- [Builder kivy options](https://kivy.org/doc/stable/guide/lang.html)
- [CSV file generator 1](https://www.mockaroo.com/)
- [CSV file generator 2](https://onlinerandomtools.com/generate-random-csv)

