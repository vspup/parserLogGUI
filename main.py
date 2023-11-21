# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')
    # convert log to map

    import math
    import matplotlib.pyplot as plt

    import tkinter as tk
    from tkinter import ttk
    from tkinter import filedialog as fd

    import re
    import locale

    from datetime import datetime


    from dateutil import parser

    mainI = []
    mainV = []
    VV = []
    time = []
    nameLog = ''


    # Root window
    root = tk.Tk()
    root.title('Convert log files')
    root.grid_rowconfigure(0, weight=1)
    root.grid_columnconfigure(0, weight=1)

    # Log
    text = tk.Text(root, height=12)
    text.grid(column=0, row=0, sticky='nsew', columnspan=4)

    line = ["Thu Nov 16 15:06:35 2023", "aaaa"]






    def open_log_file():
        global mainI, mainV, time, dt, VV, t0, nameLog
        timeR = []
        # file type
        filetypes = (
            ('log files', '*.txt'),
            ('All files', '*.*')
        )
        # show the open file dialog
        f = fd.askopenfile(filetypes=filetypes, initialdir='./raw_log/')
        nameLog = f.name
        text.insert('end', '--> Read : ')
        text.insert('end', f.name)
        text.insert('end', '\n')


        T = []
        I1 = []
        I2 = []
        I3 = []
        I4 = []
        I5 = []
        I6 = []
        I7 = []
        I8 = []

        T18 = []
        V18 = []

        Ni = []
        Vi = []
        param = ''
        nn = 0
        ni = -1

        while True:

            # считываем строку
            line = f.readline()
            # прерываем цикл, если строка пустая
            if not line:

                break

            if len(line) > 0:
                # search start
                if re.search(r'\w{3}\s\w{3}\s\w{2}\s\d{2}:\d{2}:\d{2,4}\s\w{4}', line, re.IGNORECASE) != None:

                    sct = re.search(r'\w{3}\s\w{3}\s\w{2}\s\d{2}:\d{2}:\d{2,4}\s\w{4}', line, re.IGNORECASE)
                    ct = datetime.strptime(sct[0], "%a %b %d %H:%M:%S %Y")
                    #print(ct.strftime('%d.%b.%Y %H:%M:%S'))
                    ti = ct


                elif re.search('data point id', line) != None:
                    l = re.sub(r' ', '', line)
                    #print(l.split(':'))
                    if l.split(':')[1] == '0x1000\n':
                        param = 'Im'
                    elif l.split(':')[1] == '0x0201\n':
                        param = 'bcb_Uin'
                    elif l.split(':')[1] == '0x0202\n':
                        param = 'bcm_Uout'
                    else:
                        param = ''
                    #print(param, end='')

                elif re.search('number of elements:', line) != None:
                    l = re.sub(r' ', '', line)
                    l = re.sub(r'\n', '', line)
                    #print('[' + str(int(l.split(':')[1])) + ':', end='')
                    nn = int(l.split(':')[1])


                elif re.search('element index:', line) != None:
                    l = re.sub(r' ', '', line)
                    l = re.sub(r'\n', '', line)
                    #print(str(int(l.split(':')[1])) + '] = ', end='')
                    ni = int(l.split(':')[1])
                    Ni.append(ni)

                elif re.search('value:', line) != None:
                    l = re.sub(r' ', '', line)
                    ll = re.sub(r'\n', '', l)

                    vi = float(ll.split(':')[1])

                    Vi.append(vi)
                    if ni == nn-1:
                        if param != '':
                            print('/' + str(ct) + '/ ' + str(param) + '[' + str(nn) + '] = ' + str(Vi))
                            if param == 'Im':
                                T.append(ct)
                                I1.append(Vi[0])
                                I2.append(Vi[1]+0.5)
                                I3.append(Vi[2]+1)
                                I4.append(Vi[3]+1.5)
                                I5.append(Vi[4]+2)
                                I6.append(Vi[5]+2.5)
                                I7.append(Vi[6]+3)
                                I8.append(Vi[7]+3.5)
                            elif param == 'bcm_Uout':
                                T18.append(ct)
                                if Vi[0]>=0.0:
                                    V18.append(Vi[0])
                                else:
                                    V18.append(0)
                        Vi.clear()
                        Ni.clear()
                        param = ''
                        nn = 0
                        ni = -1




        # закрываем файл
        f.close
        print(T)
        print(I2)
        print(I3)
        print(I2[250])
        print(I3[250])
        print(len(I1))

        # graf
        # I m

        #ax_I = plt.plot(T, I1, 'b', T, I2, 'g', T, I3, 'r', T, I4, 'c', T, I5, 'm', T, I6, 'y', T, I7, 'k', T, I8, 'k--')

        #ax_I = plt.subplot(2, 1, 1)
        ax_I = plt
        ax_U = ax_I.twinx()

        ax_I.plot(T, I1, 'b', T, I2, 'g', T, I3, 'r', T, I4, 'c-x', T, I5, 'm', T, I6, 'y', T, I7, 'k', T, I8, 'k--')
        ax_U.plot(T18, V18, 'g--', linewidth= 3)

        #ax_I8.plot(T, I8, color='k', linestyle='--')

        #ax_I.set_ylabel('I, A')
        #ax_U.set_ylabel('U, V')

        # 18V
        #ax_U = plt.subplot(2, 1, 2)
        #ax_U.plot(T18, V18, color='g')
        #ax_U.set_xlabel('t, min')
        #ax_U.set_ylabel('U, V')
        #ax_U.grid()

        plt.show()

        text.insert('end', '--> Can write\n')


    # open XML file button
    open_Log = ttk.Button(
        root,
        text='Open Log File',
        command=open_log_file
    )
    open_Log.grid(column=0, row=2, sticky='w', padx=10, pady=10)


    ######
    def save_log_file():
        global mainI, mainV, time, dt, VV, t0, nameLog

        # file type
        filetypes = (
            ('log files', '*.map'),
            ('All files', '*.*')
        )
        # show the open file dialog
        name = nameLog.split('/')
        nm = str(name[-1])
        name = nm.replace('.txt', '.map')
        print(nm.replace('.txt', '.map'))

        def_name = str(name) + '.map'
        f = fd.asksaveasfile(mode='w', defaultextension=".map", initialfile=def_name, initialdir='./map/')
        nameMAP = f.name
        text.insert('end', '<<- Start write to : ')
        text.insert('end', f.name)
        text.insert('end', '\n')

        fmap = open(nameMAP, 'w')
        # i = 0
        for i in range(len(time)):
            fmap.write(str(time[i]) + ' | ' + str(mainI[i]) + ' | ' + str(mainV[i]) + ' \n ')
            print(str(time[i]) + ' | ' + str(mainI[i]) + ' | ' + str(mainV[i]))
            # text.insert('end', str(time[i])+' | '+str(mainI[i])+' | '+str(mainV[i])+' \n ')
            text.yview(tk.END)

        # закрываем файл
        text.insert('end', '--> write map \n ')
        text.yview(tk.END)
        f.close

        save_Log['state'] = tk.NORMAL


    # sawe file button
    save_Log = ttk.Button(
        root,
        text='Save Log File',
        command=save_log_file
    )
    save_Log.grid(column=1, row=2, sticky='w', padx=10, pady=10)




    root.mainloop()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
