
invoice = open("Level4InvoiceInformation.txt")
line = "junk"
first=True



#Loop runs once per line read from teh file        
while not (line == ""):
    line = invoice.readline()
    if line == "H\n":
        if first == False:           
            print "%64s%9.2f" % ("Shipping:",shipping)
            print "%74s" % "--------"
            print "%64s%9.2f" % ("Subtotal:",shipping + total)
        subtotal = 0

        headerInfo = invoice.readline().split(":")
        first=False

        customerName = headerInfo[1]
        street = headerInfo[2]
        city = headerInfo[3]
        province = headerInfo[4] 
        postalCode = headerInfo[5]
        invoiceDate = headerInfo[6]
        invoiceNumber = headerInfo[7]
        shipping = headerInfo[8]

        if shipping == "PC\n":
            shipping = 35.00
        elif shipping == "XP\n":
            shipping = 20.00
        else:
            shipping = 10.00 

        


        print
        print "   ","------------------------------------------------------------------------"
        print
        print
        print "      ","            C A N T E R B U R Y   B O O K S   L T D."
        print "      ","          2346 Industrial Ave, Burlington, ON L7S 2W1"
        print "      ","                       (905)-673-2596)"
        print 
        print
        print "    ","Invoice Number                                     Invoice Date"
        print "    ","--------------                                     ------------"
        print "    ","   ",invoiceNumber,"                                         ",invoiceDate
        print
        print
        print "    ","SOLD TO:", customerName
        print "    ","        ", street
        print "    ","        ", city,province
        print "    ","        ", postalCode
        print
        print
        print "    ","Item Description                    Quantity    Unit Price    Total"
        print "    ","---------------------------------  ----------  ------------  -------"
        
    elif line == "D\n":
        
        detailInfo = invoice.readline()
        detailInfo = detailInfo.replace('\n', '')
        detailInfo = detailInfo.split(":")


        item = detailInfo[1]
        quantity = detailInfo[2]

        
        price = detailInfo[3] 
        total = float(detailInfo[3])*int(detailInfo[2])
        

        print "     %-44s%1s%14s%9.2f" % (item,quantity,price,total)
        subtotal = total + subtotal
        print
        



    else: # not an 'h' or a 'd'
        print "WTF"
        print "DEBUG execing the ELSE"
        print "%64s%9.2f" % ("Shipping:",shipping)
        print "%74s" % "--------"
        print "%64s%9.2f" % ("Subtotal:",subtotal + shipping)
##        print
##        print "%64s%9.2f" % ("GST:",
##        print "%74s" % "========"
##        print "%64s%9.2f" % ("PST:",
##        print "%64s%9.2f" % ("Total:",                    
        print "   ","------------------------------------------------------------------------"



