from flask import Flask

from .incremental_search import incremental_search
from .Bisection import bisection
from .fixed_point import fixed_point
from .false_rule import false_rule
from .Newton import newton
from .secant import secant
from .multi_root import multi_root
from .gaussian_elimination import gaussian_elimination
from .partial_pivot import partial_pivot
from .total_pivot import total_pivot
from .simple_lu import simple_lu
from .parcial_lu import parcial_lu
from .croult import croult
from .doolittle import doolittle
from .cholesky import cholesky


def create_app():
    app = Flask(__name__)

    app.register_blueprint(incremental_search)
    app.register_blueprint(bisection)
    app.register_blueprint(fixed_point)
    app.register_blueprint(false_rule)
    app.register_blueprint(newton)
    app.register_blueprint(secant)
    app.register_blueprint(multi_root)
    app.register_blueprint(gaussian_elimination)
    app.register_blueprint(partial_pivot)
    app.register_blueprint(total_pivot)
    app.register_blueprint(simple_lu)
    app.register_blueprint(parcial_lu)
    app.register_blueprint(croult)
    app.register_blueprint(doolittle)
    app.register_blueprint(cholesky)

    return app
