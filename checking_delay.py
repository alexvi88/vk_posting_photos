import argparse


def delay_of_first_post():

    delay = 0

    parser = argparse.ArgumentParser(description=
                                     'This script posts photos')

    parser.add_argument('--time',
                        help='delay of first post in hours',
                        type=int)

    args = parser.parse_args()

    need_first_post_delay = (args.time is not None)

    if need_first_post_delay:
        delay = int(args.time)

    return delay
