import argparse
import datetime
import settings
from last_post_time import last_postponed_post_time

def delay_of_first_post():

    delay = 0

    parser = argparse.ArgumentParser(description=
                                     'This script posts photos')

    parser.add_argument('--time',
                        help='delay of first post in hours',
                        type=int)

    parser.add_argument('--afterall',
                        help='first one will be posted after all',
                        action='store_true')

    args = parser.parse_args()

    need_first_post_delay = (args.time is not None)
    need_posting_after_all = args.afterall

    if need_posting_after_all:
        last_postponed_time = int(last_postponed_post_time())

        if last_postponed_time != 0:
            now_temp_d = datetime.datetime.now()
            now_date = now_temp_d.timestamp()
            delay += int(last_postponed_time - now_date) + settings.posts_interval

    if need_first_post_delay:
        delay += int(args.time)*3600

    return delay
