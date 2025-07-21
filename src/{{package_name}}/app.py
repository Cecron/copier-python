

def main(args):
    print(f"Invoked with {args}")

    if args.action is not None:
        args.action(args)

