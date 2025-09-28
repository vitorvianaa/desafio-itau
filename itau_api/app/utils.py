from flask import jsonify

class Utils:

    @staticmethod
    def send_response(status, response, message = None, error = None):

        if message:
            response = {"data": response, "message": message}

        elif error:
            response = {"data": response, "error": error}

        elif message and error:
            response = {"data": response, "message": message, "error": error}
        else:
            response = {"data": response}
        
        return jsonify(response), status