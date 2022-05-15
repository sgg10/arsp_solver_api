from flask import request


def method_response(method, get_res, error_res):
    try:
        return method(**request.get_json()).run() if request.method == "POST" else get_res
    except TypeError:
        return error_res
