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
import json

json_string = '{"execution_count": null}'
json_string = json_string.replace("null", "None")  # Replace JavaScript null with Python None
data = eval(json_string)  # Safely convert to Python dictionary

print(data)  # Debug ke liye
import json

json_string = '{"execution_count": null}'
print("Raw JSON Data:", json_string)  # Debugging ke liye

try:
    data = json.loads(json_string)
    print("Parsed Data:", data)
except json.JSONDecodeError as e:
    print("JSON Error:", e)

# Flask App Start
from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "Flask App is Running!"

if __name__ == '__main__':
    print("Starting Flask App...")  # Debugging ke liye
    app.run(debug=True)




