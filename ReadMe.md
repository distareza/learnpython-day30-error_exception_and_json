    type of exeption :
        FileNotFoundError
            with open("file.txt") as file:
                file.read()
                
        KeyError
            a_dict = {"key": "value"}
            value = a_dict["non_existing_key"]
            
        IndexError
            list = ["Apple", "Banana", "Pear"]
            list[3]
            
        TypeError
            text = "abc"
            print(text + 1)

        Exception
            general error
        
        BaseException,RuntimeError,OSError,SyntaxError,ZeroDivisionError,
        NameError,ValueError,AssertionError 

    try:
        <Something that might cause an exception>
    except: 
        <do this if there was an exception>
    else:
        <do this if there were no exception>
    finally:
        <do this no matter what happen>


----------------------------------------------------------

    https://docs.python.org/3/library/json.html 
    
    import json
    new_data = { key: value }
    try:
        with open("data.json", "r") as data_file:
            data = json.load(data_file)
            data.update(new_data)
    except FileNotFoundError:
        data = new_data
    except json.decoder.JSONDecodeError:
        data = new_data

    with open("data.json", "w") as data_file:
        json.dump(data, data_file, indent=4)


