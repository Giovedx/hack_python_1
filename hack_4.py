"""
text: "fooziman" output => "foozimaN"
"""

def fn_hack_4():
    result = "fooziman"
    result = result[:7] + result[7].upper() 
    print(result)
    return result


fn_hack_4()