from app import create_app

app = create_app()


@app.route("/")
def index():
    return {
        "message": "Welcome to ARSP Solver API"
    }

# Error Handlers


@app.errorhandler(500)
def internal_server_error(error):
    return {
        "name": "Error 500 - Internal Server Error",
        "message": error.description
    }


@app.errorhandler(404)
def not_found(error):
    return {
        "name": "Error 404 - Not Found",
        "message": error.description
    }


if __name__ == "__main__":
    app.run(port=3000, debug=True, host="0.0.0.0")
