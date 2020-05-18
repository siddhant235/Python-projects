from twilio.rest import Client 
 
account_sid = 'AC05e17340392a66f5c73a6c82231951b2' 
auth_token = '6ccc831c816314c4d0f6e2a2ae785c67' 
client = Client(account_sid, auth_token) 
 
message = client.messages.create( 
                              from_='+19196421036',  
                              body='hi',      
                              to='+917355669926' 
                          ) 
 
print(message.sid)