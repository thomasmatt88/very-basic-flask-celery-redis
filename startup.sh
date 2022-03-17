#!/bin/bash

# Start the first process
celery -A celery_tasks worker --loglevel=info -f celery.logs &
  
# Start the second process
python app.py &

# Wait for any process to exit
wait -n
  
# Exit with status of process that exited first
exit $?