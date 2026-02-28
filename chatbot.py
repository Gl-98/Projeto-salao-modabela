import re
from datetime import datetime

class Chatbot:
    def __init__(self):
        # Base de conhecimento do chatbot
        self.respostas = {
            'saudacao': [
                'Olá! 👋 Como posso te ajudar hoje?',
                'Oi! 😊 Em que posso ser útil?',
                'Olá! Seja bem-vindo(a)! Como posso ajudar?'
            ],
            'horario': {
                'salao': '🕐 O salão funciona de Segunda a Sábado, das 9h às 18h.',
                'loja': '🕐 A loja funciona de Segunda a Sábado, das 9h às 19h.'
            },
            'servicos_salao': '''💇‍♀️ Serviços do Salão:
• Corte feminino e masculino
• Coloração e mechas
• Escova e penteados
• Hidratação e tratamentos
• Manicure e pedicure
• Design de sobrancelhas''',
            'servicos_loja': '''👗 Na loja você encontra:
• Roupas femininas
• Acessórios
• Bolsas e sapatos
• Moda casual e festa
• Tamanhos variados''',
            'preco': 'Os valores variam conforme o serviço. Para orçamento personalizado, fale conosco pelo WhatsApp! 💬',
            'agendamento': '📅 Para agendar, clique no botão "FALAR NO WHATSAPP" e escolha o melhor horário!',
            'localizacao': '📍 Estamos localizados em Vila Velha, ES. Entre em contato pelo WhatsApp para endereço completo!',
            'pagamento': '💳 Aceitamos: Dinheiro, PIX, Cartão de débito e crédito (parcelas disponíveis).',
            'whatsapp': '📱 Clique no botão "FALAR NO WHATSAPP" do serviço desejado (Salão ou Loja) e vamos conversar!',
            'despedida': [
                'Até logo! 👋 Qualquer dúvida, estamos aqui!',
                'Foi um prazer ajudar! 😊 Até breve!',
                'Tchau! 💕 Esperamos ver você em breve!'
            ],
            'default': 'Desculpe, não entendi sua pergunta. 😅 Pergunte sobre: horários, serviços, preços, agendamento ou localização!'
        }
        
        # Palavras-chave para identificar intenções
        self.intencoes = {
            'saudacao': ['oi', 'olá', 'ola', 'hey', 'bom dia', 'boa tarde', 'boa noite'],
            'horario': ['horário', 'horario', 'abre', 'fecha', 'funciona', 'aberto', 'que horas'],
            'servicos_salao': ['serviço', 'servico', 'salão', 'salao', 'cabelo', 'corte', 'coloração', 'escova', 'manicure', 'pedicure'],
            'servicos_loja': ['loja', 'roupa', 'blusa', 'vestido', 'calça', 'saia', 'moda', 'acessório', 'acessorio', 'bolsa'],
            'preco': ['preço', 'preco', 'valor', 'quanto custa', 'quanto é', 'quanto fica'],
            'agendamento': ['agendar', 'marcar', 'horário disponível', 'horario disponivel', 'marcar horário'],
            'localizacao': ['onde', 'endereço', 'endereco', 'localização', 'localizacao', 'fica'],
            'pagamento': ['pagamento', 'pagar', 'cartão', 'cartao', 'pix', 'dinheiro', 'débito', 'debito', 'crédito', 'credito'],
            'whatsapp': ['whatsapp', 'whats', 'contato', 'falar', 'telefone', 'número', 'numero'],
            'despedida': ['tchau', 'até logo', 'ate logo', 'falou', 'obrigado', 'obrigada', 'valeu']
        }
    
    def identificar_intencao(self, mensagem):
        """Identifica a intenção do usuário baseado na mensagem"""
        mensagem_lower = mensagem.lower()
        
        # Verificar cada intenção
        for intencao, palavras_chave in self.intencoes.items():
            for palavra in palavras_chave:
                if palavra in mensagem_lower:
                    return intencao
        
        return 'default'
    
    def responder(self, mensagem):
        """Gera uma resposta baseada na mensagem do usuário"""
        intencao = self.identificar_intencao(mensagem)
        
        # Respostas especiais para horário
        if intencao == 'horario':
            mensagem_lower = mensagem.lower()
            if 'salão' in mensagem_lower or 'salao' in mensagem_lower or 'cabelo' in mensagem_lower:
                return self.respostas['horario']['salao']
            elif 'loja' in mensagem_lower or 'roupa' in mensagem_lower:
                return self.respostas['horario']['loja']
            else:
                return f"{self.respostas['horario']['salao']}\n\n{self.respostas['horario']['loja']}"
        
        # Respostas que são listas (aleatórias)
        if intencao in ['saudacao', 'despedida']:
            import random
            return random.choice(self.respostas[intencao])
        
        # Respostas diretas
        if intencao in self.respostas:
            return self.respostas[intencao]
        
        return self.respostas['default']


# Teste local (opcional)
if __name__ == '__main__':
    bot = Chatbot()
    print("🤖 Chatbot de teste iniciado! Digite 'sair' para encerrar.\n")
    
    while True:
        mensagem = input("Você: ")
        if mensagem.lower() in ['sair', 'exit', 'quit']:
            print("Bot: Até logo! 👋")
            break
        
        resposta = bot.responder(mensagem)
        print(f"Bot: {resposta}\n")
