import boto3

# Crear un cliente SNS
sns_client = boto3.client('sns')

# ARN del topic SNS (cámbialo por el ARN de tu topic SNS)
sns_topic_arn = 'arn:aws:sns:us-east-1:309691585403:queue-customer'

def lambda_handler(event, context):
    # Mensaje a enviar
    messages = event['Records']
    for record in messages:
        eventSourcearn = record['eventSourceARN']
        eventSourcearnName = eventSourcearn.split(":")[-1]
        # Publicar el mensaje en SNS
        response = sns_client.publish(
            TopicArn=sns_topic_arn,
            Message = record["body"],
            Subject='Notificación desde la queue ' + eventSourcearnName
        )
    
    # Log de la respuesta (opcional)
    print(response)
    
    return {
        'statusCode': 200,
        'body': 'Mensaje enviado a SNS'
    }
