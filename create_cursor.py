"""
Autor: Rafael A. Nunes (rafa.nunes2018@hotmail.com) 2024 

Descrição:  
Este script cria um cursor x11 a partir de uma imagem PNG já editada (com imagem e transparência).
O usuário pode especificar o caminho da imagem, as coordenadas do hotspot do cursor (ponto em que a interação acontece),
o nome do arquivo de saída do cursor e o tamanho desejado do cursor.
O script cria arquivos temporários e os remove após a criação do cursor x11, garantindo uma operação limpa.

# Funciona em Linux Mint 22; não foi testado em outros sistemas.  

Requisitos:  
 - Python 3 ou superior instalado.  
 - Biblioteca PIL (Pillow) instalada. Para instalar, use o seguinte comando:

    pip install Pillow  

Uso:
 - No terminal do Linux, digite:

    python3 create_cursor.py <image_path> <hotspot-x> <hotspot-y> [<output-name>] [<size>]  

Argumentos:  
- `<image_path>`: Caminho para a imagem PNG que será usada para criar o cursor. Pode ser um caminho absoluto ou relativo.  
- `<hotspot-x>`: Coordenada X do ponto de hotspot do cursor (o ponto dentro da imagem que indica onde a interação ocorre, em pixels).  
- `<hotspot-y>`: Coordenada Y do ponto de hotspot do cursor (semelhante ao hotspot X, mas na direção vertical).  
- `[<output-name>]`: (Opcional) Nome do arquivo de saída para o cursor. Se não for especificado, o nome padrão será "xcursor".  
- `[<size>]`: (Opcional) Tamanho do cursor em pixels. Se não for fornecido, o tamanho padrão será 25 pixels.  

arquivos temporários:
- Imagem PNG  (redimensionamento da imagem conforme o tamanho de pixels especificado).
- Arquivo de cursor (.cursor).

Observações: 
 - Se não sabe onde fica o hotspot da sua imagem, use o script "identifica_hotspot.py" para descobrir.
 - Em "output-name", o local de saída por padrao é o mesmo diretório do script, como opção, pode colocar apenas o caminho onde o cursor padrao será gerado,
   ou pode especificar o caminho absoluto com nome onde será salvo o novo cursor. 

Exemplos:  
1. python3 create_cursor.py /caminho/para/imagem/mycursor.png 10 10  
   - Cria um cursor a partir da imagem com o caminho especificado, usando as coordenadas (10, 10) para o hotspot e com o nome padrão "xcursor" e tamanho padrão de 25 pixels.  

2. python3 create_cursor.py mycursor.png 10 10
   # Para utilizar argumentos de caminho relativo, basta colocar a imagem PNG junto do mesmo diretório deste script.
   - Cria um cursor da imagem "mycursor.png", usando (10, 10) como hotspot, com o nome padrão e tamanho padrão.  

3. python3 create_cursor.py mycursor.png 10 10 nome_cursor  
   - Cria um cursor da imagem "mycursor.png", usando (10, 10) como hotspot, e salva como "nome_cursor.cursor".  

4. python3 create_cursor.py mycursor.png 10 10 /caminho/para/salvar/  
   - Cria um cursor e o salva no caminho especificado, utilizando o nome padrão de "xcursor" e tamanho padrão de 25 pixels.  

5. python3 create_cursor.py mycursor.png 10 10 /caminho/para/salvar/nome_cursor  
   - Cria um cursor da imagem, usando (10, 10) como hotspot, e salva como "nome_cursor.cursor" no diretório especificado.  
""" 

from PIL import Image  
import os  
import sys  
import subprocess  

def create_cursor(image_path, hotspot_x, hotspot_y, output_name, size=25):  
    """  
    Cria um cursor x11 a partir de uma imagem PNG.  
    
    Parâmetros:  
    - image_path (str): Caminho para a imagem PNG que será usada para criar o cursor.  
    - hotspot_x (int): Coordenada X do ponto de hotspot do cursor.  
    - hotspot_y (int): Coordenada Y do ponto de hotspot do cursor.  
    - output_name (str): Nome do arquivo de saída do cursor (padrão é "xcursor"). 
    - size (int): Tamanho do cursor em pixels (padrão é 25).  
    
    O script redimensiona a imagem, gera um arquivo de cursor e remove os arquivos temporários após a criação.  
    """  
    # Abre a imagem  
    img = Image.open(image_path)  

    # Redimensiona a imagem para o tamanho especificado  
    img = img.resize((size, size), Image.LANCZOS)  

    # Salva a imagem redimensionada  
    resized_image_path = os.path.join(os.path.dirname(image_path), f'resized_{output_name}.png')  
    img.save(resized_image_path, format='PNG')  

    # Cria o arquivo .cursor  
    cursor_file_name = os.path.join(os.path.dirname(image_path), f'{output_name}.cursor')  
    with open(cursor_file_name, 'w') as cursor_file:  
        cursor_file.write(f"{size} {hotspot_x} {hotspot_y} {resized_image_path}\n")  

    # Chama xcursorgen para gerar o cursor  
    subprocess.run(['xcursorgen', cursor_file_name, output_name])  

    # Remove a imagem redimensionada e o arquivo .cursor após a criação do cursor  
    os.remove(resized_image_path)  
    os.remove(cursor_file_name)  

    print(f'Cursor "{output_name}" criado com sucesso!')  

def get_unique_cursor_name(base_name):  
    """  
    Gera um nome único para o arquivo de cursor.  
    
    Parâmetros:  
    - base_name (str): Nome base para o cursor.  
    
    Retorna:  
    - str: Nome único para o cursor, adicionando "(copia X)" se necessário.  
    """  
    cursor_file_name = f"{base_name}.cursor"  
    count = 1  

    # Verifica se o arquivo já existe e cria um novo nome se necessário  
    while os.path.exists(cursor_file_name):  
        cursor_file_name = f"{base_name} (copia {count}).cursor"  
        count += 1  

    return base_name  # Retorna o nome base para uso posterior  

if __name__ == "__main__":  
    """  
    Função principal que executa o script.  
    
    O script aceita 3 ou 4 argumentos:  
    - <image_path>: Caminho para a imagem PNG.  
    - <hotspot-x>: Coordenada X do hotspot.  
    - <hotspot-y>: Coordenada Y do hotspot.  
    - [<output-name>]: (Opcional) Nome do arquivo de saída do cursor.  
    - [<size>]: (Opcional) Tamanho do cursor em pixels.  
    
    Exemplo de uso:  
    python create_cursor.py mycursor.png 10 10 [output-name] [size]  
    """  
    if len(sys.argv) < 4 or len(sys.argv) > 5:  
        print("Uso: python create_cursor.py <image_path> <hotspot-x> <hotspot-y> [<output-name>] [<size>]")  
        sys.exit(1)  

    image_path = sys.argv[1]  
    # Verifica se é apenas o nome do arquivo e ajusta com o diretório atual  
    if not os.path.isabs(image_path):  
        image_path = os.path.join(os.getcwd(), image_path)  

    hotspot_x = int(sys.argv[2])  
    hotspot_y = int(sys.argv[3])  
    output_name = "xcursor"  # Nome padrão  
    size = 25  # Valor padrão  

    # Verifica se o nome do cursor foi especificado  
    if len(sys.argv) == 5:  
        output_name = sys.argv[4]  
        
        if sys.argv[4].isdigit():  
            size = int(sys.argv[4])  # Atualiza o tamanho se o argumento for um número  
        else:  
            output_name = sys.argv[4]  # Caso contrário, atualiza para o nome do cursor  

    # Gera um nome único para o cursor  
    output_name = get_unique_cursor_name(output_name)  

    create_cursor(image_path, hotspot_x, hotspot_y, output_name, size)
