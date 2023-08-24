"""Allows you to see the Python implementation of yt_dlp commands in CLI.

!!! I DO NOT OWN THIS !!!

The syntax goes like this:

    [PYTHON ENVIRONMENT LOCATION] [SCRIPT_PATH] [CLI COMMANDS TO BE CONVERTED]
    
The first two parts, the [PYTHON ENVIRONMENT LOCATION] and [SCRIPT_PATH], will be generated once you click "Run Python File" button. 
The script will execute without any parameters given, but you can then start to append CLI commands easily by using the upper arrow key to recall the input history.

Example:

    D:/Programs/miniconda3/python.exe d:/Cyber/Project/MacGyver/yt-dlp-related/cli_to_api.py --ignore-errors --format bestaudio --extract-audio --audio-format mp3 --audio-quality 160K --output "%(title)s.%(ext)s" --yes-playlist '<YouTube playlist URL>'

Notice that the script runs on direct execution. 
"""
# Allow direct execution
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import yt_dlp
import yt_dlp.options

create_parser = yt_dlp.options.create_parser


def parse_patched_options(opts):
    patched_parser = create_parser()
    patched_parser.defaults.update({
        'ignoreerrors': False,
        'retries': 0,
        'fragment_retries': 0,
        'extract_flat': False,
        'concat_playlist': 'never',
    })
    yt_dlp.options.create_parser = lambda: patched_parser
    try:
        return yt_dlp.parse_options(opts)
    finally:
        yt_dlp.options.create_parser = create_parser


default_opts = parse_patched_options([]).ydl_opts


def cli_to_api(opts, cli_defaults=False):
    opts = (yt_dlp.parse_options if cli_defaults else parse_patched_options)(opts).ydl_opts

    diff = {k: v for k, v in opts.items() if default_opts[k] != v}
    if 'postprocessors' in diff:
        diff['postprocessors'] = [pp for pp in diff['postprocessors']
                                  if pp not in default_opts['postprocessors']]
    return diff


if __name__ == '__main__':
    from pprint import pprint

    print('\nThe arguments passed translate to:\n')
    pprint(cli_to_api(sys.argv[1:]))
    print('\nCombining these with the CLI defaults gives:\n')
    pprint(cli_to_api(sys.argv[1:], True))