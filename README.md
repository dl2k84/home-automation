# home-automation

IrDA home automation web code written in Python and with the Flask framework

Read this to understand the spec of IR byte codes that needs to be sent to control electrical appliances in your home:

https://gist.github.com/dl2k84/6081780

UI
Static HTML stored in /src/static
Flask expects static files to be here in order to be served.

## API

### Lighting

GET /lighting  
Returns the current lighting state id stored by the server

GET /lighting/{stateId}  
Toggles the lighting state to requested {stateId}

GET /lighting/sync/{stateId}  
Sets the current lighting state id stored by the server to the requested {stateId}  
This is useful to adjust the state when you've  
- Used a remote control to change lighting state, or  
- An IR signal failed to be sent or delivered, or  
- Power goes out and the real light state and server known state is out of sync.  
and other similar causes.

GET /lighting/reference  
Reference service that returns a JSONArray in the following format:  

    [  
        { "stateId": "stateName" },  
        { "stateId": "stateName" },  
        ...  
    ]

eg

    [ { "0": "off" } ]


### Airconditioner

GET /aircon  
Returns current aircon status in JSON format  
e.g.,

    {  
        "mode": string,  
        "temperature": int,  
        "turnOn": bool  
    }

POST /aircon  
Send request to aircon in JSON format as follows:

    {
        "mode": string,  
        "temperature": int,  
        "turnOn": bool  
    }

mode: aircon/dehumidifier/heater  
temperature requested temperature as int  
turnOn: true to turn on, false to turn off  

Response: same as GET /aircon above


###Human Presence Detector

GET /presenceCount  
Returns integer number of registered device(s) / human(s) detected, or 0 if no one detected.  

GET /presence  
Returns list of registered devices(s) / humans(s) detected.  
e.g.,

    [
        "bob",
        "jane"
    ]
