from Services import Services
import json
from distutils.log import debug
from flask import Flask
from jinja2 import Environment
app = Flask(__name__)


class Urls(Services):

    @app.route("/")
    def home():
        return '<h1>Welcome!</h1><h2>These are the Endpoints:</h2><div>http://localhost:8080/conf_env Displays all the Linux Env vars</div><div>&nbsp;</div><div>http://localhost:8080/env/<span style="color: #ff0000;">variable_name</span>/<span style="color: #ff0000;">variable_value</span> Enter a valid name and a valid value in those two to create a new Env Var</div><div>&nbsp;</div><div>http://localhost:8080/running_software Lists All Running Software</div>'

    @app.route("/conf_env")
    def printenv():
        env = Services.env()
        return "<h1>env_vars using env:</h1>" + json.dumps(env)
        
    @app.route("/env/<env_name>/<env_Var>")
    def create_var(env_name, env_Var):
            return Services.create_var(env_name, env_Var)

    @app.route('/running_software')
    def running_software():
        return Services.running_software()





if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8282, debug=True)
