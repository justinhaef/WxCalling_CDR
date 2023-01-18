import os
import typer
import requests
import json
from rich import print, print_json
from dotenv import load_dotenv
load_dotenv()

app = typer.Typer()

class Locations():
    def __init__(self, access_token: str):
        self.access_token = access_token
        self.base_url = "https://webexapis.com/v1/locations"
        self.session = requests.Session()
        self.session.headers.update({'Authorization': f'Bearer {self.access_token}'})

    def get_locations(self):
        location_names = []
        response = self.session.get(url=self.base_url)
        locations_json = json.loads(response.text)
        for names in locations_json["items"]:
            # print(names)
            location_names.append(names['name'])
        return location_names

@app.command()
def list():
    """ List out all Webex Calling Locations
    """
    locations = Locations(access_token=os.getenv("APP_ACCESS"))
    names = locations.get_locations()
    for name in names:
        print(f":office: [bold green]{name}[/bold green]")

    print("[bold red]Alert![/bold red] [green]Congratulations, you have listed your locations![/green]")
    print("[bold green]Use these names to generate your call detail records in Analytics[/bold green] :wave:")

if __name__ == "__main__":
    app()