import sys

from sh import mkdocs


def serve():
    """Serve documentation site."""
    mkdocs(
        'serve', '-a', 'localhost:8211',
        stderr=sys.stderr, stdout=sys.stdout,
    )
