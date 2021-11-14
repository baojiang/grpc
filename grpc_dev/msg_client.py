#=============================================================
# -*- coding:UTF-8 -*-
# File Name: msg_client.py
# Author: baojiang
# mail: baojiang@oppo.com
# Created Time: 六 11/13 03:27:04 2021
#=============================================================
#!/usr/bin/python
import grpc
import msg_pb2
import msg_pb2_grpc
 
def run():
    # NOTE(gRPC Python Team): .close() is possible on a channel and should be
    # used in circumstances in which the with statement does not fit the needs
    # of the code.
    with grpc.insecure_channel('localhost:50051') as channel:
        stub = msg_pb2_grpc.MsgServiceStub(channel)
        response = stub.GetMsg(msg_pb2.MsgRequest(name='world'))
    print("Client received: " + response.msg)
 
 
if __name__ == '__main__':
    run()
