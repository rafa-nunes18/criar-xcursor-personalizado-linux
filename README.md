<h1 align="center">Criar cursor para linux</h1>

Este script através do xcursorgen cria um cursor x11 a partir de uma imagem PNG já editada (transparência).
Para ser usando no sistema Linux.

## testado em 

Linux Mint 22, não foi testado em outros sistemas.  

## Requisitos do sistema

  - libX11, libXcursor, libXrender, libXft, libcairo.

      Você pode instalar essas bibliotecas usando o gerenciador de pacotes de sua distribuição Linux.

      sudo apt-get install libx11-dev libxcursor-dev libxrender-dev libxft-dev libcairo2-dev
    
 - xcursorgen.

    O xcursorgen está incluído no pacote x11-utils. Use o comando:
   
    sudo apt install x11-utils
   
 - Python 3 ou superior instalado.
   
   use o comando para atualizar os pacotes.
   
   sudo apt update
      
 - Biblioteca PIL (Pillow) instalada.

    Para instalar, use o seguinte comando:

    pip install Pillow  

## Instrunções

  - Baixe o arquivo "create_cursor.py".
  
  - Abra o terminal e navegue para o diretório específico com o arquivo.

    cd /caminho/para/o/diretorio  

  - Comando para criar cursor:

    python3 create_cursor.py "image_path" "hotspot-x" "hotspot-y" "output-name" "size"  

    Argumentos:

      - image_path: Caminho para a imagem PNG que será usada para criar o cursor. Pode ser um caminho absoluto ou relativo.
     
      - hotspot-x: Coordenada X do ponto de hotspot do cursor (o ponto dentro da imagem que indica onde a interação ocorre, em pixels).
     
      - hotspot-y: Coordenada Y do ponto de hotspot do cursor (semelhante ao hotspot X, mas na direção vertical).
     
      - output-name: (Opcional) Nome do arquivo de saída para o cursor. Se não for especificado, o nome padrão será "xcursor".
     
      - size: (Opcional) Tamanho do cursor em pixels. Se não for fornecido, o tamanho padrão será 25 pixels.  

Obs: Se não sabe onde fica o hotspot da sua imagem, use o script "identificar_hotspot.py" para descobrir.

## Exemplos de uso:

1. python3 create_cursor.py /caminho/para/imagem/mycursor.png 10 10
 
Cria um cursor a partir da imagem com o caminho especificado, usando as coordenadas (10, 10) para o hotspot e com o nome padrão "xcursor" e tamanho padrão de 25 pixels.  

3. python3 create_cursor.py mycursor.png 10 10
   
** Para utilizar argumentos de caminho relativo, basta colocar a imagem PNG junto do mesmo diretório deste script. **
Cria um cursor da imagem "mycursor.png", usando (10, 10) como hotspot, com o nome padrão e tamanho padrão.  

5. python3 create_cursor.py mycursor.png 10 10 nome_cursor  

Cria um cursor da imagem "mycursor.png", usando (10, 10) como hotspot, e salva como "nome_cursor.cursor".  

6. python3 create_cursor.py mycursor.png 10 10 /caminho/para/salvar/  

Cria um cursor e o salva no caminho especificado, utilizando o nome padrão de "xcursor" e tamanho padrão de 25 pixels.  

7. python3 create_cursor.py mycursor.png 10 10 /caminho/para/salvar/nome_cursor  

Cria um cursor da imagem, usando (10, 10) como hotspot, e salva como "nome_cursor.cursor" no diretório especificado.  


Rafael A. Nunes ( rafa.nunes2018@hotmail.com ) 2024

Instagram: @rafa33alves
