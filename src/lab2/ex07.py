def format_record(tuptup):
    otvetik = ''
    if type(tuptup) == tuple:
        if len(tuptup) == 3:
            fio = tuptup[0]
            gruppochka = tuptup[1]
            gpa = tuptup[2]
            if type(fio) == str and type(gruppochka) == str and type(gpa) == float and len(fio.split()) >= 2:
                fio = fio.split()
                if len(fio) == 2:
                    fam = fio[0].capitalize()
                    name = fio[1].capitalize()
                    new_fio = f'{fam} {name[0]}.,'
                if len(fio) == 3:
                    fam = fio[0].capitalize()
                    name = fio[1].capitalize()
                    otch = fio[2].capitalize()
                    new_fio = f'{fam} {name[0]}.{otch[0]}.,'
                new_gruppochka = f'гр. {gruppochka},'
                otvetik = f'{new_fio} {new_gruppochka} {gpa:.2f}'
                return otvetik
            else:
                raise ValueError

tuptup = ("Иванов Иван Иванович", "BIVT-25", 4.6)
print(format_record(tuptup))