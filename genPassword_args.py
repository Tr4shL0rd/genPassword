#!/usr/bin/env python3
import argparse


class Args:
    def __init__(self) -> None:
        pass

    def pwrd_args(self):
        parser = argparse.ArgumentParser(description="Generates a Password")
        parser.add_argument(
            "-l",
            dest="pass_length",
            action="store",
            type=int,
            default=12,
            help="Length of password",
        )

        parser.add_argument(
            "-c","--case",
            dest="case",
            action="store",
            default="all",
            help="the case to use for the password (all[default],full, lower, upper, digits,symbols)"
        )
        parser.add_argument(
            "--version",
            dest="version",
            action="store_true",
            help="displays program version"
        )
        parser.add_argument(
            "--clip",
            dest="clip",
            action="store_true",
            help="Copy to clipboard"
        )
        # parser.add_argument(
        #     "--fullcase",
        #     action="store_true",
        #     default=False,
        #     dest="use both upper and lower case"
        # )
        # parser.add_argument(
        #     "--lowercase",
        #     action="store_false",
        #     default=False,
        #     dest="use lowercase"
        # )
        # parser.add_argument(
        #     "--uppercase",
        #     action="store_false",
        #     default=False,
        #     dest="use uppercase"
        # )
        # parser.add_argument(
        #     "--digits",
        #     action="store_false",
        #     default=False,
        #     dest="use digits"
        # )
        # parser.add_argument(
        #     "--symbols",
        #     action="store_false",
        #     default=False,
        #     dest="use symbols"
        # )
        
        args = parser.parse_args()
        return args
