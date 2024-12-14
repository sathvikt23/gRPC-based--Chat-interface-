import grpc 
import chat_pb2
import chat_pb2_grpc

def chat():
    channel=grpc.insecure_channel('localhost:50051')
    stub=chat_pb2_grpc.ChatServiceStub(channel)

    def message_generator():
        while True :
            user = input ("Enter your name ")
            reciptent=input("Enter recipient (lve blank for group chat)")
            message=input("Enter your message (type 'exit')")

            if message.lower()=="exit":
                print("Bye bye ")
                break

            chat_message=chat_pb2.ChatMessage(
                User=user,
                message=message,
                reciptent=reciptent,
                is_private=True if reciptent!="Group" else False

            )
            yield chat_message
        
    response_iterator=stub.Chat(message_generator())
    for response in response_iterator:
            print(f"Recived from {response.User}:{response.message}")
def send_private_message():
        channel=grpc.insecure_channel("localhost:50051")
        stub=chat_pb2_grpc.ChatServiceStub(channel)

        while True :
            user = input ("Enter your name ")
            
            reciptent=input("Enter recipient (lve blank for group chat)")
            
            message=input("Enter your message (type 'exit')")
            

            if message.lower()=="exit":
                print("Bye bye ")
                break
            chat_message=chat_pb2.ChatMessage(
                User=user,
                message=message,
                reciptent=reciptent,
                is_private=True if reciptent!="Group" else False

            )
            
            response=stub.SendPrivateMessage(chat_message)
            print(response.message)
            
def main():
     print("1. Group Chat (Bi-Directional Streaming)")
     print("2. Send Private Message")
     choice = input("Enter 1 or 2: ")

     if choice == "1":
            print("Starting Group Chat...")
            chat()
     elif choice == "2":
            print("Starting Private Messaging...")
            send_private_message()
     else:
            print("Invalid choice! Exiting.")
            return

if __name__ == '__main__':
    main()