from openai import OpenAI

client = OpenAI()

response = client.chat.completions.create(
  model="gpt-4o-mini",
  messages=[
    {
      "role": "user",
      "content": [
        {"type": "text", "text": f"{Prompt}"},
        {
          "type": "image_url",
          "image_url": {
            "url": f"{Image Url}",
          },
        },
      ],
    }
  ],
  max_tokens=3000,
)

print(response.choices[0])
