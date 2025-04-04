from .server import main
import asyncio
import logging

if __name__ == "__main__":
    logging.basicConfig(
        level=logging.DEBUG,
        format="%(asctime)s [%(levelname)s] %(message)s",
        datefmt="%Y-%m-%dT%H:%M:%S",
    )
    logging.info("Starting Illustrator MCP server")
    asyncio.run(main())