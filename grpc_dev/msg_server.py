#=============================================================
# -*- coding:UTF-8 -*-
# File Name: msg_server.py
# Author: baojiang
# mail: baojiang@oppo.com
# Created Time: 六 11/13 03:36:52 2021
#=============================================================
#!/usr/bin/python
import grpc
import msg_pb2
import msg_pb2_grpc
from concurrent import futures #并发库
import time
 
_ONE_DAY_IN_SECONDS = 60 * 60 * 24
 
class MsgServicer(msg_pb2_grpc.MsgServiceServicer):

    def GetMsg(self, request, context):
        print("Received name: %s" % request.name)
        return msg_pb2.MsgResponse(msg='Hello, %s!' % request.name)
  
def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    msg_pb2_grpc.add_MsgServiceServicer_to_server(MsgServicer(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    try:
        while True:
            time.sleep(_ONE_DAY_IN_SECONDS)
    except KeyboardInterrupt:
        server.stop(0)
 
if __name__ == '__main__':
  serve()
