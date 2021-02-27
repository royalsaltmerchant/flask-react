from flask import Flask
import time

app = Flask(__name__)
if __name__ == "__main__":
  app.run(debug=True)

@app.route('/api/time')
def get_current_time():
  return {'time': time.time()}