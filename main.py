from flask import Flask, render_template, request
from random import choice
import solver

someList = [1, 2, 3, 4,5]

web_site = Flask(__name__)

@web_site.route('/')
def index():
  a=solver.show()
  return render_template('index.html',a00=a[0],a01=a[1],b1=a[2],myList = someList,len=len(someList))

web_site.run(host='0.0.0.0', port=8080)