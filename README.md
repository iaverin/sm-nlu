# Requirements 
Python: 3.9 

# Installation 
```
pip install -m requirements.txt
python -m spacy download ru_core_news_sm
```

# starting
 
```
waitress-serve --port 5005 --call nluserver:create_app
```

# Docker 
```
docker build --tag nluserver .
docker run  -p 5005:5005 -d nluserver
```


 
 
