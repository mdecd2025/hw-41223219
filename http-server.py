import os
import threading
import http.server
import ssl

def domake():
    # 設定伺服器地址 (改為 8000)
    server_address = ('localhost', 8000)
    httpd = http.server.HTTPServer(server_address, http.server.SimpleHTTPRequestHandler)

    # 創建 SSL 上下文
    context = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)
    context.load_cert_chain(certfile='./localhost.crt', keyfile='./localhost.key')

    # 使用 context 來包裝 socket
    httpd.socket = context.wrap_socket(httpd.socket, server_side=True)

    print(os.getcwd())
    print("8000 https server started")
    httpd.serve_forever()

# 利用執行緒啟動 HTTPS 伺服器
make = threading.Thread(target=domake)
make.start()
