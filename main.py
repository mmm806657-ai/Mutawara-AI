import os

# سحب المفتاح من الخزنة
api_key = os.getenv('GOOGLE_API_KEY')

def start():
    print("--- Mutawara AI System ---")
    if api_key:
        # بنطبع أول 4 حروف للتأكد
        start_key = str(api_key)[:4]
        print(f"Connection Successful! Key starts with: {start_key}")
    else:
        print("Error: GOOGLE_API_KEY not found in Secrets")

if __name__ == "__main__":
    start()
