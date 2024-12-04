import json
import boto3
 
sqs = boto3.client('sqs')

def get_names_queues():
    dic = {
        "Travel Schedules and Tickets" : "https://sqs.us-east-1.amazonaws.com/309691585403/travel-schedules-tickets",
        "Customer Service and Support" : "https://sqs.us-east-1.amazonaws.com/309691585403/customer-service-support",
        "Reservations and Luggage" : "https://sqs.us-east-1.amazonaws.com/309691585403/reservations-luggage"
    }

    return dic


def get_data():
    dic = {
        "Travel Schedules and Tickets" : ["airline","travel","trip","journey","management","flight","cost","money","flying","airport","fly","Boarding","travelling","flights","scdeduled"],
        "Customer Service and Support" : ["request","check-in","seat","support","service","website","advice","seats","direct","can you take","please","I need","Visa","take","Can anyone","passport"],
        "Reservations and Luggage" : ["luggage","Reservations","Bookings","Holdings","booked","booking","suitcases","suitcase","passenger"]
    }

    return dic


def lambda_handler(event, context):
    data = get_data()
    queues = get_names_queues()
    messages = event['Records']
    for record in messages:
        body = record["body"]
        msg_json = json.loads(body)
        msg = msg_json["message"]
        validate = True
        for key,value in data.items():
            if any(word in msg for word in value):
                sqs.send_message(QueueUrl = queues[key], MessageBody = json.dumps(msg_json))
                print("Message sent to: " + key)
                validate = False
                break
        if validate:
            print(msg)
