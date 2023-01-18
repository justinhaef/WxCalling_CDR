import os
import typer
import requests
import json
from rich import print, print_json
from rich.progress import Progress, SpinnerColumn, TextColumn
from dotenv import load_dotenv
load_dotenv()
import logging
log = logging.getLogger(__name__)

app = typer.Typer()

class Analytics():
    def __init__(self, access_token: str):
        self.access_token = access_token
        self.base_url = "https://analytics.webexapis.com/v1/cdr_feed"
        self.session = requests.Session()
        self.session.headers.update({'Authorization': f'Bearer {self.access_token}'})

    def create_report(self, start: str, end: str, site: str):
        payload = {
            'startTime': start, 
            'endTime': end, 
            'locations': site,
            # 'max': 
        }
        response = self.session.get(url=self.base_url, params=payload)
        return response.text

@app.command()
def generate(
    site: str = typer.Argument(..., help="Name of the site to create report (only 1 site at a time)"),
    start_date: str = typer.Option(..., prompt="What is the start date (YYYY-MM-DD)"),
    start_time: str = typer.Option(..., prompt="What is the start time (HH:MM:SS"),
    end_date: str = typer.Option(..., prompt="What is the end date (YYYY-MM-DD)"),
    end_time: str = typer.Option(..., prompt="What is the end time (HH:MM:SS)"),
):
    """ Create the Detailed Call History report. 
        Site name required, only 1 site name accepted at this time.  You will be prompted for the start/end times.

        Timezone values will be to the Control Hub timezone
    """

    print(" :watch: [bold red]Timezone values will be in UTC[/bold red]")
    
    #for now we'll trust the user input valid data
    start = start_date + 'T' + start_time + ".000Z"
    end = end_date + 'T' + end_time + ".000Z"
    log.info(f'StartTime: {start} EndTime: {end}')

    with Progress(
        SpinnerColumn(), TextColumn("[progress.description]{task.description}"),
        transient=True,
    ) as progress:
        progress.add_task(description="Generating Detail Call Report...", total=None)

        analytics = Analytics(access_token=os.getenv("APP_ACCESS"))
        result = analytics.create_report(start, end, site)
    print(":rocket: [bold green]Congratulations, your report is done![/bold green]")
    print_json(result)


if __name__ == "__main__":
    app()