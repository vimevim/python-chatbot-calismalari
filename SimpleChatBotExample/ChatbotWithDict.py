inputOutputDict = {
    "merhaba" :"Merhaba, hoşgeldiniz.",
    "hoş buldum" : "",#tepkisiz
    "hoş bulduk" : "",
    "nasılsın" : "İyiyim efendim, siz nasılsınız?",
    "iyiyim" : "Bunu duyduğuma sevindim.",
    "2+2 kaç eder" :"4 eder efendim",
    "ankarada hava durumu ne" : "Soğuk, brrrrr.",
    "adın ne" : "Benim adım Ayelar",
    "ismin ne" :"adın ne",#aynı soruların cevaplarını eşleştir
    "senin adın ne" : "adın ne",
}
# diyalogu sonsuz döngüye sokuyoruz
while(True):
    # kullanıcıdan girdi alıyoruz
    userInput = input("User: ")
    # kullanıcı girdisini küçük harfe çeviriyoruz
    userInput=userInput.lower()
    # kullanıcı girdisinde ki noktalama işaretlerini yok ediyoruz
    userInput=userInput.replace(".","")
    userInput=userInput.replace("!","")
    userInput=userInput.replace("?","")
    # kullanıcı girdisinin dictionary içerisinde var mı kontrol ediyoruz
    if(userInput in inputOutputDict):
        # kullanıcı girsininin karşılığı var mı kontrol ediyoruz
        if(inputOutputDict[userInput] !=""):
            #kullanıcı girdisinin karşılığı var ama karşılık dictionary içerisinde var mı kontrol ediyoruz
            if (inputOutputDict[userInput] in inputOutputDict):
                print(inputOutputDict[inputOutputDict[userInput]])
            #kullanıcı girdisinin karşılığı dictionary içerisinde yoksa, karşılığı kullanıcıya veriyoruz
            else:
                print(inputOutputDict[userInput])
        #kullanıcı girdisinin karşılığı yoksa pass geçiyoruz
        else:
            pass
    #kullanıcı girdisi dictionary içerisinde yoksa "ne dediğinizi anlamadım" mesajı veriyoruz
    else:
        print("Ne dediğinizi anlamadım")
