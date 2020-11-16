import string
import random

inputOutputDict = {
    "merhaba" :["Merhaba.","Selam","Merhaba hoşgeldiniz.","Merhabalar","Selamlar"],
    "hoş buldum" : "",#tepkisiz
    "hoş bulduk" : "",
    "nasılsın" : "İyiyim efendim, siz nasılsınız?",
    "iyiyim" : "Bunu duyduğuma sevindim.",
    "2 artı 2 kaç eder" :"4 eder efendim",
    "ankarada hava durumu ne" : "Soğuk, brrrrr.",
    "adın ne" : "Benim adım Ayelar",
    "ismin ne" :"adın ne",#aynı soruların cevaplarını eşleştir
    "senin adın ne" : "adın ne"
}
def ciktiAl(girdi):
    # kullanıcı girdisinin dictionary içerisinde var mı kontrol ediyoruz
    if (girdi in inputOutputDict):
        # kullanıcı girsininin karşılığı var mı kontrol ediyoruz
        if (inputOutputDict[girdi] != ""):
            # kullanıcı girdisinin karşılığı var ama karşılık dictionary içerisinde var mı kontrol ediyoruz
            if (str(inputOutputDict[girdi]) not in inputOutputDict):#list değeri str ile kıyaslanamadığı için str() dönüşümü uygulandı
                #eğer girdi rastgeleyse random üretip random indexini çağırıyoruz
                if isinstance(inputOutputDict[girdi], list) == True:
                    rand = random.randint(0,len(inputOutputDict[girdi])-1)
                    #girdinin rastgele indeksini çağırıyoruz
                    print(inputOutputDict[girdi][rand])
                else:
                    #eğer girdi liste değilse girdiyi çağırıyoruz
                    print(inputOutputDict[girdi])
            # kullanıcı girdisinin karşılığı dictionary içerisinde yoksa, karşılığı kullanıcıya veriyoruz
            else:
                print(inputOutputDict[inputOutputDict[girdi]])
        # kullanıcı girdisinin karşılığı yoksa pass geçiyoruz
        else:
            pass
    # kullanıcı girdisi dictionary içerisinde yoksa "ne dediğinizi anlamadım" mesajı veriyoruz
    else:
        print("Ne dediğinizi anlamadım")
# diyalogu sonsuz döngüye sokuyoruz
while(True):
    # kullanıcıdan girdi alıyoruz
    userInput = input("User: ")
    # kullanıcı girdisini küçük harfe çeviriyoruz
    userInput=userInput.lower()
    # kullanıcı girdisinde ki noktalama işaretlerini yok ediyoruz
    userInput = "".join([c for c in userInput if c in string.digits + string.ascii_letters + "ÖÜÇŞĞöüçşıİğ "])
    ciktiAl(userInput)
