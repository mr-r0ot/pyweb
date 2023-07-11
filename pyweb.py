import os,shutil


def page(folder="templates",page="index.html", title="Pyweb Site",background=False,background_linear_gradient=False,font_page="sans-serif",charset="UTF-8",lang="en",content="IE=edge",page_center=False):
    try:
        shutil.rmtree(folder)
    except:
        pass
    os.mkdir(folder)
    os.chdir(folder)

    __html=open(page,"w+")
    __css=open("style.css","w+")
    __js=open("main.js","w+")
    __html.write(f"""
<!DOCTYPE html>
<html lang="{lang}">
<head>
    <meta charset="{charset}">
    <meta http-equiv="X-UA-Compatible" content="{content}">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{title}</title>
    <link rel="stylesheet" href="style.css" />
</head>
<body>
""")
#///////////////////////////



    #Set Page On center
    if page_center!=False:
        page_center=("""
    display: flex;
    align-items: center;
    flex-direction: column;
    height: 100vh;
    padding: 10px;
""")
    else:
        page_center=("")
    
# /////////////////////////////




    #Set Background
    bcgcode_bb=("")
    if background!=False:
        bcgcode_bb=("""background-color: """+background+""";""")
    
    bcgcode_gg=("")
    if background_linear_gradient!=False:
        bcgcode_gg=("""background: linear-gradient("""+background_linear_gradient+""");""")




    #Make Css Code
    csspcode=("""
body{
    """+page_center+"""
    """+bcgcode_bb+"""
    """+bcgcode_gg+"""
}
* {
	margin: 0;
	padding: 0;
	font-family: """+font_page+""";
	color: #222;
}
a {
	text-decoration: none;
}
ul {
	list-style-type: none;
}
""")
#//////////////////////////
    #Write Code
    __css.write(csspcode)
    __css.close()
    __html.close()
    __js.close()
#==========================================










def print(text,page="index.html",type="h1",font_size="60px",font_family="unset",color="#000",text_align="center"):
    __html=open(page,"a+")
    hhcode=(f"""    <{type} style="font-size: {font_size}; font-family: {font_family}; color: {color}; text-align: {text_align}; ">{text}</{type}>""")
    __html.write(hhcode)
    __html.close()
#==========================================






def input(page="index.html",text="",type="text",width="300px",height="50px",background_color="#000",font_size="25px",name="",id="",font_family="unset",color="#ffffff",text_align="center"):
    __html=open(page,"a+")
    #Satrt Make
    code=(f'''  <input type="{type}" style="width: {width}; height: {height}; background-color: {background_color}; font-size: {font_size}; font-family: {font_family}; color: {color}; text-align: {text_align};" placeholder="{text}" ''')

    #set id and name
    if id!="":
        code=('''{} id="{}" '''.format(code,id))
    if name!="":
        code=('''{} name="{}" '''.format(code,name))
    
    #End
    code=("{} ></input>".format(code))

    #Write To Index File
    __html.write(code)
    __html.close()







def button_link(text,link,page="index.html",width="170px",height="70px",justify_content="space-evenly",flex_direction="column",display="flex",background_color="#000",font_size="30px",font_family="unset",color="#ffffff",text_align="center"):
    __html=open(page,"a+")
    code=(f'''  <div style="width: {width};height: {height};background-color: {background_color};color: {color};display: {display};font-family: {font_family};flex-direction: {flex_direction};justify-content: {justify_content};align-items: {text_align};">   <a style="background-color: {background_color}; font-size: {font_size}; font-family:{font_family}; color: {color}; text-align: {text_align};" href="{link}">{text}</a>  </div>''')
    __html.write(code)
    __html.close()





def button(text,page="index.html",onclick="",width="180px",height="80px",background_color="#000",font_size="30px",font_family="unset",color="#ffffff",text_align="center"):
    __html=open(page,"a+")
    code=(f'''  <button onclick="{onclick}" style="width: {width}; height: {height}; background-color: {background_color}; font-size: {font_size}; font-family:{font_family}; color: {color}; text-align: {text_align};">{text}</button>''')
    __html.write(code)
    __html.close()













class JS:



    class cookie:
        def new(data,page="main.js",var=False):
            __js=open(page,"a+")
            if var==False:
                code=(f'''document.cookie = "{data}"; ''')
            else:
                code=(f'''document.cookie = {data}; ''')
            __js.write(code)
            __js.close()
    





    class request:
        def new(varname,url,page="main.js",var=False):
            __js=open(page,"a+")
            if var==False:
                code=('''
var request = new XMLHttpRequest();
request.open('GET', "'''+str(url)+'''", true);
request.onload = function() { var '''+str(varname)+''' = request.status };
request.onerror = function() { var '''+str(varname)+''' = "error" };
request.send();
''')
            else:
                code=('''
var request = new XMLHttpRequest();
request.open('GET', '''+str(url)+''', true);
request.onload = function() { var '''+str(varname)+''' = request.status };
request.onerror = function() { var '''+str(varname)+''' = "error" };
request.send();
''')
            __js.write(code)
            __js.close()










    def sava_var(varname,data,page="main.js",var=False):
        __js=open(page,"a+")
        if var==False:
            code=(f'''var {varname} = "{data}";''')
        else:
            code=(f'''var {varname} = {data};''')
        __js.write(code)
        __js.close()
    

    def reload(page="main.js"):
        __js=open(page,"a+")
        code=(f''' location.reload(); ''')
        __js.write(code)
        __js.close()


    def open_function(function_name,idgetlist=[],jscode="",page="main.js"):
        __js=open(page,"a+")
        ffget=("")
        for cx in idgetlist:
            ffget=("""
    var {};
""".format(cx))
        
        for cxw in idgetlist:
            ffget=("""
    {} = document.getElementById("{}").value;
""".format(cxw,cxw))
                
        code=('''
function '''+function_name+'''() {
'''+ffget+'''
'''+jscode+'''
''')
        __js.write(code)
        __js.close()


    def close(page="main.js"):
        __js=open(page,"a+")
        code=('''}''')
        __js.write(code)
        __js.close()


    def alert(text,var=False,page="main.js"):
        __js=open(page,"a+")
        if var==False:
            code=(f'''alert("{text}");''')
        else:
            code=(f'''alert({text});''')
        __js.write(code)
        __js.close()


    def write_on_page(text,var=False,page="main.js"):
        __js=open(page,"a+")
        if var==False:
            code=(f'''document.write("{text}");''')
        else:
            code=(f'''document.write({text});''')
        __js.write(code)
        __js.close()


    def console(text,page="main.js",type="log",var=False):
        __js=open(page,"a+")
        if var==False:
            code=(f'''console.{type}("{text}");''')
        else:
            code=(f'''console.{type}({text});''')
        __js.write(code)
        __js.close()


    def open_while(wh,page="main.js"):
        __js=open(page,"a+")
        code=('''
    while ('''+str(wh)+'''){
    ''')
        __js.write(code)
        __js.close()


    def open_url(url,page="main.js",var=False,type="onwindow",width="400",height="300"):
        __js=open(page,"a+")
        if type=="newwindow":
            if var=="False":
                code=(f'''window.open("{url}","","toolbar=no, width={width},height={height},directories=no,menubar=no,scrollbars=no");''')
            else:
                code=(f'''window.open({url},"","toolbar=no, width={width},height={height},directories=no,menubar=no,scrollbars=no");''')
        else:
            if var==False:
                code=(f'''window.open("{url}");''')
            else:
                code=(f'''window.open({url});''')
        __js.write(code)
        __js.close()










def run(browers=False,page="index.html",js_file="main.js", host='0.0.0.0',home_file="index.html",port="8080",varname='app',flask_code=""):
    __html=open(page,"a+")
    __html.write(f"""
    <script src="{js_file}"></script>
    </body>
</html>
""")
    __html.close()
    if browers==True:
        os.startfile("index.html")
    else:
        from flask import Flask, render_template
        exec(f"""
try:
    exec("from flask import Flask, render_template")
except:
    print("Flask Lib Not Installed!")
    exit()
from flask import Flask, render_template
{varname} = Flask('app')

@{varname}.route("/")
def home():
    return render_template("{home_file}")

{flask_code}

app.run(host='{host}', port={port})
""")
