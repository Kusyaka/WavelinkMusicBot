from json import loads, JSONDecodeError
from os import sep
from traceback import print_exc
from typing import Any, Dict, List, Union

def jsonLoad(filename) -> Union[Dict, List, str]:
    """Loads arg1 as json and returns its contents"""
    with open(filename, "r", encoding='utf8') as file:
        try:
            output = loads(file.read())
        except JSONDecodeError:
            print(f"Could not load json file {filename}: file seems to be incorrect!\n{print_exc()}", flush=True)
            raise
        except FileNotFoundError:
            print(f"Could not load json file {filename}: file does not seem to exist!\n{print_exc()}", flush=True)
            raise
        file.close()
    return output

def configGet(key: str, *args: str) -> Any:
    """Get value of the config key
    ### Args:
        * key (str): The last key of the keys path.
        * *args (str): Path to key like: dict[args][key].
    ### Returns:
        * any: Value of provided key
    """    
    this_dict = jsonLoad("config.json")
    this_key = this_dict
    for dict_key in args:
        this_key = this_key[dict_key] # type: ignore
    return this_key[key] # type: ignore

def locale(key: str, *args: str, locale=configGet("locale")) -> str:
    """Get value of locale string
    ### Args:
        * key (str): The last key of the locale's keys path.
        * *args (list): Path to key like: dict[args][key].
        * locale (str): Locale to looked up in. Defaults to config's locale value.
    ### Returns:
        * any: Value of provided locale key
    """ 
    if (locale == None):
        locale = configGet("locale")
    
    try:
        this_dict = jsonLoad(f'locale{sep}{locale}.json')
    except FileNotFoundError:
        return f'⚠️ Locale in config is invalid: could not get "{key}" in {str(args)} from locale "{locale}"'

    this_key = this_dict
    for dict_key in args:
        this_key = this_key[dict_key] # type: ignore
        
    try:
        return this_key[key] # type: ignore
    except KeyError:
        return f'⚠️ Locale in config is invalid: could not get "{key}" in {str(args)} from locale "{locale}"'