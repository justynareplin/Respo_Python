def alfabetyczniebezpowtorzen(a):
    words = a.split(" ")
    words = sorted(list(set(words)))
    print(" ".join(words))

alfabetyczniebezpowtorzen("nie było jeszcze żadnego krzewu polnego na ziemi ani żadna trawa polna jeszcze nie wzeszła i nie było człowieka by uprawiał ziemię")
