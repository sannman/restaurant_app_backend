import os
from dotenv import load_dotenv
from supabase import create_client, Client

# Load local .env file (if present)
load_dotenv()

# Expected env vars: SUPABASE_URL and SUPABASE_ANON_KEY
url: str = os.environ.get("SUPABASE_URL")
anon_key: str = os.environ.get("SUPABASE_ANON_KEY") or os.environ.get("SUPABASE_KEY")



supabase: Client = create_client(url, anon_key)

user_what = input("Buyer or Seller? ")

if user_what == "Seller" or user_what == "S" or user_what == "s":
    dish = input("Enter dish name: ")
    price = int(input("Enter dish price: "))  
    response = (
        supabase.table("DISH")
        .insert({"id": 5, "Dish": dish,"Price": price})
        .execute()
)

if user_what == "Buyer" or user_what == "B" or user_what == "b":
    response = (
        supabase.table("DISH")
        .select("*")
        .execute()
    )
print(response.data)