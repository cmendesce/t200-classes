#!/usr/bin/env python3

from web import create_app

if __name__ == '__main__':
    web_app = create_app()
    web_app.run(host='0.0.0.0', debug=True)
    