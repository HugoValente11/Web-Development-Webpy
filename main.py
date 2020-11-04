# -*- coding: utf-8 -*-
"""
Created on Wed Nov  4 14:25:07 2020

@author: Hugo
"""

# get web.py
# pip3 install web.py

# import module 
import web

# Set routes (You can use Regex)
urls =(
       '/(.*)/(.*)', 'index'
       )

# Specify where to find templates to render 
render = web.template.render('resources/')

# Create web application
app = web.application(urls, globals())

# Define class index and method GET
class index:
    def GET(self, name, age):
        name = name[0].upper() + name[1:]
        return render.main(name,age)
    
if __name__ == "__main__":
    app.run()

