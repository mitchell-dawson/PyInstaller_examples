# PyInstaller_examples
Examples applications using PyInstaller

1. Make one file
2. one file with a numpy, csv import, Build as one-file also
3. two files, one imports function from other 
4. three files, two .py, one .csv, one reads from other (runtime changes)
5. four files, two .py, two .csvs in a subfolder, py file reads in folder of CSVs
6. Kivy app Simple One .py file Kivy app
7. Kivy app with .py file and .ky file
8. Kivy app,  .py and .kv, one imports function from other
9. Kivy app, 2 .py, .kv, .csv, one imports function from other which reads .csv
10. Full ground truthing app


App1 - Simplest app possible
```
pyinstaller main.spec
```

App2 - Import standard function
```
pyinstaller --name app_2 main.py
```

App3 - Import a function from another script
```
pyinstaller --onefile --name app_3 main.py
```

App4 - Include a single data file
```
pyinstaller--onefile --add-data="MOCK_DATA.csv:." --name app_4 main.py
```

App5 - Include folders of data
```
pyinstaller --onefile --add-data "data:data" --name app_5 main.py
```

App6 - Simple single file Kivy app 
```
pyinstaller --onefile --name app_6 main.py
```

App7 - Kivy app with a separate kv file
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

