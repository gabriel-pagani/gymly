# Dashly - Dashboard Management System
Sistema de gerenciamento de dashboards integrado com Power BI e Metabase

## 🚀 Instalação e Configuração Inicial

#### 1. Clone o repositório:
```bash
git clone https://github.com/gabriel-pagani/dashly.git && cd dashly/
```
#### 2. Configure as variáveis de ambiente:
Crie um arquivo .env na raiz do projeto (baseado no [.env.example](https://github.com/gabriel-pagani/dashly/blob/main/.env.example)) e configure as credenciais do banco e do Django.
```bash
cp .env.example .env
```
```bash
# Conteúdo do .env após a cópia
SECRET_KEY="CHANGE-ME"
DEBUG="1"  # 1 = True | 0 = False
ALLOWED_HOSTS="CHANGE-ME,CHANGE-ME,CHANGE-ME"
CSRF_TRUSTED_ORIGINS="CHANGE-ME,CHANGE-ME,CHANGE-ME"
POSTGRES_DB="CHANGE-ME"
POSTGRES_USER="CHANGE-ME"
POSTGRES_PASSWORD="CHANGE-ME"
POSTGRES_HOST="database"
POSTGRES_PORT="5432"
```

#### 3. Build e Start inicial:
Execulte o comando de build para instalar as dependências, compilar o React e subir os containers.
```bash
make build-project
```

#### 4. Crie um super usuário (Admin):
Para acessar o sistema pela primeira vez, você precisa criar um super usuário.
```bash
make container-terminal
# Dentro do container:
python manage.py createsuperuser
```

## 🛠️ Comandos de Manutenção
O projeto utiliza um [Makefile](https://github.com/gabriel-pagani/dashly/blob/main/Makefile) para simplificar as operações diárias.

# License
See the [LICENSE](https://github.com/gabriel-pagani/dashly/blob/main/LICENSE) file for more details.

# Contact Information
Email: gabrielpaganidesouza@gmail.com
