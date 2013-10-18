import db
import reference

from flask import Flask, redirect, url_for, request, json, jsonify
from optparse import OptionParser

# Parse command line arguments
parser = OptionParser()
parser.add_option("-l", "--logfile")

(options, args) = parser.parse_args()

app = Flask(__name__, static_url_path='')

#if not app.debug:
if options.logfile:
    import logging
    from logging import FileHandler
    file_handler = FileHandler(options.logfile)
    file_handler.setLevel(logging.WARNING)
    app.logger.addHandler(file_handler)

@app.route('/')
def hello_world():
  #return 'Hello World!'
  return redirect(url_for('static', filename='index.html'))

# Get the current light state
@app.route('/lighting')
def getLightingStatus():
  return str(db.getLightingStatus())

# Sync light state. This can be used when system stored light state
# differs from actual state. Because there is only 1 code to toggle
# light state, this'll have to be done anytime an IR signal doesn't
# reach its mark
@app.route('/lighting/sync/<mode>')
def syncLightingStatus(mode):
  db.updateLightingStatus(int(mode))
  return "Lighting status synced to Mode=" + mode

# Switch light state to requested state
@app.route('/lighting/<mode>')
def lighting(mode):
  print "Mode=", mode
  db.setLighting(int(mode))
  return "Lighting control! Mode=" + mode

# Lighting reference service
@app.route('/lighting/reference')
def getLightingReference():
  return str(reference.getReference("REFERENCE_LIGHTING"))

# Aircon
# GET: Return current status
# POST: Validate the request to be processed and issued to the aircon unit
# All request and responses uses JSON as the serialization format
@app.route('/aircon', methods=['POST', 'GET'])
def aircon():
  if request.method == 'POST':
    return jsonify(db.setAircon(request.json))
  else:
    return jsonify(db.getAirconStatus())

# Human Presence Detector
@app.route('/presenceCount')
def getPresenceCount():
  return str(db.getPresenceCount())

@app.route('/presence')
def getPresence():
  return json.dumps(db.getPresence())

# Disable cache for site
@app.after_request
def add_no_cache(response):
  if request.method == 'POST':
    response.cache_control.no_cache = True
  return response


if __name__ == '__main__':
    app.run(host='0.0.0.0')

