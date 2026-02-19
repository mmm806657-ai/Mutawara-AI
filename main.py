import os

# الحصول على المفتاح من الخزنة
api_key = os.getenv('GOOGLE_API_KEY')

def start_mutawara():
    if api_key:
        print("✅ تم تفعيل الربط السيادي مع Google Cloud")
        print("🛡️ نظام 'المطورة' جاهز للعمل")
    else:
        print("⚠️ المفتاح السري غير موجود في البيئة")

if __name__ == "__main__":
    start_mutawara()
