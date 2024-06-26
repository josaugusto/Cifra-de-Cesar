import PySimpleGUI as sg
from sys import exit
from main import *


def criar_interface():

    # Tema 
    sg.theme('DarkBlue2')

    #janelas
    def criar_menu():
        layoutMenu = [ 
            [sg.Text('Bem-vindo ao programa de criptografia de Cifra de César\nPor favor selecione uma das três opções a baixo')],
            [sg.Button('Criptografar', size=(15, 2), expand_x=True)],
            [sg.Button('Descriptografar', size=(15, 2), expand_x=True)],
            [sg.Button('Criptoanálise', size=(15, 2), expand_x=True)]
        ]
        return sg.Window('Cifra de César', layoutMenu, finalize=True)

    def criar_janela_criptografar():
        layoutCriptografar = [
            [sg.Text('Informe a mensagem a ser Criptografada:')], 
            [sg.Multiline(key='mensagem', auto_refresh=True, size=(50, 10))],
            [sg.Text('Informe a chave(0 a 25)'), sg.Input(key='chave', size=(2, 0)), sg.Checkbox('Esquerda'), sg.Checkbox('Direita')],
            [sg.Button('Codificar')],
            [sg.Text('Mensagem Criptografada:')],
            [sg.Multiline(size=(50, 10), do_not_clear=False, reroute_stdout=True)],
            [sg.Button('Voltar')]
        ]
        return sg.Window('Criptografar', layoutCriptografar, finalize=True)

    def criar_janela_descriptografar():
        layoutDescriptografar = [
            [sg.Text('Informe a mensagem Criptografada:')],
            [sg.Multiline(key='mensagem', auto_refresh=True, size=(50, 10))],
            [sg.Text('Informe a chave(0 a 25)'), sg.Input(key='chave', size=(2, 0)), sg.Checkbox('Esquerda'), sg.Checkbox('Direita')],
            [sg.Button("Decodificar")],
            [sg.Text('Mensagem Descriptografada:')],
            [sg.Multiline(size=(50, 10),  do_not_clear=False, reroute_stdout=True)],
            [sg.Button('Voltar')]
        ]
        return sg.Window('Descriptografar', layoutDescriptografar, finalize=True)

    def criar_janela_criptoanalise():
        layoutCriptoanalise = [
            [sg.Text('Informe a mensagem Criptografada:')],
            [sg.Multiline(key='mensagem', auto_refresh=True, size=(50, 10))],
            [sg.Button('Criptoanálisar')],
            [sg.Multiline(size=(50, 10),  do_not_clear=False, reroute_stdout=True)],
            [sg.Button('Voltar')]
        ]
        return sg.Window('Criptoanálise', layoutCriptoanalise, finalize=True)

    menu, janela_criptografar, janela_descriptografar, janela_criptoanálise = criar_menu(), None, None, None

    while True:
        janela, evento, valores = sg.read_all_windows()

        if evento == sg.WINDOW_CLOSED:
            janela.close()
            exit() 
            
        #Criptografar 
        if evento == 'Criptografar' and janela == menu:
            janela.hide() 
            janela_criptografar = criar_janela_criptografar()
        elif evento == 'Codificar':
            if valores[0] == True and valores[1] == True or valores[0] == valores[1] == False:
                sg.popup('ERRO!, Marque uma das duas opções(Esquerda ou Direita)', title='Erro')
            elif valores['chave'] == '' or not(0 <= int(valores['chave']) <= 25):
                sg.popup('Informe um valor válido para a chave(0 a 25)', title='Erro')
            elif valores[0] == True:
                print(f"{criptografar(valores['mensagem'], int(valores['chave']), 'E')}")
            elif valores[1] == True:
                print(f"{criptografar(valores['mensagem'], int(valores['chave']), 'D')}")
        elif evento == 'Voltar' and janela == janela_criptografar:
            janela_criptografar.close()
            menu.UnHide()

        #Descriptografar
        if evento == 'Descriptografar':
            janela.hide()
            janela_descriptografar = criar_janela_descriptografar()
        elif evento == 'Decodificar':
            if valores[0] == True and valores[1] == True or valores[0] == valores[1] == False:
                sg.popup('ERRO!, Marque uma das duas opções(Esquerda ou Direita)', title='Erro')
            elif valores['chave'] == '' or not(0 <= int(valores['chave']) <= 25):
                sg.popup('Informe um valor válido para a chave(0 a 25)', title='Erro')
            elif valores[0] == True:
                print(f"{descriptografar(valores['mensagem'], int(valores['chave']), 'E')}")
            else:
                print(f"{descriptografar(valores['mensagem'], int(valores['chave']), 'D')}")
            
        elif evento == 'Voltar' and janela == janela_descriptografar:
            janela_descriptografar.close()
            menu.UnHide()

        #Criptoanálise
        if evento == 'Criptoanálise':
            janela.hide()
            janela_criptoanálise = criar_janela_criptoanalise()
        elif evento == 'Criptoanálisar':
            criptoanalise(valores['mensagem'])
        elif evento == 'Voltar' and janela == janela_criptoanálise:
            janela.close()
            menu.UnHide()
criar_interface()
