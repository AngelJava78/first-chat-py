from openai import OpenAI
from azure.identity import DefaultAzureCredential, get_bearer_token_provider
endpoint = "https://prj-ai103-dev-eu2-resource.services.ai.azure.com/openai/v1"
deployment_name = "gpt-5-mini"
azure_endpoint="https://ai.azure.com/.default"
token_provider=get_bearer_token_provider(DefaultAzureCredential(),azure_endpoint)
client = OpenAI(
    base_url=endpoint,
    api_key=token_provider
)
# response = client.responses.create(
#     model= deployment_name,
#     input="Quién ganó el 3er. lugar del mundial de futbol 2026. https://www.telemundo.com/noticias/noticias-telemundo/internacional/live-blog/mundial-2026-francia-inglaterra-partido-tercer-lugar-rcna588179"
# )

# answer = response.output_text;
# print(f"Answer: {answer}")

while True:
    input_text = input("Question: ")
    if input_text.lower() == "exit":
        break

    response = client.responses.create(
        model= deployment_name,
        input=input_text
    )
    print("Answer:")
    print(response.output_text)

