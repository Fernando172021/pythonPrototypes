from tkinter import *

data = {
    'MOTORISTAS'         : [],
    'CHEGADA EADI'       : [],
    'SAIDA EADI'         : [],
    'CHEGADA BRIDGESTONE': [],
    'SAIDA BRIDGESTONE'  : []
    }

def click():
    if inputValue.get() != '':
        data['MOTORISTAS'].append(inputValue.get())
        inputValue.delete(0, 'end')
    else: 
        end_word['text'] = 'Insira as Informações'

    if inputValue2.get() != '':
        data['CHEGADA EADI'].append(inputValue2.get())
        inputValue2.delete(0, 'end')
    else: 
        end_word['text'] = 'Insira as Informações'

    if inputValue3.get() != '':
        data['SAIDA EADI'].append(inputValue3.get())
        inputValue3.delete(0, 'end')
    else: 
        end_word['text'] = 'Insira as Informações'

    if inputValue4.get() != '':
        data['CHEGADA BRIDGESTONE'].append(inputValue4.get())
        inputValue4.delete(0, 'end')
    else: 
        end_word['text'] = 'Insira as Informações'

    if inputValue5.get() != '':
        data['SAIDA BRIDGESTONE'].append(inputValue5.get())
        inputValue5.delete(0, 'end')
    else: 
        end_word['text'] = 'Insira as Informações'

window = Tk()
window.title('Wilson Sons')

word_init = Label(window, text= 'Clique no botão para ver as cotações das moedas')
word_init.grid(column = 0, row = 0, padx= 10, pady=10)

inputLabel = Label(window, text='MOTORISTA')
inputLabel.grid(column= 0, row= 1)

inputValue = Entry(window)
inputValue.grid(column= 0, row= 2)

inputLabel2 = Label(window, text= 'CHEGADA EADI')
inputLabel2.grid(column= 0, row= 3)

inputValue2 = Entry(window)
inputValue2.grid(column= 0, row= 4)

inputLabel3 = Label(window, text= 'SAIDA EADI')
inputLabel3.grid(column= 0, row= 5)

inputValue3 = Entry(window)
inputValue3.grid(column= 0, row= 6)

inputLabel4 = Label(window, text= 'CHEGADA BRIDGESTONE')
inputLabel4.grid(column= 0, row= 7)

inputValue4 = Entry(window)
inputValue4.grid(column= 0, row= 8)

inputLabel5 = Label(window, text= 'SAIDA BRIDGESTONE')
inputLabel5.grid(column= 0, row= 9)

inputValue5 = Entry(window)
inputValue5.grid(column= 0, row= 10, pady= 10)

button1 = Button(window, text='Gerar Planilha', command=click)
button1.grid(column= 0, row= 11, pady= 10)

end_word = Label(window, text='')
end_word.grid(column= 0, row= 12, pady= 10)

window.mainloop()
