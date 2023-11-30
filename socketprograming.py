import socket

def send_msg(sock, msg):
    """d"""
    #これまでに送信できたバイト数
    total_sent_len = 0
    #送信したいバイト数
    total_msg_len = len(msg)
    #まだ送信したいデータが残っているか確認する
    while total_sent_len < total_msg_len:
        #ソケットにバイト列を書き込み書き込めたバイト数を得る
        sent_len = sock.send(msg[total_sent_len:])
        #全く書き込めなければ接続完了
        if sent_len == 0:
            raise RuntimeError('socket connection broken')
        #書き込めた文を加算する
        total_sent_len += sent_len
def recv_msg(sock, chunk_len=1024):
    """j"""
    while True:
        #ソケットから指定したバイト数を読み込む
        received_chunk = sock.recv(chunk_len)
    #まっタック読めなかったときは接続できてる
        if len(received_chunk) == 0:
            break
        yield received_chunk

def main():
    """スクリプトとして実行されたときに呼び出されるメイン関数"""
    #IPv4/TCPで通神するソケットを用意する
    client_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    client_socket.connect(('127.0.0.1',80)
            request_text = 'GET/HTTP/1.0\r\n\r\n'
            request_bytes = request_text.encode('ASCII')
            send_msg(client_socket,request_bytes)
            received_bytes = b''.join(recv_msg(client_socket))
            received_text = received_bytes.decode('ASCII')
            print(received_text)
            client_socket.close()

if __name__ == '_main_':
    """d"""
    main()


