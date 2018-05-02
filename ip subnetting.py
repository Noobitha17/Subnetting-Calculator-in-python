from tkinter import Tk, Label, Button, Entry, messagebox, font, Text
import ipcalc,ipaddress,netaddr
from netaddr import *
from ipaddress import *

class MyFirstGUI:
    def __init__(self, master):
        self.master = master
        master.title("A simple GUI developed by Roshan")
    #This entire codes are for the ip version 4 table
        self.t1 = Text(master,height=45, width=72, state="disabled", bg="linen")
        self.t1.place(x=10, y=32)

        self.t2=Text(master,height=50,width=45,bg="gainsboro")
        self.t2.place(x=595,y=70)

        self.l1 = Label(font="Calibre 25 bold", fg="red", pady=7, bg="linen", text="Ip Address Version4")
        self.l1.place(x=20, y=35)

        self.b1 =  Button(text="Ip Subnetting Calculator", pady=1, bg="black", font="Calibre 25 bold", fg="red",
                       activebackground="purple",padx=10)
        self.b1.place(x=580, y=0)

        self.ip_entry_label = Label(text="Enter the ip address/CIDR =>:", font="Calibre 12 bold", fg="blue", bg="white")
        self.ip_entry_label.place(x=20, y=110)

        self.ip_entry = Entry(width=16, font="Calibre 14 bold")
        self.ip_entry.place(x=270, y=110)
        self.ip_entry.insert(1, "eg 192.168.1.0/24")


        def ip_entry_clear(event):
            self.ip_entry.delete(0, 1000)

        self.ip_entry.bind("<Button-1>" and "<Button-2>" and "<Button-3>", ip_entry_clear)
        self.ip_entry.bind("<FocusIn>", ip_entry_clear)

        subnet_button = Button(text="SUBNET", fg="cyan", bg="black", font="Calibre 16 bold", padx=12, pady=3,
                                 activebackground="lawn green", activeforeground="red",command=self.ip_re )

        subnet_button.place(x=455, y=90)

        self.ip_version1 =Label(text="Ip Version  ", font="Calibre 16 bold", pady=4, bg="gold", padx=8, bd=0,fg="black")
        self.ip_version1.place(x=10, y=155)

        self.ip_version2 = Label(font="Calibre 16 bold", pady=4, bg="gold", padx=70, bd=0, fg="black")
        self.ip_version2.place(x=130, y=155)

        self.ip_version3 = Label(font="Calibre 16 bold", pady=4, bg="gold", padx=124, bd=0, fg="black")
        self.ip_version3.place(x=250, y=155)





########################################################################################################################
        # The labels for showing the entered ip
        self.ip_show1=Label(text="Entered ip", font="Calibre 16 bold", pady=4, bg="gold", padx=16, bd=0,fg="black")
        self.ip_show1.place(x=9,y=192)

        self.ip_show2 = Label(  font="Calibre 16 bold", pady=4, bg="gold", padx=70, bd=0,
                              fg="black")
        self.ip_show2.place(x=180, y=192)

        self.ip_show3 = Label(font="Calibre 16 bold", pady=4, bg="gold", padx=124, bd=0, fg="black" )
        self.ip_show3.place(x=250, y=192)
########################################################################################################################
        # The third label for total host
        self.ip_host1 = Label(text="Prefix length     ", font="Calibre 16 bold", pady=4, bg="gold", padx=16, bd=0,fg="black")
        self.ip_host1.place(x=9, y=229)

        self.ip_host2 = Label(font="Calibre 16 bold", pady=4, bg="gold", padx=70, bd=0,fg="black")
        self.ip_host2.place(x=180, y=229)

        self.ip_host3 = Label(font="Calibre 16 bold", pady=4, bg="gold", padx=144, bd=0, fg="black")
        self.ip_host3.place(x=250, y=229)


########################################################################################################################
        self.ip_totalhost1 = Label(text="Total Host    ", font="Calibre 16 bold", pady=4, bg="gold", padx=16, bd=0,fg="black")
        self.ip_totalhost1.place(x=9, y=266)

        self.ip_total2 = Label(font="Calibre 16 bold", pady=4, bg="gold", padx=80, bd=0, fg="black")
        self.ip_total2.place(x=160, y=266)

        self.ip_total3 = Label(font="Calibre 16 bold", pady=4, bg="gold", padx=105, bd=0, fg="black")
        self.ip_total3.place(x=260, y=266)

        


        #self.ip_total5 = Label(font="Calibre 16 bold", pady=4, bg="red", padx=62, bd=0, fg="black")
        #self.ip_total5.place(x=0, y=266)
####################################################################################################################
        self.ip_usehost1 = Label(text="Total Usable Host    ", font="Calibre 16 bold", pady=4, bg="gold", padx=16, bd=0,
                                   fg="black")
        self.ip_usehost1.place(x=9, y=303)

        self.ip_usehost2 = Label(font="Calibre 16 bold", pady=4, bg="gold", padx=50, bd=0, fg="black")
        self.ip_usehost2.place(x=230, y=303)

        self.ip_usehost3 = Label(font="Calibre 16 bold", pady=4, bg="gold", padx=65, bd=0, fg="black")
        self.ip_usehost3.place(x=330, y=303)


####################################################################################################################

        self.ip_hostrange1 = Label(text="Usable Host \n    Range  ", font="Calibre 16 bold", pady=9, bg="gold", padx=16, bd=0,
                                 fg="black")
        self.ip_hostrange1.place(x=9, y=341)

        self.ip_hostrange2 = Label(font="Calibre 16 bold", pady=6, bg="gold", padx=75, bd=0, fg="black")
        self.ip_hostrange2.place(x=270, y=341)

        self.ip_hostrange3 = Label(font="Calibre 16 bold", pady=6, bg="gold", padx=75, bd=0, fg="black")
        self.ip_hostrange3.place(x=270, y=371)


        self.ip_hostrange4 = Label(font="Calibre 16 bold", pady=20.8, bg="gold", padx=71, bd=0, fg="black")
        self.ip_hostrange4.place(x=165, y=341)

        ########################################################################################################
        self.subnet_mask1=Label(text="Subnet Mask:",font="Calibre 16 bold", pady=9, bg="gold", padx=16, bd=0,
                                 fg="black")
        self.subnet_mask1.place(x=9,y=411)

        self.subnet_mask2 = Label(  font="Calibre 16 bold", pady=9, bg="gold", padx=16, bd=0,
                                  fg="black")
        self.subnet_mask2.place(x=177, y=411)

        self.subnet_mask3 = Label(font="Calibre 16 bold", pady=9, bg="gold", padx=132, bd=0,
                                  fg="black")
        self.subnet_mask3.place(x=207, y=411)
        #################################################################################################
        self.broadcast_id1 = Label(text="Broadcast id:", font="Calibre 16 bold", pady=9, bg="gold", padx=16, bd=0,
                                  fg="black")
        self.broadcast_id1.place(x=9, y=457)

        self.broadcast_id2 = Label(font="Calibre 16 bold", pady=9, bg="gold", padx=16, bd=0,
                                  fg="black")
        self.broadcast_id2.place(x=176, y=457)

        self.broadcast_id3 = Label(font="Calibre 16 bold", pady=9, bg="gold", padx=132, bd=0,
                                  fg="black")
        self.broadcast_id3.place(x=207, y=457)

#############################################################################################

        self.wildcardmask_1 = Label(text="Wildcard Mask:", font="Calibre 16 bold", pady=9, bg="gold", padx=16, bd=0,
                                   fg="black")
        self.wildcardmask_1.place(x=9, y=503)

        self.wildcardmask_2 = Label(font="Calibre 16 bold", pady=9, bg="gold", padx=16, bd=0,
                                   fg="black")
        self.wildcardmask_2.place(x=185, y=503)

        self.wildcardmask_3 = Label(font="Calibre 16 bold", pady=9, bg="gold", padx=130, bd=0,
                                   fg="black")
        self.wildcardmask_3.place(x=211, y=503)

##############################################################################################

        self.ip_class1=Label(text="Ip Class:",font="Calibre 16 bold", pady=9, bg="gold", padx=16, bd=0,
                                   fg="black")
        self.ip_class1.place(x=9,y=549)

        self.ip_class2=Label( font="Calibre 16 bold", pady=9, bg="gold", padx=90, bd=0,
                                   fg="black")
        self.ip_class2.place(x=125,y=549)

        self.ip_class3 = Label(font="Calibre 16 bold", pady=9, bg="gold", padx=90, bd=0,
                              fg="black")
        self.ip_class3.place(x=305, y=549)



    #################################################################################################
        self.ip_type1=Label(text="Ip Type:",font="Calibre 16 bold", pady=9, bg="gold", padx=16, bd=0,
                                   fg="black")
        self.ip_type1.place(x=9,y=594)

        self.ip_type2=Label(font="Calibre 16 bold", pady=9, bg="gold", padx=90, bd=0,fg="black"
                            )
        self.ip_type2.place(x=120,y=594)



        self.ip_type3=Label(font="Calibre 16 bold", pady=9, bg="gold", padx=90, bd=0, fg="black"
                              )
        self.ip_type3.place(x=211,y=594)

        self.ip_type4=Label(font="Calibre 16 bold", pady=9, bg="gold", padx=90, bd=0, fg="black")
        self.ip_type4.place(x=340,y=594)
        ##################################################################################################

        self.ipv4_label_clear=Label(font="Calibre 16 bold", pady=9, bg="white", padx=15, bd=0, fg="blue",text='To Clear the field click here   ==> ')
        self.ipv4_label_clear.place(x=11,y=709)


        self.b6=Button(text="Clear Fields",command=self.clear,bg='black',fg='cyan',font="Calibre 15 bold",pady=5,padx=15,activebackground="lawn green", activeforeground="red")
        self.b6.place(x=429,y=701)

        ####################################################################################################

#Integer entering
        self.binary1 = Label(text="BINARY CONVERTER", bg="red", fg="lawn green", font="Calibre 19 bold", pady=5,
                             padx=49)
        self.binary1.place(x=596, y=70)

        self.binary2=Label(text="Enter Integer =>", bg="gainsboro", fg="blue", font="Calibre 15 bold", pady=3)
        self.binary2.place(x=596,y=120)

        self.binary3 = Entry( font="Calibre 12 bold",width=10 )
        self.binary3.place(x=758, y=124)

        self.binary4 = Button(font="Calibre 12 bold", width=8,text="get binary",bg="black",fg="red",
                              command=self.int_to_binary)
        self.binary4.place(x=863, y=120)
# Binary entering
        self.binary5 = Label(text="Enter Binary=>", bg="gainsboro", fg="blue", font="Calibre 15 bold", pady=3)
        self.binary5.place(x=596, y=160)

        self.binary6 = Entry(font="Calibre 13 bold", width=11)
        self.binary6.place(x=750, y=163)


        self.binary7 = Button(font="Calibre 12 bold", width=8,text="get integer",bg="black",fg="red",command=self.bin_to_int)
        self.binary7.place(x=863, y=161)

        self.binary8 = Label(text="Enter Integer =>", bg="gainsboro", fg="blue", font="Calibre 15 bold", pady=3)
        self.binary8.place(x=596, y=120)


        self.binary_label_1 = Label( bg="gold", fg="red", font="Calibre 19 bold", pady=5,
                             padx=80)
        self.binary_label_1.place(x=596, y=200)

        self.label_clear=Button(text="C",bg="black",fg="red",pady=1,padx=10,font="Calibre 16 bold",command=self.label_clear)
        self.label_clear.place(x=596,y=200)
#################################
        self.route_summarize_title=Label(text="Route Summarization", bg="red", fg="lawn green", font="Calibre 19 bold", pady=4,
                             padx=49)
        self.route_summarize_title.place(x=596,y=245)

        self.route_summarize1 = Label(text="Lowest ip => ", bg="gainsboro", fg="blue", font="Calibre 15 bold", pady=3)
        self.route_summarize1.place(x=600, y=290)

        self.route_summarize2 = Entry(font="Calibre 15 bold", width=19)
        self.route_summarize2.place(x=730, y=295)

        self.route_summarize3=Label(text="Highest ip => ", bg="gainsboro", fg="blue", font="Calibre 15 bold", pady=3)
        self.route_summarize3.place(x=600,y=330)

        self.route_summarize4=Entry(font="Calibre 15 bold", width=19)
        self.route_summarize4.place(x=730, y=335)



        self.summarize_label=Label( bg="gold", fg="red", font="Calibre 16 bold", pady=5,
                             padx=50)
        self.summarize_label.place(x=658,y=370)

        self.route_summarize_button = Button(font="Calibre 12 bold", width=8, text="Summarize", bg="black", fg="red",pady=4,padx=5
                                             ,command=self.summarizing_route)
        self.route_summarize_button.place(x=595, y=370)

        self.summarize_clear=Button(text="C",bg="black",fg="red",pady=0,padx=2,font="Calibre 16 bold",command=self.clear_route_summarize)
        self.summarize_clear.place(x=920,y=408)

    def summarizing_route(self):
        try:
            self.route1=[]
            self.route2=self.route1.append(IPNetwork( self.route_summarize2.get()))
            self.route3=self.route1.append(IPNetwork(self.route_summarize4.get()))
            self.route4=str(cidr_merge(self.route1)).replace('[IPNetwork(','')
            self.route5=str(self.route4).replace(')]','')
            self.summarize_label.config(text=self.route5)
        except Exception as e:
            print()


    def clear_route_summarize(self):
        self.route_summarize2.delete(0,100000000)
        self.route_summarize4.delete(0,100000000)
        self.summarize_label.config(text="")


    def label_clear(self):
        self.binary_label_1.config(text="")
        self.binary6.delete(0,10000)
        self.binary3.delete( 0,10000)
    def int_to_binary(self):
        try:
            self.int_to_bin1= self.binary3.get()
            self.int_to_bin2=bin(int(self.int_to_bin1))
            self.int_to_bin3=self.int_to_bin2[2:]
            self.int_to_bin4=str(self.int_to_bin3).rjust(8,"0")
            self.binary_label_1.config(text="")
            self.int_to_bin5=str( self.int_to_bin1 ) +str("  =  ")+  str(  self.int_to_bin4)
            self.binary_label_1.config(text=  self.int_to_bin5)
        except Exception as e:
            print(e)

    def bin_to_int(self):
        try:
            self.bin_to_int1=self.binary6.get()
            self.bin_to_int2=str( self.bin_to_int1)
            self.bin_to_int3=int(self.bin_to_int2,2)
            self.binary_label_1.config(text="")
            self.bin_to_int4=str(self.bin_to_int1) +str("=") +str(self.bin_to_int3)
            self.binary_label_1.config(text=self.bin_to_int4)
        except Exception as e:
            print(e)








    def ip_re(self):
        try:
            self.a1=ipaddress.IPv4Interface(self.ip_entry.get())
            self.a2=self.a1.ip
            a3=str(self.a2.version) +str("    (32 bits)")
            self.ip_version3.config(text=a3)

    # The code for the second row
            self.ip_show3.config(text=self.a2)
    # The code is for the third row
            self.c1=IPNetwork(self.ip_entry.get())
            self.ip_host3.config(text=self.c1.prefixlen)


#This code is for the fourth row
            self.d1= self.ip_entry.get()
            self.d2=IPNetwork(self.d1)
            self.ip_total3.config(text=self.d2.size)
#This code is for the fifth row
            self.e1=self.d2.size-2
            self.ip_usehost3.config(text=self.e1)

#####################################################################
            self.f1=IPNetwork(self.ip_entry.get())
            self.f2=list(self.f1)
            self.f3=str(" From  ")+str((self.f2[1]))
            self.f4=str("To ")+      str((self.f2[-2]))
            self.ip_hostrange2.config(text=self.f3)
            self.ip_hostrange3.config(text=self.f4)

###########################################################################
            self.g1=IPNetwork(self.ip_entry.get())
            self.g2=self.g1.netmask
            self.subnet_mask3.config(text=self.g2)
#################################################################################
            self.i2=self.g1.broadcast
            self.broadcast_id3.config(text=self.i2)






#########################################################################################
            self.j1=self.g1.hostmask
            self.wildcardmask_3.config(text=self.j1)

###########################################################################################
            if str(self.a1) > "0" and str(self.a1) <= "127":
                self.ip_class3.config(text="A")
            if str(self.a1) > "128" and str(self.a1) <= "173":
                self.ip_class3.config(text="B")
            if str(self.a1) > "173" and str(self.a1) <= "193":
                self.ip_class3.config(text="C")
###########################################################################################
            ip_type5=self.a1
            if self.a1.is_reserved:
                self.ip_type4.config(text="Reserved")
            if self.a1.is_private:
                self.ip_type4.config(text="Private")
            if self.a1.is_loopback:
                self.ip_type4.config(text="loopback")
            if self.a1.is_global:
                self.ip_type4.config(text="Public")
            if self.a1.is_unspecified:
                self.ip_type4.config(text="Unspecified")

#######################################################################################


        except Exception as e:
            print(e)


    def clear(self):
        self.ip_version3.config(text="")
        self.ip_show3.config(text="")
        self.ip_host3.config(text="")
        self.ip_total3.config(text="")

        self.ip_usehost3.config(text="")
        self.ip_hostrange2.config(text="")
        self.ip_hostrange3.config(text="")
        self.subnet_mask3.config(text="")
        self.broadcast_id3.config(text="")
        self.wildcardmask_3.config(text="")
        self.ip_class3.config(text="")
        self.ip_type4.config(text="")
        #This code is for the binary conversion text and route summarization






root = Tk()
my_gui = MyFirstGUI(root)
root.config(bg="cyan")
root.mainloop()

