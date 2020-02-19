
def main(name,key):
    fp = open(name)
    fp.seek(0, 2)
    begin = 0
    end = fp.tell()
    prev=0
    while (begin < end):
        fp.seek((end + begin) / 2, 0)
        if (end + begin) / 2 == prev:
            fp.seek(max(begin-100,0), 0)
            if max(begin-100,0)!=0:
                fp.readline()
            while(fp.tell()<end):
                line = fp.readline().strip().split()
                if len(line)==1:
                    line_key = ""
                    pp=line[0]
                else:
                    password=line[0]
                    for i in line[1:-1]:
                        password=password+" "+i
                    line_key = password 
                    pp=line[-1]
                if (key == line_key):
                    return pp
            return None            
            
        prev=(end + begin) / 2
        fp.readline()
        line = fp.readline().strip().split()
        password=line[0]
        for i in line[1:-1]:
            password=password+" "+i
        line_key = password
        pp=line[-1]
        if (key == line_key):
            return pp
        elif (key > line_key):
            begin = fp.tell()
        else:
            end = fp.tell()
            

def main4(name,key):
    fp = open(name)
    fp.seek(0, 2)
    begin = 0
    end = fp.tell()
    prev=0
    while (begin < end):
        fp.seek((end + begin) / 2, 0)
        
        if (end + begin) / 2 == prev:
            fp.seek(max(begin-100,0), 0)
            if max(begin-100,0)!=0:
                fp.readline()
            while(fp.tell()<end):
                line = fp.readline().strip().split(")")
                line_key = line[0]+")"
                if (key == line_key):
                    return line[1]
            return None                    
        prev=(end + begin) / 2
        fp.readline()
        line = fp.readline().strip().split(")")
        line_key = line[0]+")"
        if (key == line_key):
            return line[1]
        elif (key > line_key):
            begin = fp.tell()
        else:
            end = fp.tell()

