import db

from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
  return 'Hello World!'

# Get the current light state
@app.route('/lighting')
def getLightingStatus():
  return "Mode=" + str(db.getLightingStatus())

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


if __name__ == '__main__':
    app.run(host='0.0.0.0')

