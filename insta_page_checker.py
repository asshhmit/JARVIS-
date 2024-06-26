from tkinter import *
import instaloader


def page(nof2, nofe2):

    from tkinter import messagebox
    import instaloader
    
    root = Tk()
    root.configure(bg='black')
    root.geometry("500x250")
    root.title('INSTAGRAM PAGE CHECKER')
    font=('Areal',20)

    lable1 = Label(root, text="FOLLOWING -->", bg='black',  fg='WHITE', font = ('Areal', 20))
    lable1.place(x=50,y=110)

    label2 = Label(root, text='FOLLOWERS -->', bg = 'black', fg ='white', font=('Areal', 20) )
    label2.place(x=50, y=160)

    label3 = Label(root , text="INSTAGRAM",          bg ='black', fg = 'white', font=('Areal', 30))
    label3.place(x=125, y= 50)

    label4 = Label(root ,     text= nofe2 ,      bg = 'black', fg = 'white', font=('Areal', 20))
    label4.place(x=280, y= 110)

    label5 = Label(root ,     text= nof2 ,      bg = 'black', fg = 'white', font=('Areal', 20))
    label5.place(x=280, y= 160)
    root.mainloop()

if __name__ == '__main__':
                # Create an instance of Instaloader class
    bot = instaloader.Instaloader()

                # Provide the Instagram handle of the profile
    profile_handle = "asshhmit"

                # Load a profile from an Instagram handle
    profile = instaloader.Profile.from_username(bot.context, profile_handle)

    nof = float(profile.followers) 
    nofe = float(profile.followees)
    if nof > 0 and nof <100 and nofe > 0 and nofe < 100 :
        nof2 = nof 
                    
        page(nof, nofe)
    elif nof > 100 and nof < 1000 and nofe > 100 and nofe < 1000:
                    
        nof2 = nof 
        page(nof, nofe)
    elif nof > 1000  and nof < 10000 and  nofe > 1000 and nofe <10000:
                    
        page("{:.2f}".format(nof / 1000) + 'k', "{:.2f}".format(nofe / 1000) + 'k')

    elif nof > 10000 and nof < 10000000000000000000 and nofe > 1000 and nofe < 100000:
        page("{:.2f}".format(nof / 1000) + 'k', "{:.2f}".format(nofe / 1000) + 'k')

