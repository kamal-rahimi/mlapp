from app import server


WSGI_APP_PORT = 8000

if __name__ == '__main__':
    server.run(host="0.0.0.0", port=WSGI_APP_PORT)