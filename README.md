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




# Now we go into more details.
```
pyweb.page(folder="templates",page="index.html", title="Pyweb Site",background="#222",background_linear_gradient=False,font_page="sans-serif",charset="UTF-8",lang="en",content="IE=edge",page_center=False)
```

Using ```folder=""``` we can specify the name of the folder that will be created.
By using ```page=""``` we can specify the name of the file, this feature is also present in the rest of the functions.
By using ```title=""``` we can specify the title of the site.
By using ```background=""``` we can specify the background of the site.
By using ```font_page=""``` we can specify the font of the site.
By using ```page_center=``` we can specify whether all the components of the site are in the middle of the page or not.



# print hello world
```
pyweb.print(text="hello world",page="index.html",type="h1",font_size="60px",font_family="unset",color="#000",text_align="center")
```

# start site
```
run(browers=False,page="index.html",js_file="main.js", host='0.0.0.0',home_file="index.html",port="8080",varname='app',flask_code="")
```
```
