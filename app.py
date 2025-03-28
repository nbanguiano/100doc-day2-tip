from flask import Flask, request, render_template, jsonify, send_from_directory, url_for
import os
import mimetypes
from config import BASE_PATH, STATIC_PATH, is_production

# Ensure proper MIME types
mimetypes.add_type('text/css', '.css')
mimetypes.add_type('application/javascript', '.js')

app = Flask(__name__, 
            static_url_path=STATIC_PATH,
            static_folder='static')

@app.route(f'{BASE_PATH}/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        total = request.form.get('total')
        tip = request.form.get('tip')
        pax = request.form.get('pax')

        total_tip = (float(tip) * float(total)) / 100
        total_bill = float(total) + total_tip
        
        def split_bill(total, tip, pax):
            return f"Each person should pay: ${round(total_bill / float(pax), 2)}"
        
        result = split_bill(total, tip, pax)
        
        if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
            return jsonify({'result': result})
        return render_template('index.html', result=result, base_path=BASE_PATH)
    
    return render_template('index.html', base_path=BASE_PATH)

# Explicit route for serving static files with proper MIME types
@app.route('/static/<path:filename>')
def serve_static(filename):
    mimetype = mimetypes.guess_type(filename)[0] or 'application/octet-stream'
    response = send_from_directory(app.static_folder, filename)
    response.headers['Content-Type'] = mimetype
    return response

if __name__ == '__main__':
    env = 'production' if is_production() else 'development'
    print(f"Running in {env} mode")
    print(f"Base path: {BASE_PATH}")
    print(f"Static folder is at: {app.static_folder}")
    print(f"Static URL path is: {app.static_url_path}")
    app.run(debug=True, host='127.0.0.1', port=8085)
    # app.run(debug=not is_production())