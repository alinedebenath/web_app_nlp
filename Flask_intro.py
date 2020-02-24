#!/usr/bin/env python
# coding: utf-8

# In[ ]:





# Flask for webapp : http://www.xavierdupre.fr/app/ensae_teaching_cs/helpsphinx/notebooks/TD2A_eco_debuter_flask.html

# In[2]:


from flask import Flask  # pip install flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!"

if __name__ == "__main__":
    app.run()


# In[ ]:




