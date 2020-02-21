function_dict = {
"function_1": "false",
"function_2": "false"
}
def begin_1():
    function_dict.update({"function_1": "true"})
def begin_2():
    function_dict.update({"function_1": "true"})
def end_1():
    function_dict.update({"function_1": "false"})
def end_3():
    function_dict.update({"function_1": "false"})
    
begin_1()

def function_1():
    print(function_dict)
    print("Success")
    end_1()
    print(function_dict)
    begin_2()
def function_2():
    print("whoa")
    print(function_dict)
    begin_1()













if function_dict.get("function_1") == "true":
    function_1()
if function_dict.get("function_1") == "true":
    function_2()
