import os

class Services:
    def env():
        env = dict(os.environ)
        return env
    def printenv():
        f = os.popen('printenv')
        r = f.read()
        return r
    
    def create_var(env_name, env_Var):
        env_name = str(env_name).upper()
        var = os.environ[str(env_name)] = str(env_Var)
        
        f = os.popen('export'+ var)
        r = f.read()
        return "new env_var {}" .format(env_name) + r 

    def running_software():
        return os.popen('ps aux').read()