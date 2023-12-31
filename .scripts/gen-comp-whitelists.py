#! /usr/bin/env python3

# Adapted from https://github.com/DNSCrypt/dnscrypt-proxy/blob/master/utils/generate-domains-blocklist/generate-domains-blocklist.py
# Re-purposed to generate whitelists, with a few changes and tweaks

from __future__ import print_function

import argparse
import re
import sys
import fnmatch

try:
    import urllib2 as urllib

    URLLIB_NEW = False
except (ImportError, ModuleNotFoundError):
    import urllib.request as urllib
    from urllib.request import Request

    URLLIB_NEW = True


log_info = sys.stderr
log_err = sys.stderr


def parse_trusted_list(content):
    rx_comment = re.compile(r"^(#|$)")
    rx_inline_comment = re.compile(r"\s*#\s*[a-z0-9-].*$")
    rx_trusted = re.compile(r"^([*a-z0-9.-]+)\s*(@\S+)?$")
    rx_timed = re.compile(r".+\s*@\S+$")

    names = set()
    globs = set()
    rx_set = [rx_trusted]
    for line in content.splitlines():
        line = str.lower(str.strip(line))
        if rx_comment.match(line):
            continue
        line = str.strip(rx_inline_comment.sub("", line))
        if is_glob(line) and not rx_timed.match(line):
            globs.add(line)
            names.add(line)
            continue
        for rx in rx_set:
            matches = rx.match(line)
            if not matches:
                continue
            name = matches.group(1)
            names.add(name)
    return names, globs


def parse_list(content, trusted=False):
    if trusted:
        return parse_trusted_list(content)

    rx_comment = re.compile(r"^(#|$)")
    rx_inline_comment = re.compile(r"\s*#\s*[a-z0-9-].*$")
    rx_u = re.compile(
        r"^@*\|\|([a-z0-9][a-z0-9.-]*[.][a-z]{2,})\^?(\$(popup|third-party))?$"
    )
    rx_l = re.compile(r"^([a-z0-9][a-z0-9.-]*[.][a-z]{2,})$")
    rx_lw = re.compile(r"^[*][.]([a-z0-9][a-z0-9.-]*[.][a-z]{2,})$")
    rx_h = re.compile(
        r"^[0-9]{1,3}[.][0-9]{1,3}[.][0-9]{1,3}[.][0-9]{1,3}\s+([a-z0-9][a-z0-9.-]*[.][a-z]{2,})$"
    )
    rx_mdl = re.compile(r'^"[^"]+","([a-z0-9][a-z0-9.-]*[.][a-z]{2,})",')
    rx_b = re.compile(r"^([a-z0-9][a-z0-9.-]*[.][a-z]{2,}),.+,[0-9: /-]+,")
    rx_dq = re.compile(r"^address=/([a-z0-9][a-z0-9.-]*[.][a-z]{2,})/.")

    names = set()
    globs = set()
    rx_set = [rx_u, rx_l, rx_lw, rx_h, rx_mdl, rx_b, rx_dq]
    for line in content.splitlines():
        line = str.lower(str.strip(line))
        if rx_comment.match(line):
            continue
        line = str.strip(rx_inline_comment.sub("", line))
        for rx in rx_set:
            matches = rx.match(line)
            if not matches:
                continue
            name = matches.group(1)
            names.add(name)
    return names, globs


def load_from_url(url):
    log_info.write("Loading data from [{}]\n".format(url))
    req = urllib.Request(url=url, headers={"User-Agent": "dnscrypt-proxy"})
    trusted = False

    if URLLIB_NEW:
        req_type = req.type
    else:
        req_type = req.get_type()
    if req_type == "file":
        trusted = True

    response = None
    try:
        response = urllib.urlopen(req, timeout=int(args.timeout))
    except urllib.URLError as err:
        raise Exception("[{}] could not be loaded: {}\n".format(url, err))
    if trusted is False and response.getcode() != 200:
        raise Exception("[{}] returned HTTP code {}\n".format(
            url, response.getcode()))
    content = response.read()
    if URLLIB_NEW:
        content = content.decode("utf-8", errors="replace")

    return content, trusted


def name_cmp(name):
    parts = name.split(".")
    parts.reverse()
    return str.join(".", parts)


def is_glob(pattern):
    maybe_glob = False
    for i in range(len(pattern)):
        c = pattern[i]
        if c == "?" or c == "[":
            maybe_glob = True
        elif c == "*" and i != 0:
            if i < len(pattern) - 1 or pattern[i - 1] == ".":
                maybe_glob = True
    if maybe_glob:
        try:
            fnmatch.fnmatch("example", pattern)
            return True
        except:
            pass
    return False


def covered_by_glob(globs, name):
    if name in globs:
        return False
    for glob in globs:
        try:
            if fnmatch.fnmatch(name, glob):
                return True
        except:
            pass
    return False


def has_suffix(names, name):
    parts = str.split(name, ".")
    while parts:
        parts = parts[1:]
        if str.join(".", parts) in names:
            return True

    return False


def whitelists_from_config_file(
    file, ignore_retrieval_failure, output_file
):
    whitelists = {}
    all_names = set()
    unique_names = set()
    all_globs = set()

    # Load conf & whitelists
    with open(file) as fd:
        for line in fd:
            line = str.strip(line)
            if str.startswith(line, "#") or line == "":
                continue
            url = line
            try:
                content, trusted = load_from_url(url)
                names, globs = parse_list(content, trusted)
                whitelists[url] = names
                all_names |= names
                all_globs |= globs
            except Exception as e:
                log_err.write(str(e))
                if not ignore_retrieval_failure:
                    exit(1)

    output_fd = sys.stdout
    if output_file:
        output_fd = open(output_file, "w")

    # Process whitelists
    for url, names in whitelists.items():
        print(
            "\n\n########## Whitelist from {} ##########\n".format(url),
            file=output_fd,
            end="\n",
        )
        ignored, glob_ignored = 0, 0
        list_names = list()
        for name in names:
            if covered_by_glob(all_globs, name):
                glob_ignored = glob_ignored + 1
            elif has_suffix(all_names, name) or name in unique_names:
                ignored = ignored + 1
            else:
                list_names.append(name)
                unique_names.add(name)

        list_names.sort(key=name_cmp)
        if ignored:
            print("# Ignored duplicates: {}".format(
                ignored), file=output_fd, end="\n")
        if glob_ignored:
            print(
                "# Ignored due to overlapping local patterns: {}".format(
                    glob_ignored),
                file=output_fd,
                end="\n",
            )
        if ignored or glob_ignored:
            print(file=output_fd, end="\n")
        for name in list_names:
            print(name, file=output_fd, end="\n")
 
    output_fd.close()


argp = argparse.ArgumentParser(
    description="Create a unified whitelist from a set of local and remote files"
)
argp.add_argument(
    "-c",
    "--config",
    default="gen-comp-whitelists.conf",
    help="file containing whitelist sources",
)
argp.add_argument(
    "-w",
    "--whitelist",
    help=argparse.SUPPRESS,
)
argp.add_argument(
    "-i",
    "--ignore-retrieval-failure",
    action="store_true",
    help="generate list even if some urls couldn't be retrieved",
)
argp.add_argument(
    "-o",
    "--output-file",
    default=None,
    help="save generated whitelist to a text file with the provided file name",
)
argp.add_argument("-t", "--timeout", default=30, help="URL open timeout")

args = argp.parse_args()

whitelist = args.whitelist
if whitelist:
    print(
        "The option to provide a set of names to exclude from the whitelist has been changed from -w to -a\n"
    )
    argp.print_help()
    exit(1)

conf = args.config
ignore_retrieval_failure = args.ignore_retrieval_failure
output_file = args.output_file
if output_file:
    log_info = sys.stdout

whitelists_from_config_file(
    conf, ignore_retrieval_failure, output_file
)
