# -------------------------------------------------------------------------------
# Name:        CustomBase64.py
# Purpose:     Custom base64 with option to pass specific key
#
# Author:      Charles Lomboni
#
# Created:     18/05/2018
# Copyright:   (c) Charles Lomboni 2018
# Licence:     <MIT License>
# -------------------------------------------------------------------------------

import argparse
import base64
import string


def getargs():
    parser = argparse.ArgumentParser("key")
    parser.add_argument("strToDecode", help="String to decode from base64")

    # Optional argument
    parser.add_argument("-k", "--key", help="Custom base64 key")

    return parser.parse_args()


def custombase64(strToTranslate, customKey):
    standardBase64 = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/"
    fixedString = strToTranslate.translate(string.maketrans(customKey, standardBase64))
    return base64.decodestring(fixedString)


def main():

    args = getargs()

    if args.key is not None:
        print custombase64(args.strToDecode, args.key)
    else:
        print base64.decodestring(args.strToDecode)



if __name__ == '__main__':
    main()