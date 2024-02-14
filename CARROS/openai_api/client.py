from openai import OpenAI


client = OpenAI(
    api_key='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'
)

def get_car_ai_bio(model, brand, year):
    frase = ''''
    Me mostre uma descrição de venda para o carro {} {} {} em apenas 250 caracteres. Fale coisas específicas desse modelo.
    Descreva especificações técnicas desse modelo de carro.
    '''
    message = frase.format(brand, model, year)
    response = client.chat.completions.create(
        messages=[
            {
                'role': 'user',
                'content': message
            }
        ],
        max_tokens=1000,
        model='gpt-3.5-turbo',
    )

    return response.choices[0].message.content
