import httpx
import dns.resolver as DR
import ssl
from decouple import config

def resolve_with_custom_dns(domain, dns_server):
    resolver = DR.Resolver()
    resolver.nameservers = dns_server
    answers = resolver.resolve(domain, 'A')
    return answers[0].to_text()

def call_gemini_api(api_key, prompt: str):
    domain = "generativelanguage.googleapis.com"
    path = f"/v1beta/models/gemini-2.0-flash:generateContent?key={api_key}"

    # DNS های لاین ۱۴ (شاتل)
    ip = resolve_with_custom_dns(domain, ["178.22.122.100", "185.51.200.2"])

    headers = {
        "Host": domain,
        "Content-Type": "application/json",
    }

    payload = {
        "contents": [
            {
                "parts": [
                    {
                        "text": prompt
                    }
                ]
            }
        ]
    }

    # ساختن SSL context بدون اعتبارسنجی
    context = ssl.create_default_context()
    context.check_hostname = False
    context.verify_mode = ssl.CERT_NONE

    url = f"https://{ip}/{path}"

    transport = httpx.HTTPTransport(retries=2, ssl_context=context)

    with httpx.Client(headers=headers, transport=transport) as client:
        response = client.post(url=url, json=payload)
        return response

# استفاده
prompt = 'Tell me about machine learning.'
API_KEY = config('API_KEY', cast=str)
response = call_gemini_api(api_key=API_KEY, prompt=prompt)

print("Status code:", response.status_code)
print("Response:", response.text)
