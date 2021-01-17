from app import server

if __name__ == '__main__':
    wsgi_app_port = config.WSGI_APP_PORT
    server.run(host="0.0.0.0", port=wsgi_app_port)