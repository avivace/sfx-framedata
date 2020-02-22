import connexion
import logging
import app
from flask_cors import CORS

logging.basicConfig(level=logging.INFO)
app = connexion.App(__name__, specification_dir='openapi/')
CORS(app.app)
app.add_api('sfx.yaml', base_path="/api/v1")
app.run(port=8081,server='tornado')
