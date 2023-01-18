import os
from pathlib import Path
from requests_oauthlib import OAuth2Session
import typer
from rich import print
from dotenv import find_dotenv, load_dotenv, set_key
load_dotenv()

import logging
log = logging.getLogger(__name__)

app = typer.Typer()


client_id = os.getenv("APP_CLIENTID")
client_secret = os.getenv("APP_SECRETID")
redirect_uri = "https://localhost:8080/webex-teams-auth.html"

authorization_base_url = 'https://webexapis.com/v1/authorize'
token_url = 'https://webexapis.com/v1/access_token/'

scope = [
    "spark-admin:calling_cdr_read",
    "spark-admin:locations_read",
    ]

@app.command()
def main():
    webex_auth = OAuth2Session(client_id, scope=scope, redirect_uri=redirect_uri)

    authorization_url, state = webex_auth.authorization_url(authorization_base_url)
    print('[bold yellow]Opening default browser for authentication...[/bold yellow]')
    print(f'{authorization_url}')
    typer.launch(f'{authorization_url}')
    

    redirect_response = typer.prompt('Paste the full redirect URL here')

    response = webex_auth.fetch_token(
        token_url,
        client_secret=client_secret,
        include_client_id=True,
        authorization_response=redirect_response
        )

    log.info(f'Access and Refresh tokens obtained.')
    log.debug(f"Access Token: {response['access_token']}")
    log.debug(f"Refresh Token: {response['refresh_token']}")

    dotenv_file = find_dotenv()
    set_key(dotenv_file, "APP_ACCESS", response['access_token'])
    set_key(dotenv_file, "APP_REFRESH", response['refresh_token'])

    print("[bold red]Alert![/bold red] [green]You have successfully passed OAuth2.0 Authentication![/green] :boom:")
    print("[bold green]Please proceed to other commands in this CLI application. :wave:")

if __name__ == "__main__":
    app()