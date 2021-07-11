from flask import Flask
from google.cloud import storage
import json
import os

app = Flask(__name__)

# credentails for accessing cloud storage 
storage_client = storage.Client.from_service_account_json('gcloud_private_key.json')
# storage_client = storage.Client()
# bucket_name = os.environ.get('BUCKET_NAME')
bucket_name = 'bucket1go'
BUCKET = storage_client.get_bucket(bucket_name)

@app.route('/create_json')
def create_json():
    json_file = {
        'Name': 'Anurag',
        'Age': '21'
    }
    filename = 'test.json'
    blob = BUCKET.blob(filename)
    blob.upload_from_string(
        data=json.dumps(json_file),
        content_type='application/json'
        )
    return 'UPLOAD COMPLETE'


@app.route('/get_json')
def get_json():
    filename = 'test.json'
    blob = BUCKET.get_blob(filename)
    file_data = json.loads(blob.download_as_string())
    return file_data


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
