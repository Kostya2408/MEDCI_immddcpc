import csv
from collections import Counter
filename = '/home/kostya2408/Загрузки/медицинские_протоколы.csv'  # Укажите путь к вашему файлу .csv

with open(filename, 'r') as file:
    reader = csv.reader(file, delimiter= ";")
    column_seven = [row[6].lower().rstrip('.') for row in reader]

x = 10

numbreak = []
items = []
counts = []
counts_dop = []
flag = 0


while flag == 0:
    y = 0
    items.clear()
    counts.clear()

    while y<10:
        y = 0
        top_10 = Counter(column_seven).most_common(x)

        for item, count in top_10:

            if item not in ["нет", "жалоб нет", "не предъявляет", "на момент осмотра жалоб нет", "на момент осмотра жалоб не предъявляет", "активно не предъявляет", "жалоб на момент осмотра не предъявляет", "жалоб в момент осмотра не предъявляет","на момент осмотра не предъявляет","на момент осмотра нет","жалоб не предъявляет","активно нет","активных жалоб не предъявляет","активных жалоб на момент осмотра нет","активных жалоб нет","на момент осмотра не имеет","в настоящее время жалоб не предъявляет","активных нет","на момент осмотра активно не предъявляет","жалоб не имеет","на момент осмотра не предьявляет","на момент осмотра жалоб активно не предъявляет","жалобы:  нет","не предьявляет","жалоб активно не предъявляет","жалоб на момент осмотра нет","жалоб нет. кожные покровы чистые, педикулеза, чесотки и других заразных заболеваний не выявлено. согласно приказу медицинских противопоказаний к работе в должности не имеет","жалоб в момент осмотра не предъявляет. головные боли, обмороки, чмт отрицает","-","прежние","на момент осмотра жалобы активно не предъявляет","профилактический осмотр","на приеме с законным представителем (мамой). активных жалоб нет","повторно, после получения результатов дообследования экспертный анамнез: со слов пациентки, за текущий год. на лн не была в настоящее время лн не имеет. согласие на прием и  обследование получено, подписано","проф. осмотр перед вакцинацией. жалоб нет","на момент осмотра активных жалоб нет"]:
                z = 0

                for i in numbreak:

                    if i == item:
                        z += 1

                if z == 0:
                    items.append(item)
                    counts.append(count)
                    y += 1



            else:
                x += 1

    items_po_clowno = []
    items_po_clowno.clear()
    for i in items:
        I = i.split(" ")
        U=[]
        for u in I:
            U.append(u.rstrip(","))

        items_po_clowno.append(U)



    y_chet = 0
    for i in reversed(items_po_clowno):
        u_chet = 0
        for u in items_po_clowno:
            if len(items_po_clowno)-y_chet  < u_chet:
                break
            flag_sowpadenia = 0
            chetchik = 0
            if len(i) > len(u):
                koef = len(u)*0.5
            else:
                koef = len(i)*0.5
            if i != u:

                for r in i:
                    for t in u:

                        if r == t:
                            if len(r)>4 and len(t)>4:
                                chetchik += 1
                                

            
            if chetchik > koef:

                
                numbreak.append(i)
                flag_counts_dop = 0
                while(flag_counts_dop==0):
                    if 0 <= u_chet < len(counts_dop):
                        counts_dop[u_chet] += counts[y_chet]


                        flag_sowpadenia = 1
                        flag_counts_dop = 1

                    else:
                        counts_dop.append(0)


            u_chet += 1
        y_chet += 1
    if y_chet > 120:
        chet_vivod = 0
        counts_obedin = []
        for i in counts:
            counts_obedin.append(int(counts[i]) + int(counts_dop[i]))
        while chet_vivod <= 10:

            print(items_po_clowno[chet_vivod], " ", counts_obedin[chet_vivod])
            chet_vivod += 1
        break
