#!/usr/bin/python3
"""
1-main
"""
import sys

if _name_ == '_main_':
    top_ten = _import_('1-top_ten').top_ten
    if len(sys.argv) < 2:
        print("Please pass an argument for the subreddit to search.")
    else:
        top_ten(sys.argv[1])
