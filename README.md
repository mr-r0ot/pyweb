# pyweb framework
A great and simple framework for building different sites!


# Setup
Place the pyweb.py file next to your main file


# Creat A Site
```
# add pyweb to project
import pyweb

# make new page
pyweb.page()

# print hello world
pyweb.print("hello world")

# start site
pyweb.run(browers=True)
```
If you want the site to run on the local host, ```browser=False``` and if you want it to run on your browser, ```browers=True```
and more...
```
run(browers=False,page="index.html",js_file="main.js", host='0.0.0.0',home_file="index.html",port="8080",varname='app',flask_code="")
```
