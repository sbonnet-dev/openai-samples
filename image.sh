curl https://api.openai.com/v1/images/generations \
  -H 'Content-Type: application/json' \
  -H 'Authorization: Bearer YOURKEY' \
  -d '{
  "prompt": "your sentence",
  "n": 1,
  "size": "1024x1024"
}'
