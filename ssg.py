import typer
from ssg.site import Site

def main(source, dest):
    source = "content"
    dest = "dist"
    config = {
        "source": source,
        "dest": dest
    }
    class Site(**config.build())
    