# waveshell, main entry

import os
import sys
import logging
import wsgiref.handlers 

def get_wavecode(wid):
    """return the code from parameter wave's id"""
    from wirewave import WaveReader
    w = WaveReader()
    w.read(wid)
    code = w.get_root_text()
    logging.info(code)
    return code

def main():
    """read, and execute the main file"""
    codewave = "googlewave.com!w+L7QfCXQuE"
    wavecode = get_wavecode(codewave)
    exec wavecode
    wsgiref.handlers.CGIHandler().run(app)
    return

    

if __name__ == '__main__':
    main()
