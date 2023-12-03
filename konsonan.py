def filter_konsonan(kalimat):
    huruf = ''

    for i in kalimat:
      if i not in 'aiueo':
            huruf += i
    return huruf

hasilnya = filter_konsonan('Nurul Fikri')
print('huruf konsonan dari kata nurul fikri adalah', hasilnya)