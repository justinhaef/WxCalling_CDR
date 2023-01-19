# Webex Detailed Call History CLI Application

This CLI application has been created for demonstration purposes have how someone can use the [Detailed Call History API.](https://developer.webex.com/docs/api/v1/webex-calling-detailed-call-history/get-detailed-call-history)

## How to setup to use this CLI application

1. Please use a python virutal enviornment
1. `git clone https://github.com/justinhaef/WxCalling_CDR.git`
1. Rename `.env-template` to `.env`
1. Populate `.env` file with your [Integrations](https://developer.webex.com/docs/integrations) `clientID` and `secretID`
1. This CLI will populate that `.env` file with your `Access Token` and your `Refresh Token`.  As with all tokens, keep these safe.  Delete if you want when you're done running this application.  
1. run `pip install -r requirements.txt`

## How to use this CLI application
1. `python webex auth main`
1. You will be prompted to authenticate to Webex using your browser.  You will also be prompted to agree to the scopes being requested by your integration.  
1. You then need to copy the `localhost:8080` URL that is provided back in your browser.  Paste that into your command line.
1. `python webex locations list`
1. `python webex analytics generate {site name}`

Each of those commands has a `--help` option. 