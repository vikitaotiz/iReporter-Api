from app import app
from instance.config import DevelopmentConfig
app.config['DEBUG'] = DevelopmentConfig
# app.config['PROPAGATE_EXCEPTIONS'] = True

if __name__ == "__main__":
    app.run()
