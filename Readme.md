# Flask app using Alpine

## Instructions
1. Make sure you have Docker intalled on your machine
2. Go to scripts folder
3. make sure you have the right permissions to run the scripts ´chmod 700 bake.sh launch.sh´ 
4. Run bake.sh
5. Run launch.sh
6. Your Flask app is ready to use. simply type localhost:8282.

# Endpoints
You can also find the endpoints described at the homepage (http://127.0.0.1:8080/)

http://127.0.0.1:8080/ Homepage, returns a warm Welcome and the endpoints for this project.
http://127.0.0.1:8080/conf_env Returns a list of all Linux env_vars
http://127.0.0.1:8080/env/{env_name}/{env_Var} Creates a new env var with the env_name and the env_var that you provide. You can check if it was created in the /conf_env endpoint.
http://127.0.0.1:8080/running_software Returns a list of all running softwares in the virtual enviroment.
