import grpc 
from concurrent import futures 
import time 
import chat_pb2
import chat_pb2_grpc


class ChatServices(chat_pb2_grpc.ChatServiceServicer):
    def Chat(self,request_iterator , context):
        response_list=[]
        for chat_message in request_iterator:
            for chat_message in request_iterator:
                print(f"Recived message from {chat_message.User}:{chat_message}")

                response_list.append(
                    chat_pb2.ChatMessage(
                        User=chat_message.User,
                        message=f"{chat_message.message}",
                        reciptent=chat_message.reciptent,
                        is_private=chat_message.is_private
                    )
                )
        return response_list
    
    def SendPrivateMessage(self, request, context):
        print(f"Recived message from {request.User}:{request.reciptent}:{request.message}")
        return chat_pb2.ChatMessage(
            User=request.User,
            message="Message sent succesfully",
            reciptent=request.reciptent,
            is_private=request.is_private
        )
        

def serve():
    server=grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    chat_pb2_grpc.add_ChatServiceServicer_to_server(ChatServices(),server)

    server.add_insecure_port('[::]:50051')
    print("Server on 50051")

    server.start()
    server.wait_for_termination()

if __name__ =='__main__':
    serve()