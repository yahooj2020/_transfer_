_#! encoding=utf8


# 各种编程语言的后缀  https://gist.github.com/ppisarczyk/43962d06686722d26d176fad46879d41
import markdown

#
import os


def writeinto_htmlfile(filename,data):
    with open(filename,"a",newline="",encoding="utf-8") as f:
        f.write(data)
        f.write("\n")



def get_md_text(filename):

    cs_md_top = "``` \n"
    cs_md_body = ""
    cs_md_footer = "\n```"
    with open(filename,"r",encoding="utf-8") as f:
        data = f.readlines()
        cs_md_body = "".join(data)

    ret_string = cs_md_top + cs_md_body +cs_md_footer
    return ret_string





css_theme_dict ={
    ".bat":"igor",
    ".cs":"material",
    ".java":"material",
    ".jl":"material",
    ".js":"material",
    ".json":"material",
    ".R":"material",
    ".yml":"material",
    ".yaml":"material",
    ".c":"native",
    ".h":"native",
    ".php":"native",
    ".pl":"native",
    ".py":"native",
    ".rb":"native",
    ".sh":"native",
    ".sql":"native",
    ".swift":"native",
    ".go":"monokai",
    ".lua":"monokai",
    ".vue":"monokai",
    ".ts":"monokai",
    # "":"default",

}



def read_file_to_html(file_folder):

    for_test_file = os.path.join(os.getcwd(), file_folder)
    for i1, i2, files in os.walk(for_test_file):
        for item in files:
            css_template_top = '<head> \n  <meta http-equiv="Content-Type" content="text/html; charset=UTF-8" /> \n  <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/css/bootstrap.min.css" >'
            writeinto_htmlfile(os.path.join(templates_path,item+".html"), css_template_top)
            if "." in item :
                suffix_info = "." + item.split(".")[1]
                if suffix_info in css_theme_dict.keys():
                    css_theme_name =css_theme_dict[suffix_info]
                    css_theme_template = '<link rel="stylesheet" href="../static/{0}.css"> \n </head> \n <body>'.format(css_theme_name)
                    writeinto_htmlfile(os.path.join(templates_path,item+".html"),css_theme_template)
                    file_path_info = os.path.join(i1,item)
                    ret_file = get_md_text(file_path_info)

                    html = markdown.markdown(ret_file, extensions=[
                        "markdown.extensions.extra",
                        "markdown.extensions.codehilite",
                    ])
                    writeinto_htmlfile(os.path.join(templates_path,item+".html"),html)
                else:
                    css_theme_name = "default"
                    css_theme_template = '<link rel="stylesheet" href="../static/{0}.css"> \n </head> \n <body>'.format(
                        css_theme_name)
                    writeinto_htmlfile(os.path.join(templates_path,item+".html"), css_theme_template)
                    file_path_info = os.path.join(i1, item)
                    ret_file = get_md_text(file_path_info)

                    html = markdown.markdown(ret_file, extensions=[
                        "markdown.extensions.extra",
                        "markdown.extensions.codehilite",
                    ])
                    writeinto_htmlfile(os.path.join(templates_path,item+".html"), html)

            else:
                css_theme_name ="default"
                css_theme_template = '<link rel="stylesheet" href="../static/{0}.css"> \n </head> \n <body>'.format(css_theme_name)
                writeinto_htmlfile(os.path.join(templates_path,item+".html"),css_theme_template)
                file_path_info = os.path.join(i1,item)
                ret_file = get_md_text(file_path_info)

                html = markdown.markdown(ret_file, extensions=[
                    "markdown.extensions.extra",
                    "markdown.extensions.codehilite",
                ])
                writeinto_htmlfile(os.path.join(templates_path,item+".html"),html)



if __name__ == "__main__":
    templates_path = os.path.join(os.getcwd(),"templates")

    ret_file = get_md_text(file_path_info)

    html = markdown.markdown(ret_file, extensions=[
        "markdown.extensions.extra",
        "markdown.extensions.codehilite",
    ])
    writeinto_htmlfile(os.path.join(templates_path, item + ".html"), html)

# pygments---->css file theme
# from pygments import highlight
# from pygments.lexers import PythonLexer
# from pygments.formatters import HtmlFormatter
#
# code = 'print "Hello World"'
# print(highlight(html,lexer=PythonLexer(),formatter=HtmlFormatter()))



# vs java NG,
# xcode java NG,
# zenburn java NG,
# fruity java NG,
# rainbow_dash java NG,
# solarized-light java NG,
# stata-dark java NG,
# perldoc java NG,
# manni.css java NG,
# murphy  python NG
# python, java ,javascript,php ,c c++ golang,


# default :
# gruvbox-dark :
# igor : .bat
# material :  .cs  .java  .jl  .js .json .R  .yml .yaml
# native:  .c .h  .php  .pl .py  .rb  .sh .sql   .swift
# pastie
# vim
# monokai : .go .lua  .vue .ts


