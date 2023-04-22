
class Ticket:
    counter_id = 2000  # Ticket counter generated for assigning the ticket
    tktlist = []            # Ticket list created


    def __init__(self, ID, TKTcreatorf_name, TKTcreatorl_name, contact_eml, TKTissue_description):   #constructor method of a class is created using arguments- ID, Tkt_creatordetail, contact_email, TKTissue_description
        self.tkt_num = Ticket.counter_id + 1
        self.ID = ID
        self.TKTcreatorf_name = TKTcreatorf_name
        self.TKTcreatorl_name = TKTcreatorl_name
        self.contact_eml = contact_eml
        self.TKTissue_description = TKTissue_description
        self.tkt_sts = "Open"
        self.tkt_rspns = "No response given"
        Ticket.counter_id += 1
        Ticket.tktlist.append(self)
    

    def give_tkt_rspns(self, tkt_rspns):                       # ticket response function is defined.
        self.tkt_rspns = tkt_rspns
 

    def open_ticket(self):                                          # ticket status function is defined.
        self.tkt_sts = "open ticket" 


    def tkt_resolved (self):                                          # ticket resolved function is defined.
        self.tkt_sts = "Closed"   


def tkt_statistics_detail():                              #ticket statistics detail is created here.
        for t in Ticket.tktlist:
            total_tkt_crtd = len(t.tktlist)
            total_tkt_rslvd = 0          
            if t.tkt_sts == "Closed":
                total_tkt_rslvd += 1  
            tkt_to_be_rslvd = 0
            if t.tkt_sts != "Closed":
                tkt_to_be_rslvd += 1 
        print(f'\nTotal number of tickets are: {total_tkt_crtd}')
        print(f'Total number of tickets resolved: {total_tkt_rslvd}')  
        print(f'Total number of be resolved: {tkt_to_be_rslvd}')   

                     
def print_menu():
    while True:
        
        print("\n=====Helpdesk Ticketing System Program =====")                    # Menu is created for the helpdesk system.
        print("1. Generate New ticket")
        print("2. Give your response to the ticket")
        print("3. Update and submit the ticket")
        print("4. See ticket stats")
        print("5. View all tickets")
        print("6. End the program and exit")
        print("=============================")

        option = input("\nEnter from one of the options: ")

        if option == "1":                                                                             # New ticket generated with all the details
            ID = input('Input staff ID: ')
            TKTcreatorf_name = input('Input ticket creator first name: ')
            TKTcreatorl_name = input('Input ticket creator last name: ')
            contact_eml = input('Enter contact email: ')
            TKTissue_description = input('Enter issue description in detail: ')

            t = Ticket(ID, TKTcreatorf_name, TKTcreatorl_name, contact_eml, TKTissue_description)  
            desc = str.lower(TKTissue_description)
            index = desc.find("change password")
            if index != -1: 
                if len(TKTcreatorf_name) > 2 and len(ID) > 1:    
                    password = ID[0:2] + TKTcreatorf_name[0:3]                                             # New password logic is created here, where it will automatically gets 2 words from staff ID and 3 words from creator name.
                else:
                    password="USHDHJHD"
                t.tkt_rspns = "New generated password is :", password
                print(t.tkt_rspns)
            else:    
             print(f'Ticket {t.tkt_num} is generated.') 
                   
        elif option == "2":                                                                           # Response is added to the ticket
            tkt_num = int(input("Please input your ticket number here:"))
            tkt_rspns= input('Input your response: ')
            ticket = False
            for t in Ticket.tktlist:
                if t.tkt_num == tkt_num:
                   t.give_tkt_rspns(tkt_rspns)
                   print(f'your ticket {tkt_num} is updated.')
                   ticket = True
                   break   
            if not ticket:    
                print(f"Ticket {tkt_num} not found.") 
                           
        elif option == "3":                                                                           # Ticket is updated and resolved.
            tkt_num = int(input("Please input your ticket number here:"))
            ticket = False
            for t in Ticket.tktlist:
                if t.tkt_num == tkt_num:
                    t.tkt_resolved()
                    print(f'Your ticket {tkt_num} is resolved.')
                    ticket = True
                    break   
            if not ticket:    
                print(f"Ticket {tkt_num} not found.")  

        elif option == "4":                                                                           #ticket statistic is generated in which ticket generated count, ticket resolved count and ticket to be resolved count will be shown.
            tkt_statistics_detail() 
                            
        elif option == "5":                           # here all the tickets will be viewed with all the details
            print("-----------------------------")
            print ("\nTicket Number:", t.tkt_num)
            print("Staff ID is:", t.ID)
            print("Ticket creator full name is:", t.TKTcreatorf_name  + " " + t.TKTcreatorl_name) 
            print("Contact email address is:", t.contact_eml)
            print("Issue description is:", t.TKTissue_description)
            print("Ticket response:",t.tkt_rspns )
            print("Ticket status:", t.tkt_sts)
            print("-----------------------------")

        elif option == "6":                                                                            # Program ends here.
            print('Program ends here... Thanks')
            exit()  
            break

        else:
            print('Invalid choice. Please try again.')                  # if selecting wrong option, then this error will be displayed.


print_menu()

