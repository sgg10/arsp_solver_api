class BaseMethod:

    def run(self):
        pass

    def success_response(self, result, **kwargs):
        return {
            "method_status": "success",
            "result": result,
            **kwargs
        }

    def failed_response(self, result, **kwargs):
        return {
            "method_status": "failed",
            "result": result,
            **kwargs
        }
