#!/usr/bin/env python
# coding: utf-8

# In[1]:


from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "Hello, Flask is working!"

if __name__ == '__main__':
    app.run(debug=True)


# In[ ]:


from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "Hello, Flask is working!"

if __name__ == '__main__':
    app.run(debug=True)


# In[ ]:


execution_count = None


# In[ ]:


execution_count = None


# In[ ]:


import json

data = json.loads('{"execution_count": None}')


# In[ ]:


import json

data = json.loads('{"execution_count": None}', strict=False)
# OR Manually Replace Null
data = json.loads('{"execution_count": None}'.replace("None", "None"))


# In[ ]:





# In[ ]:




