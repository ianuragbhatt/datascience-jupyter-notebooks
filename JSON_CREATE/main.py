from flask import Flask
from google.cloud import storage
import json
import os

app = Flask(__name__)


@app.route('/create_json')
def create_json():
    # Automatically set credentials for your bucket storage
    storage_client = storage.Client()
    # json value
    json_file = {
        'Name': 'Anurag',
        'Age': '21'
    }
    # Get bucket name from environment variable in app.yaml file
    bucket_name = os.environ.get('BUCKET_NAME')
    bucket = storage_client.get_bucket(bucket_name)
    # declare your file name
    blob = bucket.blob('first_text.json')
    # upload json data were we will set content_type as json
    blob.upload_from_string(
        data=json.dumps(json_file),
        content_type='application/json'
        )
    return 'UPLOAD COMPLETE'


@app.route('/get_json')
def get_json():
    # Automatically set credentials for your bucket storage
    storage_client = storage.Client()
    # Get bucket name from environment variable in app.yaml file
    bucket_name = os.environ.get('BUCKET_NAME')
    bucket = storage_client.get_bucket(bucket_name)
    # Get the file we want
    blob = bucket.get_blob('first_text.json')
    fileData = json.loads(blob.download_as_string())
    return fileData


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
