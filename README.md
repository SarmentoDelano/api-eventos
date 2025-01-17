# **API de Gerenciamento de Eventos**

Uma API desenvolvida com Django REST Framework para gerenciar eventos, participantes e inscrições, permitindo a organização eficiente de eventos e a administração de participantes.

---

## **Recursos da API**

A API fornece funcionalidades para:
- Gerenciar **Eventos**:
  - Criar, visualizar, atualizar e excluir eventos.
  - Configurar local, data, capacidade e descrição do evento.
- Gerenciar **Participantes**:
  - Criar, visualizar, atualizar e excluir informações de participantes.
  - Validar dados como CPF, e-mail e telefone.
- Gerenciar **Inscrições**:
  - Registrar participantes em eventos específicos.
  - Listar inscrições por evento e participante.

---

## **Tecnologias Utilizadas**

- **Python**: Linguagem de programação.
- **Django**: Framework web.
- **Django REST Framework (DRF)**: Para criar APIs RESTful.
- **SQLite**: Banco de dados padrão para desenvolvimento.

---

## **Configuração do Ambiente**

### **1. Pré-requisitos**
- Python 3.8+
- Pipenv ou pip para gerenciamento de pacotes
- Git instalado
- Banco de dados SQLite ou outro configurado

### **2. Clonar o Repositório**
```bash
git clone https://github.com/SarmentoDelano/api-eventos.git
cd api-eventos
```

### **3. Instalar Dependências**
```bash
pip install -r requirements.txt
```

### **4. Executar Migrações**
```bash
python manage.py makemigrations
python manage.py migrate
```

### **5. Rodar o Servidor**
```bash
python manage.py runserver
```

A API estará disponível em `http://127.0.0.1:8000/`.

---

## **Endpoints**

### **Eventos**
| Método | Endpoint           | Descrição                                |
|--------|--------------------|------------------------------------------|
| GET    | /eventos/          | Lista todos os eventos                  |
| POST   | /eventos/          | Cria um novo evento                     |
| GET    | /eventos/{id}/     | Recupera detalhes de um evento específico |
| PUT    | /eventos/{id}/     | Atualiza informações de um evento        |
| DELETE | /eventos/{id}/     | Remove um evento                        |

### **Participantes**
| Método | Endpoint           | Descrição                                |
|--------|--------------------|------------------------------------------|
| GET    | /participantes/    | Lista todos os participantes            |
| POST   | /participantes/    | Registra um novo participante           |
| GET    | /participantes/{id}/ | Recupera informações de um participante específico |
| PUT    | /participantes/{id}/ | Atualiza informações de um participante |
| DELETE | /participantes/{id}/ | Remove um participante                 |

### **Inscrições**
| Método | Endpoint               | Descrição                             |
|--------|------------------------|---------------------------------------|
| POST   | /inscricoes/           | Registra um participante em um evento|
| GET    | /inscricoes/           | Lista todas as inscrições            |
| GET    | /eventos/{id}/inscricoes/ | Lista os participantes de um evento |
| GET    | /participantes/{id}/inscricoes/ | Lista os eventos de um participante |

---

## **Validações**

A API realiza validações específicas para assegurar a integridade dos dados:
- **Participantes**:
  - Nome deve conter apenas letras e ter pelo menos 3 caracteres.
  - CPF deve ser único e conter 11 dígitos válidos.
  - E-mail deve ser válido.
  - Telefone é opcional, mas deve ter formato válido se fornecido.
- **Eventos**:
  - Título deve ter pelo menos 5 caracteres.
  - Descrição deve ter pelo menos 10 caracteres.
  - Local deve ter pelo menos 3 caracteres.
  - Capacidade deve ser um número positivo.

---
