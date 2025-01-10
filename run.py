from app import app  

print(f"Flask app: {app}") 

if __name__ == "__main__":
    app.run(debug=True,port=5001)  

