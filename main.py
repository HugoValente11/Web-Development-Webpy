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
       '/(.*)', 'index'
       )

# Create web application
app = web.application(urls, globals())

# Define class index and method GET
class index:
    def GET(self, name):
        return f"<h1>Hello {name[0].upper() + name[1:]}. </h1>How are you?"
    
if __name__ == "__main__":
    app.run()

