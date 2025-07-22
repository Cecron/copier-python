import logging

logger = logging.getLogger(__name__)

def main(args):
    logger.info(f"Invoked with {args}")

    if args.action is not None:
        args.action(args)
