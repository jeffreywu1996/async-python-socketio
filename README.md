# Example of socketio using async

# Start
Set up
```
source venv/bin/activate
pip3 install -r requirements.txt
```

Start server
```
python3 main.py
```

Start client
```
python3 client.py
```

# Run load test
```
cd load_test
npx artillery run --output report.json scenario.yml
```
