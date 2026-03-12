import boto3
import time
import calendar

client = boto3.client('logs', region_name='ap-south-1')
LOG_GROUP = "/aws/devops/autonomous-app"
LOG_STREAM = "App-Health-Stream"

try:
client.create_log_stream(logGroupName=LOG_GROUP, logStreamName=LOG_STREAM)
except client.exceptions.ResourceAlreadyExistsException:
pass

def send_status():
timestamp = int(calendar.timegm(time.gmtime()) * 1000)
message = "STATUS: OK - System Operational"
client.put_log_events(
logGroupName=LOG_GROUP,
logStreamName=LOG_STREAM,
logEvents=[{'timestamp': timestamp, 'message': message}]
)
print(f"Update sent to AWS: {message}")

if name == "main":
send_status()