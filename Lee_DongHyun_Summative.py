############################################################################################################################################################
# Name: Dong Hyun Lee
# Course: ICS3U
# File: Lee_DongHyun_Summative
# Description:
# This program is Invoice
############################################################################################################################################################

############################################################################################################################################################
# FNC NAME: shipping
# DESCRIPTION: determine the shipping method
# INPUTS:
#   method - the method of the shipping
# OUTPUTS:
#   X (X is the cost of the shipping method)
# ALGORITHM:
#   IF method EUQAL "PC\n"
#       RETURN 35.00
#   ELIF method EQUAL "XP\n"
#       RETURN 20.00
#   ELIF method EQUAL "RP\n"
#       RETURN 10.00
# HISTORY:
# 2015.05.26   Creation
############################################################################################################################################################

def shipping(method):
    if method == "PC\n":
        return 35.00
    elif method == "XP\n":
        return 20.00
    elif method == "RP\n":
        return 10.00
#END shipping()

############################################################################################################################################################
# FNC NAME: provinceTax
# DESCRIPTION: determine the tax for each province
# INPUTS:
#   province - the name of the province
# OUTPUTS:
#   X (X is the tax rate in the province)
# ALGORITHM:
#   IF province EQUAL "BC" OR province EQUAL "MB"
#       RETURN 0.07
#   ELIF province EQUAL "AB"
#       RETURN 0.00
#   ELIF province EQUAL "SK"
#       RETURN 0.05
#   ELIF province EQUAL "PE"
#       RETURN 0.10
#   ELIF province EQUAL "ON" OR province EQUAL "NB" OR province EQUAL "NS" OR province EQUAL "NL"
#       RETURN 0.13
#   ELIF province EQUAL "QC"
#       RETURN 0.075
# HISTORY:
# 2015.05.29    Creation
############################################################################################################################################################

def provinceTax(province):
    if (province == "BC") or (province == "MB"):
        return 0.07
    elif (province == "AB"):
        return 0.00
    elif (province == "SK"):
        return 0.05
    elif (province == "PE"):
        return 0.10
    elif (province == "ON") or (province == "NB") or (province == "NS") or (province == "NL"):
        return 0.13
    elif (province == "QC"):
        return 0.075
#END provinceTax()
    

############################################################################################################################################################
# INPUTS:
#   invFile - input file named "Level4InvoiceInformation.txt"
#
# OUTPUTS:
#
#
#          C A N T E R B U R Y    B O O K S    L T D .
#          2346 Industial Ave, Burlington, On L7S 2W1
#                        (905)-673-2596
#
#
#   Invoice Number                              Invoice Date
#   --------------                              ------------
#   A                                           B               (A is invoice number, B is invoice date)
#
#
#   SOLD TO:    C (C is customer name)
#               D (D is customer street)
#               E (E is customer city, province)
#               F (F is customer postal code)
#
#
#       Item Description                        Quantity Unit Price     Total
#       --------------------------------------- -------- ----------   --------
#       G                                              H          I          J (G is item description, H is quantity, I is unic price, j is H * I)
#       .                                              .          .          .
#       .                                              .          .          .
#       .                                              .          .          .
#
#                                                         Shipping:          K (K is shipping price)
#                                                                     --------  
#                                                         Subtotal:          L (L is Js + K)
#
#                                                              GST:          M (M is L * 0.05)
#                                                              PST:          N (N is L * provinceTax)
#                                                                     ========
#                                                            Total:          O (O is L + M + N)
#
#
#   outFile - output file named "CanterburyBooksLtdInvoice.txt" with all of the results printed
#
# ALGORITHM:
#   info1 EQUAL []
#   info2 EQUAL []
#   startForm1 EQUAL FALSE
#   startForm2 EQUAL FALSE
#   startForm3 EQUAL FALSE
#   outFile EQUAL OPEN "CanterburyBooksLtdInvoice.txt" as WRITE
#
#   invFile EQUAL OPEN "Level4InvoiceInformation.txt" as READ
#
#   FOR line IN invFile
#       val EQUAL line.SPLIT(":")
#       IF val EQUAL ["H\n"]
#           info1 EQUAL []
#           startForm1 EQUAL TRUE
#       ELIF val EQUAL ["D\n"]
#           info2 EQUAL []
#           startForm2 EQUAL TRUE
#       IF startForm1
#           IF startForm3
#
#               PUT shipping(shippingMethod)
#               PUT "--------"
#               PUT subTotal (subTotal EQUAL subTotal + shipping(shippingMethod))
#
#               PUT shippintMethod TO outFile
#               PUT "--------" TO outFile
#               PUT subTotal TO outFile (subTotal EQUAL subTotal + shipping(shippingMethod))
#
#               subTotal EQUAL subTotal PLUS shipping(shippingMethod)
#               tax EQUAL provinceTax(userProvince)
#
#               IF userProvince EQUAL "BC" OR userProvince EQUAL "AB" OR userProvince EQUAL "SK" OR userProvince EQUAL "MB"
#                   GST EQUAL subTotal TIMES 0.05
#                   PST EQUAL subTotal TIMES tax
#                   finalTotal EQUAL subTotal PLUS GST PLUS PST
#
#                   PUT GST
#                   PUT PST
#                   PUT "========"
#                   PUT finalTotal
#
#                   PUT GST TO outFile
#                   PUT PST TO outFile
#                   PUT "========" TO outFile
#                   PUT finalTotal TO outFile
#
#               ELIF userProvince EQUAL "ON" OR userProvince EQUAL "NB" OR userProvince EQUAL "NS" OR userProvince EQUAL "NL"
#                   HST EQUAL subTotal TIMES tax
#                   finalTotal EQUAL subTotal PLUS HST
#
#                   PUT HST
#                   PUT "========"
#                   PUT finalTotal
#
#                   PUT HST TO outFile
#                   PUT "========" TO outFile
#                   PUT finalTotal TO outFile
#
#                   ELIF userProvince EQUAL "QC"
#                       GST EQUAL subTotal TIMES 0.05
#                       QST EQUAL subTotal TIMES 1.05 TIMES tax
#                       finalTotal EQUAL subTotal PLUS GST PLUS QST
#
#                       PUT GST
#                       PUT subTotal (subTotal EQUAL subTotla TIMES 1.05)
#                       PUT QST
#                       PUT "========"
#                       PUT finalTotal
#
#                       PUT GST TO outFile
#                       PUT subTotal (subTotal EQUAL subTotla TIMES 1.05) TO outFile
#                       PUT QST TO outFile
#                       PUT "========" TO outFile
#                       PUT finalTotal TO outFile
#
#                   ELIF userProvince EQUAL "PE"
#                       GST EQUAL subTotal TIMES 0.05
#                       PST EQUAL subTotal TIMES 1.05 TIMES tax
#                       finalTotal EQUAL subtotal PLUS GST PLUS PST
#
#                       PUT GST
#                       PUT subTotal (subTotal EQUAL subTotla TIMES 1.05)
#                       PUT PST
#                       PUT "========"
#                       PUT finalTotal
#
#                       PUT GST TO outFile
#                       PUT subTotal (subTotal EQUAL subTotla TIMES 1.05) TO outFile
#                       PUT PST TO outFile
#                       PUT "========" TO outFile
#                       PUT finalTotal TO outFile
#
#                   startForm3 EQUAL FALSE
#                   finalTotal EQUAL 0
#
#
#           IF NOT startForm2
#               info1.APPEND(val)
#
#           IF NOT info1 EQUAL [["H\n"]]
#               userAccNum EQUAL info1[1][0]
#               userName EQUAL info1[1][1]
#               userStreet EQUAL info1[1][2]
#               userCity EQUAL info1[1][3]
#               userProvince EQUAL info1[1][4]
#               userPostalCode EQUAL info1[1][5]
#               userInvDate EQUAL info1[1][6]
#               userInvNum EQUAL info1[1][7]
#               shippingMethod EQUAL info1[1][8]
#
#               PUT "C A N T E R B U R Y    B O O K S    L T D ."
#               PUT "2346 Industrial Ave, Burlington, ON L7S 2W1"
#               PUT "(905)-673-2596"
#               PUT "Invoice Number","Invoice Date"
#               PUT "--------------", "------------"
#               PUT userInvNum,userInvDate
#               PUT "SOLD TO:  userName,userStreet,userCity,userProvince,userPostalCode"
#               PUT "Item Description                         Quantity Unit Price     Total"
#               PUT "-"*40,"-"*8,"-"*10,"  --------"
#
#               PUT "C A N T E R B U R Y    B O O K S    L T D ." TO outFile
#               PUT "2346 Industrial Ave, Burlington, ON L7S 2W1" TO outFile
#               PUT "(905)-673-2596" TO outFile
#               PUT "Invoice Number", "Invoice Date" TO outFile
#               PUT "--------------", "------------" TO outFile
#               PUT userInvNum,userInvDate TO outFile
#               PUT "SOLD TO:  userName,userStreet,userCity,userProvince,userPostalCode" TO outFile
#               PUT "Item Description", "Quantity Unit Price", "Total" TO outFile
#               PUT "-"*40,"-"*8,"-"*10,"  --------" TO outFile
#
#               tax EQUAL provinceTax(userProvince)
#               startForm3 EQUAL TRUE
#               subTotal EQUAL 0
#               startForm1 EQUAL FALSE
#                   
#           ELIF startForm2
#           IF NOT startForm1
#               info2.APPEND(val)
#
#           IF NOT info2 EQUAL [["D\n"]]
#               itemNum EQUAL info2[1][0]
#               itemDescription EQUAL info2[1][1]
#               quantity EQUAL info2[1][2]
#               price EQUAL info2[1][3]
#               total EQUAL quantity TIMES price
#
#               PUT itemDescription,quantity,price,total
#
#               PUT itemDescription,quantity,price,total TO outFile
#
#               subTotal EQUAL subTotal PLUS total
#               startForm2 EQUAL FALSE
#                   
#       PUT shipping(shippingMethod)
#       PUT "--------"
#       PUT subTotal (subTotal EQUAL subTotal PLUS shipping(shippingMethod))
#
#       PUT shipping(shippingMethod) TO outFile
#       PUT "--------" TO outFile
#       PUT subTotal (subTotal EQUAL subTotal PLUS shipping(shippingMethod)) TO outFile
#
#       subTotal EQUAL subTotal PLUS shipping(shippingMethod)
#       tax EQUAL provinceTax(userProvince)
#       
#       IF userProvince EQUAL "BC" OR userProvince EQUAL "AB" OR userProvince EQUAL "SK" OR userProvince EQUAL "MB"
#           GST EQUAL subTotal TIMES 0.05
#           PST EQUAL subTotal TIMES tax
#           finalTotal EQUAL subTotal PLUS GST PLUS PST
#
#           PUT GST
#           PUT PST
#           PUT "========"
#           PUT finalTotal
#
#           PUT GST TO outFile
#           PUT PST TO outFile
#           PUT "========" TO outFile
#           PUT finalTotal TO outFile
#           
#       ELIF userProvince EQUAL "ON" OR userProvince EQUAL "NB" OR userProvince EQUAL "NS" OR userProvince EQUAL "NL"
#           HST EQUAL subTotal TIMES tax
#           finalTotal EQUAL subTotal PLUS HST
#           PUT HST
#           PUT "========"
#           PUT finalTotal
#
#           PUT HST TO outFile
#           PUT "========" TO outFile
#           PUT finalTotal TO outFile
#           
#       ELIF userProvince EQUAL "QC"
#           GST EQUAL subTotal TIMES 0.05
#           QST EQUAL subTotal TIMES 1.05 TIMES tax
#           finalTotal EQUAL subTotal PLUS GST PLUS QST
#
#           PUT GST
#           PUT subTotal (subTotal EQUAL subTotal TIMES 1.05)
#           PUT QST
#           PUT "========"
#           PUT finalTotal
#
#           PUT GST TO outFile
#           PUT subTotal (subTotal EQUAL subTotal TIMES 1.05) TO outFile
#           PUT QST TO outFile
#           PUT "========" TO outFile
#           PUT finalTotal TO outFile
#           
#       ELIF userProvince EQUAL "PE"
#           GST EQUAL subTotal TIMES 0.05
#           PST EQUAL subTotal TIMES 1.05 TIMES tax
#           finalTotal EQUAL subtotal PLUS GST PLUS PST
#
#           PUT GST
#           PUT subTotal (subTotal EQUAL subTotal TIMES 1.05)
#           PUT PST
#           PUT "========"
#           PUT finalTotal
#
#           PUT GST TO outFile
#           PUT subTotal (subTotal EQUAL subTotal TIMES 1.05) TO outFile
#           PUT PST TO outFile
#           PUT "========" TO outFile
#           PUT finalTotal TO outFile
#
#       CLOSE invFile
#   CLOSE outFile
#
# History:
# 2015.05.25    Creation (shipping)
# 2015.05.26    Edition
# 2015.05.27    Edition
# 2015.05.28    Edition
# 2015.05.29    Edition (provinces)
# 2015.06.01    Edition (writing)
# 2015.06.02    Edition (writing)
# 2015.06.03    Edition (algorithm)
# 2015.06.04    Edition (algorithm)
# 2015.06.15    Edition (algorithm)
############################################################################################################################################################

#main
info1 = []
info2 = []
startForm1 = False
startForm2 = False
startForm3 = False

#open as write mode
outFile = open("CanterburyBooksLtdInvoice.txt","w")

#Try...except
try:
    #open as read mode
    invFile = open("Level4InvoiceInformation.txt", "r")

except IOError,e:
    print "Failed to open %s for reading: %s" %("Level4InvoiceInformation.txt",e)
    
else:
    #For statement - reading
    for line in invFile:
        val = line.split(":")
        
        #If statement
        if val == ["H\n"]:
            info1 = []
            startForm1 = True
        elif val == ["D\n"]:
            info2 = []
            startForm2 = True
        #ENDIF

        #If statement
        if startForm1:
            
            #If statement
            if startForm3 == True:
                
                #shipping and subtotal
                print
                print " "*50,"Shipping: %10.2f" %(shipping(shippingMethod))
                print "%71s" %("--------")
                print " "*50,"Subtotal: %10.2f" %(subTotal + shipping(shippingMethod))
                print
                
                #writing
                outFile.write("\n")
                outFile.write(" "*50)
                outFile.write(" ")
                outFile.write("Shipping: %10.2f" %(shipping(shippingMethod)))
                outFile.write("\n")
                outFile.write("%71s" %("--------"))
                outFile.write("\n")
                outFile.write(" "*50)
                outFile.write(" ")
                outFile.write("Subtotal: %10.2f" %(subTotal + shipping(shippingMethod)))
                outFile.write("\n")
                outFile.write("\n")
                
                subTotal += shipping(shippingMethod)
                tax = provinceTax(userProvince)

                #If statement
                if (userProvince == "BC") or (userProvince == "AB") or (userProvince == "SK") or (userProvince == "MB"): #BC or AB or SK or MB
                    GST = subTotal*0.05
                    PST = subTotal*tax
                    finalTotal = subTotal + GST + PST
                    
                    #tax and final total
                    print " "*55,"GST: %10.2f" %(GST)
                    print " "*55,"PST: %10.2f" %(PST)
                    print "%71s" %("========")
                    print " "*53,"Total: %10.2f" %(finalTotal)

                    #writing
                    outFile.write(" "*55)
                    outFile.write(" ")
                    outFile.write("GST: %10.2f" %(GST))
                    outFile.write("\n")
                    outFile.write(" "*55)
                    outFile.write(" ")
                    outFile.write("PST: %10.2f" %(PST))
                    outFile.write("\n")
                    outFile.write("%71s" %("========"))
                    outFile.write("\n")
                    outFile.write(" "*53)
                    outFile.write(" ")
                    outFile.write("Total: %10.2f" %(finalTotal))
                    outFile.write("\n")
                    
                elif (userProvince == "ON") or (userProvince == "NB") or (userProvince == "NS") or (userProvince == "NL"): #ON or NB or NS or NL
                    HST = subTotal*tax
                    finalTotal = subTotal + HST

                    #tax and final total
                    print " "*55,"HST: %10.2f" %(HST)
                    print "%71s" %("========")
                    print " "*53,"Total: %10.2f" %(finalTotal)

                    #writing
                    outFile.write(" "*55)
                    outFile.write(" ")
                    outFile.write("HST: %10.2f" %(HST))
                    outFile.write("\n")
                    outFile.write("%71s" %("========"))
                    outFile.write("\n")
                    outFile.write(" "*53)
                    outFile.write(" ")
                    outFile.write("Total: %10.2f" %(finalTotal))
                    outFile.write("\n")
                    
                elif (userProvince == "QC"): #QC
                    GST = subTotal*0.05
                    QST = subTotal*1.05*tax
                    finalTotal = subTotal + GST + QST

                    #tax and final total
                    print " "*55,"GST: %10.2f" %(GST)
                    print " "*50,"Subtotal: %10.2f" %(subTotal*1.05)
                    print " "*55,"QST: %10.2f" %(QST)
                    print "%71s" %("========")
                    print " "*53,"Total: %10.2f" %(finalTotal)

                    #writing
                    outFile.write(" "*55)
                    outFile.write(" ")
                    outFile.write("GST: %10.2f" %(GST))
                    outFile.write("\n")
                    outFile.write(" "*50)
                    outFile.write(" ")
                    outfile.write("Subtotal: %10.2f" %(subTotal*1.05))
                    outFile.write("\n")
                    outFile.write(" "*55)
                    outFile.write(" ")
                    outfile.write("QST: %10.2f" %(QST))
                    outFile.write("\n")
                    outFile.write("%71s" %("========"))
                    outFile.write("\n")
                    outFile.write(" "*53)
                    outFile.write(" ")
                    outfile.write("Total: %10.2f" %(finalTotal))
                    outFile.write("\n")
                    
                elif (userProvince == "PE"): #PE
                    GST = subTotal*0.05
                    PST = subTotal*1.05*tax
                    finalTotal = subtotal + GST + PST

                    #tax and final total
                    print " "*55,"GST: %10.2f" %(GST)
                    print " "*50,"Subtotal: %10.2f" %(subTotal*1.05)
                    print " "*55,"PST: %10.2f" %(PST)
                    print "%71s" %("========")
                    print " "*53,"Total: %10.2f" %(finalTotal)

                    #writing
                    outFile.write(" "*55)
                    outFile.write(" ")
                    outFile.write("GST: %10.2f" %(GST))
                    outFile.write("\n")
                    outFile.write(" "*50)
                    outFile.write(" ")
                    outFile.write("Subtotal: %10.2f" %(subTotal*1.05))
                    outFile.write("\n")
                    outFile.write(" "*55)
                    outFile.write(" ")
                    outFile.write("PST: %10.2f" %(PST))
                    outFile.write("\n")
                    outFile.write("%71s" %("========"))
                    outFile.write("\n")
                    outFile.write(" "*53)
                    outFile.write(" ")
                    outFile.write("Total: %10.2f" %(finalTotal))
                    outFile.write("\n")
                #ENDIF
                    
                startForm3 = False
                finalTotal = 0
            #ENDIF

            #If statement    
            if not startForm2:
                info1.append(val)
            #ENDIF

            #If statement    
            if not(info1 == [["H\n"]]):
                userAccNum = info1[1][0]
                userName = info1[1][1]
                userStreet = info1[1][2]
                userCity = info1[1][3]
                userProvince = info1[1][4]
                userPostalCode = info1[1][5]
                userInvDate = info1[1][6]
                userInvNum = info1[1][7]
                shippingMethod = info1[1][8]

                #Heading
                print
                print
                print "%60s" %"C A N T E R B U R Y    B O O K S    L T D ."
                print "%60s" %"2346 Industrial Ave, Burlington, ON L7S 2W1"
                print "\t\t\t\t(905)-673-2596\n\n"
                print "%-40s %s" %("Invoice Number", "Invoice Date")
                print "%-40s %s" %("--------------", "------------")
                print "%-40s %s\n\n" %(userInvNum,userInvDate)
                print "SOLD TO:  %s\n\t  %s\n\t  %s, %s\n\t  %s\n\n" %(userName,userStreet,userCity,userProvince,userPostalCode)
                print "Item Description                         Quantity Unit Price     Total"
                print "-"*40,"-"*8,"-"*10,"  --------"

                #Writing
                outFile.write("\n")
                outFile.write("\n")
                outFile.write("\n")
                outFile.write("%60s" %"C A N T E R B U R Y    B O O K S    L T D .")
                outFile.write("\n")
                outFile.write("%60s" %"2346 Industrial Ave, Burlington, ON L7S 2W1")
                outFile.write("\n")
                outFile.write("\t\t\t\t(905)-673-2596\n\n")
                outFile.write("\n")
                outFile.write("%-40s %s" %("Invoice Number", "Invoice Date"))
                outFile.write("\n")
                outFile.write("%-40s %s" %("--------------", "------------"))
                outFile.write("\n")
                outFile.write("%-40s %s\n\n" %(userInvNum,userInvDate))
                outFile.write("\n")
                outFile.write("SOLD TO:  %s\n\t  %s\n\t  %s, %s\n\t  %s\n\n" %(userName,userStreet,userCity,userProvince,userPostalCode))
                outFile.write("\n")
                outFile.write("Item Description                         Quantity Unit Price     Total")
                outFile.write("\n")
                outFile.write("-"*40)
                outFile.write(" ")
                outFile.write("-"*8)
                outFile.write(" ")
                outFile.write("-"*10)
                outFile.write(" ")
                outFile.write("  --------")
                outFile.write("\n")

                tax = provinceTax(userProvince)
                startForm3 = True
                subTotal = 0
                startForm1 = False
            #ENDIF
                
        elif startForm2:
            
            #If statement
            if not startForm1:
                info2.append(val)
            #ENDIF

            #If statement 
            if not(info2 == [["D\n"]]):
                itemNum = info2[1][0]
                itemDescription = info2[1][1]
                quantity = int(info2[1][2])
                price = float(info2[1][3].strip())
                total = quantity * price

                #item information
                print "%-40s %8s %10s   %8.2f\n" %(itemDescription,quantity,price,total),

                #writing
                outFile.write("%-40s %8s %10s   %8.2f\n" %(itemDescription,quantity,price,total))
                subTotal += total
                startForm2 = False
            #ENDIF
        #ENDIF
    #ENDFOR

    #shipping and subtotal            
    print
    print " "*50,"Shipping: %10.2f" %(shipping(shippingMethod))
    print "%71s" %("--------")
    print " "*50,"Subtotal: %10.2f" %(subTotal + shipping(shippingMethod))

    #writing
    outFile.write("\n")
    outFile.write(" "*50)
    outFile.write(" ")
    outFile.write("Shipping: %10.2f" %(shipping(shippingMethod)))
    outFile.write("\n")
    outFile.write("%71s" %("--------"))
    outFile.write("\n")
    outFile.write(" "*50)
    outFile.write(" ")
    outFile.write("Subtotal: %10.2f" %(subTotal + shipping(shippingMethod)))
    outFile.write("\n")

    subTotal += shipping(shippingMethod)
    tax = provinceTax(userProvince)

    #If statement
    if (userProvince == "BC") or (userProvince == "AB") or (userProvince == "SK") or (userProvince == "MB"): #BC or AB or SK or MB
        GST = subTotal*0.05
        PST = subTotal*tax
        finalTotal = subTotal + GST + PST

        #tax and final total
        print " "*55,"GST: %10.2f" %(GST)
        print " "*55,"PST: %10.2f" %(PST)
        print "%71s" %("========")
        print " "*53,"Total: %10.2f" %(finalTotal)

        #writing
        outFile.write(" "*55)
        outFile.write(" ")
        outFile.write("GST: %10.2f" %(GST))
        outFile.write("\n")
        outFile.write(" "*55)
        outFile.write(" ")
        outFile.write("PST: %10.2f" %(PST))
        outFile.write("\n")
        outFile.write("%71s" %("========"))
        outFile.write(" "*53)
        outFile.write(" ")
        outFile.write("Total: %10.2f" %(finalTotal))
        outFile.write("\n")
        
    elif (userProvince == "ON") or (userProvince == "NB") or (userProvince == "NS") or (userProvince == "NL"): #ON or NB or NS or NL
        HST = subTotal*tax
        finalTotal = subTotal + HST

        #tax and final total
        print " "*55,"HST: %10.2f" %(HST)
        print "%71s" %("========")
        print " "*53,"Total: %10.2f" %(finalTotal)

        #writing
        outFile.write(" "*55)
        outFile.write(" ")
        outFile.write("HST: %10.2f" %(HST))
        outFile.write("\n")
        outFile.write("%71s" %("========"))
        outFile.write("\n")
        outFile.write(" "*53)
        outFile.write(" ")
        outFile.write("Total: %10.2f" %(finalTotal))
        
    elif (userProvince == "QC"): #QC
        GST = subTotal*0.05
        QST = subTotal*1.05*tax
        finalTotal = subTotal + GST + QST

        #tax and final total
        print " "*55,"GST: %10.2f" %(GST)
        print
        print " "*50,"Subtotal: %10.2f" %(subTotal*1.05)
        print " "*55,"QST: %10.2f" %(QST)
        print "%71s" %("========")
        print " "*53,"Total: %10.2f" %(finalTotal)

        #writing
        outFile.write(" "*55)
        outFile.write(" ")
        outFile.write("GST: %10.2f" %(GST))
        outFile.write("\n")
        outFile.write("\n")
        outFile.write(" "*50)
        outFile.write(" ")
        outFile.write("Subtotal: %10.2f" %(subTotal*1.05))
        outFile.write("\n")
        outFile.write(" "*55)
        outFile.write(" ")
        outFile.write("QST: %10.2f" %(QST))
        outFile.write("\n")
        outFile.write("%71s" %("========"))
        outFile.write("\n")
        outFile.write(" "*53)
        outFile.write(" ")
        outFile.write("Total: %10.2f" %(finalTotal))
        outFile.write("\n")
        
    elif (userProvince == "PE"): #PE
        GST = subTotal*0.05
        PST = subTotal*1.05*tax
        finalTotal = subtotal + GST + PST

        #tax and final total
        print " "*55,"GST: %10.2f" %(GST)
        print
        print " "*50,"Subtotal: %10.2f" %(subTotal*1.05)
        print " "*55,"PST: %10.2f" %(PST)
        print "%71s" %("========")
        print " "*53,"Total: %10.2f" %(finalTotal)

        #writing
        outFile.write(" "*55)
        outFile.write(" ")
        outFile.write("GST: %10.2f" %(GST))
        outFile.write("\n")
        outFile.write("\n")
        outFile.write(" "*50)
        outFile.write(" ")
        outFile.write("Subtotal: %10.2f" %(subTotal*1.05))
        outFile.write("\n")
        outFile.write(" "*55)
        outFile.write(" ")
        outFile.write("PST: %10.2f" %(PST))
        outFile.write("\n")
        outFile.write( "%71s" %("========"))
        outFile.write("\n")
        outFile.write(" "*53)
        outFile.write(" ")
        outFile.write("Total: %10.2f" %(finalTotal))
        outFile.write("\n")
    #ENDIF

    #closing
    invFile.close()
outFile.close()


#ENDMain
