# Serverless Template Start Project

Repositorio de exemplo para organização de projetos serverless em estilo mono-repo e templates de exemplo de serviços serverless 

- libs: Pasta com codigos reutilizaveis para os projetos
- services: Pasta com os serviços em Serverless Framework
- shared_resources: Pasta para criação de recursos compartilhado entre os serviços

## Plugins Serverless Framework
Alguns plugins do Serverless Framework que são comuns nos projetos e são recomendados o seu uso

- serverless-iam-roles-per-function: Cria role e policy para cada função lambda
- serverless-plugin-aws-alerts: Cria alarmes para cada função lambda
- serverless-python-requirements: Baixa dependencias de modulos Python pelo requirements.txt

**OBS:** As nomenclaturas de pastas dos projetos Serverless são somente exemplos, siga a nomenclatura que melhor represente o seu projeto real