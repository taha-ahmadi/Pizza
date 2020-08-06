import textwrap

def display(datas):
    wrapper = textwrap.TextWrapper(width=20)
    # assume that your data rows are tuples
    template = "{0:8}|{1:30}|{2:10}|{3:10}" # column widths: 8, 10, 15, 7, 10
    print (template.format("ID", "TODO", "DEADLINE", "COMPLETE")) # header
    for rec in datas: 
            w =wrapper.wrap(text=rec[1])
            for i in w:
                if rec[3]:
                    complete = "✅"
                else:
                    complete = "❌"
                print("{:9}".format(str(rec[0]))+"{:31}".format(i)+"{:10}".format(str(rec[2])),complete)




