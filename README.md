# PyInstaller_examples
Examples applications using PyInstaller

1. Make one file
2. one file with a numpy, csv import, Build as one-file also
3. two files, one imports function from other 
4. three files, two .py, one .csv, one reads from other (runtime changes)
5. four files, two .py, two .csvs in a subfolder, py file reads in folder of CSVs

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
