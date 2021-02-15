from typing import Optional, List
from aiohttp import web
from aiohttp.web_request import Request
import requests
from requests import HTTPError
import typer

PYPI_URL = "https://pypi.org/simple"

def get_package_url(package_name: str, indices: List[str]) -> Optional[str]:
    typer.echo(f"Looking for {package_name}")
    for index_url in indices:
        package_url = f"{index_url.rstrip('/')}/{package_name}/"
        try:
            with requests.get(package_url) as r:
                r.raise_for_status()
            typer.echo(f"    Found at {package_url}")
            return package_url
        except HTTPError:
            typer.echo(f"    Not found at {package_url}")
    return None

def make_package_handler(indices: List[str]):
    async def _package(request: Request):
        package_url = get_package_url(request.match_info['package_name'], indices=indices)
        if not package_url:
            raise web.HTTPNotFound()
        raise web.HTTPTemporaryRedirect(location=package_url)
    return _package

def main(private_index: List[str], host: str = "localhost", port: int = 8080):
    indices = [*private_index, PYPI_URL]
    typer.echo("Proxying with the following list:")
    typer.echo("\n".join("    " + index for index in indices))
    app = web.Application()
    app.add_routes([web.get('/{package_name}/', make_package_handler(indices))])
    web.run_app(app, host=host, port=port)

if __name__ == '__main__':
    typer.run(main)