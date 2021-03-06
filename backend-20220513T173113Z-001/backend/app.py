# %%
import os
from flask import send_from_directory, Flask
from flask_cors import CORS
from config.config import DevelopmentConfig

from api.twitter_route import twitter_route

app = Flask(__name__)
app.config.from_object(DevelopmentConfig)
# %%

# %%
app.register_blueprint(twitter_route)

CORS(app)

if __name__ == "__main__":
    app.run(host=app.config["HOST_ADDRESS"], port=app.config["PORT"])
