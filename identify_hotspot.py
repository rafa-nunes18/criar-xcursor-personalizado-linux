"""  
identify_hotspot.py  

Descrição:  
Este script permite ao usuário identificar e marcar as coordenadas de um ponto de hotspot em uma imagem usando a biblioteca OpenCV.  
Ao clicar na imagem exibida, um círculo vermelho é desenhado na área do clique e as coordenadas do hotspot são impressas no terminal.  
Este script é útil para determinar a localização exata de interação em imagens, o que pode ser aplicável em várias áreas, como design de interfaces e desenvolvimento de jogos.  

Autor: Rafael A. Nunes  
Data de Criação: 2023-10-01  

Requisitos:  
 - Python 3 ou superior instalado.  
 - Biblioteca OpenCV instalada. Para instalar, use o seguinte comando:  
   
    pip install opencv-python  

Uso:  
 - executar o script  

Observações:  
 - O caminho da imagem deve ser ajustado manualmente no código. A imagem deve estar no mesmo tamanho que o cursor quando utilizado.  
 - Ao clicar com o botão esquerdo do mouse sobre a imagem, as coordenadas do hotspot serão mostradas no terminal.  

Exemplo de execução:  
- Execute o script e clique na imagem exibida para ver as coordenadas do hotspot e um círculo vermelho marcado na posição do clique.  

"""  

import cv2  

def click_event(event, x, y, flags, params):  
    """  
    Função de callback para eventos de clique do mouse.  
    Quando o botão esquerdo do mouse é clicado, as coordenadas do hotspot são impressas  
    no terminal e um círculo vermelho é desenhado na imagem.  

    Parâmetros:  
    - event: Tipo de evento (neste caso, clique do botão esquerdo).  
    - x: Coordenada X do clique.  
    - y: Coordenada Y do clique.  
    - flags: Flags do evento (não utilizado neste exemplo).  
    - params: Parâmetros adicionais (não utilizado neste exemplo).  
    """  
    if event == cv2.EVENT_LBUTTONDOWN:  
        print(f"Hotspot: ({x}, {y})")  
        cv2.circle(img, (x, y), 5, (0, 0, 255), -1)  
        cv2.imshow("Image", img)  

# Carrega a imagem  
img_path = 'imagens/cursores/cursor-cry-x25.png'  # Substitua pelo caminho da sua imagem  
img = cv2.imread(img_path)  

cv2.imshow("Image", img)  
cv2.setMouseCallback("Image", click_event)  

cv2.waitKey(0)  
cv2.destroyAllWindows()