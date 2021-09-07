# Requirements 
Python: 3.9 

# Installation 
```
pip install -m requirements.txt
python -m spacy download ru_core_news_sm
```

# Starting
 
```
waitress-serve --port 5005 --call nluserver:create_app
```

# Docker 
```
docker build --tag nluserver .
docker run  -p 5005:5005 -d nluserver
```

# Test the installation
```
### Request 
POST localhost:5005/intent
Content-Type: application/json

{"text": "Где заказ", "context":["global"]}

### Response's body should be

{
  "text": "Где заказ",
  "intent": "order_status",
  "context": [
    "global"
  ]
}

```


 
 
