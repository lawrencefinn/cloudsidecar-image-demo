# Cloud Sidecar Image Upload Demo
python - the python worker that polls sqs/pubsub, converts an image from png to jpg, and uploads ot back up to s3/gcs
play - scala web application that allows people to upload a jpg, it stores the image in s3/gcs, posts a message to 
sqs/pubsub to have the worker conver it, waits a few seconds, tries to render converted image from s3/gcs
