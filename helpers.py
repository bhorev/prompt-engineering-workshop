from IPython.display import display, Markdown
from IPython.display import JSON

def prettyPrint(text):
    display(Markdown('<font size="3">'+text+'</font>')) 
    
def prettyJSON(text):
    md = """
```json
""" + text + """
```
"""
    #display(Markdown('<font size="3">\`\`\`json\n'+text+'\`\`\`</font>')) 
    display(Markdown(md)) 
    
def prettyCode(text):
    display(Markdown(text))