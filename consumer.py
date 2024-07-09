from kafka import KafkaConsumer, KafkaProducer
import json

# Kafka Consumer to consume messages from the 'user-login' topic
consumer = KafkaConsumer(
    'user-login',
    bootstrap_servers='localhost:29092',
    value_deserializer=lambda x: json.loads(x.decode('utf-8'))
)

# Kafka Producer to produce messages to the 'processed-user-login' topic
producer = KafkaProducer(
    bootstrap_servers='localhost:29092',
    value_serializer=lambda x: json.dumps(x).encode('utf-8')
)

# Process messages and produce to the new topic
for message in consumer:
    data = message.value
    # Example processing: filter messages where device_type is 'android'
    if data['device_type'] == 'android':
        producer.send('processed-user-login', value=data)
        print(f"Processed message: {data}")

print("Consumer and producer setup complete.")
