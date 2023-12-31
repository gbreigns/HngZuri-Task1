from flask import Flask, request, jsonify
from datetime import datetime, timezone, timedelta
import pytz

app = Flask(__name__)

@app.route("/api", methods=["GET"])
def api():
    # Get query parameters
    slack_name = request.args.get('slack_name')
    track = request.args.get('track')

    # Validate required parameters
    if not slack_name or not track:
        return jsonify({'error': 'All required parameters are not provided'}), 400

    # Get the current day of the week
    current_day = datetime.now(timezone.utc).strftime('%A')

    # Get the current UTC time with validation of +/-2 hours
    utc_time = datetime.now(pytz.utc)
    utc_offset = utc_time.utcoffset().total_seconds() / 3600
    if abs(utc_offset) > 2:
        return jsonify({'error': 'Invalid UTC offset'}), 400

    # Construct GitHub URLs
    github_repo_url = 'https://github.com/gbreigns/HngZuri-Task1'
    github_file_url = f'{github_repo_url}/blob/main/main.py'
   

    # Prepare the response JSON
    response = {
        'slack_name': slack_name,
        'current_day': current_day,
        'utc_time': utc_time.strftime('%Y-%m-%dT%H:%M:%SZ'),
        'track': track,
        'github_file_url': github_file_url,
        'github_repo_url': github_repo_url,
        'status_code': 'Success'
    }

    return jsonify(response)

if __name__ == '__main__':
    app.run(debug=True)
