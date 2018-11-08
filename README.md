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


app1
```
pyinstaller main.spec
```

app_2
```
pyinstaller --name app_2 main.py
```

app3
```
pyinstaller --onefile --name app_3 main.py
```

app4
```
pyinstaller--onefile --add-data="MOCK_DATA.csv:." --name app_4 main.py
```
app5 (including folders of data is different to including single files)
```
pyinstaller --onefile --add-data "data:data" --name app_5 main.py
```

app6
```
pyinstaller --onefile --name app_6 main.py
```