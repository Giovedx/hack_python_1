"""
text: "fooziman" output => ["F","0","0","Z","1","M","@","N"]
"""

def fn_hack_10():
    result = "fooziman"
    result = result.upper()
    result = result.replace("O" , "0").replace("I","1").replace("A", "@")
    result = list(result)
    
    print(result)
    return result  

fn_hack_10()

