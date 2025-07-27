import asyncio
import logging

# Try relative import first, fallback to absolute import
try:
    from .server import main
except ImportError:
    from server import main

def run_server():
    logging.basicConfig(
        level=logging.DEBUG,
        format="%(asctime)s [%(levelname)s] %(message)s",
        datefmt="%Y-%m-%dT%H:%M:%S",
    )
    logging.info("Starting Illustrator MCP server from CLI")
    asyncio.run(main())

if __name__ == "__main__":
    run_server()
                