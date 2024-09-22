from kafka import KafkaProducer
import json

# Initialize the producer
producer = KafkaProducer(
    bootstrap_servers='localhost:9092,localhost:9093',  # Adjust if necessary
    value_serializer=lambda v: json.dumps(v).encode('utf-8'),  # Serialize JSON
    key_serializer=lambda k: str(k).encode('utf-8')  # Serialize keys
)

def produce_data(topic, data):
    try:
        # Send the message
        producer.send(topic, key=data['id'], value=data)  # No need to encode manually
        producer.flush()  # Ensure all messages are sent
        print(f"Message sent to topic '{topic}': {data}")
    except Exception as e:
        print(f"Failed to produce message: {e}")

data = {
    'id': 1,
    'name': 'Test Message',
    'value': 'testing 123'
}

produce_data('test_topic', data)
