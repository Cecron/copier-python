class Hello:
    def __init__(self):
        self.parser = None

    def add_subparser(self, subparsers):
        self.parser = subparsers.add_parser("hello", help="Great someone by name.")
        self.parser.add_argument(
            "-n",
            "--name",
            metavar="NAME",
            required=False,
            type=str,
            dest="name",
            default="World",
            help="Name to greet. (default: %(default)s)",
        )
        self.parser.set_defaults(action=self)

    def __call__(self, args):
        print(f"Hello {args.name}!")
