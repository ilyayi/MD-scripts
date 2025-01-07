from flask import Flask, request, jsonify
from scraper import scrape_data

app = Flask(__name__)

@app.route('/scrape', methods=['GET'])
def scrape():
    url = request.args.get('url')
    if not url:
        return jsonify({"error": "No URL provided"}), 400
    data = scrape_data(url)
    if data:
        # Save data to the database here (to be implemented in the next step)
        return jsonify({"data": data})
    else:
        return jsonify({"error": "Failed to scrape data"}), 500

if __name__ == '__main__':
    app.run(debug=True)
