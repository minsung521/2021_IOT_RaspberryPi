import os
path = "./static/images/1 copy 3.jpeg"
if os.path.isfile(path) : 
  os.remove(path)